const https = require('https');
const http = require('http');

// Cookie存储 - 使用环境变量和内存组合存储
let globalCookies = {};

// 尝试从环境变量恢复cookie（简单的持久化方案）
function getCookieKey(sessionId) {
    return `COOKIE_${sessionId.replace(/[^a-zA-Z0-9]/g, '_')}`;
}

function saveCookieToEnv(sessionId, cookieValue) {
    try {
        // 注意：Netlify Functions的环境变量是只读的，这里只是演示
        // 实际生产环境应该使用外部存储（如Redis、数据库等）
        globalCookies[sessionId] = cookieValue;
        console.log(`💾 Cookie已保存到内存 [${sessionId.substring(0, 15)}...]`);
    } catch (error) {
        console.warn('⚠️ Cookie保存失败:', error.message);
    }
}

function getCookieFromStorage(sessionId) {
    // 首先从内存中获取
    if (globalCookies[sessionId]) {
        console.log(`📖 从内存获取Cookie [${sessionId.substring(0, 15)}...]`);
        return globalCookies[sessionId];
    }
    
    console.log(`❌ 内存中未找到Cookie [${sessionId.substring(0, 15)}...]`);
    return null;
}

exports.handler = async (event, context) => {
    console.log('🚀 代理请求开始');
    console.log('  - HTTP方法:', event.httpMethod);
    console.log('  - 请求头:', JSON.stringify(event.headers, null, 2));
    console.log('  - 查询参数:', JSON.stringify(event.queryStringParameters, null, 2));
    
    // 处理CORS预检请求
    if (event.httpMethod === 'OPTIONS') {
        return {
            statusCode: 200,
            headers: {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Headers': 'Content-Type',
                'Access-Control-Allow-Methods': 'GET, POST, PUT, DELETE, OPTIONS'
            },
            body: ''
        };
    }

    try {
        // 解析请求数据 - 支持GET查询参数和POST请求体
        let requestData;
        if (event.httpMethod === 'GET' && event.queryStringParameters) {
            // GET请求，从查询参数获取数据
            requestData = {
                path: event.queryStringParameters.path,
                method: event.queryStringParameters.method || 'GET',
                sessionId: event.queryStringParameters.sessionId,
                headers: {}
            };
        } else if (event.httpMethod === 'POST' && event.body) {
            // POST请求，从请求体获取数据
            requestData = JSON.parse(event.body);
        } else {
            return {
                statusCode: 400,
                headers: {
                    'Access-Control-Allow-Origin': '*'
                },
                body: JSON.stringify({ error: 'Missing request data' })
            };
        }
        
        console.log('  - 解析后的请求数据:', JSON.stringify(requestData, null, 2));
        
        const { path, method = 'GET', body, csrfToken, headers: clientHeaders = {}, sessionId, clientCookies } = requestData;
        
        if (!path) {
            console.log('❌ 缺少path参数');
            return {
                statusCode: 400,
                headers: {
                    'Access-Control-Allow-Origin': '*'
                },
                body: JSON.stringify({ error: 'Path is required' })
            };
        }
        
        console.log('✅ 请求参数验证通过:', { path, method, sessionId });

        // 构建完整URL
        const url = `https://www.luogu.com.cn${path}`;
        
        // 获取会话ID - 优先使用客户端提供的sessionId，确保一致性
        let clientSessionId = sessionId;
        
        // 如果没有提供sessionId，尝试从其他来源获取
        if (!clientSessionId) {
            // 使用客户端IP作为备用标识
            clientSessionId = event.headers['x-forwarded-for'] || event.headers['x-real-ip'] || 'default';
            console.log('⚠️ 未提供sessionId，使用备用标识:', clientSessionId);
        } else {
            console.log('✅ 使用客户端提供的sessionId:', clientSessionId.substring(0, 15) + '...');
        }
        
        // 设置请求头 - 严格按照洛谷API规范
        const requestHeaders = {
            // 必须：User-Agent不能包含python-requests
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Accept': '*/*',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'Accept-Encoding': 'gzip, deflate, br', // 支持压缩
            'Connection': 'keep-alive',
            // 必须：对于非GET请求，Referer为洛谷主站
            'Referer': 'https://www.luogu.com.cn/',
            'Origin': 'https://www.luogu.com.cn'
        };

        // 对于验证码请求，设置特定的Accept头
        if (path === '/lg4/captcha') {
            requestHeaders['Accept'] = 'image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8';
        }

        // 对于DataResponse类型的请求，添加必要的头
        if (clientHeaders && clientHeaders['x-luogu-type']) {
            requestHeaders['x-luogu-type'] = clientHeaders['x-luogu-type'];
        }

        // 对于LentilleDataResponse类型的请求，添加必要的头
        if (clientHeaders && clientHeaders['x-lentille-request']) {
            requestHeaders['x-lentille-request'] = clientHeaders['x-lentille-request'];
        }

        // 添加客户端传递的头部
        Object.assign(requestHeaders, clientHeaders);
        
        // 调试：输出最终的请求头
        console.log(`🔍 [${clientSessionId}] 最终请求头:`, JSON.stringify(requestHeaders, null, 2));

        // 添加Cookie - 优先使用服务端保存的，备用客户端传递的
        const savedCookie = getCookieFromStorage(clientSessionId);
        const cookieToUse = savedCookie || clientCookies;
        
        if (cookieToUse) {
            requestHeaders['Cookie'] = cookieToUse;
            const cookieSource = savedCookie ? '服务端保存' : '客户端传递';
            console.log(`🍪 [${clientSessionId}] 使用${cookieSource}的Cookie:`, cookieToUse.substring(0, 100) + '...');
            
            // 如果使用的是客户端传递的cookie，同时保存到服务端
            if (!savedCookie && clientCookies) {
                saveCookieToEnv(clientSessionId, clientCookies);
                console.log(`💾 [${clientSessionId}] 客户端Cookie已同步到服务端`);
            }
        } else {
            console.log(`❌ [${clientSessionId}] 没有找到任何Cookie（服务端或客户端）`);
            console.log(`📊 当前所有会话Cookie:`, Object.keys(globalCookies).map(key => ({
                sessionId: key.substring(0, 15) + '...',
                cookieLength: globalCookies[key] ? globalCookies[key].length : 0
            })));
            
            // 如果是提交相关的请求且没有Cookie，给出明确提示
            if (path.includes('/fe/api/problem/submit/')) {
                console.log('🚨 提交请求但没有登录Cookie，这可能导致"未登录"错误');
                console.log('🔍 建议检查：');
                console.log('  1. 是否在同一个sessionId下登录？');
                console.log('  2. 登录后是否成功保存了Cookie？');
                console.log('  3. Netlify Functions实例是否发生了重启？');
                console.log('  4. 客户端是否传递了cookie备份？');
            }
        }

        // 如果是非GET请求，添加必要的头部（按洛谷API规范）
        if (method !== 'GET') {
            requestHeaders['Content-Type'] = 'application/json';
            // 必须：对于非GET请求，Referer为洛谷主站
            requestHeaders['Referer'] = 'https://www.luogu.com.cn/';
            
            // 必须：对于非GET请求，需要CSRF令牌（除非在请求主体中给出）
            if (csrfToken) {
                requestHeaders['x-csrf-token'] = csrfToken;
                console.log(`🔐 [${clientSessionId}] 添加CSRF令牌:`, csrfToken.substring(0, 10) + '...');
            } else {
                console.log(`⚠️ [${clientSessionId}] 非GET请求缺少CSRF令牌，可能导致请求失败`);
            }
        }

        // 发起请求到洛谷API
        const response = await makeRequest(url, {
            method: method,
            headers: requestHeaders,
            body: body ? JSON.stringify(body) : undefined
        });

        console.log('🔍 洛谷API详细响应信息:');
        console.log('  - 请求URL:', url);
        console.log('  - 请求方法:', method);
        console.log('  - 响应状态:', response.statusCode);
        console.log('  - 响应内容类型:', response.headers['content-type']);
        console.log('  - 响应内容长度:', response.body ? response.body.length : 0);
        console.log('  - 响应头:', JSON.stringify(response.headers, null, 2));
        
        // 如果是404错误，输出更多调试信息
        if (response.statusCode === 404) {
            console.log('❌ 洛谷API返回404错误:');
            console.log('  - 完整URL:', url);
            console.log('  - 请求头:', JSON.stringify(requestHeaders, null, 2));
            console.log('  - 响应体前500字符:', response.body ? response.body.substring(0, 500) : 'empty');
        }

        // 保存Cookie（如果有Set-Cookie头部）
        let savedCookies = null;
        if (response.headers['set-cookie']) {
            const cookies = Array.isArray(response.headers['set-cookie']) 
                ? response.headers['set-cookie'] 
                : [response.headers['set-cookie']];
            
            // 解析并保存Cookie
            const cookieStrings = cookies.map(cookie => {
                // 只保留cookie的name=value部分，去掉Path、Domain等属性
                return cookie.split(';')[0];
            }).filter(Boolean);
            
            if (cookieStrings.length > 0) {
                const cookieValue = cookieStrings.join('; ');
                saveCookieToEnv(clientSessionId, cookieValue);
                savedCookies = cookieValue; // 保存用于返回给客户端
                console.log(`🍪 [${clientSessionId}] 保存Cookie:`, cookieValue.substring(0, 100) + '...');
                console.log(`📊 [${clientSessionId}] 当前所有会话Cookie:`, Object.keys(globalCookies));
                
                // 检查是否包含重要的登录相关cookie
                const hasLoginCookies = cookieValue.includes('_uid') || cookieValue.includes('__client_id');
                if (hasLoginCookies) {
                    console.log(`✅ [${clientSessionId}] 检测到登录相关Cookie (_uid 或 __client_id)`);
                } else {
                    console.log(`⚠️ [${clientSessionId}] 未检测到登录相关Cookie，可能影响后续请求`);
                }
            }
        }

        // 准备响应体，如果有新的cookie，添加到响应中
        let responseBody = response.body;
        if (savedCookies && response.headers['content-type']?.includes('application/json')) {
            try {
                const jsonBody = JSON.parse(responseBody);
                // 添加cookie信息到响应中，供客户端保存
                jsonBody._cookies = savedCookies;
                responseBody = JSON.stringify(jsonBody);
                console.log(`📤 [${clientSessionId}] 在响应中添加Cookie信息供客户端保存`);
            } catch (error) {
                console.log(`⚠️ [${clientSessionId}] 无法解析JSON响应，跳过Cookie添加`);
            }
        }

        // 返回响应
        return {
            statusCode: response.statusCode,
            headers: {
                'Content-Type': response.headers['content-type'] || 'application/json',
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Headers': 'Content-Type',
                'Access-Control-Allow-Methods': 'GET, POST, PUT, DELETE, OPTIONS',
                // 如果有cookie，也通过自定义头返回（作为备用方案）
                ...(savedCookies && { 'X-Saved-Cookies': savedCookies })
            },
            body: responseBody
        };

    } catch (error) {
        console.error('代理请求失败:', error);
        return {
            statusCode: 500,
            headers: {
                'Access-Control-Allow-Origin': '*'
            },
            body: JSON.stringify({ 
                error: 'Internal server error',
                message: error.message 
            })
        };
    }
};

// 辅助函数：发起HTTP请求
function makeRequest(url, options) {
    return new Promise((resolve, reject) => {
        const urlObj = new URL(url);
        const isHttps = urlObj.protocol === 'https:';
        const client = isHttps ? https : http;
        
        const requestOptions = {
            hostname: urlObj.hostname,
            port: urlObj.port || (isHttps ? 443 : 80),
            path: urlObj.pathname + urlObj.search,
            method: options.method || 'GET',
            headers: options.headers || {}
        };

        const req = client.request(requestOptions, (res) => {
            let data = [];
            let isBase64 = false;

            // 检查是否是二进制内容（如图片）
            const contentType = res.headers['content-type'] || '';
            if (contentType.startsWith('image/')) {
                isBase64 = true;
            }

            res.on('data', (chunk) => {
                data.push(chunk);
            });

            res.on('end', () => {
                let body;
                const buffer = Buffer.concat(data);
                
                if (isBase64) {
                    body = buffer.toString('base64');
                } else {
                    // 处理压缩编码
                    const encoding = res.headers['content-encoding'];
                    const zlib = require('zlib');
                    
                    try {
                        if (encoding === 'gzip') {
                            body = zlib.gunzipSync(buffer).toString('utf8');
                        } else if (encoding === 'deflate') {
                            body = zlib.inflateSync(buffer).toString('utf8');
                        } else if (encoding === 'br') {
                            body = zlib.brotliDecompressSync(buffer).toString('utf8');
                        } else {
                            body = buffer.toString('utf8');
                        }
                    } catch (e) {
                        console.error('解压缩失败:', e.message, '编码:', encoding);
                        // 如果解压失败，尝试直接解码
                        body = buffer.toString('utf8');
                    }
                }

                console.log('响应状态码:', res.statusCode);
                console.log('响应头:', res.headers);
                console.log('内容编码:', res.headers['content-encoding']);
                console.log('响应体长度:', body.length);
                console.log('响应体前200字符:', body.substring(0, 200));

                resolve({
                    statusCode: res.statusCode,
                    headers: res.headers,
                    body: body,
                    isBase64Encoded: isBase64
                });
            });
        });

        req.on('error', (error) => {
            reject(error);
        });

        // 如果有请求体，写入数据
        if (options.body) {
            req.write(options.body);
        }

        req.end();
    });
}
