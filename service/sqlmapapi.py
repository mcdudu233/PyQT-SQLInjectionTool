import requests
import time

# base_url1 = "http://localhost:8775"
BASE_URL = "http://127.0.0.1:8775/"


def get_version():
    """获取服务器版本"""
    response = requests.get(f"{BASE_URL}/version")
    response.raise_for_status()
    return response.json()


def create_task():
    """创建新任务"""
    response = requests.get(f"{BASE_URL}/task/new")
    response.raise_for_status()
    data = response.json()
    if data.get("success"):
        return data["taskid"]
    raise Exception("Failed to create task")


def start_scan(taskid, url):
    """启动扫描"""
    response = requests.post(
        f"{BASE_URL}/scan/{taskid}/start",
        json={"url": url},
        headers={"Content-Type": "application/json"}
    )
    response.raise_for_status()
    return response.json()


def get_scan_status(taskid):
    """获取扫描状态"""
    response = requests.get(f"{BASE_URL}/scan/{taskid}/status")
    response.raise_for_status()
    return response.json()


def get_scan_data(taskid):
    """获取扫描结果"""
    response = requests.get(f"{BASE_URL}/scan/{taskid}/data")
    response.raise_for_status()
    return response.json()


def delete_task(taskid):
    """删除任务"""
    response = requests.get(f"{BASE_URL}/task/{taskid}/delete")
    response.raise_for_status()
    return response.json()


def poll_scan_completion(taskid, interval=5):
    """轮询扫描状态直到完成"""
    while True:
        status = get_scan_status(taskid)
        if status["status"] in ["terminated", "stopped"]:
            return status
        time.sleep(interval)


# 使用示例
if __name__ == "__main__":
    taskid = None
    try:
        # 获取版本信息
        version_info = get_version()
        print(f"Server version: {version_info['version']}")

        # 创建新任务
        taskid = create_task()
        print(f"Created new task: {taskid}")

        # 启动扫描
        scan_start = start_scan(taskid, "http://testphp.vulnweb.com/artists.php?artist=1")
        print(f"Scan started: {scan_start}")

        # 轮询扫描状态
        print("Polling scan status...")
        final_status = poll_scan_completion(taskid)
        print(f"Final scan status: {final_status}")

        # 获取扫描结果
        scan_data = get_scan_data(taskid)
        print(f"Scan data: {scan_data}")

    except requests.exceptions.RequestException as e:
        print(f"HTTP error occurred: {str(e)}")
    except Exception as e:
        print(f"Error: {str(e)}")
    finally:
        # 清理任务
        if taskid:
            delete_task(taskid)
            print(f"Task {taskid} deleted")
