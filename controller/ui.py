from PySide6.QtCore import QUrl

from ui.modules import Ui_MainWindow


class UIWidgetsFunctions:
    def __init__(self, main, ui: Ui_MainWindow):
        self.main = main
        self.ui = ui

    ###########################
    ### 自动注入界面组件调用接口 ###
    ###########################
    ### URL设置 lineedit url ###
    def setURL(self): pass

    ### 启动浏览 button browse ###
    def startBrowing(self):
        url = self.ui.url.text()
        if not url.startswith(("http://", "https://")):
            url = "http://" + url
        self.ui.url.setText(url)

        self.ui.webPage.setUrl(QUrl(url))
        self.ui.webPage.repaint()

    ### 网页加载完成 QWebEngineView webPage ###
    def finishWebPage(self, success):
        # 强制刷新
        self.ui.webPage.repaint()

    ### 开始检测 ###
    def startDetection(self):pass

    ###########################
    ### 手动注入界面组件调用接口 ###
    ###########################
    ### 地址设置 lineedit address ###
    def setAddress(self): pass

    ### 超时设置 lineedit overtime ###
    def setOvertime(self): pass

    ### 获取注入类型 comboBox injectionTyoe ###
    def setStyleSheetInjectionType(self): pass

    ### 线程设置 lineedit thread ###
    def setThread(self): pass

    ### 端口设置 lineedit portID ###
    def setPortID(self): pass

    ### SSL是否选择 checkbox ssl ###
    def ifSSL(self): pass

    ### 编码设置 checkbox coding ###
    def setCoding(self): pass

    ### 数据库类型设置 checkbox databaseType ###
    def setDatabase(self): pass

    ### 重试次数设置 lineedit retry ###
    def setRetryTimes(self): pass

    ### 识别注入 button btn_startInjection ###
    def startInjection(self): pass

    ### 到处配置 button btn_exportConfiguration ###
    def exportConfiguration(self): pass

    ### 文件操作 ###
    ### 路径名设置 lineedit path ###
    def setPath(self): pass

    ### 文件编码设置 comboBox fileOperationCoding ###
    def setFileOprationCoding(self): pass

    ### 文件操作设置 conmobox fileOpreation ###
    def setFileOperation(self): pass

    ### 开始 button btn_stratFileOperation ###
    def startFileOperation(self): pass

    ### 停止  button btn_stopFileOperation ###
    def stopFileOperation(self): pass

    ### 显示操作结果 ###
    def showFIleOperation(self): pass

    ###########################
    ### 数据中心组件调用接口 ###
    ###########################
    ### 数据库信息展示 plaintextview databaseInformation ###
    def showDatabaseInformation(self): pass

    ### 获取数据展示 plaintextview getData ###
    def showGettingData(self): pass

    ### 开始标志 lineedit beginning ###
    def setBeginnig(self): pass

    ### 条数设置 linedit number ###
    def setNumnber(self): pass

    ### 获取数据 btn_getData ###
    def gettingData(self): pass

    ### 导出数据 button btn_exportData ###
    def exportData(self): pass

    ### 停止获取数据 button stopGettingData ###
    def stopGettingData(self): pass

    ### 编码类型 ###
    def dataCodingType(self): pass

    ###########################
    ### 命令执行界面组件调用接口 ###
    ###########################
    ### 命令设置 lineedit commandInput ###
    def setCommand(self): pass

    ### 开始命令 button btn_startCommand ###
    def startCommand(self): pass

    ### 停止命令 button btn_stopCommand ###
    def stopCommand(self): pass

    ### 命令展示 plainTextview commandResults ###
    def showCommmad(self): pass

    ### 是否选择回显结果 checkbox echoResults ###
    def ifEchoResults(self): pass

    ###########################
    ### 日志中心界面组件调用接口 ###
    ###########################
    ### 日志展示 plaintext log ###
    def showLog(self): pass

    ### 数据包发包记录 tableWidget packetSendingRecord ###
    def showPacketSendingRecord(self): pass
