const https = require('https');

exports.handler = async (event, context) => {
    // 设置CORS头
    const headers = {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Headers': 'Content-Type',
        'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
        'Cache-Control': 'no-cache, no-store, must-revalidate',
        'Pragma': 'no-cache',
        'Expires': '0'
    };

    // 处理预检请求
    if (event.httpMethod === 'OPTIONS') {
        return {
            statusCode: 200,
            headers,
            body: ''
        };
    }

    try {
        console.log('🖼️ 专用验证码函数被调用');
        
        // 获取sessionId
        let sessionId = '';
        if (event.httpMethod === 'GET') {
            sessionId = event.queryStringParameters?.sessionId || '';
        } else if (event.httpMethod === 'POST') {
            const body = JSON.parse(event.body || '{}');
            sessionId = body.sessionId || '';
        }

        console.log('SessionId:', sessionId ? sessionId.substring(0, 10) + '...' : 'empty');

        // 构建请求选项 - 严格按照洛谷API规范
        const options = {
            hostname: 'www.luogu.com.cn',
            path: '/lg4/captcha',
            method: 'GET',
            headers: {
                // 必须：User-Agent不能包含python-requests
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
                // 图片请求专用Accept头
                'Accept': 'image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
                'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
                'Accept-Encoding': 'gzip, deflate, br',
                'Connection': 'keep-alive',
                // 必须：Referer为洛谷主站
                'Referer': 'https://www.luogu.com.cn/',
                // 浏览器安全相关头
                'Sec-Fetch-Dest': 'image',
                'Sec-Fetch-Mode': 'no-cors',
                'Sec-Fetch-Site': 'same-origin',
                'Sec-Ch-Ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
                'Sec-Ch-Ua-Mobile': '?0',
                'Sec-Ch-Ua-Platform': '"Windows"'
            }
        };

        // 如果有sessionId，添加Cookie
        if (sessionId) {
            options.headers['Cookie'] = `__client_id=${sessionId}`;
        }

        console.log('发送验证码请求到:', options.hostname + options.path);

        // 发送请求
        const imageData = await new Promise((resolve, reject) => {
            const req = https.request(options, (res) => {
                console.log('验证码响应状态:', res.statusCode);
                console.log('验证码响应头:', res.headers);

                if (res.statusCode !== 200) {
                    reject(new Error(`HTTP ${res.statusCode}`));
                    return;
                }

                const chunks = [];
                res.on('data', (chunk) => {
                    chunks.push(chunk);
                });

                res.on('end', () => {
                    const buffer = Buffer.concat(chunks);
                    console.log('✅ 验证码图片获取成功，大小:', buffer.length, 'bytes');
                    resolve({
                        buffer: buffer,
                        contentType: res.headers['content-type'] || 'image/jpeg'
                    });
                });
            });

            req.on('error', (error) => {
                console.error('❌ 验证码请求错误:', error);
                reject(error);
            });

            req.setTimeout(10000, () => {
                req.destroy();
                reject(new Error('请求超时'));
            });

            req.end();
        });

        // 返回图片数据
        return {
            statusCode: 200,
            headers: {
                ...headers,
                'Content-Type': imageData.contentType,
                'Content-Length': imageData.buffer.length.toString()
            },
            body: imageData.buffer.toString('base64'),
            isBase64Encoded: true
        };

    } catch (error) {
        console.error('❌ 验证码函数错误:', error);
        
        return {
            statusCode: 500,
            headers,
            body: JSON.stringify({
                error: '获取验证码失败',
                message: error.message
            })
        };
    }
};
