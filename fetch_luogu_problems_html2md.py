import os
import re
import requests
from pathlib import Path
from bs4 import BeautifulSoup
from markdownify import markdownify as md

PROBLEM_DIR = Path(__file__).parent / 'problem'
BASE_URL = 'https://www.luogu.com.cn/problem/'

# 获取所有已存在的题号，返回最大题号编号（如P1000->1000）
def get_last_problem_id():
    ids = []
    for entry in PROBLEM_DIR.iterdir():
        m = re.match(r'P(\\d+)$', entry.name)
        if m:
            ids.append(int(m.group(1)))
    return max(ids) if ids else 999  # 洛谷题号从P1000开始

def fetch_problem_html(pid):
    url = f'{BASE_URL}P{pid}'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
        "Referer": "https://www.luogu.com.cn/",
        "Accept-Language": "zh-CN,zh;q=0.9"
    }
    resp = requests.get(url, headers=headers)
    if resp.status_code != 200:
        return None
    soup = BeautifulSoup(resp.text, 'html.parser')
    # 题号和标题
    title_tag = soup.find('h1', {'id': f'P{pid}'})
    if not title_tag:
        # 兼容部分页面标题结构
        title_tag = soup.find('h1')
    title = title_tag.text.strip() if title_tag else f'P{pid}'
    # 题面内容区域（兼容洛谷实际结构）
    article = soup.find('article')
    if not article:
        return None
    # 转为markdown
    content_md = md(str(article), heading_style="ATX")
    return {
        'pid': f'P{pid}',
        'title': title,
        'content_md': content_md,
        'content_html': str(article)
    }

def generate_md(problem):
    pid = problem['pid']
    title = problem['title']
    content_md = problem['content_md']
    tpl = f"""# {pid} {title}\n\n{content_md}\n"""
    return tpl

def main(batch=20, from_head=False):
    PROBLEM_DIR.mkdir(exist_ok=True)
    if from_head:
        pid = 1000
        print(f"从 P1000 开始，批量爬取 {batch} 道题...")
    else:
        last_id = get_last_problem_id()
        pid = last_id + 1
        print(f"从 P{last_id+1} 开始，批量爬取 {batch} 道题...")
    count = 0
    while count < batch:
        out_dir = PROBLEM_DIR / f'P{pid}'
        out_file = out_dir / 'index.md'
        if not from_head and out_file.exists():
            print(f"P{pid} 已存在，自动跳过")
            pid += 1
            continue
        print(f"尝试爬取 P{pid} ...", end='')
        problem = fetch_problem_html(pid)
        if problem:
            out_dir.mkdir(exist_ok=True)
            md_text = generate_md(problem)
            html_file = out_dir / 'index.html'
            # 保存 Markdown
            with open(out_file, 'w', encoding='utf-8') as f:
                f.write(md_text)
            # 保存 mkdocs-material 风格完整 HTML
            html_content = problem.get('content_html', '')
            # 读取模板
            template_path = PROBLEM_DIR / 'html_template_material.html'
            if template_path.exists():
                with open(template_path, 'r', encoding='utf-8') as tf:
                    template = tf.read()
            else:
                template = '<!doctype html><html><head><title>{title}</title></head><body>{article}</body></html>'
            canonical = f'https://luogu.cb-x2-jun.run.place/problem/P{pid}/'
            html_full = template.format(
                canonical=canonical,
                title=problem['title'],
                article=html_content
            )
            with open(html_file, 'w', encoding='utf-8') as f:
                f.write(html_full)
            print('成功')
            count += 1
        else:
            print('跳过')
        pid += 1
    print('本次批量爬取结束。')

if __name__ == '__main__':
    import sys
    batch = 20
    from_head = False
    for arg in sys.argv[1:]:
        if arg in ('--from-head', '-f'):
            from_head = True
        elif arg.isdigit():
            batch = int(arg)
    main(batch, from_head)
