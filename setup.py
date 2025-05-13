from cx_Freeze import setup, Executable

from ui.setup import ui_to_py, rc_to_py


def py_to_exe():
    """将Python脚本转换为可执行文件"""

    files = ['ui/icon.ico', 'ui/themes/']

    target = Executable(
        script="main.py",
        base="Win32GUI",
        icon="ui/icon.ico"
    )

    setup(
        name="SQL注入工具",
        version="1.0",
        description="基于PyQt的自动化SQL注入工具",
        author="dudu233,nini233,Astrid233,jingchuan",
        options={'build_exe': {'include_files': files}},
        executables=[target]
    )


if __name__ == '__main__':
    # 先编译界面文件和资源文件
    rc_to_py('ui/')
    ui_to_py('ui/')

    # 创建可执行文件
    py_to_exe()
