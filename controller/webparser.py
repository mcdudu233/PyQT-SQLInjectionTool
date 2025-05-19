import re
import urllib.parse
import requests
from bs4 import BeautifulSoup
from typing import List, Optional, Dict

# 测试的URL
url = 'https://demo.testfire.net/login.jsp'

# 发送GET请求，获取网页内容
response = requests.get(url)

# 将网页内容转化为BeautifulSoup对象，方便解析
soup = BeautifulSoup(response.content, "html.parser")

# 检查响应状态
if response.status_code == 200:
    html_content = response.text

    # 使用 BeautifulSoup 解析HTML内容
    soup = BeautifulSoup(html_content, 'html.parser')

    # 查找网页中负责登录的部分form
    login_form = soup.find('form')