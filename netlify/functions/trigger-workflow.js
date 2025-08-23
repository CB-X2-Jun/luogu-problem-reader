// Netlify Function - 触发GitHub Actions工作流
// 文件路径: /netlify/functions/trigger-workflow.js

exports.handler = async (event, context) => {
  // 设置CORS头
  const headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Allow-Methods': 'POST, OPTIONS',
  };

  // 处理预检请求
  if (event.httpMethod === 'OPTIONS') {
    return {
      statusCode: 200,
      headers,
      body: '',
    };
  }

  // 只允许POST请求
  if (event.httpMethod !== 'POST') {
    return {
      statusCode: 405,
      headers,
      body: JSON.stringify({ error: 'Method not allowed' }),
    };
  }

  let body;
  try {
    body = JSON.parse(event.body);
  } catch (error) {
    return {
      statusCode: 400,
      headers,
      body: JSON.stringify({ error: 'Invalid JSON body' }),
    };
  }

  const { workflow } = body;

  if (!workflow) {
    return {
      statusCode: 400,
      headers,
      body: JSON.stringify({ error: 'Workflow name is required' }),
    };
  }

  // GitHub API配置
  const GITHUB_TOKEN = process.env.GITHUB_TOKEN;
  const REPO_OWNER = 'CB-X2-Jun';
  const REPO_NAME = 'luogu-problem-reader';

  if (!GITHUB_TOKEN) {
    return {
      statusCode: 500,
      headers,
      body: JSON.stringify({ error: 'GitHub token not configured' }),
    };
  }

  // 工作流映射
  const workflowMap = {
    'daily-stats': 'daily-stats.yml',
    'theme-automation': 'theme-automation.yml',
    'seo-optimization': 'seo-optimization.yml',
    'data-visualization': 'data-visualization.yml'
  };

  const workflowFile = workflowMap[workflow];
  if (!workflowFile) {
    return {
      statusCode: 400,
      headers,
      body: JSON.stringify({ error: 'Invalid workflow name' }),
    };
  }

  try {
    // 触发GitHub Actions工作流
    const response = await fetch(
      `https://api.github.com/repos/${REPO_OWNER}/${REPO_NAME}/actions/workflows/${workflowFile}/dispatches`,
      {
        method: 'POST',
        headers: {
          'Authorization': `token ${GITHUB_TOKEN}`,
          'Accept': 'application/vnd.github.v3+json',
          'Content-Type': 'application/json',
          'User-Agent': 'Netlify-Function'
        },
        body: JSON.stringify({
          ref: 'main', // 或者你的默认分支名
          inputs: {} // 可以根据需要添加输入参数
        })
      }
    );

    if (response.ok) {
      return {
        statusCode: 200,
        headers,
        body: JSON.stringify({
          success: true,
          message: `${workflow} 工作流已成功触发`,
          workflow: workflow
        }),
      };
    } else {
      const errorData = await response.text();
      console.error('GitHub API Error:', errorData);
      
      return {
        statusCode: response.status,
        headers,
        body: JSON.stringify({
          error: 'Failed to trigger workflow',
          details: errorData
        }),
      };
    }

  } catch (error) {
    console.error('Error triggering workflow:', error);
    return {
      statusCode: 500,
      headers,
      body: JSON.stringify({
        error: 'Internal server error',
        details: error.message
      }),
    };
  }
};
