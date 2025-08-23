#!/usr/bin/env python3
"""
README统计信息更新器
自动更新README中的统计徽章和信息
"""

import json
import datetime
from pathlib import Path

def load_stats():
    """加载统计数据"""
    stats_file = Path('stats') / 'daily_stats.json'
    badges_file = Path('stats') / 'badges.json'
    
    stats = {}
    badges = {}
    
    if stats_file.exists():
        with open(stats_file, 'r', encoding='utf-8') as f:
            stats = json.load(f)
    
    if badges_file.exists():
        with open(badges_file, 'r', encoding='utf-8') as f:
            badges = json.load(f)
    
    return stats, badges

def generate_badges_markdown(badges):
    """生成徽章的Markdown代码"""
    if not badges:
        return ""
    
    badge_lines = []
    
    # 题目总数徽章
    if 'total_problems' in badges:
        badge_lines.append(f"![题目总数](https://img.shields.io/badge/题目总数-{badges['total_problems']}-blue)")
    
    # 样例覆盖率徽章
    if 'sample_rate' in badges:
        color = "green" if float(badges['sample_rate'].rstrip('%')) > 90 else "yellow" if float(badges['sample_rate'].rstrip('%')) > 70 else "red"
        badge_lines.append(f"![样例覆盖率](https://img.shields.io/badge/样例覆盖率-{badges['sample_rate']}-{color})")
    
    # 数学题目徽章
    if 'math_problems' in badges:
        badge_lines.append(f"![数学题目](https://img.shields.io/badge/数学题目-{badges['math_problems']}-purple)")
    
    # 最后更新徽章
    if 'last_update' in badges:
        update_date = badges['last_update'].split()[0]  # 只取日期部分
        badge_lines.append(f"![最后更新](https://img.shields.io/badge/最后更新-{update_date}-brightgreen)")
    
    return " ".join(badge_lines)

def generate_stats_table(stats):
    """生成统计信息表格"""
    if not stats:
        return ""
    
    table = """
## 📊 题库统计

| 统计项目 | 数值 |
|---------|------|
"""
    
    if 'total_problems' in stats:
        table += f"| 📚 题目总数 | {stats['total_problems']} |\n"
    
    if 'problems_with_samples' in stats:
        table += f"| ✅ 有样例题目 | {stats['problems_with_samples']} |\n"
        
        if 'total_problems' in stats and stats['total_problems'] > 0:
            rate = stats['problems_with_samples'] / stats['total_problems'] * 100
            table += f"| 📈 样例覆盖率 | {rate:.1f}% |\n"
    
    if 'math_problems' in stats:
        table += f"| 🧮 数学题目 | {stats['math_problems']} |\n"
    
    if 'interactive_problems' in stats:
        table += f"| 🎮 交互题目 | {stats['interactive_problems']} |\n"
    
    if 'avg_problem_length' in stats:
        table += f"| 📝 平均题目长度 | {stats['avg_problem_length']} 字符 |\n"
    
    if 'recent_problems' in stats and stats['recent_problems']:
        latest = max(stats['recent_problems'])
        table += f"| 🆕 最新题目 | P{latest} |\n"
    
    if 'update_date' in stats:
        table += f"| 🔄 统计更新时间 | {stats['update_date']} |\n"
    
    return table

def update_readme():
    """更新README文件"""
    readme_file = Path('README.md')
    
    # 如果README不存在，创建一个基础版本
    if not readme_file.exists():
        create_basic_readme()
    
    # 加载统计数据
    stats, badges = load_stats()
    
    # 读取现有README
    with open(readme_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 生成新的内容
    badges_md = generate_badges_markdown(badges)
    stats_table = generate_stats_table(stats)
    
    # 更新徽章区域
    if badges_md:
        badge_start = "<!-- BADGES_START -->"
        badge_end = "<!-- BADGES_END -->"
        
        if badge_start in content and badge_end in content:
            start_pos = content.find(badge_start)
            end_pos = content.find(badge_end) + len(badge_end)
            content = (
                content[:start_pos] +
                badge_start + "\n" + badges_md + "\n" + badge_end +
                content[end_pos:]
            )
        else:
            # 在标题后插入徽章
            lines = content.split('\n')
            if lines and lines[0].startswith('# '):
                lines.insert(1, "")
                lines.insert(2, badge_start)
                lines.insert(3, badges_md)
                lines.insert(4, badge_end)
                lines.insert(5, "")
                content = '\n'.join(lines)
    
    # 更新统计表格区域
    if stats_table:
        stats_start = "<!-- STATS_START -->"
        stats_end = "<!-- STATS_END -->"
        
        if stats_start in content and stats_end in content:
            start_pos = content.find(stats_start)
            end_pos = content.find(stats_end) + len(stats_end)
            content = (
                content[:start_pos] +
                stats_start + "\n" + stats_table + "\n" + stats_end +
                content[end_pos:]
            )
        else:
            # 在文件末尾添加统计表格
            content += f"\n\n{stats_start}\n{stats_table}\n{stats_end}\n"
    
    # 写回README
    with open(readme_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("📝 README.md 已更新")

def create_basic_readme():
    """创建基础README文件"""
    readme_content = """# 洛谷题目浏览站

<!-- BADGES_START -->
<!-- BADGES_END -->

一个用于浏览洛谷题目的静态网站，提供清晰的题目展示和便捷的浏览体验。

## 🌟 特性

- 📚 **完整题库**: 收录洛谷平台题目
- 🎨 **美观界面**: 简洁现代的Material Design风格
- 🔍 **便捷浏览**: 支持题目列表和详情查看
- 📱 **响应式设计**: 适配各种设备屏幕
- ⚡ **快速加载**: 静态页面，访问速度快
- 🧮 **数学公式**: 完整支持LaTeX数学公式渲染
- 💻 **代码高亮**: 语法高亮显示代码块

## 🚀 使用方法

1. 访问 [题目列表](problem/list/) 浏览所有题目
2. 点击题目标题查看详细内容
3. 每道题目包含题目描述、输入输出格式、样例等完整信息

## 🛠️ 技术栈

- **前端**: HTML5, CSS3, JavaScript
- **样式**: Material Design
- **数学渲染**: KaTeX
- **代码高亮**: Highlight.js
- **自动化**: GitHub Actions
- **部署**: GitHub Pages

## 📈 更新机制

- 🤖 **自动爬取**: 定期自动更新题目内容
- 📊 **每日统计**: 自动生成题库统计信息
- 🎯 **智能推荐**: 每日推荐优质题目

<!-- STATS_START -->
<!-- STATS_END -->

## 📄 许可证

本项目采用 MIT 许可证。

---

💡 **提示**: 本站仅供学习交流使用，题目版权归洛谷平台所有。
"""
    
    with open('README.md', 'w', encoding='utf-8') as f:
        f.write(readme_content)
    
    print("📝 已创建基础 README.md")

def main():
    print("📝 开始更新README统计信息...")
    
    update_readme()
    
    print("✅ README统计信息更新完成!")

if __name__ == '__main__':
    main()
