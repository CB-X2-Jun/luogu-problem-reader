exports.handler = async (event, context) => {
    console.log('测试函数被调用');
    console.log('HTTP方法:', event.httpMethod);
    console.log('请求路径:', event.path);
    
    return {
        statusCode: 200,
        headers: {
            'Access-Control-Allow-Origin': '*',
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            message: 'Netlify Functions工作正常',
            method: event.httpMethod,
            path: event.path,
            timestamp: new Date().toISOString()
        })
    };
};
