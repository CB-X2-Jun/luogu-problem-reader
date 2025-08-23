#!/usr/bin/env python3
"""
首页统计更新器 - 动态更新首页的统计信息
"""

import json
import datetime
from pathlib import Path
import re

def load_stats():
    """加载最新的统计数据"""
    stats_dir = Path('stats')
    
    # 默认统计数据
    default_stats = {
        'total_problems': 0,
        'sample_coverage': 0.0,
        'math_problems': 0,
        'interactive_problems': 0,
        'last_update': datetime.datetime.now().strftime('%Y年%m月%d日')
    }
    
    # 尝试加载每日统计
    daily_stats_file = stats_dir / 'daily_stats.json'
    if daily_stats_file.exists():
        try:
            with open(daily_stats_file, 'r', encoding='utf-8') as f:
                daily_stats = json.load(f)
                return {
                    'total_problems': daily_stats.get('total_problems', 0),
                    'sample_coverage': daily_stats.get('sample_coverage_percent', 0.0),
                    'math_problems': daily_stats.get('math_problems', 0),
                    'interactive_problems': daily_stats.get('interactive_problems', 0),
                    'last_update': daily_stats.get('date', default_stats['last_update'])
                }
        except:
            pass
    
    # 如果没有统计文件，手动计算
    return calculate_stats()

def calculate_stats():
    """手动计算统计数据"""
    problem_dir = Path('problem')
    total_problems = 0
    problems_with_samples = 0
    math_problems = 0
    interactive_problems = 0
    
    for problem_path in problem_dir.glob('P*/'):
        if not problem_path.is_dir():
            continue
            
        md_file = problem_path / 'index.md'
        if not md_file.exists():
            continue
        
        total_problems += 1
        
        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # 检查是否有样例
            if '## 输入输出样例' in content:
                problems_with_samples += 1
            
            # 检查是否是数学题
            if '$' in content or '\\(' in content:
                math_problems += 1
            
            # 检查是否是交互题
            if '交互' in content or 'IO交互' in content:
                interactive_problems += 1
                
        except:
            continue
    
    sample_coverage = (problems_with_samples / total_problems * 100) if total_problems > 0 else 0
    
    return {
        'total_problems': total_problems,
        'sample_coverage': round(sample_coverage, 1),
        'math_problems': math_problems,
        'interactive_problems': interactive_problems,
        'last_update': datetime.datetime.now().strftime('%Y年%m月%d日')
    }

def load_theme_info():
    """加载主题信息"""
    stats_dir = Path('stats')
    theme_file = stats_dir / 'theme_info.json'
    
    default_theme = {
        'recommended_theme': 'summer',
        'theme_display': '夏季 🌞'
    }
    
    if theme_file.exists():
        try:
            with open(theme_file, 'r', encoding='utf-8') as f:
                theme_info = json.load(f)
                
                theme_map = {
                    'spring': '春季 🌸',
                    'summer': '夏季 🌞',
                    'autumn': '秋季 🍂',
                    'winter': '冬季 ❄️',
                    'chinese_new_year': '春节 🧧',
                    'christmas': '圣诞 🎄',
                    'halloween': '万圣节 🎃'
                }
                
                theme = theme_info.get('recommended_theme', 'summer')
                return {
                    'recommended_theme': theme,
                    'theme_display': theme_map.get(theme, '夏季 🌞')
                }
        except:
            pass
    
    return default_theme

def count_sitemap_urls():
    """统计sitemap中的URL数量"""
    sitemap_file = Path('sitemap.xml')
    if sitemap_file.exists():
        try:
            with open(sitemap_file, 'r', encoding='utf-8') as f:
                content = f.read()
                # 计算<url>标签数量
                url_count = content.count('<url>')
                return url_count
        except:
            pass
    
    return 1383  # 默认值

def update_homepage_stats():
    """更新首页统计信息"""
    index_file = Path('index.html')
    if not index_file.exists():
        print("❌ index.html 文件不存在")
        return False
    
    # 加载数据
    stats = load_stats()
    theme_info = load_theme_info()
    sitemap_urls = count_sitemap_urls()
    
    print(f"📊 加载统计数据:")
    print(f"   题目总数: {stats['total_problems']}")
    print(f"   样例覆盖率: {stats['sample_coverage']}%")
    print(f"   数学题目: {stats['math_problems']}")
    print(f"   交互题目: {stats['interactive_problems']}")
    print(f"   当前主题: {theme_info['theme_display']}")
    print(f"   SEO URLs: {sitemap_urls}")
    
    # 读取首页内容
    with open(index_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 更新统计数据
    replacements = [
        # 实时统计面板
        (r'<div style="font-size: 2\.5rem; font-weight: bold; margin-bottom: 0\.5rem;">\d+</div>\s*<div style="opacity: 0\.9;">题目总数</div>',
         f'<div style="font-size: 2.5rem; font-weight: bold; margin-bottom: 0.5rem;">{stats["total_problems"]}</div>\n          <div style="opacity: 0.9;">题目总数</div>'),
        
        (r'<div style="font-size: 2\.5rem; font-weight: bold; margin-bottom: 0\.5rem;">\d+\.?\d*%</div>\s*<div style="opacity: 0\.9;">样例覆盖率</div>',
         f'<div style="font-size: 2.5rem; font-weight: bold; margin-bottom: 0.5rem;">{stats["sample_coverage"]}%</div>\n          <div style="opacity: 0.9;">样例覆盖率</div>'),
        
        (r'<div style="font-size: 2\.5rem; font-weight: bold; margin-bottom: 0\.5rem;">\d+</div>\s*<div style="opacity: 0\.9;">数学题目</div>',
         f'<div style="font-size: 2.5rem; font-weight: bold; margin-bottom: 0.5rem;">{stats["math_problems"]}</div>\n          <div style="opacity: 0.9;">数学题目</div>'),
        
        (r'<div style="font-size: 2\.5rem; font-weight: bold; margin-bottom: 0\.5rem;">\d+</div>\s*<div style="opacity: 0\.9;">交互题目</div>',
         f'<div style="font-size: 2.5rem; font-weight: bold; margin-bottom: 0.5rem;">{stats["interactive_problems"]}</div>\n          <div style="opacity: 0.9;">交互题目</div>'),
        
        # 更新时间
        (r'📅 最后更新: \d{4}年\d{1,2}月\d{1,2}日',
         f'📅 最后更新: {stats["last_update"]}'),
        
        # 主题信息
        (r'<span style="background: #3498db; color: white; padding: 0\.2rem 0\.8rem; border-radius: 12px; font-size: 0\.8rem;">[^<]+</span>',
         f'<span style="background: #3498db; color: white; padding: 0.2rem 0.8rem; border-radius: 12px; font-size: 0.8rem;">{theme_info["theme_display"]}</span>'),
        
        # SEO URL数量
        (r'<span style="background: #28a745; color: white; padding: 0\.2rem 0\.8rem; border-radius: 12px; font-size: 0\.8rem;">\d+</span>',
         f'<span style="background: #28a745; color: white; padding: 0.2rem 0.8rem; border-radius: 12px; font-size: 0.8rem;">{sitemap_urls}</span>')
    ]
    
    # 应用替换
    updated_content = content
    for pattern, replacement in replacements:
        updated_content = re.sub(pattern, replacement, updated_content)
    
    # 保存更新后的内容
    with open(index_file, 'w', encoding='utf-8') as f:
        f.write(updated_content)
    
    print("✅ 首页统计信息更新完成!")
    return True

def main():
    print("🔄 开始更新首页统计信息...")
    
    success = update_homepage_stats()
    
    if success:
        print("\n✅ 首页统计信息更新成功!")
    else:
        print("\n❌ 首页统计信息更新失败!")

if __name__ == '__main__':
    main()
