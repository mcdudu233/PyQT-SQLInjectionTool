import re
import urllib.parse
import requests
from bs4 import BeautifulSoup
from typing import List, Optional, Dict

# 测试的URL
url = 'https://passport.jd.com/uc/login'

# 创建一个会话对象来保持会话状态
session = requests.Session()

# 发送GET请求，获取网页内容
response = session.get(url)

# 检查响应状态
if response.status_code == 200:
    html_content = response.text

    # 使用 BeautifulSoup 解析HTML内容
    soup = BeautifulSoup(html_content, 'html.parser')

    # 查找网页中负责登录的部分，可能是form，也可能是其他元素
    login_form = soup.find('form') or soup.find('div', {'id': 'login'})  # 处理不同结构



