import subprocess


def ui_to_py(path: str):
    """
    将 .ui 文件转换为 Python 代码
    :param path:
    :return:
    """
    input_file = path + 'main.ui'
    output_file = path + 'modules/ui_main.py'

    # 将 .ui 文件转换为 Python 代码
    result = subprocess.run(['pyside6-uic', input_file, '-o', output_file], capture_output=True,
                            text=True)
    if result.returncode != 0:
        print("界面文件转换失败：", end="")
        print(result.stderr)
        exit()

    # 将 import resources_rc 改成 from . resources_rc import *
    with open(output_file, 'r') as file:
        data = file.read()
    data = data.replace('import resources_rc', 'from . resources_rc import *')
    with open(output_file, 'w') as file:
        file.write(data)


if __name__ == '__main__':
    ui_to_py('')
