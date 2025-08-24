#!/usr/bin/env python3
"""
洛谷登录测试脚本（安全版本）
用于安全地测试洛谷登录功能
"""

import requests
import json
import getpass
from bs4 import BeautifulSoup

class LuoguLoginTester:
    def __init__(self):
        self.session = requests.Session()
        # 设置符合API要求的User-Agent
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'Referer': 'https://www.luogu.com.cn/',
        })
        self.csrf_token = None
        self.base_url = 'https://www.luogu.com.cn'
    
    def get_csrf_token_from_login_page(self):
        """从登录页面获取CSRF Token"""
        try:
            print("正在从登录页面获取CSRF Token...")
            response = self.session.get(f'{self.base_url}/auth/login')
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                csrf_meta = soup.find('meta', {'name': 'csrf-token'})
                if csrf_meta:
                    self.csrf_token = csrf_meta.get('content')
                    print(f"✅ 成功获取CSRF Token: {self.csrf_token[:20]}...")
                    return True
                else:
                    print("❌ 未找到CSRF Token")
                    return False
            else:
                print(f"❌ 获取登录页面失败，状态码: {response.status_code}")
                return False
        except Exception as e:
            print(f"❌ 获取CSRF Token时出错: {e}")
            return False
    
    def check_current_user(self):
        """检查当前登录状态"""
        try:
            print("\n🔍 检查当前登录状态...")
            response = self.session.get(f'{self.base_url}/_lfe/config')
            if response.status_code == 200:
                data = response.json()
                if 'currentUser' in data and data['currentUser']:
                    user = data['currentUser']
                    print(f"✅ 当前已登录用户: {user.get('name', 'N/A')} (UID: {user.get('uid', 'N/A')})")
                    return True
                else:
                    print("❌ 当前未登录")
                    return False
            else:
                print(f"❌ 检查登录状态失败，状态码: {response.status_code}")
                return False
        except Exception as e:
            print(f"❌ 检查登录状态时出错: {e}")
            return False
    
    def login_with_credentials(self, username, password, captcha=''):
        """使用用户名和密码登录"""
        try:
            print(f"\n🔑 尝试登录用户: {username}")
            
            # 确保有CSRF Token
            if not self.csrf_token:
                if not self.get_csrf_token_from_login_page():
                    print("❌ 无法获取CSRF Token，登录失败")
                    return False
            
            # 准备登录数据
            login_data = {
                'username': username,
                'password': password,
                'captcha': captcha
            }
            
            headers = {
                'Content-Type': 'application/json',
                'x-csrf-token': self.csrf_token,
                'Referer': f'{self.base_url}/auth/login'
            }
            
            # 发送登录请求
            response = self.session.post(
                f'{self.base_url}/do-auth/password',
                json=login_data,
                headers=headers
            )
            
            print(f"登录请求状态码: {response.status_code}")
            
            if response.status_code == 200:
                try:
                    data = response.json()
                    if data.get('success', False):
                        print("✅ 登录成功！")
                        # 验证登录状态
                        self.check_current_user()
                        return True
                    else:
                        error_msg = data.get('message', '未知错误')
                        print(f"❌ 登录失败: {error_msg}")
                        
                        # 检查是否需要验证码（处理Unicode编码的错误信息）
                        needs_captcha = (
                            'captcha' in error_msg.lower() or 
                            'verification' in error_msg.lower() or 
                            '验证码' in error_msg or
                            '\u8bf7\u8f93\u5165\u9a8c\u8bc1\u7801' in error_msg or  # "请输入验证码"的Unicode
                            data.get('errorMessage') == '\u8bf7\u8f93\u5165\u9a8c\u8bc1\u7801'
                        )
                        
                        if needs_captcha:
                            print("💡 需要验证码，请查看 captcha.jpg 文件")
                            captcha_code = input("请输入验证码: ").strip()
                            if captcha_code:
                                print("🔄 使用验证码重新尝试登录...")
                                return self.login_with_credentials(username, password, captcha_code)
                            else:
                                print("❌ 未输入验证码，登录失败")
                                return False
                        
                        return False
                except json.JSONDecodeError:
                    print("❌ 登录响应不是有效的JSON格式")
                    print(f"响应内容: {response.text[:200]}...")
                    return False
            else:
                print(f"❌ 登录请求失败，状态码: {response.status_code}")
                print(f"响应内容: {response.text[:200]}...")
                
                # 对于400错误，也要检查是否需要验证码
                if response.status_code == 400:
                    try:
                        data = response.json()
                        error_msg = data.get('errorMessage', data.get('message', ''))
                        
                        # 检查是否需要验证码
                        needs_captcha = (
                            'captcha' in error_msg.lower() or 
                            'verification' in error_msg.lower() or 
                            '验证码' in error_msg or
                            '\u8bf7\u8f93\u5165\u9a8c\u8bc1\u7801' in error_msg or
                            error_msg == '\u8bf7\u8f93\u5165\u9a8c\u8bc1\u7801'
                        )
                        
                        if needs_captcha:
                            print("💡 需要验证码，请查看 captcha.jpg 文件")
                            captcha_code = input("请输入验证码: ").strip()
                            if captcha_code:
                                print("🔄 使用验证码重新尝试登录...")
                                return self.login_with_credentials(username, password, captcha_code)
                            else:
                                print("❌ 未输入验证码，登录失败")
                                return False
                    except json.JSONDecodeError:
                        pass
                
                return False
                
        except Exception as e:
            print(f"❌ 登录过程中出错: {e}")
            return False
    
    def get_captcha_image(self):
        """获取验证码图片"""
        try:
            print("\n🖼️ 获取验证码图片...")
            response = self.session.get(f'{self.base_url}/api/verify/captcha')
            if response.status_code == 200:
                # 保存验证码图片
                with open('captcha.jpg', 'wb') as f:
                    f.write(response.content)
                print(f"✅ 验证码图片已保存为 captcha.jpg ({len(response.content)} bytes)")
                return True
            else:
                print(f"❌ 获取验证码失败，状态码: {response.status_code}")
                return False
        except Exception as e:
            print(f"❌ 获取验证码时出错: {e}")
            return False
    
    def interactive_login(self):
        """交互式登录"""
        print("🚀 洛谷安全登录测试")
        print("=" * 50)
        
        # 检查当前登录状态
        if self.check_current_user():
            print("您已经登录，无需重新登录")
            return True
        
        # 获取CSRF Token
        if not self.get_csrf_token_from_login_page():
            print("无法获取CSRF Token，无法继续登录")
            return False
        
        # 获取验证码（可选）
        get_captcha = input("\n是否需要获取验证码图片？(y/N): ").lower().strip()
        if get_captcha == 'y':
            self.get_captcha_image()
        
        # 获取登录凭据
        print("\n请输入登录信息:")
        username = input("用户名或邮箱: ").strip()
        if not username:
            print("❌ 用户名不能为空")
            return False
        
        password = getpass.getpass("密码: ")
        if not password:
            print("❌ 密码不能为空")
            return False
        
        # 尝试登录
        return self.login_with_credentials(username, password)

def main():
    """主函数"""
    tester = LuoguLoginTester()
    
    print("洛谷登录测试工具")
    print("注意: 此工具仅用于测试API功能，请使用您自己的账号")
    print("密码输入时不会显示，这是正常的安全行为")
    print()
    
    # 交互式登录
    success = tester.interactive_login()
    
    if success:
        print("\n🎉 登录测试成功！")
        print("您现在可以测试需要登录的API功能")
    else:
        print("\n❌ 登录测试失败")
        print("请检查用户名、密码是否正确，或是否需要验证码")

if __name__ == "__main__":
    main()
