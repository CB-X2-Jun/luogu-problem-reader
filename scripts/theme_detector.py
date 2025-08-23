#!/usr/bin/env python3
"""
主题检测器 - 根据日期自动检测合适的主题
"""

import datetime
import json
from pathlib import Path

def detect_current_season():
    """检测当前季节"""
    now = datetime.datetime.now()
    month = now.month
    
    if month in [3, 4, 5]:
        return 'spring'
    elif month in [6, 7, 8]:
        return 'summer'
    elif month in [9, 10, 11]:
        return 'autumn'
    else:
        return 'winter'

def detect_holidays():
    """检测当前节日"""
    now = datetime.datetime.now()
    month = now.month
    day = now.day
    
    holidays = []
    
    # 春节 (简化检测，实际应该用农历)
    if month == 2 and 1 <= day <= 15:
        holidays.append('chinese_new_year')
    
    # 情人节
    if month == 2 and day == 14:
        holidays.append('valentines')
    
    # 愚人节
    if month == 4 and day == 1:
        holidays.append('april_fools')
    
    # 劳动节
    if month == 5 and day == 1:
        holidays.append('labor_day')
    
    # 儿童节
    if month == 6 and day == 1:
        holidays.append('childrens_day')
    
    # 中秋节 (简化检测)
    if month == 9 and 10 <= day <= 20:
        holidays.append('mid_autumn')
    
    # 国庆节
    if month == 10 and 1 <= day <= 7:
        holidays.append('national_day')
    
    # 万圣节
    if month == 10 and day == 31:
        holidays.append('halloween')
    
    # 圣诞节
    if month == 12 and 20 <= day <= 31:
        holidays.append('christmas')
    
    return holidays

def get_theme_colors(theme_type):
    """获取主题配色方案"""
    themes = {
        'spring': {
            'primary': '#2ecc71',
            'secondary': '#27ae60',
            'accent': '#f39c12',
            'background': '#ecf0f1',
            'text': '#2c3e50'
        },
        'summer': {
            'primary': '#3498db',
            'secondary': '#2980b9',
            'accent': '#e74c3c',
            'background': '#ecf0f1',
            'text': '#2c3e50'
        },
        'autumn': {
            'primary': '#e67e22',
            'secondary': '#d35400',
            'accent': '#f39c12',
            'background': '#fdf2e9',
            'text': '#2c3e50'
        },
        'winter': {
            'primary': '#34495e',
            'secondary': '#2c3e50',
            'accent': '#3498db',
            'background': '#ecf0f1',
            'text': '#2c3e50'
        },
        'chinese_new_year': {
            'primary': '#e74c3c',
            'secondary': '#c0392b',
            'accent': '#f1c40f',
            'background': '#fdf2e9',
            'text': '#2c3e50'
        },
        'christmas': {
            'primary': '#27ae60',
            'secondary': '#229954',
            'accent': '#e74c3c',
            'background': '#f8f9fa',
            'text': '#2c3e50'
        },
        'halloween': {
            'primary': '#e67e22',
            'secondary': '#d35400',
            'accent': '#8e44ad',
            'background': '#2c3e50',
            'text': '#ecf0f1'
        }
    }
    
    return themes.get(theme_type, themes['summer'])  # 默认夏季主题

def detect_recommended_theme():
    """检测推荐的主题"""
    holidays = detect_holidays()
    
    # 优先级：节日 > 季节
    if 'christmas' in holidays:
        return 'christmas'
    elif 'halloween' in holidays:
        return 'halloween'
    elif 'chinese_new_year' in holidays:
        return 'chinese_new_year'
    else:
        return detect_current_season()

def save_theme_info():
    """保存主题信息"""
    recommended_theme = detect_recommended_theme()
    current_season = detect_current_season()
    current_holidays = detect_holidays()
    
    theme_info = {
        'recommended_theme': recommended_theme,
        'current_season': current_season,
        'current_holidays': current_holidays,
        'theme_colors': get_theme_colors(recommended_theme),
        'detection_date': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }
    
    # 确保目录存在
    stats_dir = Path('stats')
    stats_dir.mkdir(exist_ok=True)
    
    # 保存主题信息
    with open(stats_dir / 'theme_info.json', 'w', encoding='utf-8') as f:
        json.dump(theme_info, f, ensure_ascii=False, indent=2)
    
    return theme_info

def main():
    print("🎨 开始检测当前主题...")
    
    theme_info = save_theme_info()
    
    print(f"📅 当前季节: {theme_info['current_season']}")
    print(f"🎉 当前节日: {', '.join(theme_info['current_holidays']) if theme_info['current_holidays'] else '无'}")
    print(f"🌈 推荐主题: {theme_info['recommended_theme']}")
    print(f"🎨 主色调: {theme_info['theme_colors']['primary']}")
    
    print("\n✅ 主题检测完成!")

if __name__ == '__main__':
    main()
