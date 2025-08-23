#!/usr/bin/env python3
"""
图表生成器 - 生成各种数据可视化图表
"""

import json
import os
from pathlib import Path
from collections import Counter, defaultdict
import re

def load_problem_data():
    """加载题目数据进行分析"""
    problem_dir = Path('problem')
    problems_data = []
    
    for problem_path in problem_dir.glob('P*/'):
        if not problem_path.is_dir():
            continue
            
        problem_id = problem_path.name
        md_file = problem_path / 'index.md'
        
        if not md_file.exists():
            continue
        
        with open(md_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 提取题目信息
        problem_info = {
            'id': problem_id,
            'content_length': len(content),
            'has_samples': '## 输入输出样例' in content,
            'has_math': '$' in content or '\\(' in content,
            'is_interactive': '交互' in content or 'IO交互' in content,
            'tags': extract_tags(content),
            'difficulty_hints': extract_difficulty_hints(content)
        }
        
        problems_data.append(problem_info)
    
    return problems_data

def extract_tags(content):
    """从题目内容中提取标签"""
    tags = []
    
    # 基于关键词提取标签
    if '动态规划' in content or 'DP' in content:
        tags.append('动态规划')
    if '图论' in content or '最短路' in content or '拓扑排序' in content:
        tags.append('图论')
    if '数学' in content or '数论' in content:
        tags.append('数学')
    if '字符串' in content or 'KMP' in content:
        tags.append('字符串')
    if '贪心' in content:
        tags.append('贪心')
    if '搜索' in content or 'DFS' in content or 'BFS' in content:
        tags.append('搜索')
    if '排序' in content:
        tags.append('排序')
    if '模拟' in content:
        tags.append('模拟')
    
    return tags

def extract_difficulty_hints(content):
    """提取难度提示"""
    hints = []
    
    if 'NOIP' in content:
        if '普及' in content:
            hints.append('NOIP普及')
        elif '提高' in content:
            hints.append('NOIP提高')
        else:
            hints.append('NOIP')
    
    if 'NOI' in content and 'NOIP' not in content:
        hints.append('NOI')
    
    if 'USACO' in content:
        hints.append('USACO')
    
    return hints

def generate_svg_chart(data, title, filename):
    """生成SVG格式的图表"""
    # 简单的SVG条形图生成
    width = 800
    height = 400
    margin = 60
    
    # 计算数据
    if isinstance(data, dict):
        labels = list(data.keys())[:10]  # 只显示前10项
        values = [data[label] for label in labels]
    else:
        labels = [str(i) for i in range(len(data))]
        values = data
    
    if not values:
        return
    
    max_value = max(values) if values else 1
    bar_width = (width - 2 * margin) / len(values)
    
    # 生成SVG
    svg_content = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg width="{width}" height="{height}" xmlns="http://www.w3.org/2000/svg">
    <style>
        .title {{ font: bold 16px sans-serif; text-anchor: middle; }}
        .label {{ font: 12px sans-serif; text-anchor: middle; }}
        .bar {{ fill: #3498db; }}
        .bar:hover {{ fill: #2980b9; }}
    </style>
    
    <!-- 标题 -->
    <text x="{width/2}" y="30" class="title">{title}</text>
    
    <!-- 条形图 -->
'''
    
    for i, (label, value) in enumerate(zip(labels, values)):
        x = margin + i * bar_width
        bar_height = (value / max_value) * (height - 2 * margin - 40) if max_value > 0 else 0
        y = height - margin - bar_height
        
        svg_content += f'''
    <rect x="{x + 5}" y="{y}" width="{bar_width - 10}" height="{bar_height}" class="bar"/>
    <text x="{x + bar_width/2}" y="{height - margin + 15}" class="label">{label}</text>
    <text x="{x + bar_width/2}" y="{y - 5}" class="label">{value}</text>
'''
    
    svg_content += '</svg>'
    
    # 保存文件
    charts_dir = Path('charts')
    charts_dir.mkdir(exist_ok=True)
    
    with open(charts_dir / filename, 'w', encoding='utf-8') as f:
        f.write(svg_content)

def generate_difficulty_chart(problems_data):
    """生成难度分布图"""
    difficulty_count = Counter()
    
    for problem in problems_data:
        if problem['difficulty_hints']:
            for hint in problem['difficulty_hints']:
                difficulty_count[hint] += 1
        else:
            difficulty_count['其他'] += 1
    
    generate_svg_chart(difficulty_count, '题目难度分布', 'difficulty_distribution.svg')
    print("📊 难度分布图已生成")

def generate_tag_chart(problems_data):
    """生成标签分布图"""
    tag_count = Counter()
    
    for problem in problems_data:
        for tag in problem['tags']:
            tag_count[tag] += 1
    
    # 只显示前10个标签
    top_tags = dict(tag_count.most_common(10))
    
    generate_svg_chart(top_tags, '题目标签分布 (Top 10)', 'tag_distribution.svg')
    print("🏷️ 标签分布图已生成")

def generate_feature_chart(problems_data):
    """生成特征分布图"""
    features = {
        '有样例': sum(1 for p in problems_data if p['has_samples']),
        '数学题': sum(1 for p in problems_data if p['has_math']),
        '交互题': sum(1 for p in problems_data if p['is_interactive']),
        '普通题': len(problems_data) - sum(1 for p in problems_data if p['has_math'] or p['is_interactive'])
    }
    
    generate_svg_chart(features, '题目特征分布', 'feature_distribution.svg')
    print("🎯 特征分布图已生成")

def generate_length_histogram(problems_data):
    """生成题目长度分布直方图"""
    lengths = [p['content_length'] for p in problems_data]
    
    # 分组统计
    bins = [0, 500, 1000, 1500, 2000, 3000, 5000, float('inf')]
    bin_labels = ['<500', '500-1K', '1K-1.5K', '1.5K-2K', '2K-3K', '3K-5K', '>5K']
    
    length_dist = {}
    for i, (start, end) in enumerate(zip(bins[:-1], bins[1:])):
        count = sum(1 for length in lengths if start <= length < end)
        length_dist[bin_labels[i]] = count
    
    generate_svg_chart(length_dist, '题目长度分布', 'length_distribution.svg')
    print("📏 长度分布图已生成")

def save_chart_index():
    """生成图表索引页面"""
    charts_dir = Path('charts')
    if not charts_dir.exists():
        return
    
    html_content = '''<!DOCTYPE html>
<html lang="zh">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>数据可视化 - 洛谷题目浏览站</title>
    <style>
        body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; margin: 0; padding: 20px; background: #f8f9fa; }
        .container { max-width: 1200px; margin: 0 auto; }
        h1 { color: #2c3e50; text-align: center; margin-bottom: 2rem; }
        .chart-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(400px, 1fr)); gap: 2rem; }
        .chart-card { background: white; border-radius: 8px; padding: 1.5rem; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }
        .chart-card h3 { margin-top: 0; color: #34495e; }
        .chart-card svg { width: 100%; height: auto; }
        .back-link { display: inline-block; margin-bottom: 2rem; color: #3498db; text-decoration: none; }
        .back-link:hover { text-decoration: underline; }
    </style>
</head>
<body>
    <div class="container">
        <a href="../" class="back-link">← 返回主页</a>
        <h1>📊 数据可视化</h1>
        <div class="chart-grid">
'''
    
    charts = [
        ('difficulty_distribution.svg', '题目难度分布', '展示不同难度级别题目的数量分布'),
        ('tag_distribution.svg', '题目标签分布', '展示最受欢迎的题目标签'),
        ('feature_distribution.svg', '题目特征分布', '展示题目的各种特征统计'),
        ('length_distribution.svg', '题目长度分布', '展示题目内容长度的分布情况')
    ]
    
    for filename, title, description in charts:
        if (charts_dir / filename).exists():
            html_content += f'''
            <div class="chart-card">
                <h3>{title}</h3>
                <p style="color: #7f8c8d; margin-bottom: 1rem;">{description}</p>
                <object data="{filename}" type="image/svg+xml" style="width: 100%; height: 300px;"></object>
            </div>
'''
    
    html_content += '''
        </div>
    </div>
</body>
</html>'''
    
    with open(charts_dir / 'index.html', 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print("📄 图表索引页面已生成")

def main():
    print("📊 开始生成数据可视化图表...")
    
    # 加载数据
    problems_data = load_problem_data()
    print(f"📚 已加载 {len(problems_data)} 道题目数据")
    
    # 生成各种图表
    generate_difficulty_chart(problems_data)
    generate_tag_chart(problems_data)
    generate_feature_chart(problems_data)
    generate_length_histogram(problems_data)
    
    # 生成索引页面
    save_chart_index()
    
    print("\n✅ 数据可视化图表生成完成!")

if __name__ == '__main__':
    main()
