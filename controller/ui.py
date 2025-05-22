import datetime
import html
from PySide6.QtCore import QTimer, Qt, QModelIndex
from PySide6.QtGui import QStandardItem
from PySide6.QtWidgets import QMessageBox, QListWidgetItem, QLineEdit, QWidget, QTableWidgetItem

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
        self.current_kwargs = None

    def __del__(self):
        # 关闭SQLMap API
        if self.sqlmap:
            self.sqlmap.stop()

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
        try:
            self.ui.btn_startInjection.setDisabled(True)

            if self.current_task_id is not None:
                self.sqlmap.delete_task(self.current_task_id)
                self.current_task_id = None
            task_id = self.sqlmap.create_task()

            # 额外的参数
            kwargs = {}

            # 预处理URL
            url = self.ui.autoUrl.text()
            if not url.startswith(("http://", "https://")):
                if self.ui.https:
                    url = "https://" + url
                else:
                    url = "http://" + url
            self.ui.autoUrl.setText(url)

            # 获取注入参数
            if self.ui.paramList.count() == 0:
                params = None
            else:
                params = []
                for i in range(self.ui.paramList.count()):
                    params.append(self.ui.paramList.item(i).text())
                kwargs |= {"testParameter": ",".join(params)}

            # 请求方式
            if self.ui.requestMethod.currentText() == "GET":
                if params is not None:
                    url += "?"
                    for key in params:
                        url += key + "=xxx&"
                    url = url[:len(url) - 1]
                kwargs |= {"method": "GET"}
            elif self.ui.requestMethod.currentText() == "POST":
                if params is not None:
                    tmp = ""
                    for key in params:
                        tmp += key + "=xxx&"
                    tmp = tmp[:len(tmp) - 1]
                    kwargs |= {"data": tmp}
                kwargs |= {"method": "POST"}
            else:
                kwargs |= {"method": self.ui.requestMethod.currentText()}

            # 数据库类型
            if self.ui.databaseType.currentText() != "自动检测":
                kwargs |= {"dbms": self.ui.databaseType.currentText()}

            # 注入方式
            if self.ui.injectionType.currentText() != "自动检测":
                # B：Boolean-based blind（布尔盲注） 1
                # E：Error-based（报错注入） 2
                # Q：Inline queries（内联注入） 3
                # S：Stacked queries（堆叠注入） 4
                # T：Time-based blind（时间盲注） 5
                # U：Union query-based（联合注入） 6
                key = None
                tmp = self.ui.injectionType.currentText()
                if tmp == "布尔盲注":
                    key = "B"
                elif tmp == "报错注入":
                    key = "E"
                elif tmp == "内联注入":
                    key = "Q"
                elif tmp == "堆叠注入":
                    key = "S"
                elif tmp == "时间盲注":
                    key = "T"
                elif tmp == "联合注入":
                    key = "U"
                if key is not None:
                    kwargs |= {"technique": key}

            # 风险等级
            kwargs |= {"risk": self.ui.riskLevel.currentText()}

            # 注入等级
            kwargs |= {"level": self.ui.injectionLevel.currentText()}

            # 加入URL
            kwargs |= {"url": url}

            # 不需要用户干预
            kwargs |= {"batch": True}

            # 尝试注入
            self.current_kwargs = kwargs
            self.sqlmap.start_scan(task_id, **kwargs)

            # 等待并获取数据
            self.sqlmap.poll_scan_completion(task_id)
            datas, errors = self.sqlmap.get_scan_data(task_id)

            if len(datas) == 0 and len(errors) == 0:
                QMessageBox.warning(self.main, "注入失败", "未检测到注入点，详细信息请查看日志！")
                self.ui.btn_logCenter.click()
            else:
                for data in datas:
                    # print(data)
                    # 解析注入的数据
                    if data["type"] == 1:
                        for value in data["value"]:
                            # 允许的注入类型
                            for inject in value["data"]:
                                if self.ui.injectionType.currentText() == "自动检测":
                                    show_border_effect_yes(self.ui.injectionType)
                                    self.ui.injectionType.setCurrentIndex(int(inject))
                                    break
                            # 数据库类型
                            if self.ui.databaseType.currentText() == "自动检测":
                                show_border_effect_yes(self.ui.databaseType)
                                self.ui.databaseType.setCurrentText(value["dbms"])

                            # 添加到注入日志
                            for inject in value["data"]:
                                self.showPayloadRecord(
                                    [url, value["data"][inject]["title"], value["data"][inject]["payload"],
                                     value["data"][inject]["matchRatio"]])
                            self.showDatabaseInformation([value["dbms"], value["dbms_version"], value["os"]])
                            # for i in value:
                            #     print(i)
                for error in errors:
                    print(error)

            logs = self.sqlmap.get_scan_log(task_id)
            for log in logs:
                self.showLog(log["message"], log["level"], log["time"])

            self.current_task_id = task_id
            self.ui.btn_startInjection.setDisabled(False)
        except Exception as e:
            QMessageBox.critical(self.main, "注入失败", "注入失败，请查看日志！原因：" + str(e))
            print(e)

            self.ui.btn_startInjection.setDisabled(False)
            self.ui.btn_logCenter.click()

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

    ### 设置注入类型 combox injectionLevel###
    def setInjectionLevel(self):
        pass

    ### 设置风险等级 combox riskLevel ###
    def setRiskLevel(self):
        pass

    ### 文件操作 ###
    ### 路径名设置 lineedit path ###
    def setPath(self):
        pass

    ### 文件操作设置 conmobox fileOpreation ###
    def setFileOperation(self):
        pass

    ### 开始 button btn_startFileOperation ###
    def startFileOperation(self):
        if self.current_task_id is None:
            QMessageBox.information(self.main, "提示", "当前没有注入对象！请先到自动注入或手动注入界面识别注入！")
        else:
            if self.ui.path.text() == "":
                show_border_effect_no(self.ui.path)
                return

            try:
                if self.ui.fileOperationType.currentText() == "读取文件":
                    kwargs = self.current_kwargs | {"fileRead": self.ui.path.text()}
                elif self.ui.fileOperationType.currentText() == "写入文件":
                    kwargs = self.current_kwargs | {"fileWrite": self.ui.path.text(), "fileDest": self.ui.path.text()}
                else:
                    pass

                self.sqlmap.start_scan(self.current_task_id, **kwargs)
                # 等待并获取数据
                self.sqlmap.poll_scan_completion(self.current_task_id)
                datas, errors = self.sqlmap.get_scan_data(self.current_task_id)

                if self.ui.fileOperationType.currentText() == "读取文件":
                    for data in datas[::-1]:
                        if data["type"] == 22:
                            bin_data = data["value"]
                            if len(bin_data) == 0:
                                self.ui.fileOperationResults.setPlainText(
                                    f"读取靶机文件 '{self.ui.path.text()}' 失败！或者文件内容为空！")
                            else:
                                try:
                                    # 写入文件
                                    # with open(self.ui.path.text(), "wb") as f:
                                    #     f.write(bin_data)

                                    self.ui.fileOperationResults.setPlainText(bin_data)
                                except Exception as e:
                                    self.ui.fileOperationResults.setPlainText(
                                        f"文件显示失败！请查看编码是否匹配！原因：{str(e)}")
                            break
                elif self.ui.fileOperationType.currentText() == "写入文件":
                    for data in datas[::-1]:
                        print(data)
                        if data["type"] == 23:
                            break
                else:
                    pass

                for error in errors:
                    print(error)

                logs = self.sqlmap.get_scan_log(self.current_task_id)
                for log in logs:
                    self.showLog(log["message"], log["level"], log["time"])
            except Exception as e:
                QMessageBox.critical(self.main, "文件操作失败", "文件操作失败，请查看日志！原因：" + str(e))
                print(e)


    ### 显示操作结果 ###
    def showFIleOperation(self):
        pass



    ###########################
    ### 数据中心组件调用接口 ###
    ###########################
    ### 数据库信息展示 tablewidget databaseInformation 无绑定槽函数需求，可直接在函数中调用###
    def showDatabaseInformation(self, args, startAt=1):
        row = startAt
        for i in range(len(args)):
            if self.ui.databaseInformation.item(row, 1) is None:
                if args[i] is None:
                    args[i] = "未知"
                elif type(args[i]) is list:
                    args[i] = ",".join(args[i])
                self.ui.databaseInformation.setItem(row, 1, QTableWidgetItem(str(args[i])))
            else:
                self.ui.databaseInformation.item(row, 1).setText(args[i])
            row += 1

    ### 表信息展示 tablwidget tableInformation 无绑定槽函数需求，可直接在函数中调用###
    def showTableInformation(self):
        pass

    ### 数据库内容展示 treewidget databaseContent 无绑定槽函数需求，可直接在函数中调用###
    def showDatabseContent(self):
        pass

    ### 开始标志 lineedit beginning ###
    def setBeginnig(self):
        pass

    ### 条数设置 linedit number ###
    def setNumnber(self):
        pass

    ### 获取数据 btn_getData ###
    def gettingData(self):
        if self.current_task_id is None:
            QMessageBox.information(self.main, "提示", "当前没有注入对象！请先到自动注入或手动注入界面识别注入！")
        else:
            try:
                kwargs = self.current_kwargs | {"extensiveFp": True, "getHostname": True,
                                                "getCurrentUser": True, "getCurrentDb": True}
                self.sqlmap.start_scan(self.current_task_id, **kwargs)
                # 等待并获取数据
                self.sqlmap.poll_scan_completion(self.current_task_id)
                datas, errors = self.sqlmap.get_scan_data(self.current_task_id)

                args = []

                # 主机名
                for data in datas[::-1]:
                    if data["type"] == 6:
                        args.append(data["value"])
                        break

                # 当前用户
                for data in datas[::-1]:
                    if data["type"] == 4:
                        args.append(data["value"])
                        break

                # 当前数据库
                for data in datas[::-1]:
                    if data["type"] == 5:
                        args.append(data["value"])
                        break

                # 数据库指纹
                for data in datas[::-1]:
                    if data["type"] == 2:
                        args.append(data["value"])
                        break

                self.showDatabaseInformation(args, 4)

                for error in errors:
                    print(error)

                logs = self.sqlmap.get_scan_log(self.current_task_id)
                for log in logs:
                    self.showLog(log["message"], log["level"], log["time"])
            except Exception as e:
                QMessageBox.critical(self.main, "获取数据库信息失败", "获取数据库信息失败，请查看日志！原因：" + str(e))
                print(e)

    ### 导出数据 button btn_exportData ###
    def exportData(self):
        pass

    ### 停止获取数据 button stopGettingData ###
    def stopGettingData(self):
        pass

    ### 获取数据库内容 button btn_getDatabaseContent###
    def getDatabseContent(self):
        if self.current_task_id is None:
            QMessageBox.information(self.main, "提示", "当前没有注入对象！请先到自动注入或手动注入界面识别注入！")
        else:
            try:
                kwargs = self.current_kwargs | {"getDbs": True}
                self.sqlmap.start_scan(self.current_task_id, **kwargs)
                # 等待并获取数据
                self.sqlmap.poll_scan_completion(self.current_task_id)
                datas, errors = self.sqlmap.get_scan_data(self.current_task_id)

                # 获取数据库
                for data in datas[::-1]:
                    if data["type"] == 12:
                        databases = data["value"]
                        for database in databases:
                            db_item = QStandardItem(database)
                            db_item.setFlags(db_item.flags() & ~Qt.ItemIsEditable)
                            db_item.setData("database", Qt.UserRole + 1)  # 类型标识
                            db_item.setData(False, Qt.UserRole + 2)  # 是否已加载
                            db_item.setToolTip(f"双击展开，加载当前数据库表")
                            self.ui.databaseTreeModel.appendRow(db_item)
                        break

                for error in errors:
                    print(error)

                logs = self.sqlmap.get_scan_log(self.current_task_id)
                for log in logs:
                    self.showLog(log["message"], log["level"], log["time"])
            except Exception as e:
                QMessageBox.critical(self.main, "获取数据库内容失败", "获取数据库内容失败，请查看日志！原因：" + str(e))
                print(e)

    ### 编码类型 ###
    def dataCodingType(self):
        pass

    ### 双击展开树形 ###
    def expandTree(self, index: QModelIndex):
        item = self.ui.databaseTreeModel.itemFromIndex(index)

        if not item:
            return

        if item.data(Qt.UserRole + 1) == "database":
            try:
                # 已经加载过
                if item.data(Qt.UserRole + 2):
                    return

                # 添加加载提示
                loading_item = QStandardItem("加载中...")
                loading_item.setEnabled(False)
                item.appendRow(loading_item)
                self.ui.databaseTree.expand(index)

                kwargs = self.current_kwargs | {"db": item.text(), "getTables": True}
                self.sqlmap.start_scan(self.current_task_id, **kwargs)
                # 等待并获取数据
                self.sqlmap.poll_scan_completion(self.current_task_id)
                datas, errors = self.sqlmap.get_scan_data(self.current_task_id)

                # 移除加载提示
                item.removeRow(0)

                # 添加表节点
                for data in datas[::-1]:
                    if data["type"] == 13:
                        tables = data["value"][item.text()]
                        for table in tables:
                            table_item = QStandardItem(table)
                            table_item.setFlags(table_item.flags() & ~Qt.ItemIsEditable)
                            table_item.setData("table", Qt.UserRole + 1)
                            table_item.setToolTip(f"双击获取表数据")
                            item.appendRow(table_item)
                        # print(data["value"])
                        break

                # 标记已加载
                item.setData(True, Qt.UserRole + 2)
                self.ui.databaseTree.expand(index)

                for error in errors:
                    print(error)

                logs = self.sqlmap.get_scan_log(self.current_task_id)
                for log in logs:
                    self.showLog(log["message"], log["level"], log["time"])
            except Exception as e:
                QMessageBox.critical(self.main, "获取数据库表失败", "获取数据库表失败，请查看日志！原因：" + str(e))
                print(e)
        elif item.data(Qt.UserRole + 1) == "table":
            # 加载表内容
            try:
                # 添加加载提示
                self.ui.tableInformation.clear()
                self.ui.tableInformation.setRowCount(1)
                self.ui.tableInformation.setColumnCount(1)
                self.ui.tableInformation.setItem(0, 0, QTableWidgetItem("加载中..."))

                kwargs = self.current_kwargs | {"tbl": item.text(), "dumpTable": True}
                self.sqlmap.start_scan(self.current_task_id, **kwargs)
                # 等待并获取数据
                self.sqlmap.poll_scan_completion(self.current_task_id)
                datas, errors = self.sqlmap.get_scan_data(self.current_task_id)

                # 移除加载提示
                self.ui.tableInformation.clear()

                # 添加表节点
                for data in datas[::-1]:
                    if data["type"] == 17:
                        # print(data["value"])
                        tables: dict = data["value"]
                        self.ui.tableInformation.setColumnCount(len(tables))
                        self.ui.tableInformation.setRowCount(len(tables))
                        i = 0
                        for column in tables:
                            # print(column)
                            self.ui.tableInformation.setItem(0, i, QTableWidgetItem(column))
                            if tables[column].get('values') is not None:
                                j = 1
                                for word in tables[column]["values"]:
                                    # print(word)
                                    self.ui.tableInformation.setItem(j, i, QTableWidgetItem(word))
                                    j += 1

                            # table_item = QStandardItem(table)
                            # table_item.setFlags(table_item.flags() & ~Qt.ItemIsEditable)
                            # table_item.setData("table", Qt.UserRole + 1)
                            # table_item.setToolTip(f"双击获取表数据")
                            # item.appendRow(table_item)
                            i += 1
                        break

                for error in errors:
                    print(error)

                logs = self.sqlmap.get_scan_log(self.current_task_id)
                for log in logs:
                    self.showLog(log["message"], log["level"], log["time"])
            except Exception as e:
                QMessageBox.critical(self.main, "获取数据库表失败", "获取数据库表失败，请查看日志！原因：" + str(e))
                print(e)
        else:
            pass

    ###########################
    ### 命令执行界面组件调用接口 ###
    ###########################
    ### 命令设置 lineedit commandInput ###
    def setCommand(self):
        pass

    ### 开始命令 button btn_startCommand ###
    def startCommand(self):
        if self.current_task_id is None:
            QMessageBox.information(self.main, "提示", "当前没有注入对象！请先到自动注入或手动注入界面识别注入！")
        else:
            try:
                if self.ui.commandInput.text() == "":
                    show_border_effect_no(self.ui.commandInput)
                    return

                kwargs = self.current_kwargs | {"osCmd": self.ui.commandInput.text()}
                self.sqlmap.start_scan(self.current_task_id, **kwargs)
                # 等待并获取数据
                self.sqlmap.poll_scan_completion(self.current_task_id)
                datas, errors = self.sqlmap.get_scan_data(self.current_task_id)

                # 获取命令执行结果
                if self.ui.echoResults.isChecked():
                    for data in datas[::-1]:
                        if data["type"] == 24:
                            self.ui.commandResults.setPlainText(data["value"])
                            break

                for error in errors:
                    print(error)

                logs = self.sqlmap.get_scan_log(self.current_task_id)
                for log in logs:
                    self.showLog(log["message"], log["level"], log["time"])
            except Exception as e:
                QMessageBox.critical(self.main, "命令执行失败", "命令执行失败，请查看日志！原因：" + str(e))
                print(e)

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
    ### 添加payload记录 ###
    def showPayloadRecord(self, args, time=None):
        # 获取时间
        if time is None:
            time = datetime.datetime.now().strftime("%H:%M:%S")

        # 插入行
        row = self.ui.packetSendingRecord.rowCount()
        self.ui.packetSendingRecord.insertRow(row)

        # 写入数据
        self.ui.packetSendingRecord.setItem(row, 0, QTableWidgetItem(time))
        for i in range(len(args)):
            if args[i] is None:
                args[i] = "未知"
            elif type(args[i]) is list:
                args[i] = ",".join(args[i])
            self.ui.packetSendingRecord.setItem(row, i + 1, QTableWidgetItem(str(args[i])))

    ### 添加文本到日志 ###
    def showLog(self, txt, level="PLAIN", time=None):
        # 设置最大行数
        # len(self.ui.log.toPlainText().split("\n"))

        # 对应的颜色
        level_colors = {
            'INFO': '#00CC00',  # 绿色
            'WARNING': '#FF9900',  # 橙色
            'CRITICAL': '#FF0000',  # 红色
            'DEBUG': '#999999',  # 灰色
            'ERROR': '#CC00FF'  # 紫色
        }

        escaped_msg = html.escape(txt)
        # 获取对应等级的颜色
        color = level_colors.get(level, '#000000')  # 默认黑色
        # 获取时间
        if time is None:
            time = datetime.datetime.now().strftime("%H:%M:%S")
        # 构建HTML格式字符串
        html_str = f"""
               <div style="margin:2px 0;">
                   <span style="color:#666666;">[{time}]</span>
                   <span style="color:{color}; font-weight:500;">[{level}]</span>
                   <span style="color:{color};">{escaped_msg}</span>
               </div>
               """
        self.ui.log.appendHtml(html_str)
