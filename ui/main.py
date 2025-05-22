# ///////////////////////////////////////////////////////////////
#
# BY: WANDERSON M.PIMENTA
# PROJECT MADE WITH: Qt Designer and PySide6
# V: 1.0.0
#
# This project can be used freely for all uses, as long as they maintain the
# respective credits only in the Python scripts, any information in the visual
# interface (GUI) can be modified without any implication.
#
# There are limitations on Qt licenses if you want to use your products
# commercially, I recommend reading them on the official website:
# https://doc.qt.io/qtforpython/licenses.html
#
# ///////////////////////////////////////////////////////////////
import ctypes
import sys
import os
import platform

# IMPORT / GUI AND MODULES AND WIDGETS
# ///////////////////////////////////////////////////////////////
from controller.ui import *
from .modules import *
from .widgets import *

# SET AS GLOBAL WIDGETS
# ///////////////////////////////////////////////////////////////
widgets = None

# 自适应Windows系统缩放比例
try:
    # 调用 Windows API 函数获取缩放比例
    user32 = ctypes.windll.user32
    user32.SetProcessDPIAware()
    scaling_factor = user32.GetDpiForSystem()
    # 计算缩放比例
    scaling_factor = scaling_factor / 96.0
    print("Windows桌面的缩放比例:", scaling_factor)
    dpi = scaling_factor * 100
    os.environ["QT_FONT_DPI"] = str(dpi)

except Exception as e:
    print("获取Windows桌面缩放比例时出错:", e)
    os.environ["QT_FONT_DPI"] = "96"  # 采用默认值


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.dragPos = None
        # 加载界面UI文件
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        global widgets
        widgets = self.ui

        # 加载自定义主题
        useCustomTheme = False
        themeFile = "ui\\themes\\py_dracula_light.qss"
        if useCustomTheme:
            UIFunctions.theme(self, themeFile, True)
            AppFunctions.setThemeHack(self)

        # 使用自定义工具栏 | MAC 和 LINUX 改为 False
        Settings.ENABLE_CUSTOM_TITLE_BAR = True

        # 程序名
        title = "SQL自动注入工具"
        description = "SQL自动注入工具"
        self.setWindowTitle(title)
        widgets.titleRightInfo.setText(description)

        # 设置界面功能绑定
        UIFunctions.uiDefinitions(self)

        # 菜单按钮信号槽绑定
        widgets.toggleButton.clicked.connect(lambda: UIFunctions.toggleMenu(self, True))
        widgets.btn_home.clicked.connect(self.menuButtonClick)
        widgets.btn_exit.clicked.connect(self.menuButtonClick)
        widgets.btn_manualInjection.clicked.connect(self.menuButtonClick)
        widgets.btn_dataCenter.clicked.connect(self.menuButtonClick)
        widgets.btn_command.clicked.connect(self.menuButtonClick)
        widgets.btn_logCenter.clicked.connect(self.menuButtonClick)
        widgets.btn_fileOperation.clicked.connect(self.menuButtonClick)

        # 侧边栏
        def openCloseLeftBox():
            UIFunctions.toggleLeftBox(self, True)

        def openCloseRightBox():
            UIFunctions.toggleRightBox(self, True)

        widgets.settingsTopBtn.clicked.connect(openCloseRightBox)

        # 设置主页
        widgets.stackedWidget.setCurrentWidget(widgets.autoInjection)
        widgets.btn_home.setStyleSheet(UIFunctions.selectMenu(widgets.btn_home.styleSheet()))

        # 绑定其他页面控件
        self.widgetsFunctions = UIWidgetsFunctions(self, self.ui)

        ### 手动注入界面信号槽 ###
        widgets.btn_startInjection.clicked.connect(self.widgetsFunctions.startInjection)
        widgets.autoUrl.textChanged.connect(self.widgetsFunctions.setAutoUrl)
        widgets.inspectionInterval.textChanged.connect(self.widgetsFunctions.setInspectionInterval)
        widgets.injectionType.currentIndexChanged.connect(self.widgetsFunctions.setStyleSheetInjectionType)
        widgets.https.stateChanged.connect(self.widgetsFunctions.ifHttps)
        widgets.databaseType.currentIndexChanged.connect(self.widgetsFunctions.setDatabase)
        widgets.requestMethod.currentIndexChanged.connect(self.widgetsFunctions.setRequestMethod)
        widgets.btn_addParam.clicked.connect(self.widgetsFunctions.addParamToList)
        widgets.btn_deleteParam.clicked.connect(self.widgetsFunctions.deleteParamFromList)
        widgets.injectionLevel.currentIndexChanged.connect(self.widgetsFunctions.setInjectionLevel)
        widgets.riskLevel.currentIndexChanged.connect(self.widgetsFunctions.setRiskLevel)

        ### 自动输入界面信号槽 ###
        widgets.browse.clicked.connect(self.widgetsFunctions.startBrowsing)
        widgets.detection.clicked.connect(self.widgetsFunctions.startDetection)
        widgets.url.textChanged.connect(self.widgetsFunctions.setURL)
        widgets.webPage.loadFinished.connect(self.widgetsFunctions.finishWebPage)
        self.ui.webPage.setZoomFactor(0.5)

        ### 数据中心界面信号槽 ###
        self.ui.databaseTreeModel = QStandardItemModel()
        self.ui.databaseTreeModel.setHorizontalHeaderLabels(["数据库结构"])
        widgets.databaseTree.setModel(self.ui.databaseTreeModel)
        widgets.databaseTree.doubleClicked.connect(self.widgetsFunctions.expandTree)
        widgets.btn_getData.clicked.connect(self.widgetsFunctions.gettingData)
        widgets.btn_exportData.clicked.connect(self.widgetsFunctions.exportData)
        widgets.btn_getDatabaseContent.clicked.connect(self.widgetsFunctions.getDatabseContent)


        ### 命令执行界面信号槽 ###

        widgets.btn_startCommand.clicked.connect(self.widgetsFunctions.startCommand)
        widgets.commandInput.textChanged.connect(self.widgetsFunctions.setCommand)
        widgets.echoResults.stateChanged.connect(self.widgetsFunctions.ifEchoResults)

        ### 文件操作界面信号槽 ###
        widgets.btn_startFileOperation.clicked.connect(self.widgetsFunctions.startFileOperation)
        widgets.path.textChanged.connect(self.widgetsFunctions.setPath)
        widgets.fileOperationType.currentIndexChanged.connect(self.widgetsFunctions.setFileOperation)

        # 显示界面
        self.show()

    # 菜单栏被点击
    def menuButtonClick(self):
        # GET BUTTON CLICKED
        btn = self.sender()
        btnName = btn.objectName()

        # SHOW HOME PAGE
        if btnName == "btn_home":
            widgets.stackedWidget.setCurrentWidget(widgets.autoInjection)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        # SHOW MANUALINJECTION
        if btnName == "btn_manualInjection":
            widgets.stackedWidget.setCurrentWidget(widgets.manualInjection)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        # SHOW LOGCENTER
        if btnName == "btn_logCenter":
            widgets.stackedWidget.setCurrentWidget(widgets.logCenter)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        # SHOW DATACENTER
        if btnName == "btn_dataCenter":
            widgets.stackedWidget.setCurrentWidget(widgets.dataCenter)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        # SHOW COMMAND
        if btnName == "btn_command":
            widgets.stackedWidget.setCurrentWidget(widgets.command)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        # SHOW LOGCENTER
        if btnName == "btn_logCenter":
            widgets.stackedWidget.setCurrentWidget(widgets.logCenter)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        # SHOW NEW PAGE
        if btnName == "btn_new":
            widgets.stackedWidget.setCurrentWidget(widgets.new_page)  # SET PAGE
            UIFunctions.resetStyle(self, btnName)  # RESET ANOTHERS BUTTONS SELECTED
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))  # SELECT MENU

        # SHOW FILEOPERATION
        if btnName == "btn_fileOperation":
            widgets.stackedWidget.setCurrentWidget(widgets.fileOperation)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        if btnName == "btn_exit":
            del self.widgetsFunctions
            sys.exit(0)

        # PRINT BTN NAME
        # print(f'Button "{btnName}" pressed!')

    # 尺寸改变事件
    def resizeEvent(self, event):
        # Update Size Grips
        UIFunctions.resize_grips(self)

    # 鼠标事件
    def mousePressEvent(self, event):
        # SET DRAG POS WINDOW
        self.dragPos = event.globalPos()

        # PRINT MOUSE EVENTS
        if event.buttons() == Qt.LeftButton:
            print('Mouse click: LEFT CLICK')
        if event.buttons() == Qt.RightButton:
            print('Mouse click: RIGHT CLICK')

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton and self.dragPos:
            self.move(self.pos() + event.globalPos() - self.dragPos)
            self.dragPos = event.globalPos()
            event.accept()

    def mouseReleaseEvent(self, event):
        self.dragPos = None
        event.accept()


def main():
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("icon.ico"))
    window = MainWindow()
    code = app.exec_()
    del window.widgetsFunctions
    sys.exit(code)
