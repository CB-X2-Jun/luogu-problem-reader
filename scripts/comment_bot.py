#!/usr/bin/env python3
"""
洛谷题目浏览站 - 自动回复评论Bot
监控GitHub Discussions并自动回复常见问题
"""

import os
import re
import json
import time
import requests
from datetime import datetime, timedelta

class CommentBot:
    def __init__(self):
        self.github_token = os.environ.get('GITHUB_TOKEN')
        self.repo_owner = 'Eternity-Sky'
        self.repo_name = 'luogu-problem-reader'
        self.base_url = 'https://api.github.com'
        
        # API请求头
        self.headers = {
            'Authorization': f'token {self.github_token}',
            'Accept': 'application/vnd.github.v3+json',
            'User-Agent': 'Luogu-Comment-Bot/1.0'
        }
        
        # 自动回复规则配置
        self.reply_rules = self.load_reply_rules()
        
    def load_reply_rules(self):
        """加载自动回复规则"""
        return {
            # 题目相关问题
            'problem_not_found': {
                'keywords': ['找不到题目', '题目不存在', '404', '页面不存在'],
                'reply': '''👋 你好！看起来你遇到了题目页面的问题。

**可能的解决方案：**
1. 🔍 检查题目编号是否正确（如P1000而不是1000）
2. 📋 访问 [题目列表页面](/problem/list/) 查看所有可用题目
3. 🔄 如果是新题目，可能需要等待爬取更新

**需要帮助？** 请提供具体的题目编号，我们会尽快处理！'''
            },
            
            'sample_missing': {
                'keywords': ['样例缺失', '没有样例', '样例不见了', '输入输出样例'],
                'reply': '''📝 关于样例数据的问题：

**可能原因：**
1. 🎮 **交互题** - 某些交互题（如P1733）本身就没有传统的输入输出样例
2. 🔄 **数据更新** - 可能是爬取时的临时问题
3. 🆕 **新题目** - 刚发布的题目可能还未完全爬取

**解决方案：**
- 访问 [洛谷官网](https://www.luogu.com.cn) 确认题目是否有样例
- 如果官网有样例但这里没有，请告诉我们题目编号，我们会重新爬取

感谢反馈！🙏'''
            },
            
            'formula_render': {
                'keywords': ['公式显示', '数学公式', 'latex', '公式渲染', '公式不显示'],
                'reply': '''🔢 数学公式渲染问题：

**我们支持的公式格式：**
- 行内公式：`$公式内容$`
- 块级公式：`$$公式内容$$`
- LaTeX语法：`\\(公式\\)` 和 `\\[公式\\]`

**常见问题：**
1. 📱 **移动端** - 某些复杂公式在移动端可能显示异常
2. ⏰ **加载时间** - 公式渲染需要一点时间，请耐心等待
3. 🔄 **刷新页面** - 如果公式不显示，尝试刷新页面

如果问题持续存在，请提供具体的题目编号和公式内容！'''
            },
            
            'search_help': {
                'keywords': ['怎么搜索', '搜索功能', '找题目', '搜索题目'],
                'reply': '''🔍 搜索功能使用指南：

**搜索方式：**
1. **题目编号** - 直接输入 `P1000` 或 `1000` 跳转到对应题目
2. **题目列表** - 访问 [题目列表](/problem/list/) 浏览所有题目
3. **空搜索** - 不输入任何内容直接搜索会跳转到题目列表

**小技巧：**
- 💡 使用Ctrl+F在题目列表页面内搜索关键词
- 📚 题目按编号排序，方便查找
- 🔖 可以收藏常用题目页面

希望这些信息对你有帮助！'''
            },
            
            'site_slow': {
                'keywords': ['网站很慢', '加载慢', '打开慢', '速度慢', '卡顿'],
                'reply': '''⚡ 关于网站速度问题：

**优化建议：**
1. 🌐 **网络环境** - 检查你的网络连接
2. 🔄 **刷新页面** - 尝试强制刷新（Ctrl+F5）
3. 📱 **设备性能** - 关闭其他占用资源的程序
4. 🕒 **访问时间** - 避开网络高峰期

**我们的优化：**
- ✅ 使用Netlify CDN加速
- ✅ 图片和资源压缩
- ✅ 懒加载优化
- ✅ 缓存策略

如果问题持续，请告诉我们你的地区和网络环境！'''
            },
            
            'mobile_issue': {
                'keywords': ['手机', '移动端', '手机版', '移动版', '响应式'],
                'reply': '''📱 移动端使用问题：

**移动端优化：**
- ✅ 响应式设计，自适应屏幕
- ✅ 触摸友好的按钮和链接
- ✅ 优化的字体大小和间距

**常见问题解决：**
1. 🔄 **横屏模式** - 复杂公式建议横屏查看
2. 🔍 **缩放功能** - 可以双击放大内容
3. 📱 **浏览器** - 推荐使用Chrome或Safari

**反馈问题：** 如果遇到移动端显示问题，请告诉我们你的设备型号和浏览器版本！'''
            },
            
            'general_help': {
                'keywords': ['帮助', 'help', '怎么用', '使用方法', '新手'],
                'reply': '''🎯 洛谷题目浏览站使用指南：

**主要功能：**
- 📚 **题目浏览** - 查看洛谷题目详情、样例、提示
- 🔍 **智能搜索** - 输入题号快速跳转
- 💬 **讨论交流** - 在每个题目下方讨论解法
- 📊 **统计信息** - 查看题目分类和数量统计

**快速开始：**
1. 访问 [首页](/) 了解网站概况
2. 进入 [题目列表](/problem/list/) 浏览所有题目
3. 点击任意题目查看详情和讨论
4. 在评论区分享你的想法和解法

**需要帮助？** 随时在评论区提问，我们会及时回复！'''
            }
        }
    
    def get_recent_discussions(self, hours=1):
        """获取最近的讨论"""
        try:
            # 计算时间范围
            since = (datetime.now() - timedelta(hours=hours)).isoformat() + 'Z'
            
            # 获取仓库的discussions
            url = f'{self.base_url}/repos/{self.repo_owner}/{self.repo_name}/discussions'
            params = {
                'per_page': 50,
                'sort': 'updated',
                'direction': 'desc'
            }
            
            response = requests.get(url, headers=self.headers, params=params)
            response.raise_for_status()
            
            discussions = response.json()
            
            # 过滤最近更新的讨论
            recent_discussions = []
            for discussion in discussions:
                if discussion['updated_at'] >= since:
                    recent_discussions.append(discussion)
            
            return recent_discussions
            
        except Exception as e:
            print(f"获取讨论失败: {e}")
            return []
    
    def get_discussion_comments(self, discussion_number):
        """获取讨论的评论"""
        try:
            url = f'{self.base_url}/repos/{self.repo_owner}/{self.repo_name}/discussions/{discussion_number}/comments'
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            print(f"获取评论失败: {e}")
            return []
    
    def analyze_comment(self, comment_body, user_login=None):
        """分析评论内容，对所有评论都进行自动回复，支持@和引用格式"""
        # 处理评论内容，确保每行前加 >
        processed_body = comment_body.strip().replace('\n', '\n> ')
        
        # 构建引用块
        if user_login:
            quote = '> @' + user_login + '\n> ' + processed_body + '\n\n'
        else:
            quote = '> ' + processed_body + '\n\n'
        # 构建完整回复
        reply = (quote +
                "🤖 这是自动回复！感谢你的参与！\n\n"
                "---\n如需人工帮助请 @Eternity-Sky")
        return reply
    
    def should_reply(self, comment):
        """判断是否应该回复这个评论"""
        # 不回复自己的评论
        if comment['user']['login'] == 'github-actions[bot]':
            return False
        
        # 不回复太老的评论（超过24小时）
        comment_time = datetime.fromisoformat(comment['created_at'].replace('Z', '+00:00'))
        if (datetime.now().replace(tzinfo=comment_time.tzinfo) - comment_time).total_seconds() > 86400:
            return False
        
        # 检查是否已经回复过
        # 这里可以添加更复杂的逻辑来避免重复回复
        
        return True
    
    def get_node_ids(self, discussion_number, comment_id):
        """获取discussion和comment的node_id"""
        try:
            # 查询discussion的node_id
            query = """
            query ($owner: String!, $repo: String!, $number: Int!) {
                repository(owner: $owner, name: $repo) {
                    discussion(number: $number) {
                        id
                        comments(first: 20) {
                            nodes {
                                id
                                databaseId
                            }
                        }
                    }
                }
            }
            """
            
            variables = {
                "owner": self.repo_owner,
                "repo": self.repo_name,
                "number": discussion_number
            }
            
            response = requests.post(
                'https://api.github.com/graphql',
                headers={
                    'Authorization': f'token {self.github_token}',
                    'Content-Type': 'application/json'
                },
                json={'query': query, 'variables': variables}
            )
            response.raise_for_status()
            
            result = response.json()
            if 'errors' in result:
                print(f"❌ 获取node_id失败: {result['errors']}")
                return None, None
                
            discussion_data = result.get('data', {}).get('repository', {}).get('discussion')
            if not discussion_data:
                print("❌ 未找到discussion")
                return None, None
                
            discussion_node_id = discussion_data['id']
            comment_node_id = None
            
            # 查找对应的comment node_id
            for comment in discussion_data.get('comments', {}).get('nodes', []):
                if str(comment.get('databaseId')) == str(comment_id):
                    comment_node_id = comment['id']
                    break
                    
            if not comment_node_id:
                print(f"⚠️ 未找到评论 {comment_id} 的node_id，将仅回复到讨论")
                
            return discussion_node_id, comment_node_id
            
        except Exception as e:
            print(f"❌ 获取node_id时出错: {e}")
            return None, None
    
    def reply_to_comment(self, discussion_number, comment_id, reply_text):
        """回复评论"""
        try:
            # 获取node_ids
            discussion_node_id, comment_node_id = self.get_node_ids(discussion_number, comment_id)
            if not discussion_node_id:
                print("❌ 无法获取discussion的node_id")
                return False
                
            # 使用GraphQL API进行回复
            url = 'https://api.github.com/graphql'
            
            # GraphQL mutation
            query = """
            mutation ($discussionId: ID!, $body: String!, $replyToId: ID) {
                addDiscussionComment(input: {
                    discussionId: $discussionId,
                    body: $body,
                    replyToId: $replyToId
                }) {
                    comment {
                        id
                        body
                    }
                }
            }
            """
            
            variables = {
                "discussionId": discussion_node_id,
                "body": reply_text,
                "replyToId": comment_node_id  # 可能为None，表示回复到讨论
            }
            
            # 更新headers以支持GraphQL
            headers = self.headers.copy()
            headers['Content-Type'] = 'application/json'
            
            response = requests.post(
                url,
                headers=headers,
                json={
                    'query': query,
                    'variables': variables
                }
            )
            
            response.raise_for_status()
            result = response.json()
            
            if 'errors' in result:
                print(f"❌ GraphQL错误: {result['errors']}")
                return False
                
            print(f"✅ 成功回复讨论 #{discussion_number}")
            return True
            
        except Exception as e:
            print(f"❌ 回复失败: {e}")
            if hasattr(e, 'response') and hasattr(e.response, 'text'):
                print(f"响应内容: {e.response.text}")
            return False
    
    def process_discussions(self):
        """遍历所有Discussions，遍历所有评论，对每条评论都自动回复（除自己外）"""
        print("🤖 开始检查所有讨论...")
        
        # 获取所有Discussions（分页，每页最多100条）
        discussions = []
        page = 1
        while True:
            url = f'{self.base_url}/repos/{self.repo_owner}/{self.repo_name}/discussions'
            params = {'per_page': 100, 'page': page, 'sort': 'updated', 'direction': 'desc', 'category': 'Announcements'}
            resp = requests.get(url, headers=self.headers, params=params)
            if resp.status_code != 200:
                print(f"❌ 获取Discussions失败: {resp.status_code}")
                break
            page_discussions = resp.json()
            if not page_discussions:
                break
            discussions.extend(page_discussions)
            if len(page_discussions) < 100:
                break
            page += 1
        print(f"📋 共找到 {len(discussions)} 个讨论主题")
        
        reply_count = 0
        for discussion in discussions:
            discussion_number = discussion['number']
            print(f"🔍 检查讨论 #{discussion_number}: {discussion['title']}")
            # 获取该讨论下所有评论
            comments = self.get_discussion_comments(discussion_number)
            for comment in comments:
                if not self.should_reply(comment):
                    continue
                reply_text = self.analyze_comment(comment['body'], user_login=comment['user']['login'])
                if reply_text:
                    print(f"💬 发现需要回复的评论: {comment['body'][:50]}...")
                    bot_reply = f"{reply_text}\n\n---\n🤖 *这是自动回复，如需人工帮助请 @Eternity-Sky*"
                    if self.reply_to_comment(discussion_number, comment['id'], bot_reply):
                        reply_count += 1
                        time.sleep(2)
        print(f"✨ 处理完成，共回复了 {reply_count} 条评论")
        return reply_count

def main():
    """主函数"""
    print("🚀 洛谷题目浏览站评论Bot启动")
    
    # 检查环境变量
    if not os.environ.get('GITHUB_TOKEN'):
        print("❌ 错误: 未找到GITHUB_TOKEN环境变量")
        return
    
    # 创建Bot实例
    bot = CommentBot()
    
    # 处理讨论
    bot.process_discussions()
    
    print("🎯 Bot运行完成")

if __name__ == '__main__':
    main()
