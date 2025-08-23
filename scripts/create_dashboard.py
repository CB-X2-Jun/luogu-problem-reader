#!/usr/bin/env python3
"""
交互式仪表板创建器 - 生成交互式数据仪表板
"""

import json
import datetime
from pathlib import Path
from collections import Counter, defaultdict

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
            'difficulty_hints': extract_difficulty_hints(content)
        }
        
        problems_data.append(problem_info)
    
    return problems_data

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

def generate_dashboard_data(problems_data):
    """生成仪表板数据"""
    total_problems = len(problems_data)
    problems_with_samples = sum(1 for p in problems_data if p['has_samples'])
    math_problems = sum(1 for p in problems_data if p['has_math'])
    interactive_problems = sum(1 for p in problems_data if p['is_interactive'])
    
    # 难度分布
    difficulty_count = Counter()
    for problem in problems_data:
        if problem['difficulty_hints']:
            for hint in problem['difficulty_hints']:
                difficulty_count[hint] += 1
        else:
            difficulty_count['其他'] += 1
    
    # 长度分布
    length_bins = [0, 500, 1000, 1500, 2000, 3000, 5000, float('inf')]
    length_labels = ['<500', '500-1K', '1K-1.5K', '1.5K-2K', '2K-3K', '3K-5K', '>5K']
    length_dist = {}
    
    for i, (start, end) in enumerate(zip(length_bins[:-1], length_bins[1:])):
        count = sum(1 for p in problems_data if start <= p['content_length'] < end)
        length_dist[length_labels[i]] = count
    
    return {
        'overview': {
            'total_problems': total_problems,
            'problems_with_samples': problems_with_samples,
            'sample_coverage': round(problems_with_samples / total_problems * 100, 1) if total_problems > 0 else 0,
            'math_problems': math_problems,
            'interactive_problems': interactive_problems,
            'regular_problems': total_problems - math_problems - interactive_problems
        },
        'difficulty_distribution': dict(difficulty_count.most_common()),
        'length_distribution': length_dist,
        'last_updated': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }

def create_interactive_dashboard():
    """创建交互式仪表板HTML"""
    problems_data = load_problem_data()
    dashboard_data = generate_dashboard_data(problems_data)
    
    html_content = f'''<!DOCTYPE html>
<html lang="zh">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>交互式数据仪表板 - 洛谷题目浏览站</title>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <style>
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            margin: 0;
            padding: 20px;
            background: #f8f9fa;
            color: #2c3e50;
        }}
        .container {{
            max-width: 1200px;
            margin: 0 auto;
        }}
        .header {{
            text-align: center;
            margin-bottom: 2rem;
        }}
        .header h1 {{
            color: #2c3e50;
            margin-bottom: 0.5rem;
        }}
        .header p {{
            color: #7f8c8d;
            margin: 0;
        }}
        .stats-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 1.5rem;
            margin-bottom: 2rem;
        }}
        .stat-card {{
            background: white;
            padding: 1.5rem;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            text-align: center;
        }}
        .stat-number {{
            font-size: 2.5rem;
            font-weight: bold;
            color: #3498db;
            margin-bottom: 0.5rem;
        }}
        .stat-label {{
            color: #7f8c8d;
            font-size: 0.9rem;
        }}
        .charts-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(400px, 1fr));
            gap: 2rem;
            margin-bottom: 2rem;
        }}
        .chart-card {{
            background: white;
            padding: 1.5rem;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }}
        .chart-card h3 {{
            margin-top: 0;
            color: #2c3e50;
            text-align: center;
        }}
        .chart-container {{
            position: relative;
            height: 300px;
        }}
        .back-link {{
            display: inline-block;
            margin-bottom: 2rem;
            color: #3498db;
            text-decoration: none;
            font-weight: 500;
        }}
        .back-link:hover {{
            text-decoration: underline;
        }}
        .footer {{
            text-align: center;
            margin-top: 2rem;
            padding-top: 2rem;
            border-top: 1px solid #e9ecef;
            color: #7f8c8d;
            font-size: 0.9rem;
        }}
    </style>
</head>
<body>
    <div class="container">
        <a href="../" class="back-link">← 返回主页</a>
        
        <div class="header">
            <h1>📊 交互式数据仪表板</h1>
            <p>洛谷题目浏览站 - 实时数据分析与可视化</p>
        </div>

        <!-- 统计概览 -->
        <div class="stats-grid">
            <div class="stat-card">
                <div class="stat-number">{dashboard_data['overview']['total_problems']}</div>
                <div class="stat-label">题目总数</div>
            </div>
            <div class="stat-card">
                <div class="stat-number">{dashboard_data['overview']['sample_coverage']}%</div>
                <div class="stat-label">样例覆盖率</div>
            </div>
            <div class="stat-card">
                <div class="stat-number">{dashboard_data['overview']['math_problems']}</div>
                <div class="stat-label">数学题目</div>
            </div>
            <div class="stat-card">
                <div class="stat-number">{dashboard_data['overview']['interactive_problems']}</div>
                <div class="stat-label">交互题目</div>
            </div>
        </div>

        <!-- 图表区域 -->
        <div class="charts-grid">
            <div class="chart-card">
                <h3>题目特征分布</h3>
                <div class="chart-container">
                    <canvas id="featuresChart"></canvas>
                </div>
            </div>
            
            <div class="chart-card">
                <h3>难度分布</h3>
                <div class="chart-container">
                    <canvas id="difficultyChart"></canvas>
                </div>
            </div>
            
            <div class="chart-card">
                <h3>题目长度分布</h3>
                <div class="chart-container">
                    <canvas id="lengthChart"></canvas>
                </div>
            </div>
            
            <div class="chart-card">
                <h3>样例覆盖情况</h3>
                <div class="chart-container">
                    <canvas id="samplesChart"></canvas>
                </div>
            </div>
        </div>

        <div class="footer">
            <p>最后更新: {dashboard_data['last_updated']} | 数据来源: 洛谷题目浏览站</p>
        </div>
    </div>

    <script>
        // 图表配置
        Chart.defaults.font.family = '-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif';
        Chart.defaults.color = '#2c3e50';

        // 题目特征分布饼图
        const featuresCtx = document.getElementById('featuresChart').getContext('2d');
        new Chart(featuresCtx, {{
            type: 'doughnut',
            data: {{
                labels: ['数学题', '交互题', '普通题'],
                datasets: [{{
                    data: [{dashboard_data['overview']['math_problems']}, {dashboard_data['overview']['interactive_problems']}, {dashboard_data['overview']['regular_problems']}],
                    backgroundColor: ['#3498db', '#e74c3c', '#2ecc71'],
                    borderWidth: 2,
                    borderColor: '#fff'
                }}]
            }},
            options: {{
                responsive: true,
                maintainAspectRatio: false,
                plugins: {{
                    legend: {{
                        position: 'bottom'
                    }}
                }}
            }}
        }});

        // 难度分布柱状图
        const difficultyCtx = document.getElementById('difficultyChart').getContext('2d');
        new Chart(difficultyCtx, {{
            type: 'bar',
            data: {{
                labels: {json.dumps(list(dashboard_data['difficulty_distribution'].keys()))},
                datasets: [{{
                    label: '题目数量',
                    data: {json.dumps(list(dashboard_data['difficulty_distribution'].values()))},
                    backgroundColor: '#3498db',
                    borderColor: '#2980b9',
                    borderWidth: 1
                }}]
            }},
            options: {{
                responsive: true,
                maintainAspectRatio: false,
                scales: {{
                    y: {{
                        beginAtZero: true
                    }}
                }},
                plugins: {{
                    legend: {{
                        display: false
                    }}
                }}
            }}
        }});

        // 题目长度分布柱状图
        const lengthCtx = document.getElementById('lengthChart').getContext('2d');
        new Chart(lengthCtx, {{
            type: 'bar',
            data: {{
                labels: {json.dumps(list(dashboard_data['length_distribution'].keys()))},
                datasets: [{{
                    label: '题目数量',
                    data: {json.dumps(list(dashboard_data['length_distribution'].values()))},
                    backgroundColor: '#2ecc71',
                    borderColor: '#27ae60',
                    borderWidth: 1
                }}]
            }},
            options: {{
                responsive: true,
                maintainAspectRatio: false,
                scales: {{
                    y: {{
                        beginAtZero: true
                    }}
                }},
                plugins: {{
                    legend: {{
                        display: false
                    }}
                }}
            }}
        }});

        // 样例覆盖情况饼图
        const samplesCtx = document.getElementById('samplesChart').getContext('2d');
        new Chart(samplesCtx, {{
            type: 'pie',
            data: {{
                labels: ['有样例', '无样例'],
                datasets: [{{
                    data: [{dashboard_data['overview']['problems_with_samples']}, {dashboard_data['overview']['total_problems'] - dashboard_data['overview']['problems_with_samples']}],
                    backgroundColor: ['#2ecc71', '#e74c3c'],
                    borderWidth: 2,
                    borderColor: '#fff'
                }}]
            }},
            options: {{
                responsive: true,
                maintainAspectRatio: false,
                plugins: {{
                    legend: {{
                        position: 'bottom'
                    }}
                }}
            }}
        }});
    </script>
</body>
</html>'''
    
    # 确保目录存在
    dashboard_dir = Path('dashboard')
    dashboard_dir.mkdir(exist_ok=True)
    
    # 保存仪表板
    with open(dashboard_dir / 'index.html', 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    # 保存数据JSON
    with open(dashboard_dir / 'data.json', 'w', encoding='utf-8') as f:
        json.dump(dashboard_data, f, ensure_ascii=False, indent=2)
    
    return dashboard_data

def main():
    print("📊 开始创建交互式仪表板...")
    
    dashboard_data = create_interactive_dashboard()
    
    print(f"✅ 交互式仪表板创建完成!")
    print(f"📚 分析了 {dashboard_data['overview']['total_problems']} 道题目")
    print(f"📊 生成了 4 个交互式图表")
    print(f"🔗 访问地址: dashboard/index.html")

if __name__ == '__main__':
    main()
