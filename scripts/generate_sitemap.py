#!/usr/bin/env python3
"""
Sitemap生成器 - 自动生成网站地图
"""

import datetime
from pathlib import Path
import xml.etree.ElementTree as ET

def generate_sitemap():
    """生成sitemap.xml"""
    # 创建根元素
    urlset = ET.Element('urlset')
    urlset.set('xmlns', 'http://www.sitemaps.org/schemas/sitemap/0.9')
    
    base_url = 'https://luogu.cb-x2-jun.run.place'
    current_date = datetime.datetime.now().strftime('%Y-%m-%d')
    
    # 添加主页
    url = ET.SubElement(urlset, 'url')
    ET.SubElement(url, 'loc').text = f'{base_url}/'
    ET.SubElement(url, 'lastmod').text = current_date
    ET.SubElement(url, 'changefreq').text = 'daily'
    ET.SubElement(url, 'priority').text = '1.0'
    
    # 添加题目列表页
    url = ET.SubElement(urlset, 'url')
    ET.SubElement(url, 'loc').text = f'{base_url}/problem/list/'
    ET.SubElement(url, 'lastmod').text = current_date
    ET.SubElement(url, 'changefreq').text = 'daily'
    ET.SubElement(url, 'priority').text = '0.9'
    
    # 添加所有题目页面
    problem_dir = Path('problem')
    problem_count = 0
    
    for problem_path in sorted(problem_dir.glob('P*/')):
        if not problem_path.is_dir():
            continue
            
        problem_id = problem_path.name
        md_file = problem_path / 'index.md'
        html_file = problem_path / 'index.html'
        
        if not md_file.exists() or not html_file.exists():
            continue
        
        # 获取文件修改时间
        mod_time = datetime.datetime.fromtimestamp(html_file.stat().st_mtime)
        lastmod = mod_time.strftime('%Y-%m-%d')
        
        url = ET.SubElement(urlset, 'url')
        ET.SubElement(url, 'loc').text = f'{base_url}/problem/{problem_id}/'
        ET.SubElement(url, 'lastmod').text = lastmod
        ET.SubElement(url, 'changefreq').text = 'weekly'
        ET.SubElement(url, 'priority').text = '0.8'
        
        problem_count += 1
    
    # 格式化XML
    def indent(elem, level=0):
        i = "\n" + level*"  "
        if len(elem):
            if not elem.text or not elem.text.strip():
                elem.text = i + "  "
            if not elem.tail or not elem.tail.strip():
                elem.tail = i
            for elem in elem:
                indent(elem, level+1)
            if not elem.tail or not elem.tail.strip():
                elem.tail = i
        else:
            if level and (not elem.tail or not elem.tail.strip()):
                elem.tail = i
    
    indent(urlset)
    
    # 保存sitemap
    tree = ET.ElementTree(urlset)
    tree.write('sitemap.xml', encoding='utf-8', xml_declaration=True)
    
    print(f"🗺️ Sitemap已生成，包含 {problem_count + 2} 个URL")
    return problem_count + 2

def generate_robots_txt():
    """生成robots.txt"""
    robots_content = """User-agent: *
Allow: /

# Sitemap
Sitemap: https://luogu.cb-x2-jun.run.place/sitemap.xml

# 优化爬虫行为
Crawl-delay: 1

# 允许访问所有题目
Allow: /problem/
Allow: /problem/list/

# 统计文件可以被索引
Allow: /stats/
"""
    
    with open('robots.txt', 'w', encoding='utf-8') as f:
        f.write(robots_content)
    
    print("🤖 robots.txt已生成")

def main():
    print("🚀 开始生成SEO文件...")
    
    url_count = generate_sitemap()
    generate_robots_txt()
    
    print(f"\n✅ SEO文件生成完成！共 {url_count} 个URL")

if __name__ == '__main__':
    main()
