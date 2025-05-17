import re
import urllib.parse
import requests
from bs4 import BeautifulSoup
from typing import List, Optional, Dict
import time
import random
from threading import Thread

class WebSpider:
    def __init__(self, config: Dict):
        """
        初始化网页爬虫

        参数:
            config (dict): 配置字典，包含:
                          - max_spider_count: 最大爬取URL数量
                          - timeout: 请求超时时间(秒)
                          - retry: 重试次数
                          - use_ssl: 是否使用SSL
                          - redirect_do_get: 是否跟随重定向
                          - user_agents: 可选的User-Agent列表
        """
        self.config = config
        self.all_urls = set()  # 存储所有找到的URL，使用集合去重
        self.all_no_param_urls = set()  # 用于去重的无参数URL
        self.visited_urls = set()  # 记录已经爬取过的URL，避免重复爬取

        # 可配置的User-Agent列表，防止被识别为爬虫
        self.user_agents = config.get('user_agents', [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0"
        ])

    def crawl_links(self, start_url: str) -> None:
        """
        从起始URL开始爬取链接

        参数:
            start_url (str): 起始爬取的URL
        """
        try:
            # 自动检测是否使用HTTPS
            self.config['use_ssl'] = start_url.startswith('https')

            # 解析URL
            parsed_url = urllib.parse.urlparse(start_url)

            # 获取根域名
            root_domain = self._get_root_domain(parsed_url.hostname)

            # 发送HTTP请求
            response = self._send_request(start_url)

            if response and response.status_code == 200 and len(response.text) > 10:
                # 使用BeautifulSoup解析HTML
                soup = BeautifulSoup(response.text, 'html.parser')

                # 查找所有带href的链接
                for link in soup.find_all('a', href=True):
                    href = link['href']
                    if not self._is_valid_link(href):
                        continue

                    # 标准化URL
                    normalized_url = self._normalize_url(href, parsed_url)

                    # 检查是否属于目标域名
                    if root_domain in normalized_url:
                        # 清理URL参数用于去重
                        no_param_url = self._remove_url_params(normalized_url)

                        # 跳过已访问过的URL
                        if normalized_url not in self.visited_urls and len(self.all_urls) < self.config['max_spider_count']:
                            self.visited_urls.add(normalized_url)
                            self.all_urls.add(normalized_url)
                            self.all_no_param_urls.add(no_param_url)

                            # 延迟避免过快请求
                            time.sleep(random.uniform(0.5, 2.0))

                            # 递归爬取(可取消注释启用深度爬取)
                            # self.crawl_links(normalized_url)

        except Exception as e:
            print(f"爬取过程中发生错误: {str(e)}")

    def scan_for_sql_injection(self) -> List[Dict]:
        """添加错误处理的扫描方法"""
        injection_points = []

        for url in self.all_urls:
            try:
                if '?' not in url:
                    continue

                params = self._extract_url_params(url)
                if params and self._is_potential_injection(params):
                    injection_points.append({
                        'url': url,
                        'type': 'URL参数',
                        'params': params,
                        'risk': '高危'
                    })

                forms = self._find_forms(url)
                for form in forms:
                    if self._is_potential_injection(form['inputs']):
                        injection_points.append({
                            'url': url,
                            'type': '表单',
                            'action': form['action'],
                            'method': form['method'],
                            'inputs': form['inputs'],
                            'risk': '高危'
                        })

            except Exception as e:
                print(f"扫描URL {url} 时出错: {str(e)}")
                continue

        return injection_points

    def _send_request(self, url: str) -> Optional[requests.Response]:
        """
        发送HTTP请求(带重试机制)
        """
        for _ in range(self.config['retry']):
            try:
                headers = {
                    'User-Agent': random.choice(self.user_agents)
                }
                response = requests.get(
                    url,
                    timeout=self.config['timeout'],
                    allow_redirects=self.config['redirect_do_get'],
                    verify=False,  # 忽略SSL验证(生产环境不推荐)
                    headers=headers
                )
                return response
            except requests.RequestException as e:
                print(f"请求失败: {url} - {str(e)}")
                time.sleep(1)  # 重试间隔
                continue
        return None

    def _is_valid_link(self, href: str) -> bool:
        """检查链接是否有效"""
        if not href or '?' not in href or '=' not in href:
            return False
        if href.lower().startswith('javascript:'):
            return False
        if '.' not in href and '/' not in href:
            return False
        return True

    def _normalize_url(self, href: str, parsed_url: urllib.parse.ParseResult) -> str:
        """标准化URL格式"""
        href = href.replace('&amp;', '&')

        if href.startswith('//'):
            return f"{parsed_url.scheme}:{href}"
        elif href.startswith('/'):
            return f"{parsed_url.scheme}://{parsed_url.hostname}{href}"
        elif not any(x in href for x in ['http://', 'https://', 'www.']):
            return f"{parsed_url.scheme}://{parsed_url.hostname}{href}"

        return href.split('>')[0] if '>' in href else href

    def _find_forms(self, url: str) -> List[Dict]:
        """查找页面中的表单"""
        response = self._send_request(url)
        if not response or response.status_code != 200:
            return []

        forms = []
        soup = BeautifulSoup(response.text, 'html.parser')

        for form in soup.find_all('form'):
            form_info = {
                'action': self._get_full_url(url, form.get('action', '')),
                'method': form.get('method', 'get').lower(),
                'inputs': []
            }

            for input_tag in form.find_all(['input', 'textarea', 'select']):
                if input_tag.name == 'input' and input_tag.get('type', '').lower() in ['hidden', 'submit', 'button']:
                    continue

                field = {
                    'name': input_tag.get('name', ''),
                    'type': input_tag.get('type', 'text') if input_tag.name == 'input' else input_tag.name,
                    'value': input_tag.get('value', '')
                }
                form_info['inputs'].append(field)

            forms.append(form_info)

        return forms

    @staticmethod
    def _get_root_domain(hostname: str) -> str:
        """提取根域名"""
        parts = hostname.split('.')
        return '.'.join(parts[-2:]) if len(parts) > 2 else hostname

    @staticmethod
    def _remove_url_params(url: str) -> str:
        """移除URL中的参数部分"""
        return url.split('?')[0]

    @staticmethod
    def _extract_url_params(url: str) -> Dict:
        """更健壮的URL参数提取"""
        try:
            query = urllib.parse.urlparse(url).query
            if not query:
                return {}

            params = {}
            for param in query.split('&'):
                parts = param.split('=', 1)
                if len(parts) == 2:
                    params[parts[0]] = parts[1]
            return params

        except Exception as e:
            print(f"参数提取错误: {str(e)}")
            return {}

    @staticmethod
    def _is_potential_injection(fields) -> bool:
        """检查是否是潜在的SQL注入点"""
        suspicious_keywords = ['user', 'pass', 'id', 'name', 'query', 'search',
                               'select', 'insert', 'update', 'delete', 'where']

        # 处理表单字段列表
        if isinstance(fields, list):
            for field in fields:
                if isinstance(field, dict):
                    field_name = field.get('name', '')
                    if any(keyword in field_name.lower() for keyword in suspicious_keywords):
                        return True

        # 处理URL参数字典
        elif isinstance(fields, dict):
            for param_name in fields.keys():
                if any(keyword in param_name.lower() for keyword in suspicious_keywords):
                    return True

        return False

    @staticmethod
    def _get_full_url(base_url: str, relative_url: str) -> str:
        """将相对URL转换为完整URL"""
        if not relative_url:
            return base_url
        return urllib.parse.urljoin(base_url, relative_url)


if __name__ == "__main__":
    # 配置参数
    config = {
        'max_spider_count': 50,
        'timeout': 10,
        'retry': 3,
        'use_ssl': False,
        'redirect_do_get': True,
        'user_agents': [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0"
        ]
    }

    # 创建爬虫实例
    spider = WebSpider(config)

    # 用户输入目标URL
    target_url = input("请输入要扫描的网站URL: ").strip()
    if not target_url.startswith(('http://', 'https://')):
        target_url = f"http://{target_url}"

    print(f"\n开始爬取: {target_url}")

    # 执行爬取
    spider.crawl_links(target_url)

    # 输出结果
    print(f"\n找到 {len(spider.all_urls)} 个带参数的URL:")
    for url in spider.all_urls:
        print(url)

    # 扫描SQL注入点
    print("\n扫描潜在的SQL注入点...")
    injection_points = spider.scan_for_sql_injection()

    if injection_points:
        print(f"\n发现 {len(injection_points)} 个潜在的SQL注入点:")
        for point in injection_points:
            print(f"\n类型: {point['type']}")
            print(f"URL: {point['url']}")
            if point['type'] == '表单':
                print(f"表单Action: {point['action']}")
                print(f"请求方法: {point['method'].upper()}")
            print("可疑参数:")
            for param in (point['params'] if 'params' in point else point['inputs']):
                if isinstance(param, dict):
                    print(f"  {param['name']} ({param['type']})")
                else:
                    print(f"  {param}")
            print(f"风险等级: {point['risk']}")
    else:
        print("\n未发现明显的SQL注入点")
