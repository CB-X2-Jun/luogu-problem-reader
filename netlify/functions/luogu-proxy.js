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
            'Accept': '*/*',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            ...headers
        };

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

        // 返回响应
        return {
            statusCode: response.statusCode,
            headers: {
                'Access-Control-Allow-Origin': '*',
                'Content-Type': response.headers['content-type'] || 'application/json'
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
                if (isBase64) {
                    body = Buffer.concat(data).toString('base64');
                } else {
                    body = Buffer.concat(data).toString();
                }

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
