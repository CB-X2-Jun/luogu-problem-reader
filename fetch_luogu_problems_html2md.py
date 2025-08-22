import os
import re
import requests
import time
from pathlib import Path
from bs4 import BeautifulSoup
from markdownify import markdownify as md

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
        
        # 手动预处理代码块 - 使用相同的字符串处理方法
        def preprocess_code_blocks(text):
            lines = text.split('\n')
            result_lines = []
            in_code_block = False
            code_block_content = []
            
            for line in lines:
                if line.strip().startswith('```'):
                    if not in_code_block:
                        # 开始代码块
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
        
        # 预处理Markdown内容
        processed_md = preprocess_code_blocks(content_md)
        
        # 使用Markdown转换为HTML
        md_parser = markdown.Markdown(extensions=['tables', 'toc', 'sane_lists'])
        content_html = md_parser.convert(processed_md)
        
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
          delimiters: [{"left":"$","right":"$","display":false}],
          throwOnError: false
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
                                    # 开始代码块
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
                    
                    # 先处理代码块，再用markdown处理其他格式
                    processed_content = preprocess_code_blocks(content_to_convert)
                    
                    md_parser = markdown.Markdown(extensions=['tables', 'toc', 'sane_lists'])
                    article_html = md_parser.convert(processed_content)
                    
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
    
    table_rows = '\n'.join([
        f'<tr><td><a href="../{d.name}/index.html">{d.name}</a></td></tr>' 
        for d in problem_dirs
    ])
    
    table_html = f'''<h1>题目列表</h1>
<table>
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
    
    list_dir = PROBLEM_DIR / 'list'
    list_dir.mkdir(exist_ok=True)
    with open(list_dir / 'index.html', 'w', encoding='utf-8') as f:
        f.write(list_html)

if __name__ == '__main__':
    import sys
    
    batch = 20
    from_head = False
    refresh_mode = False
    
    for arg in sys.argv[1:]:
        if arg in ('--from-head', '-f'):
            from_head = True
        elif arg in ('--refresh', '-r'):
            refresh_mode = True
        elif arg.isdigit():
            batch = int(arg)
    
    try:
        if refresh_mode:
            refresh_html_files()
        else:
            main(batch, from_head)
    except KeyboardInterrupt:
        print("\n程序被用户中断")
    except Exception as e:
        print(f"程序运行出错: {e}")