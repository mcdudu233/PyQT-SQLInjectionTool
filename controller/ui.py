from PySide6.QtCore import QUrl, QTimer
from PySide6.QtWidgets import QMessageBox, QListWidgetItem, QLineEdit, QWidget

from service import SQLMap
from ui.modules import Ui_MainWindow


### 效果函数 ###
def show_border_effect(color, widget: QWidget, step=3, duration=100):
    """显示边框提示"""
    style = widget.styleSheet()
    # 闪多次特效
    for i in range(0, step * 2, 2):
        QTimer.singleShot(duration * i, lambda: _show_border_effect(widget, color))
        QTimer.singleShot(duration * (i + 1), lambda: _reset_border_effect(widget, style))


def _show_border_effect(widget: QWidget, color):
    """显示边框提示"""
    widget.setStyleSheet(f"border-color: {color};")
    widget.style().polish(widget)


def _reset_border_effect(widget: QWidget, style):
    """重置样式"""
    widget.setStyleSheet(style)
    widget.style().polish(widget)


def show_border_effect_yes(widget: QWidget):
    """触发正确提示效果"""
    show_border_effect("#8cd881", widget)


def show_border_effect_no(widget: QWidget):
    """触发错误提示效果"""
    show_border_effect("#ff536f", widget)


### UI组件调用函数 ###
class UIWidgetsFunctions:
    def __init__(self, main, ui: Ui_MainWindow):
        self.main = main
        self.ui = ui

        # SQLMAP API
        self.sqlmap = SQLMap()
        self.current_task_id = None

    ###########################
    ### 自动注入界面组件调用接口 ###
    ###########################
    ### URL设置 lineedit url ###
    def setURL(self):
        pass

    ### 启动浏览 button browse ###
    def startBrowsing(self):
        url = self.ui.url.text()
        if not url.startswith(("http://", "https://")):
            url = "http://" + url
        self.ui.url.setText(url)

        self.ui.webPage.load(url)

    ### 网页加载完成 QWebEngineView webPage ###
    def finishWebPage(self, success):
        # 强制刷新
        self.ui.webPage.repaint()

    ### 开始检测 ###
    def startDetection(self):
        try:
            if self.current_task_id is not None:
                self.sqlmap.delete_task(self.current_task_id)

            self.current_task_id = self.sqlmap.create_task()
            self.sqlmap.start_scan(self.current_task_id, self.ui.url.text())

            self.sqlmap.poll_scan_completion(self.current_task_id)
            data, error = self.sqlmap.get_scan_data(self.current_task_id)

            for i in data:
                print(i)

            for i in error:
                print(i)

            logs = self.sqlmap.get_scan_log(self.current_task_id)
        except Exception as e:
            QMessageBox.critical(self.main, "检测网页失败", str(e))

    ###########################
    ### 手动注入界面组件调用接口 ###
    ###########################
    ### 地址设置 lineedit address ###
    def setAutoUrl(self):
        pass

    ### 超时设置 lineedit overtime ###
    def setInspectionInterval(self):
        pass

    ### 获取注入类型 comboBox injectionTyoe ###
    def setStyleSheetInjectionType(self):
        pass

    ### HTTPS是否选择 checkbox ssl ###
    def ifHttps(self):
        pass

    ### 数据库类型设置 checkbox databaseType ###
    def setDatabase(self):
        pass

    ### 识别注入 button btn_startInjection ###
    def startInjection(self):
        pass

    ### 设置请求方式 ### combox requestMethod
    def setRequestMethod(self):
        pass

    ### 增加参数 ### button btn_addParam  lineedit paramInput  listwidget paramList
    def addParamToList(self):
        if self.ui.paramInput.text() == "":
            show_border_effect_no(self.ui.paramInput)
        else:
            self.ui.paramList.addItem(QListWidgetItem(self.ui.paramInput.text()))

    ### 删除参数 ### button btn_deleteParam
    def deleteParamFromList(self):
        if self.ui.paramList.currentIndex().row() == -1:
            show_border_effect_no(self.ui.paramList)
        else:
            self.ui.paramList.takeItem(self.ui.paramList.currentIndex().row())

    ### 文件操作 ###
    ### 路径名设置 lineedit path ###
    def setPath(self):
        pass

    ### 文件编码设置 comboBox fileOperationCoding ###
    def setFileOprationCoding(self):
        pass

    ### 文件操作设置 conmobox fileOpreation ###
    def setFileOperation(self):
        pass

    ### 开始 button btn_stratFileOperation ###
    def startFileOperation(self):
        pass

    ### 停止  button btn_stopFileOperation ###
    def stopFileOperation(self):
        pass

    ### 显示操作结果 ###
    def showFIleOperation(self):
        pass

    ###########################
    ### 数据中心组件调用接口 ###
    ###########################
    ### 数据库信息展示 plaintextview databaseInformation ###
    def showDatabaseInformation(self):
        pass

    ### 获取数据展示 plaintextview getData ###
    def showGettingData(self):
        pass

    ### 开始标志 lineedit beginning ###
    def setBeginnig(self):
        pass

    ### 条数设置 linedit number ###
    def setNumnber(self):
        pass

    ### 获取数据 btn_getData ###
    def gettingData(self):
        pass

    ### 导出数据 button btn_exportData ###
    def exportData(self):
        pass

    ### 停止获取数据 button stopGettingData ###
    def stopGettingData(self):
        pass

    ### 编码类型 ###
    def dataCodingType(self):
        pass

    ###########################
    ### 命令执行界面组件调用接口 ###
    ###########################
    ### 命令设置 lineedit commandInput ###
    def setCommand(self):
        pass

    ### 开始命令 button btn_startCommand ###
    def startCommand(self):
        pass

    ### 停止命令 button btn_stopCommand ###
    def stopCommand(self):
        pass

    ### 命令展示 plainTextview commandResults ###
    def showCommmad(self):
        pass

    ### 是否选择回显结果 checkbox echoResults ###
    def ifEchoResults(self):
        pass

    ###########################
    ### 日志中心界面组件调用接口 ###
    ###########################
    ### 日志展示 plaintext log ###
    def showLog(self):
        pass

    ### 数据包发包记录 tableWidget packetSendingRecord ###
    def showPacketSendingRecord(self):
        pass
