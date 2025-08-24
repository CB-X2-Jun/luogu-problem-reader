const https = require('https');
const http = require('http');

exports.handler = async (event, context) => {
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

    try {
        const { path, method = 'GET', body, csrfToken, headers = {} } = JSON.parse(event.body);
        
        if (!path) {
            return {
                statusCode: 400,
                headers: {
                    'Access-Control-Allow-Origin': '*'
                },
                body: JSON.stringify({ error: 'Path is required' })
            };
        }

        // 构建完整URL
        const url = `https://www.luogu.com.cn${path}`;
        
        // 设置请求头
        const requestHeaders = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Accept': path.includes('/api/') ? 'application/json, text/plain, */*' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'Accept-Encoding': 'identity',
            'Connection': 'keep-alive',
            'Cache-Control': 'no-cache',
            'Pragma': 'no-cache',
            'Sec-Fetch-Dest': path.includes('/api/') ? 'empty' : 'document',
            'Sec-Fetch-Mode': path.includes('/api/') ? 'cors' : 'navigate',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-User': path.includes('/auth/') ? '?1' : undefined,
            'Upgrade-Insecure-Requests': path.includes('/auth/') ? '1' : undefined,
            ...headers
        };

        // 移除undefined值
        Object.keys(requestHeaders).forEach(key => {
            if (requestHeaders[key] === undefined) {
                delete requestHeaders[key];
            }
        });

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

        console.log('洛谷API响应状态:', response.statusCode);
        console.log('响应内容类型:', response.headers['content-type']);
        console.log('响应内容长度:', response.body ? response.body.length : 0);

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
