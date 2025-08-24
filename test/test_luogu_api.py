#!/usr/bin/env python3
"""
洛谷API测试脚本
用于测试洛谷平台的各种API接口
"""

import requests
import json
import re
from bs4 import BeautifulSoup

class LuoguAPITester:
    def __init__(self):
        self.session = requests.Session()
        # 设置符合API要求的User-Agent（不能包含python-requests）
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'Referer': 'https://www.luogu.com.cn/',
        })
        self.csrf_token = None
        self.base_url = 'https://www.luogu.com.cn'
    
    def get_csrf_token(self):
        """获取CSRF Token"""
        try:
            print("正在获取CSRF Token...")
            response = self.session.get(f'{self.base_url}/')
            if response.status_code == 200:
                # 尝试从HTML中提取CSRF Token
                soup = BeautifulSoup(response.text, 'html.parser')
                csrf_meta = soup.find('meta', {'name': 'csrf-token'})
                if csrf_meta:
                    self.csrf_token = csrf_meta.get('content')
                    print(f"✅ 成功获取CSRF Token: {self.csrf_token[:20]}...")
                    # 更新session的默认headers
                    self.session.headers.update({
                        'x-csrf-token': self.csrf_token
                    })
                    return True
                else:
                    print("❌ 未找到CSRF Token")
                    return False
            else:
                print(f"❌ 获取主页失败，状态码: {response.status_code}")
                return False
        except Exception as e:
            print(f"❌ 获取CSRF Token时出错: {e}")
            return False
    
    def test_problem_list(self, keyword="模板", page=1):
        """测试获取题目列表API"""
        print(f"\n🔍 测试题目列表API (关键词: {keyword})")
        try:
            params = {
                'type': 'P',
                'keyword': keyword,
                'page': page,
                '_contentOnly': '1'
            }
            headers = {
                'x-luogu-type': 'content-only'
            }
            
            response = self.session.get(
                f'{self.base_url}/problem/list',
                params=params,
                headers=headers
            )
            
            print(f"状态码: {response.status_code}")
            if response.status_code == 200:
                try:
                    data = response.json()
                    if 'currentData' in data and 'problems' in data['currentData']:
                        problems = data['currentData']['problems']['result']
                        print(f"✅ 成功获取 {len(problems)} 个题目")
                        for i, problem in enumerate(problems[:3]):  # 显示前3个题目
                            print(f"  {i+1}. {problem['pid']} - {problem['title']}")
                        return True
                    else:
                        print("❌ 响应格式不正确")
                        print(f"响应内容: {response.text[:200]}...")
                except json.JSONDecodeError:
                    print("❌ 响应不是有效的JSON格式")
                    print(f"响应内容: {response.text[:200]}...")
            else:
                print(f"❌ 请求失败，状态码: {response.status_code}")
                print(f"响应内容: {response.text[:200]}...")
            return False
        except Exception as e:
            print(f"❌ 测试题目列表API时出错: {e}")
            return False
    
    def test_problem_detail(self, pid="P1000"):
        """测试获取题目详情API"""
        print(f"\n📄 测试题目详情API (题目: {pid})")
        try:
            headers = {
                'x-lentille-request': 'content-only'
            }
            
            response = self.session.get(
                f'{self.base_url}/problem/{pid}',
                headers=headers
            )
            
            print(f"状态码: {response.status_code}")
            if response.status_code == 200:
                try:
                    data = response.json()
                    if 'currentData' in data and 'problem' in data['currentData']:
                        problem = data['currentData']['problem']
                        print(f"✅ 成功获取题目: {problem['title']}")
                        print(f"  难度: {problem.get('difficulty', 'N/A')}")
                        print(f"  通过数: {problem.get('totalAccepted', 'N/A')}")
                        return True
                    else:
                        print("❌ 响应格式不正确")
                        print(f"响应内容: {response.text[:200]}...")
                except json.JSONDecodeError:
                    print("❌ 响应不是有效的JSON格式")
                    print(f"响应内容: {response.text[:200]}...")
            else:
                print(f"❌ 请求失败，状态码: {response.status_code}")
                print(f"响应内容: {response.text[:200]}...")
            return False
        except Exception as e:
            print(f"❌ 测试题目详情API时出错: {e}")
            return False
    
    def test_user_search(self, keyword="admin"):
        """测试用户搜索API"""
        print(f"\n👤 测试用户搜索API (关键词: {keyword})")
        try:
            params = {
                'keyword': keyword
            }
            
            response = self.session.get(
                f'{self.base_url}/api/user/search',
                params=params
            )
            
            print(f"状态码: {response.status_code}")
            if response.status_code == 200:
                try:
                    data = response.json()
                    if 'users' in data:
                        users = [user for user in data['users'] if user is not None]
                        print(f"✅ 成功搜索到 {len(users)} 个用户")
                        for i, user in enumerate(users[:3]):  # 显示前3个用户
                            print(f"  {i+1}. {user['name']} (UID: {user['uid']})")
                        return True
                    else:
                        print("❌ 响应格式不正确")
                        print(f"响应内容: {response.text[:200]}...")
                except json.JSONDecodeError:
                    print("❌ 响应不是有效的JSON格式")
                    print(f"响应内容: {response.text[:200]}...")
            else:
                print(f"❌ 请求失败，状态码: {response.status_code}")
                print(f"响应内容: {response.text[:200]}...")
            return False
        except Exception as e:
            print(f"❌ 测试用户搜索API时出错: {e}")
            return False
    
    def test_captcha(self):
        """测试获取验证码图片"""
        print(f"\n🖼️ 测试获取验证码图片")
        try:
            response = self.session.get(f'{self.base_url}/api/verify/captcha')
            print(f"状态码: {response.status_code}")
            print(f"Content-Type: {response.headers.get('content-type', 'N/A')}")
            
            if response.status_code == 200:
                if 'image' in response.headers.get('content-type', ''):
                    print(f"✅ 成功获取验证码图片 ({len(response.content)} bytes)")
                    return True
                else:
                    print("❌ 响应不是图片格式")
            else:
                print(f"❌ 获取验证码失败，状态码: {response.status_code}")
            return False
        except Exception as e:
            print(f"❌ 测试验证码时出错: {e}")
            return False
    
    def test_config(self):
        """测试获取配置API"""
        print(f"\n⚙️ 测试获取配置API")
        try:
            response = self.session.get(f'{self.base_url}/_lfe/config')
            print(f"状态码: {response.status_code}")
            
            if response.status_code == 200:
                try:
                    data = response.json()
                    print(f"✅ 成功获取配置信息")
                    if 'currentUser' in data:
                        user = data['currentUser']
                        if user:
                            print(f"  当前用户: {user.get('name', 'N/A')} (UID: {user.get('uid', 'N/A')})")
                        else:
                            print("  当前用户: 未登录")
                    return True
                except json.JSONDecodeError:
                    print("❌ 响应不是有效的JSON格式")
                    print(f"响应内容: {response.text[:200]}...")
            else:
                print(f"❌ 获取配置失败，状态码: {response.status_code}")
            return False
        except Exception as e:
            print(f"❌ 测试配置API时出错: {e}")
            return False
    
    def test_login_page(self):
        """测试访问登录页面"""
        print(f"\n🔐 测试访问登录页面")
        try:
            response = self.session.get(f'{self.base_url}/auth/login')
            print(f"状态码: {response.status_code}")
            
            if response.status_code == 200:
                print("✅ 成功访问登录页面")
                # 检查是否包含登录表单
                if 'login' in response.text.lower() or 'password' in response.text.lower():
                    print("✅ 页面包含登录相关内容")
                    return True
                else:
                    print("❓ 页面可能不是标准登录页面")
                    return False
            else:
                print(f"❌ 访问登录页面失败，状态码: {response.status_code}")
                return False
        except Exception as e:
            print(f"❌ 测试登录页面时出错: {e}")
            return False
    
    def test_login_api(self, username=None, password=None):
        """测试登录API（需要用户名和密码）"""
        print(f"\n🔑 测试登录API")
        
        if not username or not password:
            print("⚠️ 未提供用户名和密码，跳过登录测试")
            print("  如需测试登录，请在代码中提供用户名和密码")
            return False
        
        try:
            # 确保有CSRF Token
            if not self.csrf_token:
                print("❌ 缺少CSRF Token，无法进行登录")
                return False
            
            login_data = {
                'username': username,
                'password': password,
                'captcha': ''  # 如果需要验证码，这里需要填入
            }
            
            headers = {
                'Content-Type': 'application/json',
                'x-csrf-token': self.csrf_token,
                'Referer': f'{self.base_url}/auth/login'
            }
            
            response = self.session.post(
                f'{self.base_url}/do-auth/password',
                json=login_data,
                headers=headers
            )
            
            print(f"状态码: {response.status_code}")
            
            if response.status_code == 200:
                try:
                    data = response.json()
                    if data.get('success', False):
                        print("✅ 登录成功")
                        return True
                    else:
                        print(f"❌ 登录失败: {data.get('message', '未知错误')}")
                except json.JSONDecodeError:
                    print("❌ 响应不是有效的JSON格式")
                    print(f"响应内容: {response.text[:200]}...")
            else:
                print(f"❌ 登录请求失败，状态码: {response.status_code}")
                print(f"响应内容: {response.text[:200]}...")
            
            return False
        except Exception as e:
            print(f"❌ 测试登录API时出错: {e}")
            return False
    
    def run_all_tests(self):
        """运行所有测试"""
        print("🚀 开始洛谷API测试")
        print("=" * 50)
        
        # 获取CSRF Token
        csrf_success = self.get_csrf_token()
        
        # 运行各项测试
        tests = [
            ("配置信息API", self.test_config),
            ("验证码图片API", self.test_captcha),
            ("登录页面访问", self.test_login_page),
            ("登录API测试", lambda: self.test_login_api()),  # 不提供用户名密码，仅测试接口
            ("题目列表API", lambda: self.test_problem_list("模板")),
            ("题目详情API", lambda: self.test_problem_detail("P1000")),
            ("用户搜索API", lambda: self.test_user_search("admin")),
        ]
        
        results = []
        for test_name, test_func in tests:
            try:
                result = test_func()
                results.append((test_name, result))
            except Exception as e:
                print(f"❌ {test_name} 测试异常: {e}")
                results.append((test_name, False))
        
        # 输出测试结果汇总
        print("\n" + "=" * 50)
        print("📊 测试结果汇总:")
        for test_name, result in results:
            status = "✅ 通过" if result else "❌ 失败"
            print(f"  {test_name}: {status}")
        
        success_count = sum(1 for _, result in results if result)
        print(f"\n总计: {success_count}/{len(results)} 项测试通过")
        
        if csrf_success:
            print(f"CSRF Token: {self.csrf_token}")

def main():
    """主函数"""
    tester = LuoguAPITester()
    tester.run_all_tests()

if __name__ == "__main__":
    main()
