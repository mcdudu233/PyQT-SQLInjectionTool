import subprocess
from threading import Thread
from time import sleep

import requests

from PySide6.QtWidgets import QApplication

from service import logger

# SQLMap 服务器默认配置
RESTAPI_DEFAULT_ADAPTER = "wsgiref"
RESTAPI_DEFAULT_ADDRESS = "127.0.0.1"
RESTAPI_DEFAULT_PORT = 8775


class SQLMapServer:
    def __init__(self, address=None, port=None, adapter=None):
        self.logger = logger.setup("SQLMapServer")
        self.address = RESTAPI_DEFAULT_ADDRESS if address is None else address
        self.port = RESTAPI_DEFAULT_PORT if port is None else port
        self.adapter = RESTAPI_DEFAULT_ADAPTER if adapter is None else adapter
        self.process = None

        self.start()

    def __delete__(self, instance):
        self.stop()

    def _read_stream(self, stream, logger_method):
        """实时读取流并记录日志"""
        for line in iter(stream.readline, ''):
            if line.strip():
                logger_method(line.strip())

    def start(self):
        if self.process:
            self.stop()

        cmd = [
            "python",
            "sqlmap/sqlmapapi.py",
            "-s",
            "-H", self.address,
            "-p", str(self.port)
        ]
        self.process = subprocess.Popen(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            universal_newlines=True,
            creationflags=subprocess.CREATE_NO_WINDOW
        )

        # 启动线程监控输出
        Thread(target=self._read_stream, args=(self.process.stdout, self.logger.info)).start()
        Thread(target=self._read_stream, args=(self.process.stderr, self.logger.error)).start()

        self.logger.info(f"SQLMap API server started on {self.address}:{self.port}")

    def stop(self):
        if self.process:
            self.process.terminate()
            self.process = None
            self.logger.info("SQLMap API server stopped")


class SQLMap:
    def __init__(self):
        self.logger = logger.setup("SQLMapAPI")
        self.server = SQLMapServer()
        self.base_url = f"http://{self.server.address}:{self.server.port}/"

        self.logger.info("SQLMap API initialized at %s", self.base_url)

    def get_version(self):
        """获取服务器版本"""
        response = requests.get(f"{self.base_url}/version")
        if response.status_code == 200:
            data = response.json()
            if data.get("success"):
                return data.get("version")
            else:
                self.logger.error(f"Failed to get version: {data.get('message')}")
                raise Exception("获取SQLMap版本失败！原因：{}！".format(data.get("message")))
        else:
            self.logger.error(f"Failed to get version: {response.status_code}")
            raise Exception("获取SQLMap版本失败！请求返回码：{}！".format(response.status_code))

    def create_task(self):
        """创建新任务"""
        response = requests.get(f"{self.base_url}/task/new")
        if response.status_code == 200:
            data = response.json()
            if data.get("success"):
                return data.get("taskid")
            else:
                self.logger.error(f"创建任务失败: {data.get('message')}")
                raise Exception("创建任务失败！原因：{}！".format(data.get("message")))
        else:
            self.logger.error(f"创建任务失败，状态码：{response.status_code}")
            raise Exception("创建任务失败！请求返回码：{}！".format(response.status_code))

    def start_scan(self, taskid, url, **kwargs):
        """启动扫描"""
        response = requests.post(
            f"{self.base_url}/scan/{taskid}/start",
            json={"url": url} | kwargs,
            headers={"Content-Type": "application/json"}
        )
        if response.status_code == 200:
            data = response.json()
            if data.get("success"):
                return data.get("engineid")
            else:
                self.logger.error(f"启动扫描失败: {data.get('message')}")
                raise Exception("启动扫描失败！原因：{}！".format(data.get("message")))
        else:
            self.logger.error(f"启动扫描失败，状态码：{response.status_code}")
            raise Exception("启动扫描失败！请求返回码：{}！".format(response.status_code))

    def stop_scan(self, taskid):
        """停止扫描"""
        response = requests.get(f"{self.base_url}/scan/{taskid}/stop")
        if response.status_code == 200:
            data = response.json()
            if data.get("success"): \
                    return True
            else:
                self.logger.error(f"停止扫描失败: {data.get('message')}")
                raise Exception("停止扫描失败！原因：{}！".format(data.get("message")))
        else:
            self.logger.error(f"停止扫描失败，状态码：{response.status_code}")
            raise Exception("停止扫描失败！请求返回码：{}！".format(response.status_code))

    def get_scan_status(self, taskid):
        """
        获取扫描状态
        :status running terminated
        :returncode None 0~999
        :returns status returncode
        """
        response = requests.get(f"{self.base_url}/scan/{taskid}/status")
        if response.status_code == 200:
            data = response.json()
            if data.get("success"):
                return data.get("status"), data.get("returncode")
            else:
                self.logger.error(f"获取状态失败: {data.get('message')}")
                raise Exception("获取扫描状态失败！原因：{}！".format(data.get("message")))
        else:
            self.logger.error(f"获取状态失败，状态码：{response.status_code}")
            raise Exception("获取扫描状态失败！请求返回码：{}！".format(response.status_code))

    def get_scan_data(self, taskid):
        """
        获取扫描结果
        :returns data error
        """
        response = requests.get(f"{self.base_url}/scan/{taskid}/data")
        if response.status_code == 200:
            data = response.json()
            if data.get("success"):
                return data.get("data"), data.get("error")
            else:
                self.logger.error(f"获取数据失败: {data.get('message')}")
                raise Exception("获取扫描数据失败！原因：{}！".format(data.get("message")))
        else:
            self.logger.error(f"获取数据失败，状态码：{response.status_code}")
            raise Exception("获取扫描数据失败！请求返回码：{}！".format(response.status_code))

    def get_scan_log(self, taskid):
        """获取扫描日志"""
        response = requests.get(f"{self.base_url}/scan/{taskid}/log")
        if response.status_code == 200:
            data = response.json()
            if data.get("success"):
                return data.get("log")
            else:
                self.logger.error(f"获取日志失败: {data.get('message')}")
                raise Exception("获取扫描日志失败！原因：{}！".format(data.get("message")))
        else:
            self.logger.error(f"获取日志失败，状态码：{response.status_code}")
            raise Exception("获取扫描日志失败！请求返回码：{}！".format(response.status_code))

    def delete_task(self, taskid):
        """删除任务"""
        response = requests.get(f"{self.base_url}/task/{taskid}/delete")
        if response.status_code == 200:
            data = response.json()
            if data.get("success"):
                return data.get("success")
            else:
                self.logger.error(f"删除任务失败: {data.get('message')}")
                raise Exception("删除任务失败！原因：{}！".format(data.get("message")))
        else:
            self.logger.error(f"删除任务失败，状态码：{response.status_code}")
            raise Exception("删除任务失败！请求返回码：{}！".format(response.status_code))

    def poll_scan_completion(self, taskid, interval=800):
        """轮询扫描状态直到完成"""
        i = 0
        while True:
            try:
                i += 1
                if i == interval:
                    i = 0
                    status, _ = self.get_scan_status(taskid)
                    if status == "terminated":
                        return status
                QApplication.processEvents()
                sleep(0.001)
            except Exception as e:
                raise Exception("轮询扫描状态时发生异常")


# 使用示例
def test():
    taskid = None
    try:
        sqlmap = SQLMap()

        # 获取版本信息
        version_info = sqlmap.get_version()
        print(f"Server version: {version_info}")

        # 创建新任务
        taskid = sqlmap.create_task()
        print(f"Created new task: {taskid}")

        # 启动扫描
        scan_start = sqlmap.start_scan(taskid, "http://testphp.vulnweb.com/artists.php?artist=1")
        scan_start = sqlmap.start_scan(taskid, "http://testphp.vulnweb.com/artists.php?artist=1", getDbs=True)
        print(f"Scan started: {scan_start}")

        # 轮询扫描状态
        print("Polling scan status...")
        final_status = sqlmap.poll_scan_completion(taskid)
        print(f"Final scan status: {final_status}")

        # 获取扫描结果
        scan_data, _ = sqlmap.get_scan_data(taskid)
        print(f"Scan data:")
        for i in scan_data[0]:
            print(i)

        # 获取扫描日志
        scan_log = sqlmap.get_scan_log(taskid)
        print(f"Scan log:")
        for i in scan_log:
            print(i)
    except Exception as e:
        print(f"Error: {str(e)}")
    finally:
        # 清理任务
        if taskid:
            sqlmap.delete_task(taskid)
            print(f"Task {taskid} deleted")
        pass
