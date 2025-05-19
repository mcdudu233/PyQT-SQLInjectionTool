import re
import urllib.parse
import requests
from bs4 import BeautifulSoup
from typing import List, Optional, Dict

# 测试的URL
url = 'https://demo.testfire.net/login.jsp'

# 创建一个会话对象来保持会话状态
session = requests.Session()

# 发送GET请求，获取网页内容
response = session.get(url)

# 检查响应状态
if response.status_code == 200:
    html_content = response.text

    # 使用 BeautifulSoup 解析HTML内容
    soup = BeautifulSoup(html_content, 'html.parser')

    # 查找网页中负责登录的部分form
    login_form = soup.find('form')

    if login_form:
        print("找到登录表单")

        # 获取表单的提交地址
        action_url = login_form.get('action')

        # 如果action_url是相对路径，将其与基础URL拼接
        if action_url and not action_url.startswith(('http://', 'https://')):
            action_url = urllib.parse.urljoin(url, action_url)  # 拼接成完整的URL

        print(f"登录表单提交地址: {action_url}")

        # 查找用户名和密码字段
        username_input = login_form.find('input', {'name': 'uid'})
        password_input = login_form.find('input', {'name': 'password'})

        # 获取其他可能存在的隐藏字段，如CSRF Token
        csrf_token_input = login_form.find('input', {'name': 'CSRFToken'})  # 假设CSRF token字段名为CSRFToken

        # 获取csrf_token值，如果存在
        csrf_token = csrf_token_input['value'] if csrf_token_input else None

        # 填充表单数据
        data = {
            'uid': 'your_username',  # 替换为实际的用户名
            'password': 'your_password',  # 替换为实际的密码
        }

        # 如果有CSRF token，添加到表单数据中
        if csrf_token:
            data['CSRFToken'] = csrf_token

        # 提交POST请求模拟登录
        login_response = session.post(action_url, data=data)

        # 检查登录是否成功
        if login_response.status_code == 200:
            print("登录成功！")
            # 登录成功后，你可以继续访问需要登录才能查看的页面
            dashboard_url = 'https://demo.testfire.net/dashboard.jsp'  # 假设这是登录后的页面
            dashboard_response = session.get(dashboard_url)
            if dashboard_response.status_code == 200:
                print("成功访问登录后的页面")
            else:
                print(f"无法访问登录后的页面，状态码: {dashboard_response.status_code}")
        else:
            print("登录失败，状态码:", login_response.status_code)
else:
    print(f"请求失败，状态码: {response.status_code}")
