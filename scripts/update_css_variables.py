#!/usr/bin/env python3
"""
CSS变量更新器 - 更新CSS变量以应用主题
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

def generate_css_variables(theme_colors):
    """生成CSS变量"""
    css_vars = f"""
:root {{
    --theme-primary: {theme_colors.get('primary', '#3498db')};
    --theme-secondary: {theme_colors.get('secondary', '#2980b9')};
    --theme-accent: {theme_colors.get('accent', '#e74c3c')};
    --theme-background: {theme_colors.get('background', '#ecf0f1')};
    --theme-text: {theme_colors.get('text', '#2c3e50')};
}}
"""
    return css_vars

def update_css_files(theme_colors):
    """更新CSS文件中的变量"""
    css_vars = generate_css_variables(theme_colors)
    
    # 创建或更新主题CSS文件
    theme_css_file = Path('assets/css/theme.css')
    theme_css_file.parent.mkdir(parents=True, exist_ok=True)
    
    with open(theme_css_file, 'w', encoding='utf-8') as f:
        f.write(css_vars)
    
    print(f"✅ 主题CSS文件已更新: {theme_css_file}")
    return True

def main():
    print("🎨 开始更新CSS变量...")
    
    theme_info = load_theme_info()
    if not theme_info:
        print("❌ 未找到主题信息")
        return
    
    theme_colors = theme_info.get('theme_colors', {})
    recommended_theme = theme_info.get('recommended_theme', 'summer')
    
    print(f"🌈 当前主题: {recommended_theme}")
    print(f"🎨 主色调: {theme_colors.get('primary', '#3498db')}")
    
    # 更新CSS变量
    if update_css_files(theme_colors):
        print("✅ CSS变量更新成功!")
    else:
        print("❌ CSS变量更新失败!")
    
    print("\n✅ CSS变量更新完成!")

if __name__ == '__main__':
    main()
