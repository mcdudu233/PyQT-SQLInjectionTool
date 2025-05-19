import ui
from controller import webparser
from service import sqlmapapi
from ui.setup import ui_to_py, rc_to_py

if __name__ == '__main__':
    # 测试代码
    test = False
    if test:
        sqlmapapi.test()
        webparser.test()

    # 每次运行前先编译界面和资源文件
    rc_to_py('ui/')
    ui_to_py('ui/')

    # 运行主界面
    ui.main()
