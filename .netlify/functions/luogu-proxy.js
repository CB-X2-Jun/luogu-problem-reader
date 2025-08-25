const https = require('https');
const http = require('http');

// 全局Cookie存储（在实际生产环境中应该使用数据库或缓存）
let globalCookies = {};

exports.handler = async (event, context) => {
    // 处理CORS预检请求
    if (event.httpMethod === 'OPTIONS') {
        return {
            statusCode: 200,
            headers: {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Headers': 'Content-Type',
                'Access-Control-Allow-Methods': 'POST, OPTIONS'
            },
            body: ''
        };
    }

    // 只允许POST请求
    if (event.httpMethod !== 'POST') {
        return {
            statusCode: 405,
            headers: {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Headers': 'Content-Type',
                'Access-Control-Allow-Methods': 'POST, OPTIONS'
            },
            body: JSON.stringify({ error: 'Method not allowed' })
        };
    }

    try {
        console.log('🔍 代理函数收到请求:');
        console.log('  - HTTP方法:', event.httpMethod);
        console.log('  - 请求体长度:', event.body ? event.body.length : 0);
        
        // 简化的JSON解析，增加错误处理
        let requestData;
        try {
            requestData = JSON.parse(event.body || '{}');
        } catch (parseError) {
            console.error('❌ JSON解析失败:', parseError.message);
            return {
                statusCode: 400,
                headers: {
                    'Access-Control-Allow-Origin': '*'
                },
                body: JSON.stringify({ error: 'Invalid JSON in request body' })
            };
        }
        
        console.log('  - 解析后的请求数据:', JSON.stringify(requestData, null, 2));
        
        const { path, method = 'GET', body, csrfToken, headers: clientHeaders = {}, sessionId } = requestData;
        
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
        
        // 设置请求头
        const requestHeaders = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Accept': '*/*',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'Accept-Encoding': 'identity', // 禁用压缩
            'Connection': 'keep-alive',
            'Referer': 'https://www.luogu.com.cn/auth/login',
            'Origin': 'https://www.luogu.com.cn'
        };

        // 对于验证码请求，设置特定的Accept头
        if (path === '/lg4/captcha') {
            requestHeaders['Accept'] = 'image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8';
        }

        // 添加客户端传递的头部
        Object.assign(requestHeaders, clientHeaders);
        
        // 调试：输出最终的请求头
        console.log(`🔍 [${clientSessionId}] 最终请求头:`, JSON.stringify(requestHeaders, null, 2));

        // 添加保存的Cookie
        if (globalCookies[clientSessionId]) {
            requestHeaders['Cookie'] = globalCookies[clientSessionId];
            console.log(`🍪 [${clientSessionId}] 使用保存的Cookie:`, globalCookies[clientSessionId].substring(0, 100) + '...');
        } else {
            console.log(`❌ [${clientSessionId}] 没有找到保存的Cookie`);
            console.log(`📊 当前所有会话Cookie:`, Object.keys(globalCookies).map(key => ({
                sessionId: key.substring(0, 15) + '...',
                cookieLength: globalCookies[key] ? globalCookies[key].length : 0
            })));
            
            // 如果是提交相关的请求且没有Cookie，给出明确提示
            if (path.includes('/fe/api/problem/submit/')) {
                console.log('🚨 提交请求但没有登录Cookie，这可能导致"未登录"错误');
            }
        }

        // 如果是POST请求，添加必要的头部
        if (method === 'POST') {
            requestHeaders['Content-Type'] = 'application/json';
            requestHeaders['Referer'] = 'https://www.luogu.com.cn/auth/login';
            
            if (csrfToken) {
                requestHeaders['x-csrf-token'] = csrfToken;
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
                globalCookies[clientSessionId] = cookieStrings.join('; ');
                console.log(`🍪 [${clientSessionId}] 保存Cookie:`, globalCookies[clientSessionId]);
                console.log(`📊 [${clientSessionId}] 当前所有会话Cookie:`, Object.keys(globalCookies));
            }
        }

        // 返回响应
        return {
            statusCode: response.statusCode,
            headers: {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Headers': 'Content-Type',
                'Access-Control-Allow-Methods': 'POST, OPTIONS',
                'Content-Type': response.headers['content-type'] || 'text/html'
            },
            body: response.body,
            isBase64Encoded: response.isBase64Encoded || false
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
