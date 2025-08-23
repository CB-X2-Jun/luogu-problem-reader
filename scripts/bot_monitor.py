#!/usr/bin/env python3
"""
评论Bot监控脚本
跟踪Bot运行状态、回复统计和效果分析
"""

import os
import json
import requests
from datetime import datetime, timedelta

class BotMonitor:
    def __init__(self):
        self.github_token = os.environ.get('GITHUB_TOKEN')
        self.repo_owner = 'Eternity-Sky'
        self.repo_name = 'luogu-problem-reader'
        self.base_url = 'https://api.github.com'
        
        self.headers = {
            'Authorization': f'token {self.github_token}',
            'Accept': 'application/vnd.github.v3+json',
            'User-Agent': 'Luogu-Bot-Monitor/1.0'
        }
    
    def get_bot_activity(self, days=7):
        """获取Bot最近的活动统计"""
        try:
            # 获取最近的讨论
            url = f'{self.base_url}/repos/{self.repo_owner}/{self.repo_name}/discussions'
            params = {'per_page': 100, 'sort': 'updated', 'direction': 'desc'}
            
            response = requests.get(url, headers=self.headers, params=params)
            response.raise_for_status()
            discussions = response.json()
            
            bot_replies = 0
            total_comments = 0
            active_discussions = 0
            
            cutoff_date = datetime.now() - timedelta(days=days)
            
            for discussion in discussions:
                updated_at = datetime.fromisoformat(discussion['updated_at'].replace('Z', '+00:00'))
                if updated_at < cutoff_date.replace(tzinfo=updated_at.tzinfo):
                    continue
                
                active_discussions += 1
                
                # 获取讨论的评论
                comments_url = f"{url}/{discussion['number']}/comments"
                comments_response = requests.get(comments_url, headers=self.headers)
                
                if comments_response.status_code == 200:
                    comments = comments_response.json()
                    total_comments += len(comments)
                    
                    # 统计Bot回复
                    for comment in comments:
                        if 'github-actions[bot]' in comment.get('user', {}).get('login', ''):
                            bot_replies += 1
            
            return {
                'active_discussions': active_discussions,
                'total_comments': total_comments,
                'bot_replies': bot_replies,
                'bot_response_rate': round(bot_replies / max(total_comments, 1) * 100, 2),
                'period_days': days
            }
            
        except Exception as e:
            print(f"获取Bot活动统计失败: {e}")
            return None
    
    def generate_report(self):
        """生成Bot运行报告"""
        print("📊 生成评论Bot运行报告...")
        
        # 获取7天和30天的统计
        weekly_stats = self.get_bot_activity(7)
        monthly_stats = self.get_bot_activity(30)
        
        if not weekly_stats or not monthly_stats:
            print("❌ 无法获取统计数据")
            return
        
        report = {
            'generated_at': datetime.now().isoformat(),
            'weekly_stats': weekly_stats,
            'monthly_stats': monthly_stats,
            'performance': {
                'weekly_avg_replies_per_day': round(weekly_stats['bot_replies'] / 7, 2),
                'monthly_avg_replies_per_day': round(monthly_stats['bot_replies'] / 30, 2),
                'response_rate_trend': 'improving' if weekly_stats['bot_response_rate'] > monthly_stats['bot_response_rate'] else 'stable'
            }
        }
        
        # 保存报告
        os.makedirs('stats', exist_ok=True)
        with open('stats/bot_report.json', 'w', encoding='utf-8') as f:
            json.dump(report, f, ensure_ascii=False, indent=2)
        
        # 打印摘要
        print(f"✅ Bot运行报告生成完成")
        print(f"📈 最近7天: {weekly_stats['bot_replies']} 条回复, 响应率 {weekly_stats['bot_response_rate']}%")
        print(f"📊 最近30天: {monthly_stats['bot_replies']} 条回复, 响应率 {monthly_stats['bot_response_rate']}%")
        
        return report

def main():
    """主函数"""
    if not os.environ.get('GITHUB_TOKEN'):
        print("❌ 错误: 未找到GITHUB_TOKEN环境变量")
        return
    
    monitor = BotMonitor()
    monitor.generate_report()

if __name__ == '__main__':
    main()
