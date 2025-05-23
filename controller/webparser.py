import requests
from urllib.parse import urljoin, urlparse
from bs4 import BeautifulSoup


class WebParser:
    def __init__(self, url, html=None):
        self.base_url = url
        self.html = html
        self.session = requests.Session()
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) ParamScanner/2.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
        }
        self.parsed_url = urlparse(url)

    def _get_page_content(self):
        """获取页面内容并返回BeautifulSoup对象"""
        if self.html is None:
            try:
                response = self.session.get(
                    self.base_url,
                    headers=self.headers,
                    timeout=15,
                    allow_redirects=True
                )
                response.raise_for_status()
                return BeautifulSoup(response.content, 'html.parser')
            except Exception as e:
                print(f"Request failed: {str(e)}")
                return None
        else:
            return BeautifulSoup(self.html, 'html.parser')

    def _extract_form_elements(self, soup):
        """提取所有表单元素（包括游离元素）的详细信息"""
        forms = []

        # 处理标准表单
        for form in soup.find_all('form'):
            form_data = self._process_form_structure(form)
            forms.append(form_data)

        # 处理游离元素组成的虚拟表单
        lone_form = self._process_lone_elements(soup)
        if lone_form['params']:
            forms.append(lone_form)

        return forms

    def _process_form_structure(self, form):
        """处理单个标准表单结构"""
        form_info = {
            'action': self._resolve_url(form.get('action', '')),
            'method': form.get('method', 'get').lower(),
            'enctype': form.get('enctype', 'application/x-www-form-urlencoded'),
            'params': {}
        }

        # 处理输入元素
        for tag in form.find_all(['input', 'textarea', 'select']):
            param_info = self._extract_param_details(tag)
            if param_info:
                form_info['params'].setdefault(param_info['name'], []).append(param_info['value'])

        # 处理重复参数（合并为逗号分隔）
        for name, values in form_info['params'].items():
            form_info['params'][name] = ', '.join(filter(None, values))

        return form_info

    def _process_lone_elements(self, soup):
        """处理游离在表单外的输入元素"""
        virtual_form = {
            'action': self.base_url,
            'method': 'get',
            'params': {}
        }

        # 收集所有未被表单包含的元素
        for tag in soup.find_all(['input', 'textarea', 'select']):
            if not tag.find_parent('form'):
                param_info = self._extract_param_details(tag)
                if param_info:
                    virtual_form['params'].setdefault(param_info['name'], []).append(param_info['value'])

        # 合并重复参数
        for name, values in virtual_form['params'].items():
            virtual_form['params'][name] = ', '.join(filter(None, values))

        return virtual_form

    def _extract_param_details(self, tag):
        """提取单个HTML元素的参数详情"""
        param = {'name': None, 'value': None}

        # 过滤不需要处理的元素类型
        if tag.name == 'input':
            input_type = tag.get('type', 'text').lower()
            if input_type in ['button', 'image', 'reset']:
                return None
            param['name'] = tag.get('name')
            param['value'] = tag.get('value', '')
        elif tag.name == 'textarea':
            param['name'] = tag.get('name')
            param['value'] = tag.text.strip()
        elif tag.name == 'select':
            param['name'] = tag.get('name')
            options = tag.find_all('option')
            if options:
                selected = next((opt for opt in options if 'selected' in opt.attrs), None)
                param['value'] = selected.get('value', selected.text) if selected else options[0].get('value',
                                                                                                      options[0].text)

        # 有效性检查
        if not param['name'] or param['value'] is None:
            return None

        return param

    def _resolve_url(self, path):
        """解析完整的URL路径"""
        if not path:
            return self.base_url
        return urljoin(self.base_url, path)

    def get_all_parameters(self):
        """获取所有参数集合"""
        soup = self._get_page_content()
        if not soup:
            return []

        return self._extract_form_elements(soup)

    def generate_requests(self):
        """生成可用于测试的请求参数集合"""
        requests_list = []
        for form in self.get_all_parameters():
            request = {
                'url': form['action'],
                'method': form['method'],
                'headers': self.headers.copy(),
                'params': form['params']
            }
            requests_list.append(request)
        return requests_list


def test():
    target_url = 'http://localhost/vul/sqli/sqli_str.php'
    extractor = WebParser(target_url)
    forms = extractor.get_all_parameters()

    print(f"Discovered {len(forms)} parameter sets")
    for index, form in enumerate(forms, 1):
        print(f"\nSet {index}:")
        print(f"URL: {form['action']}")
        print(f"Method: {form['method'].upper()}")
        print(f"Parameters ({len(form['params'])}):")
        for name, value in form['params'].items():
            print(f"  {name}: {value}")
