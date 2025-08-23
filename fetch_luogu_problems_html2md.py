import os
import re
import requests
from bs4 import BeautifulSoup
import json
from pathlib import Path
import markdown
from markdownify import markdownify as md
import time
import argparse

PROBLEM_DIR = Path(__file__).parent / 'problem'
BASE_URL = 'https://www.luogu.com.cn/problem/'

def get_last_problem_id():
    """获取已下载的最后一个题目ID"""
    ids = []
    for entry in PROBLEM_DIR.iterdir():
        m = re.match(r'P(\d+)$', entry.name)
        if m:
            ids.append(int(m.group(1)))
    return max(ids) if ids else 999

def fetch_problem_html(pid):
    """获取题目HTML内容"""
    url = f'{BASE_URL}P{pid}'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
        "Referer": "https://www.luogu.com.cn/",
        "Accept-Language": "zh-CN,zh;q=0.9"
    }
    
    try:
        resp = requests.get(url, headers=headers, timeout=10)
        if resp.status_code != 200:
            return None
        
        soup = BeautifulSoup(resp.text, 'html.parser')
        
        # 尝试从JSON数据中提取完整内容
        script_tag = soup.find('script', {'id': 'lentille-context'})
        if script_tag:
            import json
            try:
                json_data = json.loads(script_tag.string)
                problem_data = json_data.get('data', {}).get('problem', {})
                content_data = problem_data.get('content', {}) or problem_data.get('contenu', {})
                
                # 获取题目名称，避免重复P编号
                problem_name = content_data.get('name', f'P{pid}')
                if problem_name.startswith(f'P{pid}'):
                    title = problem_name  # 如果名称已包含P编号，直接使用
                else:
                    title = f"P{pid} {problem_name}"  # 否则添加P编号
                
                # 构建完整的Markdown内容
                content_parts = []
                
                if content_data.get('background'):
                    content_parts.append(f"## 题目背景\n\n{content_data['background']}")
                
                if content_data.get('description'):
                    content_parts.append(f"## 题目描述\n\n{content_data['description']}")
                
                if content_data.get('formatI'):
                    content_parts.append(f"## 输入格式\n\n{content_data['formatI']}")
                
                if content_data.get('formatO'):
                    content_parts.append(f"## 输出格式\n\n{content_data['formatO']}")
                
                # 添加样例数据提取
                samples = problem_data.get('samples', [])
                if samples:
                    content_parts.append("## 输入输出样例")
                    for i, sample in enumerate(samples):
                        sample_input = sample[0] if len(sample) > 0 else ""
                        sample_output = sample[1] if len(sample) > 1 else ""
                        
                        content_parts.append(f"### 样例 #{i+1}")
                        content_parts.append(f"#### 样例输入 #{i+1}")
                        content_parts.append(f"```\n{sample_input.rstrip()}\n```")
                        content_parts.append(f"#### 样例输出 #{i+1}")
                        content_parts.append(f"```\n{sample_output.rstrip()}\n```")
                
                if content_data.get('hint'):
                    content_parts.append(f"## 说明/提示\n\n{content_data['hint']}")
                
                content_md = '\n\n'.join(content_parts)
                
            except (json.JSONDecodeError, KeyError) as e:
                print(f"JSON解析失败，回退到HTML解析: {e}")
                # 回退到原来的HTML解析方法
                title_tag = soup.find('h1', {'id': f'P{pid}'}) or soup.find('h1')
                title = title_tag.text.strip() if title_tag else f'P{pid}'
                
                article = soup.find('article')
                if not article:
                    return None
                content_md = md(str(article), heading_style="ATX")
        else:
            # 回退到原来的HTML解析方法
            title_tag = soup.find('h1', {'id': f'P{pid}'}) or soup.find('h1')
            title = title_tag.text.strip() if title_tag else f'P{pid}'
            
            article = soup.find('article')
            if not article:
                return None
            content_md = md(str(article), heading_style="ATX")
        
        # 如果从JSON获取了内容，就不需要再处理HTML的article了
        # content_md 已经在上面设置好了
        
        # 使用与刷新功能相同的Markdown处理逻辑
        import markdown
        
        # 使用标准Markdown转换为HTML，确保代码块正确渲染
        md_parser = markdown.Markdown(extensions=['fenced_code', 'tables', 'toc', 'codehilite'])
        content_html = md_parser.convert(content_md)
        
        return {
            'pid': f'P{pid}',
            'title': title,
            'content_md': content_md,
            'content_html': content_html
        }
    except Exception as e:
        print(f"获取 P{pid} 时出错: {e}")
        return None

def generate_md(problem):
    """生成Markdown格式内容"""
    return f"# {problem['pid']} {problem['title']}\n\n{problem['content_md']}\n"

import re

def safe_template_format(template, **kwargs):
    """使用占位符替换系统格式化HTML模板，完全避免花括号冲突"""
    # 替换占位符
    formatted = template.replace('CANONICAL_URL_PLACEHOLDER', kwargs.get('canonical', ''))
    formatted = formatted.replace('TITLE_PLACEHOLDER', kwargs.get('title', ''))
    formatted = formatted.replace('ARTICLE_CONTENT_PLACEHOLDER', kwargs.get('article', ''))
    
    # CSS变量
    css_vars = '{ --md-text-font: "Roboto"; --md-code-font: "Roboto Mono" }'
    formatted = formatted.replace('CSS_VARS_PLACEHOLDER', css_vars)
    
    # KaTeX配置
    katex_config = '''{ 
          delimiters: [
            {"left":"$$","right":"$$","display":true},
            {"left":"$","right":"$","display":false},
            {"left":"\\\\(","right":"\\\\)","display":false},
            {"left":"\\\\[","right":"\\\\]","display":true}
          ],
          throwOnError: false,
          strict: false,
          trust: true
        }'''
    formatted = formatted.replace('KATEX_CONFIG_PLACEHOLDER', katex_config)
    
    return formatted


def save_problem_files(pid, problem, template):
    """保存题目文件"""
    out_dir = PROBLEM_DIR / f'P{pid}'
    out_dir.mkdir(exist_ok=True)
    
    # 保存Markdown
    with open(out_dir / 'index.md', 'w', encoding='utf-8') as f:
        f.write(generate_md(problem))
    
    # 处理HTML模板
    html_full = safe_template_format(
        template,
        canonical=f'https://luogu.cb-x2-jun.run.place/problem/P{pid}/',
        title=problem['title'],
        article=problem['content_html']
    )
    
    # 保存HTML
    with open(out_dir / 'index.html', 'w', encoding='utf-8') as f:
        f.write(html_full)

def refresh_html_files():
    """刷新已有题目的HTML文件，不重新爬取"""
    print("开始刷新已有题目的HTML结构...")
    
    # 读取模板
    template_path = PROBLEM_DIR / 'html_template_material.html'
    if template_path.exists():
        with open(template_path, 'r', encoding='utf-8') as f:
            template = f.read()
    else:
        template = '<!doctype html><html><head><title>{title}</title></head><body>{article}</body></html>'
    
    refreshed_count = 0
    
    # 遍历所有已有的题目目录
    for entry in PROBLEM_DIR.iterdir():
        if entry.is_dir() and re.match(r'P\d+$', entry.name):
            md_file = entry / 'index.md'
            if md_file.exists():
                try:
                    # 读取Markdown文件
                    with open(md_file, 'r', encoding='utf-8') as f:
                        md_content = f.read()
                    
                    # 解析标题和内容
                    lines = md_content.split('\n')
                    title = lines[0].replace('# ', '') if lines else entry.name
                    
                    # 将Markdown转换为HTML
                    import markdown
                    
                    content_to_convert = '\n'.join(lines[2:]) if len(lines) > 2 else md_content
                    
                    # 手动预处理代码块 - 使用更简单的字符串处理方法
                    def preprocess_code_blocks(text):
                        lines = text.split('\n')
                        result_lines = []
                        in_code_block = False
                        code_block_content = []
                        
                        for line in lines:
                            if line.strip().startswith('```'):
                                if not in_code_block:
                                    # 开始代码块 - 添加空行确保与前面内容分离
                                    if result_lines and result_lines[-1].strip():
                                        result_lines.append('')
                                    in_code_block = True
                                    code_block_content = []
                                else:
                                    # 结束代码块
                                    in_code_block = False
                                    # 保持代码块内的换行格式和原始字符
                                    code_content = '\n'.join(code_block_content)
                                    # 只转义必要的HTML字符，保持其他字符原样
                                    import html
                                    # 先转义HTML特殊字符
                                    escaped_code = html.escape(code_content)
                                    # 然后处理Markdown转义字符，将 \* 转回 *
                                    escaped_code = escaped_code.replace('\\*', '*')
                                    escaped_code = escaped_code.replace('\\{', '{')
                                    escaped_code = escaped_code.replace('\\}', '}')
                                    # 保持连续空格格式
                                    escaped_code = escaped_code.replace('  ', '&nbsp;&nbsp;')
                                    result_lines.append(f'<pre class="hljs"><code class="hljs">{escaped_code}</code></pre>')
                                    # 代码块结束后添加空行确保与后面内容分离
                                    result_lines.append('')
                            elif in_code_block:
                                code_block_content.append(line)
                            else:
                                # 处理行内代码
                                processed_line = line
                                # 使用原始字符串避免转义问题
                                if '`' in processed_line and not processed_line.strip().startswith('<'):
                                    processed_line = re.sub(r'`([^`\n]+)`', r'<code class="hljs inline">\1</code>', processed_line)
                                result_lines.append(processed_line)
                        
                        return '\n'.join(result_lines)
                    
                    # 使用标准Markdown转换为HTML，确保代码块正确渲染
                    md_parser = markdown.Markdown(extensions=['fenced_code', 'tables', 'toc', 'codehilite'])
                    article_html = md_parser.convert(content_to_convert)
                    
                    # 创建问题对象
                    problem = {
                        'pid': entry.name,
                        'title': title,
                        'content_html': article_html
                    }
                    
                    # 生成HTML
                    html_full = safe_template_format(
                        template,
                        canonical=f'https://luogu.cb-x2-jun.run.place/problem/{entry.name}/',
                        title=title,
                        article=article_html
                    )
                    
                    # 保存HTML
                    with open(entry / 'index.html', 'w', encoding='utf-8') as f:
                        f.write(html_full)
                    
                    print(f"刷新 {entry.name} ...成功")
                    refreshed_count += 1
                    
                except Exception as e:
                    print(f"刷新 {entry.name} ...失败: {e}")
    
    print(f"HTML结构刷新完成，共刷新 {refreshed_count} 个题目。")
    generate_problem_list()

def crawl_specific_problems(problem_list):
    """批量爬取指定题目列表"""
    print(f"批量爬取指定题目，共 {len(problem_list)} 道题...")
    
    # 读取模板
    template_path = PROBLEM_DIR / 'html_template_material.html'
    if template_path.exists():
        with open(template_path, 'r', encoding='utf-8') as f:
            template = f.read()
    else:
        template = '<!doctype html><html><head><title>{title}</title></head><body>{article}</body></html>'
    
    success_count = 0
    sample_count = 0
    
    for i, pid in enumerate(problem_list, 1):
        print(f"[{i}/{len(problem_list)}] 尝试爬取 P{pid} ...", end="")
        problem = fetch_problem_html(pid)
        if problem:
            save_problem_files(pid, problem, template)
            print("成功", end="")
            success_count += 1
            
            # 检查样例数据
            if '## 输入输出样例' in problem['content_md']:
                print(" ✅")
                sample_count += 1
            else:
                print(" ⚠️")
        else:
            print('失败')
        
        # 添加延迟避免被封
        if i < len(problem_list):
            time.sleep(1)
    
    print(f"\n批量爬取完成！")
    print(f"成功: {success_count}/{len(problem_list)} 道题")
    print(f"包含样例: {sample_count}/{success_count} 道题")
    
    generate_problem_list()

def crawl_specific_problem(pid):
    """爬取指定题目"""
    crawl_specific_problems([pid])

def main(batch=20, from_head=False):
    """主函数"""
    start_id = 1000 if from_head else get_last_problem_id() + 1
    end_id = start_id + batch
    
    print(f"从 P{start_id} 开始，批量爬取 {batch} 道题...")
    
    # 读取模板
    template_path = PROBLEM_DIR / 'html_template_material.html'
    if template_path.exists():
        with open(template_path, 'r', encoding='utf-8') as f:
            template = f.read()
    else:
        template = '<!doctype html><html><head><title>{title}</title></head><body>{article}</body></html>'
    
    for pid in range(start_id, end_id):
        print(f"尝试爬取 P{pid} ...", end="")
        problem = fetch_problem_html(pid)
        if problem:
            save_problem_files(pid, problem, template)
            print("成功")
        else:
            print('跳过')
        
        pid += 1
        time.sleep(1)  # 添加延迟避免被封

    print('本次批量爬取结束。')
    generate_problem_list()

def generate_problem_list():
    """生成题目列表页面"""
    problem_dirs = [d for d in PROBLEM_DIR.iterdir() if d.is_dir() and re.match(r'^P\d+$', d.name)]
    problem_dirs.sort(key=lambda d: int(d.name[1:]))
    
    # 读取每个题目的标题数据
    problem_data = []
    for d in problem_dirs:
        problem_id = d.name
        title = "题目"  # 默认标题
        
        # 尝试从HTML文件中提取标题
        html_file = d / 'index.html'
        if html_file.exists():
            try:
                with open(html_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                    # 使用BeautifulSoup解析HTML并提取title标题
                    from bs4 import BeautifulSoup
                    soup = BeautifulSoup(content, 'html.parser')
                    title_tag = soup.find('title')
                    if title_tag:
                        full_title = title_tag.get_text().strip()
                        # 去掉重复的题号，例如 "P1001 P1001 A+B Problem" -> "A+B Problem"
                        title = full_title.replace(f'{problem_id} {problem_id} ', '').replace(f'{problem_id} ', '', 1)
                        if not title or title == problem_id:
                            title = "题目"
            except Exception as e:
                print(f"读取 {problem_id} 标题失败: {e}")
                title = "题目"
        
        problem_data.append({
            'id': problem_id,
            'title': title,
            'url': f'../{problem_id}/index.html'
        })
    
    table_rows = '\n'.join([
        f'<tr><td><a href="{p["url"]}">{p["id"]}</a></td></tr>' 
        for p in problem_data
    ])
    
    # 生成包含题目网格和JavaScript的完整页面内容
    table_html = f'''<h1>题目列表</h1>

<!-- 题目统计信息 -->
<div class="problem-stats">
  <p id="problem-count">正在加载题目统计...</p>
</div>

<!-- 题目网格 -->
<div id="problem-grid" class="problem-grid"></div>
<table style="display: none;">
  <thead><tr><th>题号</th></tr></thead>
  <tbody>
{table_rows}
  </tbody>
</table>'''
    
    # 读取模板文件
    template_path = PROBLEM_DIR / 'html_template_material.html'
    if template_path.exists():
        with open(template_path, 'r', encoding='utf-8') as tf:
            template = tf.read()
    else:
        template = '<!doctype html><html><head><title>{title}</title></head><body>{article}</body></html>'
    
    # 生成列表页面
    list_html = safe_template_format(
        template,
        canonical='https://luogu.cb-x2-jun.run.place/problem/list/',
        title='题目列表',
        article=table_html
    )
    
    # 添加题目网格的CSS和JavaScript
    additional_css = '''
      /* 题目统计信息美化 */
      .problem-stats {
        text-align: center;
        margin: 2rem 0;
        padding: 1rem;
        background: linear-gradient(135deg, #f8f9ff 0%, #e9ecef 100%);
        border-radius: 8px;
        border: 1px solid #dee2e6;
      }
      
      .problem-stats p {
        margin: 0;
        font-size: 1.1rem;
        font-weight: 600;
      }
      
      /* 题目网格布局 */
      .problem-grid {
        display: grid;
        grid-template-columns: repeat(auto-fill, minmax(350px, 1fr));
        gap: 1.5rem;
        margin: 2rem 0;
      }
      
      .problem-card {
        background: linear-gradient(135deg, #ffffff 0%, #f8f9ff 100%);
        color: #2c3e50;
        padding: 1.5rem;
        border-radius: 12px;
        text-decoration: none;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
        border: 1px solid #e1e8ed;
        transition: all 0.3s;
        position: relative;
        overflow: hidden;
        display: flex;
        flex-direction: column;
        align-items: flex-start;
      }
      
      .problem-id {
        font-weight: bold;
        font-size: 1.2rem;
        margin-bottom: 0.5rem;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 0.3rem 0.8rem;
        border-radius: 20px;
        align-self: flex-start;
      }
      
      .problem-title {
        font-size: 1rem;
        font-weight: 500;
        line-height: 1.4;
        color: #5a6c7d;
      }
      
      .problem-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 30px rgba(0, 0, 0, 0.15);
        border-color: #667eea;
      }
      
      /* 动画效果 */
      @keyframes fadeInUp {
        from {
          opacity: 0;
          transform: translateY(30px);
        }
        to {
          opacity: 1;
          transform: translateY(0);
        }
      }
    '''
    
    # 生成包含题目网格和JavaScript的完整页面内容
    table_html = f'''<h1>题目列表</h1>

<!-- 题目统计信息 -->
<div class="problem-stats">
  <p id="problem-count">正在加载题目统计...</p>
</div>

<!-- 题目网格 -->
<div id="problem-grid" class="problem-grid"></div>
'''
    
    # 读取模板文件
    template_path = PROBLEM_DIR / 'html_template_material.html'
    if template_path.exists():
        with open(template_path, 'r', encoding='utf-8') as tf:
            template = tf.read()
    else:
        template = '<!doctype html><html><head><title>{title}</title></head><body>{article}</body></html>'
    
    # 生成题目数据的JavaScript对象
    problem_data_js = json.dumps(problem_data, ensure_ascii=False)
    
    additional_js = f'''
        // 预加载的题目数据
        const problemData = {problem_data_js};
        
        // 动态生成题目网格
        const problemGrid = document.getElementById('problem-grid');
        const problemCountEl = document.getElementById('problem-count');
        
        if (problemGrid) {{
          const problemCount = problemData.length;
          
          // 更新统计信息
          problemCountEl.textContent = `共收录 ${{problemCount}} 道洛谷题目，持续更新中...`;
          
          // 生成题目卡片
          problemData.forEach((problem, index) => {{
            const card = document.createElement('a');
            card.className = 'problem-card';
            card.href = problem.url;
            
            // 创建题目ID元素
            const idElement = document.createElement('div');
            idElement.className = 'problem-id';
            idElement.textContent = problem.id;
            
            // 创建题目标题元素（使用预加载的数据）
            const titleElement = document.createElement('div');
            titleElement.className = 'problem-title';
            titleElement.textContent = problem.title;
            
            card.appendChild(idElement);
            card.appendChild(titleElement);
            
            // 添加延迟动画效果
            card.style.animationDelay = `${{index * 0.02}}s`;
            card.style.animation = 'fadeInUp 0.6s ease-out forwards';
            
            problemGrid.appendChild(card);
          }});
        }}
    '''
    
    # 生成列表页面
    list_html = safe_template_format(
        template,
        canonical='https://luogu.cb-x2-jun.run.place/problem/list/',
        title='题目列表',
        article=table_html
    )
    
    # 在HTML中插入CSS和JavaScript
    list_html = list_html.replace('</style>', additional_css + '\n      </style>')
    list_html = list_html.replace('});', '});\n        \n        ' + additional_js)
    
    # 修复highlight.js CDN链接
    list_html = list_html.replace(
        'https://cdn.jsdelivr.net/npm/highlight.js@11.9.0/lib/highlight.min.js',
        'https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/highlight.min.js'
    )
    
    # 修复hljs调用，添加安全检查
    list_html = list_html.replace(
        '<script>hljs.highlightAll();</script>',
        '<script>if (typeof hljs !== \'undefined\') { hljs.highlightAll(); }</script>'
    )
    
    # 移除错误的katex.js引用
    list_html = list_html.replace('<script src="/javascripts/katex.js"></script>', '')
    
    list_dir = PROBLEM_DIR / 'list'
    list_dir.mkdir(exist_ok=True)
    with open(list_dir / 'index.html', 'w', encoding='utf-8') as f:
        f.write(list_html)

def show_help():
    """显示帮助信息"""
    print("""
洛谷题目爬取工具使用说明：

用法：
    python fetch_luogu_problems_html2md.py [选项] [批量数量]

选项：
    -f, --from-head         从P1000开始爬取（默认从最后一题继续）
    -r, --refresh           刷新已有题目的HTML结构
    -p, --problem NUM       爬取指定题目（NUM为题目编号，如1098或P1098）
    -b, --batch START-END   批量爬取指定范围的题目（如1098-1128）
    -l, --list NUM1,NUM2... 爬取指定题目列表（用逗号分隔，如1098,1100,1102）
    -h, --help              显示此帮助信息

示例：
    python fetch_luogu_problems_html2md.py 50              # 批量爬取50道题
    python fetch_luogu_problems_html2md.py -f 10           # 从P1000开始爬取10道题
    python fetch_luogu_problems_html2md.py -r              # 刷新所有已有题目
    python fetch_luogu_problems_html2md.py -p 1098         # 爬取P1098题目
    python fetch_luogu_problems_html2md.py -b 1098-1128    # 批量爬取P1098到P1128
    python fetch_luogu_problems_html2md.py -l 1098,1100,1733  # 爬取指定题目列表
""")

if __name__ == '__main__':
    import sys
    
    batch = 20
    from_head = False
    refresh_mode = False
    specific_problem = None
    batch_range = None
    problem_list = None
    
    i = 0
    while i < len(sys.argv[1:]):
        arg = sys.argv[1:][i]
        if arg in ('--from-head', '-f'):
            from_head = True
        elif arg in ('--refresh', '-r'):
            refresh_mode = True
        elif arg in ('--help', '-h'):
            show_help()
            sys.exit(0)
        elif arg in ('--problem', '-p'):
            # 下一个参数应该是题目编号
            if i + 1 < len(sys.argv[1:]):
                next_arg = sys.argv[1:][i + 1]
                if next_arg.isdigit():
                    specific_problem = int(next_arg)
                    i += 1  # 跳过下一个参数
                elif next_arg.startswith('P') and next_arg[1:].isdigit():
                    specific_problem = int(next_arg[1:])
                    i += 1  # 跳过下一个参数
                else:
                    print("错误: --problem 参数后必须跟题目编号")
                    sys.exit(1)
            else:
                print("错误: --problem 参数后必须跟题目编号")
                sys.exit(1)
        elif arg in ('--batch', '-b'):
            # 批量范围参数，格式如 1098-1128
            if i + 1 < len(sys.argv[1:]):
                next_arg = sys.argv[1:][i + 1]
                if '-' in next_arg:
                    try:
                        start_str, end_str = next_arg.split('-', 1)
                        start = int(start_str.replace('P', ''))
                        end = int(end_str.replace('P', ''))
                        if start <= end:
                            batch_range = (start, end)
                            i += 1  # 跳过下一个参数
                        else:
                            print("错误: 起始编号必须小于等于结束编号")
                            sys.exit(1)
                    except ValueError:
                        print("错误: --batch 参数格式错误，应为 START-END")
                        sys.exit(1)
                else:
                    print("错误: --batch 参数格式错误，应为 START-END")
                    sys.exit(1)
            else:
                print("错误: --batch 参数后必须跟范围")
                sys.exit(1)
        elif arg in ('--list', '-l'):
            # 题目列表参数，格式如 1098,1100,1102
            if i + 1 < len(sys.argv[1:]):
                next_arg = sys.argv[1:][i + 1]
                try:
                    problem_list = []
                    for num_str in next_arg.split(','):
                        num_str = num_str.strip().replace('P', '')
                        if num_str.isdigit():
                            problem_list.append(int(num_str))
                        else:
                            print(f"错误: 无效的题目编号 '{num_str}'")
                            sys.exit(1)
                    i += 1  # 跳过下一个参数
                except ValueError:
                    print("错误: --list 参数格式错误")
                    sys.exit(1)
            else:
                print("错误: --list 参数后必须跟题目列表")
                sys.exit(1)
        elif arg.isdigit():
            batch = int(arg)
        i += 1
    
    try:
        if specific_problem:
            crawl_specific_problem(specific_problem)
        elif batch_range:
            start, end = batch_range
            problems = list(range(start, end + 1))
            crawl_specific_problems(problems)
        elif problem_list:
            crawl_specific_problems(problem_list)
        elif refresh_mode:
            refresh_html_files()
        else:
            main(batch, from_head)
    except KeyboardInterrupt:
        print("\n程序被用户中断")
    except Exception as e:
        print(f"程序运行出错: {e}")