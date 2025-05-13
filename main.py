import ui
from ui.setup import ui_to_py

if __name__ == '__main__':
    # 每次运行前先编译.ui文件
    ui_to_py('ui/')

    # 运行主界面
    ui.main()
