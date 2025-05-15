import requests
import time

base_url1 = "http://localhost:8775"


class SqlMapApiClient:
    def __init__(self, base_url="http://127.0.0.1:8775/"):
        self.base_url = base_url
        self.session = requests.Session()

    def get_version(self):
        """获取服务器版本"""
        response = self.session.get(f"{self.base_url}/version")
        response.raise_for_status()
        return response.json()

    def create_task(self):
        """创建新任务"""
        response = self.session.get(f"{self.base_url}/task/new")
        response.raise_for_status()
        data = response.json()
        if data.get("success"):
            return data["taskid"]
        raise Exception("Failed to create task")

    def start_scan(self, taskid, url):
        """启动扫描"""
        headers = {"Content-Type": "application/json"}
        response = self.session.post(
            f"{self.base_url}/scan/{taskid}/start",
            json={"url": url},
            headers=headers
        )
        response.raise_for_status()
        return response.json()

    def get_scan_status(self, taskid):
        """获取扫描状态"""
        response = self.session.get(f"{self.base_url}/scan/{taskid}/status")
        response.raise_for_status()
        return response.json()

    def get_scan_data(self, taskid):
        """获取扫描结果"""
        response = self.session.get(f"{self.base_url}/scan/{taskid}/data")
        response.raise_for_status()
        return response.json()

    def stop_scan(self, taskid):
        """停止扫描"""
        response = self.session.get(f"{self.base_url}/scan/{taskid}/stop")
        response.raise_for_status()
        return response.json()

    def delete_task(self, taskid):
        """删除任务"""
        response = self.session.get(f"{self.base_url}/task/{taskid}/delete")
        response.raise_for_status()
        return response.json()

    def poll_scan_completion(self, taskid, interval=5):
        """轮询扫描状态直到完成"""
        while True:
            status = self.get_scan_status(taskid)
            if status["status"] in ["terminated", "stopped"]:
                return status
            time.sleep(interval)


# 使用示例
if __name__ == "__main__":
    # 初始化客户端
    client = SqlMapApiClient()

    try:
        # 获取版本信息
        print("Server version:", client.get_version()["version"])

        # 创建新任务
        taskid = client.create_task()
        print(f"Created new task: {taskid}")

        # 启动扫描
        target_url = "http://testphp.vulnweb.com/artists.php?artist=1"
        scan_start = client.start_scan(taskid, target_url)
        print("Scan started:", scan_start)

        # 轮询扫描状态
        print("Polling scan status...")
        final_status = client.poll_scan_completion(taskid)
        print("Final scan status:", final_status)

        # 获取扫描结果
        scan_data = client.get_scan_data(taskid)
        print("Scan data:", scan_data)

    finally:
        # 清理任务
        if taskid:
            client.delete_task(taskid)
            print(f"Task {taskid} deleted")
