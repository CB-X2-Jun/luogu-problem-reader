#!/usr/bin/env python3
"""
每日题目推荐生成器
基于算法智能推荐每日题目
"""

import os
import json
import random
import datetime
from pathlib import Path
import hashlib

def get_daily_seed():
    """基于日期生成每日种子，确保同一天推荐相同题目"""
    today = datetime.date.today().strftime('%Y-%m-%d')
    return int(hashlib.md5(today.encode()).hexdigest()[:8], 16)

def load_problem_list():
    """加载所有可用题目列表"""
    problem_dir = Path('problem')
    problems = []
    
    for problem_path in problem_dir.glob('P*/'):
        if not problem_path.is_dir():
            continue
            
        problem_id = problem_path.name
        md_file = problem_path / 'index.md'
        
        if not md_file.exists():
            continue
        
        # 读取题目信息
        with open(md_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 提取题目标题
        title_match = content.split('\n')[0] if content else problem_id
        if title_match.startswith('# '):
            title = title_match[2:].strip()
        else:
            title = problem_id
        
        # 分析题目特征
        features = {
            'id': problem_id,
            'title': title,
            'has_samples': '## 输入输出样例' in content,
            'has_math': '$' in content or '\\(' in content,
            'is_interactive': '交互' in content or 'IO交互' in content,
            'length': len(content),
            'difficulty_hints': []
        }
        
        # 简单的难度推测
        if 'NOIP' in content:
            features['difficulty_hints'].append('NOIP')
        if '动态规划' in content or 'DP' in content:
            features['difficulty_hints'].append('DP')
        if '图论' in content:
            features['difficulty_hints'].append('图论')
        if '数学' in content:
            features['difficulty_hints'].append('数学')
        
        problems.append(features)
    
    return problems

def select_daily_problems(problems, count=3):
    """选择每日推荐题目"""
    if not problems:
        return []
    
    # 使用每日种子确保稳定性
    random.seed(get_daily_seed())
    
    # 分类题目
    math_problems = [p for p in problems if p['has_math']]
    interactive_problems = [p for p in problems if p['is_interactive']]
    sample_problems = [p for p in problems if p['has_samples']]
    regular_problems = [p for p in problems if not p['is_interactive']]
    
    selected = []
    
    # 策略1: 选择一道数学题
    if math_problems:
        selected.append(random.choice(math_problems))
    
    # 策略2: 选择一道有完整样例的题目
    if sample_problems and len(selected) < count:
        candidates = [p for p in sample_problems if p not in selected]
        if candidates:
            selected.append(random.choice(candidates))
    
    # 策略3: 填充剩余位置
    while len(selected) < count:
        candidates = [p for p in regular_problems if p not in selected]
        if not candidates:
            break
        selected.append(random.choice(candidates))
    
    return selected[:count]

def generate_recommendation_html(problems):
    """生成推荐题目的HTML片段"""
    if not problems:
        return "<p>暂无推荐题目</p>"
    
    today = datetime.date.today().strftime('%Y年%m月%d日')
    
    html = f"""
<!-- 每日推荐题目 - {today} -->
<div class="daily-recommendation" style="background: #f8f9fa; border-radius: 8px; padding: 1.5rem; margin: 2rem 0; border-left: 4px solid #28a745;">
  <h3 style="color: #28a745; margin-bottom: 1rem;">🌟 今日推荐题目 ({today})</h3>
  <div class="problem-grid" style="display: grid; gap: 1rem;">
"""
    
    for i, problem in enumerate(problems, 1):
        # 生成特征标签
        tags = []
        if problem['has_math']:
            tags.append('<span style="background: #e3f2fd; color: #1976d2; padding: 0.2rem 0.5rem; border-radius: 4px; font-size: 0.8rem;">数学</span>')
        if problem['is_interactive']:
            tags.append('<span style="background: #fff3e0; color: #f57c00; padding: 0.2rem 0.5rem; border-radius: 4px; font-size: 0.8rem;">交互</span>')
        if problem['has_samples']:
            tags.append('<span style="background: #e8f5e8; color: #2e7d32; padding: 0.2rem 0.5rem; border-radius: 4px; font-size: 0.8rem;">样例</span>')
        
        for hint in problem['difficulty_hints']:
            tags.append(f'<span style="background: #fce4ec; color: #c2185b; padding: 0.2rem 0.5rem; border-radius: 4px; font-size: 0.8rem;">{hint}</span>')
        
        tags_html = ' '.join(tags) if tags else ''
        
        html += f"""
    <div class="recommended-problem" style="background: white; padding: 1rem; border-radius: 6px; border: 1px solid #dee2e6;">
      <div style="display: flex; justify-content: space-between; align-items: flex-start;">
        <div>
          <h4 style="margin: 0 0 0.5rem 0;">
            <a href="problem/{problem['id']}/" style="color: #2c3e50; text-decoration: none;">
              {problem['id']} {problem['title']}
            </a>
          </h4>
          <div style="margin-top: 0.5rem;">{tags_html}</div>
        </div>
        <span style="background: #28a745; color: white; padding: 0.3rem 0.6rem; border-radius: 4px; font-size: 0.8rem;">推荐 #{i}</span>
      </div>
    </div>
"""
    
    html += """
  </div>
  <p style="margin-top: 1rem; color: #6c757d; font-size: 0.9rem; text-align: center;">
    💡 每日推荐基于算法智能选择，涵盖不同类型和难度的题目
  </p>
</div>
"""
    
    return html

def update_homepage_recommendation(recommendation_html):
    """更新主页的推荐区域"""
    index_file = Path('index.html')
    if not index_file.exists():
        print("⚠️ 主页文件不存在，跳过更新")
        return
    
    with open(index_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 查找并替换推荐区域
    start_marker = '<!-- 每日推荐题目开始 -->'
    end_marker = '<!-- 每日推荐题目结束 -->'
    
    if start_marker in content and end_marker in content:
        # 替换现有推荐区域
        start_pos = content.find(start_marker)
        end_pos = content.find(end_marker) + len(end_marker)
        
        new_content = (
            content[:start_pos] +
            start_marker + '\n' +
            recommendation_html + '\n' +
            end_marker +
            content[end_pos:]
        )
    else:
        # 在合适位置插入推荐区域
        insert_pos = content.find('<!-- 操作按钮 -->')
        if insert_pos != -1:
            new_content = (
                content[:insert_pos] +
                start_marker + '\n' +
                recommendation_html + '\n' +
                end_marker + '\n\n' +
                content[insert_pos:]
            )
        else:
            print("⚠️ 未找到合适的插入位置，跳过更新")
            return
    
    with open(index_file, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print("✅ 主页推荐区域已更新")

def save_recommendation_data(problems):
    """保存推荐数据"""
    stats_dir = Path('stats')
    stats_dir.mkdir(exist_ok=True)
    
    recommendation_data = {
        'date': datetime.date.today().strftime('%Y-%m-%d'),
        'problems': problems,
        'generated_at': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }
    
    with open(stats_dir / 'daily_recommendation.json', 'w', encoding='utf-8') as f:
        json.dump(recommendation_data, f, ensure_ascii=False, indent=2)
    
    print(f"💾 推荐数据已保存")

def main():
    print("🎯 开始生成每日题目推荐...")
    
    # 加载题目列表
    problems = load_problem_list()
    print(f"📚 加载了 {len(problems)} 道题目")
    
    # 选择推荐题目
    recommended = select_daily_problems(problems, count=3)
    print(f"✨ 选择了 {len(recommended)} 道推荐题目")
    
    if recommended:
        for i, problem in enumerate(recommended, 1):
            print(f"  {i}. {problem['id']} - {problem['title']}")
    
    # 生成HTML
    recommendation_html = generate_recommendation_html(recommended)
    
    # 更新主页
    update_homepage_recommendation(recommendation_html)
    
    # 保存数据
    save_recommendation_data(recommended)
    
    print("\n🌟 每日推荐生成完成!")

if __name__ == '__main__':
    main()
