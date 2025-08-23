#!/usr/bin/env python3
"""
每日题目统计生成器
生成题目数量、难度分布、标签统计等信息
"""

import os
import json
import datetime
from pathlib import Path
from collections import defaultdict, Counter
import re

def analyze_problems():
    """分析所有题目，生成统计信息"""
    problem_dir = Path('problem')
    stats = {
        'total_problems': 0,
        'problems_with_samples': 0,
        'difficulty_distribution': defaultdict(int),
        'tag_distribution': defaultdict(int),
        'recent_problems': [],
        'problem_lengths': [],
        'math_problems': 0,
        'interactive_problems': 0,
        'update_date': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }
    
    # 遍历所有题目目录
    for problem_path in problem_dir.glob('P*/'):
        if not problem_path.is_dir():
            continue
            
        problem_id = problem_path.name
        md_file = problem_path / 'index.md'
        
        if not md_file.exists():
            continue
            
        stats['total_problems'] += 1
        
        # 读取题目内容
        with open(md_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 检查是否有样例
        if '## 输入输出样例' in content:
            stats['problems_with_samples'] += 1
        
        # 检查是否有数学公式
        if '$' in content or '\\(' in content:
            stats['math_problems'] += 1
        
        # 检查是否是交互题
        if '交互' in content or 'IO交互' in content:
            stats['interactive_problems'] += 1
        
        # 统计题目长度
        stats['problem_lengths'].append(len(content))
        
        # 提取题目编号用于最近题目
        try:
            pid = int(problem_id[1:])  # 去掉P前缀
            stats['recent_problems'].append(pid)
        except ValueError:
            pass
    
    # 计算平均题目长度
    if stats['problem_lengths']:
        stats['avg_problem_length'] = sum(stats['problem_lengths']) // len(stats['problem_lengths'])
    else:
        stats['avg_problem_length'] = 0
    
    # 获取最新的10道题目
    stats['recent_problems'] = sorted(stats['recent_problems'], reverse=True)[:10]
    
    return stats

def generate_stats_json(stats):
    """生成统计信息JSON文件"""
    stats_file = Path('stats') / 'daily_stats.json'
    stats_file.parent.mkdir(exist_ok=True)
    
    with open(stats_file, 'w', encoding='utf-8') as f:
        json.dump(stats, f, ensure_ascii=False, indent=2)
    
    print(f"📊 统计信息已保存到 {stats_file}")

def generate_stats_badge():
    """生成README徽章信息"""
    stats_file = Path('stats') / 'daily_stats.json'
    if not stats_file.exists():
        return
    
    with open(stats_file, 'r', encoding='utf-8') as f:
        stats = json.load(f)
    
    # 生成徽章数据
    badges = {
        'total_problems': stats['total_problems'],
        'problems_with_samples': stats['problems_with_samples'],
        'sample_rate': f"{stats['problems_with_samples'] / stats['total_problems'] * 100:.1f}%" if stats['total_problems'] > 0 else "0%",
        'math_problems': stats['math_problems'],
        'last_update': stats['update_date']
    }
    
    badge_file = Path('stats') / 'badges.json'
    with open(badge_file, 'w', encoding='utf-8') as f:
        json.dump(badges, f, ensure_ascii=False, indent=2)
    
    print(f"🏆 徽章信息已保存到 {badge_file}")

def main():
    print("🚀 开始生成每日统计信息...")
    
    # 分析题目
    stats = analyze_problems()
    
    # 生成统计文件
    generate_stats_json(stats)
    generate_stats_badge()
    
    # 打印统计摘要
    print("\n📈 统计摘要:")
    print(f"  总题目数: {stats['total_problems']}")
    print(f"  有样例题目: {stats['problems_with_samples']}")
    print(f"  样例覆盖率: {stats['problems_with_samples'] / stats['total_problems'] * 100:.1f}%" if stats['total_problems'] > 0 else "  样例覆盖率: 0%")
    print(f"  数学题目: {stats['math_problems']}")
    print(f"  交互题目: {stats['interactive_problems']}")
    print(f"  平均题目长度: {stats['avg_problem_length']} 字符")
    print(f"  最新题目: P{max(stats['recent_problems']) if stats['recent_problems'] else 'N/A'}")
    
    print("\n✅ 每日统计生成完成!")

if __name__ == '__main__':
    main()
