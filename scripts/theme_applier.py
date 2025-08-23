#!/usr/bin/env python3
"""
主题应用器 - 应用检测到的主题到网站
"""

import json
from pathlib import Path
import re

def load_theme_info():
    """加载主题信息"""
    stats_dir = Path('stats')
    theme_file = stats_dir / 'theme_info.json'
    
    if theme_file.exists():
        try:
            with open(theme_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        except:
            pass
    
    return None

def apply_theme_to_homepage(theme_colors):
    """应用主题到首页"""
    index_file = Path('index.html')
    if not index_file.exists():
        return False
    
    with open(index_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 更新主题色彩（这里是示例，实际可以更复杂）
    # 可以替换CSS变量或内联样式中的颜色
    
    # 示例：更新按钮颜色
    primary_color = theme_colors.get('primary', '#3498db')
    content = re.sub(r'background: #3498db', f'background: {primary_color}', content)
    content = re.sub(r'color: #3498db', f'color: {primary_color}', content)
    
    with open(index_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    return True

def main():
    print("🎨 开始应用主题...")
    
    theme_info = load_theme_info()
    if not theme_info:
        print("❌ 未找到主题信息")
        return
    
    theme_colors = theme_info.get('theme_colors', {})
    recommended_theme = theme_info.get('recommended_theme', 'summer')
    
    print(f"🌈 应用主题: {recommended_theme}")
    print(f"🎨 主色调: {theme_colors.get('primary', '#3498db')}")
    
    # 应用主题到首页
    if apply_theme_to_homepage(theme_colors):
        print("✅ 首页主题应用成功!")
    else:
        print("❌ 首页主题应用失败!")
    
    print("\n✅ 主题应用完成!")

if __name__ == '__main__':
    main()
