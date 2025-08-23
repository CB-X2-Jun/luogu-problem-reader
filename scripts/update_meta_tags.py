#!/usr/bin/env python3
"""
Meta标签更新器 - 自动优化网站的SEO meta标签
"""

import json
import datetime
from pathlib import Path
import re

def load_problem_stats():
    """加载题目统计信息"""
    stats_dir = Path('stats')
    daily_stats_file = stats_dir / 'daily_stats.json'
    
    default_stats = {
        'total_problems': 1381,
        'sample_coverage_percent': 99.9,
        'math_problems': 1361,
        'interactive_problems': 2
    }
    
    if daily_stats_file.exists():
        try:
            with open(daily_stats_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        except:
            pass
    
    return default_stats

def generate_meta_description(stats):
    """生成动态的meta描述"""
    sample_coverage = stats.get('sample_coverage_percent', stats.get('sample_coverage', 99.9))
    return f"洛谷题目浏览站 - 收录{stats['total_problems']}道洛谷题目，{sample_coverage}%样例覆盖率，包含{stats['math_problems']}道数学题和{stats['interactive_problems']}道交互题。支持代码高亮、数学公式渲染，提供智能推荐和数据可视化。"

def generate_keywords(stats):
    """生成关键词"""
    keywords = [
        "洛谷", "luogu", "题目", "算法", "编程", "竞赛",
        "NOIP", "NOI", "USACO", "数学", "交互题",
        "代码高亮", "数学公式", "KaTeX", "题目浏览",
        "编程学习", "算法练习", "竞赛编程", "OI",
        f"{stats['total_problems']}道题目", "样例完整", "自动化更新"
    ]
    return ", ".join(keywords)

def update_index_meta_tags():
    """更新首页的meta标签"""
    index_file = Path('index.html')
    if not index_file.exists():
        print("❌ index.html 文件不存在")
        return False
    
    stats = load_problem_stats()
    
    with open(index_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 生成新的meta信息
    new_description = generate_meta_description(stats)
    new_keywords = generate_keywords(stats)
    current_date = datetime.datetime.now().strftime('%Y-%m-%d')
    
    # 更新或添加meta标签
    meta_updates = [
        # 更新description
        (r'<meta name="description" content="[^"]*">', 
         f'<meta name="description" content="{new_description}">'),
        
        # 添加或更新keywords
        (r'<meta name="keywords" content="[^"]*">',
         f'<meta name="keywords" content="{new_keywords}">'),
        
        # 更新author
        (r'<meta name="author" content="[^"]*">',
         '<meta name="author" content="CB_X2_Jun - 洛谷题目浏览站">'),
    ]
    
    updated_content = content
    
    # 应用meta标签更新
    for pattern, replacement in meta_updates:
        if re.search(pattern, updated_content):
            updated_content = re.sub(pattern, replacement, updated_content)
        else:
            # 如果meta标签不存在，添加到head部分
            if 'keywords' in replacement:
                head_pattern = r'(<meta name="description"[^>]*>)'
                updated_content = re.sub(head_pattern, f'\\1\n      <meta name="keywords" content="{new_keywords}">', updated_content)
    
    # 添加Open Graph标签（如果不存在）
    og_tags = f'''
      <!-- Open Graph / Facebook -->
      <meta property="og:type" content="website">
      <meta property="og:url" content="https://luogu.cb-x2-jun.run.place/">
      <meta property="og:title" content="洛谷题目浏览站 - {stats['total_problems']}道题目在线浏览">
      <meta property="og:description" content="{new_description}">
      <meta property="og:image" content="https://luogu.cb-x2-jun.run.place/assets/images/og-image.png">

      <!-- Twitter -->
      <meta property="twitter:card" content="summary_large_image">
      <meta property="twitter:url" content="https://luogu.cb-x2-jun.run.place/">
      <meta property="twitter:title" content="洛谷题目浏览站 - {stats['total_problems']}道题目在线浏览">
      <meta property="twitter:description" content="{new_description}">
      <meta property="twitter:image" content="https://luogu.cb-x2-jun.run.place/assets/images/og-image.png">

      <!-- 其他SEO标签 -->
      <meta name="robots" content="index, follow">
      <meta name="googlebot" content="index, follow">
      <meta name="revisit-after" content="1 days">
      <meta name="last-modified" content="{current_date}">'''
    
    # 检查是否已有OG标签，如果没有则添加
    if 'property="og:type"' not in updated_content:
        # 在canonical link后添加OG标签
        canonical_pattern = r'(<link rel="canonical"[^>]*>)'
        updated_content = re.sub(canonical_pattern, f'\\1{og_tags}', updated_content)
    
    # 保存更新后的内容
    with open(index_file, 'w', encoding='utf-8') as f:
        f.write(updated_content)
    
    print("✅ 首页meta标签更新完成!")
    return True

def update_problem_pages_meta():
    """批量更新题目页面的meta标签"""
    problem_dir = Path('problem')
    updated_count = 0
    
    for problem_path in problem_dir.glob('P*/'):
        if not problem_path.is_dir():
            continue
            
        html_file = problem_path / 'index.html'
        if not html_file.exists():
            continue
        
        try:
            with open(html_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # 提取题目标题
            title_match = re.search(r'<title>([^<]+)</title>', content)
            if not title_match:
                continue
                
            problem_title = title_match.group(1)
            problem_id = problem_path.name
            
            # 生成题目页面的meta描述
            problem_description = f"洛谷{problem_id} {problem_title} - 完整题目描述、输入输出样例、代码高亮、数学公式渲染。洛谷题目浏览站提供优质的编程学习资源。"
            
            # 更新meta描述
            if '<meta name="description"' in content:
                content = re.sub(r'<meta name="description" content="[^"]*">', 
                               f'<meta name="description" content="{problem_description}">', content)
            else:
                # 添加meta描述
                head_pattern = r'(<meta charset="UTF-8">)'
                content = re.sub(head_pattern, f'\\1\n    <meta name="description" content="{problem_description}">', content)
            
            # 添加keywords
            problem_keywords = f"洛谷, {problem_id}, {problem_title}, 算法, 编程, 题目, 样例, 代码高亮"
            if '<meta name="keywords"' not in content:
                desc_pattern = r'(<meta name="description"[^>]*>)'
                content = re.sub(desc_pattern, f'\\1\n    <meta name="keywords" content="{problem_keywords}">', content)
            
            # 保存更新后的内容
            with open(html_file, 'w', encoding='utf-8') as f:
                f.write(content)
            
            updated_count += 1
            
        except Exception as e:
            print(f"⚠️ 更新 {problem_id} 失败: {e}")
            continue
    
    print(f"✅ 批量更新了 {updated_count} 个题目页面的meta标签!")
    return updated_count

def update_list_page_meta():
    """更新题目列表页面的meta标签"""
    list_file = Path('problem/list/index.html')
    if not list_file.exists():
        print("❌ 题目列表页面不存在")
        return False
    
    stats = load_problem_stats()
    
    with open(list_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 生成列表页面的meta描述
    sample_coverage = stats.get('sample_coverage_percent', stats.get('sample_coverage', 99.9))
    list_description = f"洛谷题目列表 - 浏览全部{stats['total_problems']}道洛谷题目，支持快速搜索和筛选。包含NOIP、NOI、USACO等各类竞赛题目，{sample_coverage}%样例覆盖率。"
    
    # 更新meta标签
    if '<meta name="description"' in content:
        content = re.sub(r'<meta name="description" content="[^"]*">', 
                       f'<meta name="description" content="{list_description}">', content)
    else:
        # 在title后添加meta描述
        title_pattern = r'(<title>[^<]+</title>)'
        content = re.sub(title_pattern, f'\\1\n    <meta name="description" content="{list_description}">', content)
    
    # 保存更新后的内容
    with open(list_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("✅ 题目列表页面meta标签更新完成!")
    return True

def main():
    print("🔍 开始更新网站SEO meta标签...")
    
    stats = load_problem_stats()
    sample_coverage = stats.get('sample_coverage_percent', stats.get('sample_coverage', 99.9))
    print(f"📊 当前统计: {stats['total_problems']}道题目, {sample_coverage}%样例覆盖率")
    
    # 更新首页meta标签
    update_index_meta_tags()
    
    # 更新题目列表页面meta标签
    update_list_page_meta()
    
    # 批量更新题目页面meta标签（可选，因为数量较多）
    # update_problem_pages_meta()
    
    print("\n✅ SEO meta标签更新完成!")

if __name__ == '__main__':
    main()
