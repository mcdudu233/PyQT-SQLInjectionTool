# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.8.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWebEngineWidgets import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore
from . resources_rc import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(940, 581)
        MainWindow.setMinimumSize(QSize(940, 560))
        self.styleSheet = QWidget(MainWindow)
        self.styleSheet.setObjectName(u"styleSheet")
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.styleSheet.setFont(font)
        self.styleSheet.setStyleSheet(u"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"\n"
"SET APP STYLESHEET - FULL STYLES HERE\n"
"DARK THEME - DRACULA COLOR BASED\n"
"\n"
"///////////////////////////////////////////////////////////////////////////////////////////////// */\n"
"\n"
"QWidget{\n"
"	color: rgb(221, 221, 221);\n"
"	font: 10pt \"Segoe UI\";\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Tooltip */\n"
"QToolTip {\n"
"	color: #ffffff;\n"
"	background-color: rgba(33, 37, 43, 180);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	background-image: none;\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 2px solid rgb(255, 121, 198);\n"
"	text-align: left;\n"
"	padding-left: 8px;\n"
"	margin: 0px;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Bg App */\n"
"#bgApp {	\n"
"	background"
                        "-color: rgb(40, 44, 52);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Left Menu */\n"
"#leftMenuBg {	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"#topLogo {\n"
"	background-color: rgb(33, 37, 43);\n"
"	background-image: url(:/images/images/images/PyDracula.png);\n"
"	background-position: centered;\n"
"	background-repeat: no-repeat;\n"
"}\n"
"#titleLeftApp { font: 63 12pt \"Segoe UI Semibold\"; }\n"
"#titleLeftDescription { font: 8pt \"Segoe UI\"; color: rgb(189, 147, 249); }\n"
"\n"
"/* MENUS */\n"
"#topMenu .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color: transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#topMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#topMenu .QPushButton:pressed {	\n"
"	background-color: rgb(18"
                        "9, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#bottomMenu .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#bottomMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#bottomMenu .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#leftMenuFrame{\n"
"	border-top: 3px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* Toggle Button */\n"
"#toggleButton {\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color: rgb(37, 41, 48);\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"	color: rgb(113, 126, 149);\n"
"}\n"
"#toggleButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#toggleButton:pressed {\n"
"	background-color: rgb("
                        "189, 147, 249);\n"
"}\n"
"\n"
"/* Title Menu */\n"
"#titleRightInfo { padding-left: 10px; }\n"
"\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Extra Tab */\n"
"#extraLeftBox {	\n"
"	background-color: rgb(44, 49, 58);\n"
"}\n"
"#extraTopBg{	\n"
"	background-color: rgb(189, 147, 249)\n"
"}\n"
"\n"
"/* Icon */\n"
"#extraIcon {\n"
"	background-position: center;\n"
"	background-repeat: no-repeat;\n"
"	background-image: url(:/icons/images/icons/icon_settings.png);\n"
"}\n"
"\n"
"/* Label */\n"
"#extraLabel { color: rgb(255, 255, 255); }\n"
"\n"
"/* Btn Close */\n"
"#extraCloseColumnBtn { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#extraCloseColumnBtn:hover { background-color: rgb(196, 161, 249); border-style: solid; border-radius: 4px; }\n"
"#extraCloseColumnBtn:pressed { background-color: rgb(180, 141, 238); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Extra Content */\n"
"#extraContent{\n"
"	border"
                        "-top: 3px solid rgb(40, 44, 52);\n"
"}\n"
"\n"
"/* Extra Top Menus */\n"
"#extraTopMenu .QPushButton {\n"
"background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#extraTopMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#extraTopMenu .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Content App */\n"
"#contentTopBg{	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"#contentBottom{\n"
"	border-top: 3px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* Top Buttons */\n"
"#rightButtons .QPushButton { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#rightButtons .QPushButton:hover { background-color: rgb(44, 49, 57); border-sty"
                        "le: solid; border-radius: 4px; }\n"
"#rightButtons .QPushButton:pressed { background-color: rgb(23, 26, 30); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Theme Settings */\n"
"#extraRightBox { background-color: rgb(44, 49, 58); }\n"
"#themeSettingsTopDetail { background-color: rgb(189, 147, 249); }\n"
"\n"
"/* Bottom Bar */\n"
"#bottomBar { background-color: rgb(44, 49, 58); }\n"
"#bottomBar QLabel { font-size: 11px; color: rgb(113, 126, 149); padding-left: 10px; padding-right: 10px; padding-bottom: 2px; }\n"
"\n"
"/* CONTENT SETTINGS */\n"
"/* MENUS */\n"
"#contentSettings .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#contentSettings .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#contentSettings .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb"
                        "(255, 255, 255);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"QTableWidget */\n"
"QTableWidget {	\n"
"	background-color: transparent;\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(44, 49, 58);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(189, 147, 249);\n"
"}\n"
"QHeaderView::section{\n"
"	background-color: rgb(33, 37, 43);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::horizontalHeader {	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(33, 37, 43);\n"
"	background-co"
                        "lor: rgb(33, 37, 43);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"LineEdit */\n"
"QLineEdit {\n"
"	background-color: rgb(33, 37, 43);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"PlainTextEdit */\n"
"QPlainTextEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	padding: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-c"
                        "olor: rgb(255, 121, 198);\n"
"}\n"
"QPlainTextEdit  QScrollBar:vertical {\n"
"    width: 8px;\n"
" }\n"
"QPlainTextEdit  QScrollBar:horizontal {\n"
"    height: 8px;\n"
" }\n"
"QPlainTextEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QPlainTextEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ScrollBars */\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 8px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(189, 147, 249);\n"
"    min-width: 25px;\n"
"	border-radius: 4px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-right-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
""
                        "QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-bottom-left-radius: 4px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 8px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
" QScrollBar::handle:vertical {	\n"
"	background: rgb(189, 147, 249);\n"
"    min-height: 25px;\n"
"	border-radius: 4px\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-bottom-left-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"     subcontrol-position: bottom;\n"
"     su"
                        "bcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CheckBox */\n"
"QCheckBox::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background: 3px solid rgb(52, 59, 72);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"	back"
                        "ground-image: url(:/icons/images/icons/cil-check-alt.png);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"RadioButton */\n"
"QRadioButton::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QRadioButton::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    background: 3px solid rgb(94, 106, 130);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ComboBox */\n"
"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subco"
                        "ntrol-position: top right;\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/icons/images/icons/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(255, 121, 198);	\n"
"	background-color: rgb(33, 37, 43);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Sliders */\n"
"QSlider::groove:horizontal {\n"
"    border-radius: 5px;\n"
"    height: 10px;\n"
"	margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:horizontal:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(189, 147, 249);\n"
"    border: none;\n"
"    h"
                        "eight: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: rgb(255, 121, 198);\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    border-radius: 5px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:vertical:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:vertical {\n"
"    background-color: rgb(189, 147, 249);\n"
"	border: none;\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:vertical:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:vertical:pressed {\n"
"    background-color: rgb(255, 121, 198);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CommandLinkButton */\n"
"QCommandLi"
                        "nkButton {	\n"
"	color: rgb(255, 121, 198);\n"
"	border-radius: 5px;\n"
"	padding: 5px;\n"
"	color: rgb(255, 170, 255);\n"
"}\n"
"QCommandLinkButton:hover {	\n"
"	color: rgb(255, 170, 255);\n"
"	background-color: rgb(44, 49, 60);\n"
"}\n"
"QCommandLinkButton:pressed {	\n"
"	color: rgb(189, 147, 249);\n"
"	background-color: rgb(52, 58, 71);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Button */\n"
"#pagesContainer QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"#pagesContainer QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"#pagesContainer QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}\n"
"\n"
"")
        self.appMargins = QVBoxLayout(self.styleSheet)
        self.appMargins.setSpacing(0)
        self.appMargins.setObjectName(u"appMargins")
        self.appMargins.setContentsMargins(10, 10, 10, 10)
        self.bgApp = QFrame(self.styleSheet)
        self.bgApp.setObjectName(u"bgApp")
        self.bgApp.setStyleSheet(u"")
        self.bgApp.setFrameShape(QFrame.Shape.NoFrame)
        self.bgApp.setFrameShadow(QFrame.Shadow.Raised)
        self.appLayout = QHBoxLayout(self.bgApp)
        self.appLayout.setSpacing(0)
        self.appLayout.setObjectName(u"appLayout")
        self.appLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuBg = QFrame(self.bgApp)
        self.leftMenuBg.setObjectName(u"leftMenuBg")
        self.leftMenuBg.setMinimumSize(QSize(60, 0))
        self.leftMenuBg.setMaximumSize(QSize(60, 16777215))
        self.leftMenuBg.setFrameShape(QFrame.Shape.NoFrame)
        self.leftMenuBg.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.leftMenuBg)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.verticalLayout_3.setContentsMargins(0, 0, -1, 0)
        self.topLogoInfo = QFrame(self.leftMenuBg)
        self.topLogoInfo.setObjectName(u"topLogoInfo")
        self.topLogoInfo.setMinimumSize(QSize(0, 50))
        self.topLogoInfo.setMaximumSize(QSize(16777215, 50))
        self.topLogoInfo.setFrameShape(QFrame.Shape.NoFrame)
        self.topLogoInfo.setFrameShadow(QFrame.Shadow.Raised)
        self.topLogo = QFrame(self.topLogoInfo)
        self.topLogo.setObjectName(u"topLogo")
        self.topLogo.setGeometry(QRect(10, 5, 42, 42))
        self.topLogo.setMinimumSize(QSize(42, 42))
        self.topLogo.setMaximumSize(QSize(42, 42))
        self.topLogo.setFrameShape(QFrame.Shape.NoFrame)
        self.topLogo.setFrameShadow(QFrame.Shadow.Raised)
        self.titleLeftApp = QLabel(self.topLogoInfo)
        self.titleLeftApp.setObjectName(u"titleLeftApp")
        self.titleLeftApp.setGeometry(QRect(70, 8, 160, 20))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI Semibold"])
        font1.setPointSize(12)
        
        font1.setItalic(False)
        self.titleLeftApp.setFont(font1)
        self.titleLeftApp.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.titleLeftDescription = QLabel(self.topLogoInfo)
        self.titleLeftDescription.setObjectName(u"titleLeftDescription")
        self.titleLeftDescription.setGeometry(QRect(70, 27, 160, 16))
        self.titleLeftDescription.setMaximumSize(QSize(16777215, 16))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(8)
        font2.setBold(False)
        font2.setItalic(False)
        self.titleLeftDescription.setFont(font2)
        self.titleLeftDescription.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.verticalLayout_3.addWidget(self.topLogoInfo)

        self.leftMenuFrame = QFrame(self.leftMenuBg)
        self.leftMenuFrame.setObjectName(u"leftMenuFrame")
        self.leftMenuFrame.setFrameShape(QFrame.Shape.NoFrame)
        self.leftMenuFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalMenuLayout = QVBoxLayout(self.leftMenuFrame)
        self.verticalMenuLayout.setSpacing(0)
        self.verticalMenuLayout.setObjectName(u"verticalMenuLayout")
        self.verticalMenuLayout.setContentsMargins(0, 0, 0, 0)
        self.toggleBox = QFrame(self.leftMenuFrame)
        self.toggleBox.setObjectName(u"toggleBox")
        self.toggleBox.setMaximumSize(QSize(16777215, 45))
        self.toggleBox.setFrameShape(QFrame.Shape.NoFrame)
        self.toggleBox.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.toggleBox)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.toggleButton = QPushButton(self.toggleBox)
        self.toggleButton.setObjectName(u"toggleButton")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toggleButton.sizePolicy().hasHeightForWidth())
        self.toggleButton.setSizePolicy(sizePolicy)
        self.toggleButton.setMinimumSize(QSize(0, 45))
        self.toggleButton.setFont(font)
        self.toggleButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.toggleButton.setTabletTracking(False)
        self.toggleButton.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.toggleButton.setAutoFillBackground(False)
        self.toggleButton.setStyleSheet(u"background-image: url(:/icons/images/icons/icon_menu.png);")
        self.toggleButton.setCheckable(False)
        self.toggleButton.setAutoRepeat(False)
        self.toggleButton.setAutoExclusive(False)

        self.verticalLayout_4.addWidget(self.toggleButton)


        self.verticalMenuLayout.addWidget(self.toggleBox)

        self.topMenu = QFrame(self.leftMenuFrame)
        self.topMenu.setObjectName(u"topMenu")
        self.topMenu.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.topMenu.sizePolicy().hasHeightForWidth())
        self.topMenu.setSizePolicy(sizePolicy1)
        self.topMenu.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.topMenu.setFrameShape(QFrame.Shape.NoFrame)
        self.topMenu.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.topMenu)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.btn_home = QPushButton(self.topMenu)
        self.btn_home.setObjectName(u"btn_home")
        sizePolicy.setHeightForWidth(self.btn_home.sizePolicy().hasHeightForWidth())
        self.btn_home.setSizePolicy(sizePolicy)
        self.btn_home.setMinimumSize(QSize(0, 45))
        self.btn_home.setFont(font)
        self.btn_home.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_home.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_home.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-home.png)")

        self.verticalLayout_8.addWidget(self.btn_home)

        self.btn_manualInjection = QPushButton(self.topMenu)
        self.btn_manualInjection.setObjectName(u"btn_manualInjection")
        sizePolicy.setHeightForWidth(self.btn_manualInjection.sizePolicy().hasHeightForWidth())
        self.btn_manualInjection.setSizePolicy(sizePolicy)
        self.btn_manualInjection.setMinimumSize(QSize(0, 45))
        self.btn_manualInjection.setFont(font)
        self.btn_manualInjection.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_manualInjection.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_manualInjection.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-file.png);")

        self.verticalLayout_8.addWidget(self.btn_manualInjection)

        self.btn_dataCenter = QPushButton(self.topMenu)
        self.btn_dataCenter.setObjectName(u"btn_dataCenter")
        sizePolicy.setHeightForWidth(self.btn_dataCenter.sizePolicy().hasHeightForWidth())
        self.btn_dataCenter.setSizePolicy(sizePolicy)
        self.btn_dataCenter.setMinimumSize(QSize(0, 45))
        self.btn_dataCenter.setFont(font)
        self.btn_dataCenter.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_dataCenter.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_dataCenter.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-3d.png)")

        self.verticalLayout_8.addWidget(self.btn_dataCenter)

        self.btn_command = QPushButton(self.topMenu)
        self.btn_command.setObjectName(u"btn_command")
        sizePolicy.setHeightForWidth(self.btn_command.sizePolicy().hasHeightForWidth())
        self.btn_command.setSizePolicy(sizePolicy)
        self.btn_command.setMinimumSize(QSize(0, 45))
        self.btn_command.setFont(font)
        self.btn_command.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_command.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_command.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-map.png)")

        self.verticalLayout_8.addWidget(self.btn_command)

        self.btn_logCenter = QPushButton(self.topMenu)
        self.btn_logCenter.setObjectName(u"btn_logCenter")
        sizePolicy.setHeightForWidth(self.btn_logCenter.sizePolicy().hasHeightForWidth())
        self.btn_logCenter.setSizePolicy(sizePolicy)
        self.btn_logCenter.setMinimumSize(QSize(0, 45))
        self.btn_logCenter.setFont(font)
        self.btn_logCenter.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_logCenter.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_logCenter.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-cloudy.png)")

        self.verticalLayout_8.addWidget(self.btn_logCenter)

        self.btn_fileOperation = QPushButton(self.topMenu)
        self.btn_fileOperation.setObjectName(u"btn_fileOperation")
        sizePolicy.setHeightForWidth(self.btn_fileOperation.sizePolicy().hasHeightForWidth())
        self.btn_fileOperation.setSizePolicy(sizePolicy)
        self.btn_fileOperation.setMinimumSize(QSize(0, 45))
        self.btn_fileOperation.setFont(font)
        self.btn_fileOperation.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_fileOperation.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_fileOperation.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-cast.png)")

        self.verticalLayout_8.addWidget(self.btn_fileOperation)

        self.btn_save = QPushButton(self.topMenu)
        self.btn_save.setObjectName(u"btn_save")
        sizePolicy.setHeightForWidth(self.btn_save.sizePolicy().hasHeightForWidth())
        self.btn_save.setSizePolicy(sizePolicy)
        self.btn_save.setMinimumSize(QSize(0, 45))
        self.btn_save.setFont(font)
        self.btn_save.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_save.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_save.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-save.png)")

        self.verticalLayout_8.addWidget(self.btn_save)

        self.btn_exit = QPushButton(self.topMenu)
        self.btn_exit.setObjectName(u"btn_exit")
        sizePolicy.setHeightForWidth(self.btn_exit.sizePolicy().hasHeightForWidth())
        self.btn_exit.setSizePolicy(sizePolicy)
        self.btn_exit.setMinimumSize(QSize(0, 45))
        self.btn_exit.setFont(font)
        self.btn_exit.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_exit.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_exit.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-x.png);")

        self.verticalLayout_8.addWidget(self.btn_exit)


        self.verticalMenuLayout.addWidget(self.topMenu, 0, Qt.AlignmentFlag.AlignTop)

        self.bottomMenu = QFrame(self.leftMenuFrame)
        self.bottomMenu.setObjectName(u"bottomMenu")
        self.bottomMenu.setFrameShape(QFrame.Shape.NoFrame)
        self.bottomMenu.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.bottomMenu)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.toggleLeftBox = QPushButton(self.bottomMenu)
        self.toggleLeftBox.setObjectName(u"toggleLeftBox")
        sizePolicy.setHeightForWidth(self.toggleLeftBox.sizePolicy().hasHeightForWidth())
        self.toggleLeftBox.setSizePolicy(sizePolicy)
        self.toggleLeftBox.setMinimumSize(QSize(0, 45))
        self.toggleLeftBox.setFont(font)
        self.toggleLeftBox.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.toggleLeftBox.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.toggleLeftBox.setStyleSheet(u"background-image: url(:/icons/images/icons/icon_settings.png);")

        self.verticalLayout_9.addWidget(self.toggleLeftBox)


        self.verticalMenuLayout.addWidget(self.bottomMenu, 0, Qt.AlignmentFlag.AlignBottom)

        self.toggleBox.raise_()
        self.bottomMenu.raise_()
        self.topMenu.raise_()

        self.verticalLayout_3.addWidget(self.leftMenuFrame)


        self.appLayout.addWidget(self.leftMenuBg)

        self.extraLeftBox = QFrame(self.bgApp)
        self.extraLeftBox.setObjectName(u"extraLeftBox")
        self.extraLeftBox.setMinimumSize(QSize(0, 0))
        self.extraLeftBox.setMaximumSize(QSize(0, 16777215))
        self.extraLeftBox.setFrameShape(QFrame.Shape.NoFrame)
        self.extraLeftBox.setFrameShadow(QFrame.Shadow.Raised)
        self.extraColumLayout = QVBoxLayout(self.extraLeftBox)
        self.extraColumLayout.setSpacing(0)
        self.extraColumLayout.setObjectName(u"extraColumLayout")
        self.extraColumLayout.setContentsMargins(0, 0, 0, 0)
        self.extraTopBg = QFrame(self.extraLeftBox)
        self.extraTopBg.setObjectName(u"extraTopBg")
        self.extraTopBg.setMinimumSize(QSize(0, 50))
        self.extraTopBg.setMaximumSize(QSize(16777215, 50))
        self.extraTopBg.setFrameShape(QFrame.Shape.NoFrame)
        self.extraTopBg.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.extraTopBg)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.extraTopLayout = QGridLayout()
        self.extraTopLayout.setObjectName(u"extraTopLayout")
        self.extraTopLayout.setHorizontalSpacing(10)
        self.extraTopLayout.setVerticalSpacing(0)
        self.extraTopLayout.setContentsMargins(10, -1, 10, -1)
        self.extraIcon = QFrame(self.extraTopBg)
        self.extraIcon.setObjectName(u"extraIcon")
        self.extraIcon.setMinimumSize(QSize(20, 0))
        self.extraIcon.setMaximumSize(QSize(20, 20))
        self.extraIcon.setFrameShape(QFrame.Shape.NoFrame)
        self.extraIcon.setFrameShadow(QFrame.Shadow.Raised)

        self.extraTopLayout.addWidget(self.extraIcon, 0, 0, 1, 1)

        self.extraLabel = QLabel(self.extraTopBg)
        self.extraLabel.setObjectName(u"extraLabel")
        self.extraLabel.setMinimumSize(QSize(150, 0))

        self.extraTopLayout.addWidget(self.extraLabel, 0, 1, 1, 1)

        self.extraCloseColumnBtn = QPushButton(self.extraTopBg)
        self.extraCloseColumnBtn.setObjectName(u"extraCloseColumnBtn")
        self.extraCloseColumnBtn.setMinimumSize(QSize(28, 28))
        self.extraCloseColumnBtn.setMaximumSize(QSize(28, 28))
        self.extraCloseColumnBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/icons/images/icons/icon_close.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.extraCloseColumnBtn.setIcon(icon)
        self.extraCloseColumnBtn.setIconSize(QSize(20, 20))

        self.extraTopLayout.addWidget(self.extraCloseColumnBtn, 0, 2, 1, 1)


        self.verticalLayout_5.addLayout(self.extraTopLayout)


        self.extraColumLayout.addWidget(self.extraTopBg)

        self.extraContent = QFrame(self.extraLeftBox)
        self.extraContent.setObjectName(u"extraContent")
        self.extraContent.setFrameShape(QFrame.Shape.NoFrame)
        self.extraContent.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.extraContent)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.extraTopMenu = QFrame(self.extraContent)
        self.extraTopMenu.setObjectName(u"extraTopMenu")
        self.extraTopMenu.setFrameShape(QFrame.Shape.NoFrame)
        self.extraTopMenu.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.extraTopMenu)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.btn_share = QPushButton(self.extraTopMenu)
        self.btn_share.setObjectName(u"btn_share")
        sizePolicy.setHeightForWidth(self.btn_share.sizePolicy().hasHeightForWidth())
        self.btn_share.setSizePolicy(sizePolicy)
        self.btn_share.setMinimumSize(QSize(0, 45))
        self.btn_share.setFont(font)
        self.btn_share.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_share.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_share.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-share-boxed.png);")

        self.verticalLayout_11.addWidget(self.btn_share)

        self.btn_adjustments = QPushButton(self.extraTopMenu)
        self.btn_adjustments.setObjectName(u"btn_adjustments")
        sizePolicy.setHeightForWidth(self.btn_adjustments.sizePolicy().hasHeightForWidth())
        self.btn_adjustments.setSizePolicy(sizePolicy)
        self.btn_adjustments.setMinimumSize(QSize(0, 45))
        self.btn_adjustments.setFont(font)
        self.btn_adjustments.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_adjustments.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_adjustments.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-equalizer.png);")

        self.verticalLayout_11.addWidget(self.btn_adjustments)

        self.btn_more = QPushButton(self.extraTopMenu)
        self.btn_more.setObjectName(u"btn_more")
        sizePolicy.setHeightForWidth(self.btn_more.sizePolicy().hasHeightForWidth())
        self.btn_more.setSizePolicy(sizePolicy)
        self.btn_more.setMinimumSize(QSize(0, 45))
        self.btn_more.setFont(font)
        self.btn_more.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_more.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_more.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-layers.png);")

        self.verticalLayout_11.addWidget(self.btn_more)


        self.verticalLayout_12.addWidget(self.extraTopMenu, 0, Qt.AlignmentFlag.AlignTop)

        self.extraCenter = QFrame(self.extraContent)
        self.extraCenter.setObjectName(u"extraCenter")
        self.extraCenter.setFrameShape(QFrame.Shape.NoFrame)
        self.extraCenter.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.extraCenter)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.textEdit = QTextEdit(self.extraCenter)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setMinimumSize(QSize(222, 0))
        self.textEdit.setStyleSheet(u"background: transparent;")
        self.textEdit.setFrameShape(QFrame.Shape.NoFrame)
        self.textEdit.setReadOnly(True)

        self.verticalLayout_10.addWidget(self.textEdit)


        self.verticalLayout_12.addWidget(self.extraCenter)

        self.extraBottom = QFrame(self.extraContent)
        self.extraBottom.setObjectName(u"extraBottom")
        self.extraBottom.setFrameShape(QFrame.Shape.NoFrame)
        self.extraBottom.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_12.addWidget(self.extraBottom)


        self.extraColumLayout.addWidget(self.extraContent)


        self.appLayout.addWidget(self.extraLeftBox)

        self.contentBox = QFrame(self.bgApp)
        self.contentBox.setObjectName(u"contentBox")
        self.contentBox.setFrameShape(QFrame.Shape.NoFrame)
        self.contentBox.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.contentBox)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.contentTopBg = QFrame(self.contentBox)
        self.contentTopBg.setObjectName(u"contentTopBg")
        self.contentTopBg.setMinimumSize(QSize(0, 50))
        self.contentTopBg.setMaximumSize(QSize(16777215, 50))
        self.contentTopBg.setFrameShape(QFrame.Shape.NoFrame)
        self.contentTopBg.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.contentTopBg)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 10, 0)
        self.leftBox = QFrame(self.contentTopBg)
        self.leftBox.setObjectName(u"leftBox")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.leftBox.sizePolicy().hasHeightForWidth())
        self.leftBox.setSizePolicy(sizePolicy2)
        self.leftBox.setFrameShape(QFrame.Shape.NoFrame)
        self.leftBox.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.leftBox)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.titleRightInfo = QLabel(self.leftBox)
        self.titleRightInfo.setObjectName(u"titleRightInfo")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.titleRightInfo.sizePolicy().hasHeightForWidth())
        self.titleRightInfo.setSizePolicy(sizePolicy3)
        self.titleRightInfo.setMaximumSize(QSize(16777215, 45))
        self.titleRightInfo.setFont(font)
        self.titleRightInfo.setFrameShape(QFrame.Shape.NoFrame)
        self.titleRightInfo.setLineWidth(6)
        self.titleRightInfo.setMidLineWidth(5)
        self.titleRightInfo.setTextFormat(Qt.TextFormat.PlainText)
        self.titleRightInfo.setScaledContents(True)
        self.titleRightInfo.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.titleRightInfo.setMargin(2)
        self.titleRightInfo.setIndent(4)

        self.horizontalLayout_3.addWidget(self.titleRightInfo)


        self.horizontalLayout.addWidget(self.leftBox)

        self.rightButtons = QFrame(self.contentTopBg)
        self.rightButtons.setObjectName(u"rightButtons")
        self.rightButtons.setMinimumSize(QSize(0, 28))
        self.rightButtons.setFrameShape(QFrame.Shape.NoFrame)
        self.rightButtons.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.rightButtons)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.settingsTopBtn = QPushButton(self.rightButtons)
        self.settingsTopBtn.setObjectName(u"settingsTopBtn")
        self.settingsTopBtn.setMinimumSize(QSize(28, 28))
        self.settingsTopBtn.setMaximumSize(QSize(28, 28))
        self.settingsTopBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/icons/images/icons/icon_settings.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.settingsTopBtn.setIcon(icon1)
        self.settingsTopBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.settingsTopBtn)

        self.minimizeAppBtn = QPushButton(self.rightButtons)
        self.minimizeAppBtn.setObjectName(u"minimizeAppBtn")
        self.minimizeAppBtn.setMinimumSize(QSize(28, 28))
        self.minimizeAppBtn.setMaximumSize(QSize(28, 28))
        self.minimizeAppBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icons/images/icons/icon_minimize.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.minimizeAppBtn.setIcon(icon2)
        self.minimizeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.minimizeAppBtn)

        self.maximizeRestoreAppBtn = QPushButton(self.rightButtons)
        self.maximizeRestoreAppBtn.setObjectName(u"maximizeRestoreAppBtn")
        self.maximizeRestoreAppBtn.setMinimumSize(QSize(28, 28))
        self.maximizeRestoreAppBtn.setMaximumSize(QSize(28, 28))
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setPointSize(10)
        font3.setBold(False)
        font3.setItalic(False)
        font3.setStyleStrategy(QFont.PreferDefault)
        self.maximizeRestoreAppBtn.setFont(font3)
        self.maximizeRestoreAppBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/icons/images/icons/icon_maximize.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.maximizeRestoreAppBtn.setIcon(icon3)
        self.maximizeRestoreAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.maximizeRestoreAppBtn)

        self.closeAppBtn = QPushButton(self.rightButtons)
        self.closeAppBtn.setObjectName(u"closeAppBtn")
        self.closeAppBtn.setMinimumSize(QSize(28, 28))
        self.closeAppBtn.setMaximumSize(QSize(28, 28))
        self.closeAppBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.closeAppBtn.setIcon(icon)
        self.closeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.closeAppBtn)


        self.horizontalLayout.addWidget(self.rightButtons, 0, Qt.AlignmentFlag.AlignRight)


        self.verticalLayout_2.addWidget(self.contentTopBg)

        self.contentBottom = QFrame(self.contentBox)
        self.contentBottom.setObjectName(u"contentBottom")
        self.contentBottom.setFrameShape(QFrame.Shape.NoFrame)
        self.contentBottom.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.contentBottom)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.content = QFrame(self.contentBottom)
        self.content.setObjectName(u"content")
        self.content.setFrameShape(QFrame.Shape.NoFrame)
        self.content.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.content)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.pagesContainer = QFrame(self.content)
        self.pagesContainer.setObjectName(u"pagesContainer")
        self.pagesContainer.setStyleSheet(u"")
        self.pagesContainer.setFrameShape(QFrame.Shape.NoFrame)
        self.pagesContainer.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.pagesContainer)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(10, 10, 10, 10)
        self.stackedWidget = QStackedWidget(self.pagesContainer)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background: transparent;")
        self.home = QWidget()
        self.home.setObjectName(u"home")
        self.home.setStyleSheet(u"background-image: url(:/images/images/images/PyDracula_vertical.png);\n"
"background-position: center;\n"
"background-repeat: no-repeat;")
        self.stackedWidget.addWidget(self.home)
        self.manualInjection = QWidget()
        self.manualInjection.setObjectName(u"manualInjection")
        self.label_2 = QLabel(self.manualInjection)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 15, 81, 31))
        self.widget = QWidget(self.manualInjection)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(120, 70, 551, 331))
        self.gridLayout_5 = QGridLayout(self.widget)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.btn_exportConfiguration = QPushButton(self.widget)
        self.btn_exportConfiguration.setObjectName(u"btn_exportConfiguration")
        self.btn_exportConfiguration.setMinimumSize(QSize(150, 30))
        self.btn_exportConfiguration.setFont(font)
        self.btn_exportConfiguration.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_exportConfiguration.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        icon4 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.GoDown))
        self.btn_exportConfiguration.setIcon(icon4)

        self.gridLayout_5.addWidget(self.btn_exportConfiguration, 3, 4, 1, 2)

        self.injectionType = QComboBox(self.widget)
        self.injectionType.addItem("")
        self.injectionType.addItem("")
        self.injectionType.addItem("")
        self.injectionType.setObjectName(u"injectionType")
        self.injectionType.setFont(font)
        self.injectionType.setAutoFillBackground(False)
        self.injectionType.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.injectionType.setIconSize(QSize(16, 16))
        self.injectionType.setFrame(True)

        self.gridLayout_5.addWidget(self.injectionType, 0, 5, 1, 1)

        self.retry = QLineEdit(self.widget)
        self.retry.setObjectName(u"retry")
        self.retry.setMinimumSize(QSize(0, 30))
        self.retry.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.gridLayout_5.addWidget(self.retry, 2, 0, 1, 1)

        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_5.addWidget(self.label_3, 0, 3, 1, 2)

        self.address_2 = QLineEdit(self.widget)
        self.address_2.setObjectName(u"address_2")
        self.address_2.setMinimumSize(QSize(0, 30))
        self.address_2.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.gridLayout_5.addWidget(self.address_2, 1, 0, 1, 1)

        self.label_10 = QLabel(self.widget)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_5.addWidget(self.label_10, 2, 3, 1, 1)

        self.checkBox_3 = QCheckBox(self.widget)
        self.checkBox_3.setObjectName(u"checkBox_3")
        self.checkBox_3.setAutoFillBackground(False)
        self.checkBox_3.setStyleSheet(u"")

        self.gridLayout_5.addWidget(self.checkBox_3, 1, 5, 1, 1)

        self.coding = QComboBox(self.widget)
        self.coding.addItem("")
        self.coding.setObjectName(u"coding")
        self.coding.setFont(font)
        self.coding.setAutoFillBackground(False)
        self.coding.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.coding.setIconSize(QSize(16, 16))
        self.coding.setFrame(True)

        self.gridLayout_5.addWidget(self.coding, 2, 2, 1, 1)

        self.label_9 = QLabel(self.widget)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_5.addWidget(self.label_9, 2, 1, 1, 1)

        self.btn_startInjection = QPushButton(self.widget)
        self.btn_startInjection.setObjectName(u"btn_startInjection")
        self.btn_startInjection.setMinimumSize(QSize(150, 30))
        self.btn_startInjection.setFont(font)
        self.btn_startInjection.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_startInjection.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        icon5 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.EditSelectAll))
        self.btn_startInjection.setIcon(icon5)

        self.gridLayout_5.addWidget(self.btn_startInjection, 3, 0, 1, 1)

        self.address = QLineEdit(self.widget)
        self.address.setObjectName(u"address")
        self.address.setMinimumSize(QSize(0, 30))
        self.address.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.gridLayout_5.addWidget(self.address, 0, 0, 1, 1)

        self.overtime = QLineEdit(self.widget)
        self.overtime.setObjectName(u"overtime")
        self.overtime.setMinimumSize(QSize(0, 30))
        self.overtime.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.gridLayout_5.addWidget(self.overtime, 0, 1, 1, 2)

        self.databaseType = QComboBox(self.widget)
        self.databaseType.addItem("")
        self.databaseType.addItem("")
        self.databaseType.setObjectName(u"databaseType")
        self.databaseType.setFont(font)
        self.databaseType.setAutoFillBackground(False)
        self.databaseType.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.databaseType.setIconSize(QSize(16, 16))
        self.databaseType.setFrame(True)

        self.gridLayout_5.addWidget(self.databaseType, 2, 5, 1, 1)

        self.portID = QLineEdit(self.widget)
        self.portID.setObjectName(u"portID")
        self.portID.setMinimumSize(QSize(0, 30))
        self.portID.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.gridLayout_5.addWidget(self.portID, 1, 1, 1, 2)

        self.stackedWidget.addWidget(self.manualInjection)
        self.dataCenter = QWidget()
        self.dataCenter.setObjectName(u"dataCenter")
        self.label_7 = QLabel(self.dataCenter)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(20, 10, 71, 31))
        self.label_12 = QLabel(self.dataCenter)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(10, 40, 71, 31))
        self.getData = QPlainTextEdit(self.dataCenter)
        self.getData.setObjectName(u"getData")
        self.getData.setGeometry(QRect(310, 70, 481, 241))
        self.getData.setMinimumSize(QSize(200, 200))
        self.getData.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.label_13 = QLabel(self.dataCenter)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(300, 30, 71, 31))
        self.widget_7 = QWidget(self.dataCenter)
        self.widget_7.setObjectName(u"widget_7")
        self.widget_7.setGeometry(QRect(30, 330, 741, 88))
        self.gridLayout_7 = QGridLayout(self.widget_7)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.number = QLineEdit(self.widget_7)
        self.number.setObjectName(u"number")
        self.number.setMinimumSize(QSize(0, 30))
        self.number.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.gridLayout_7.addWidget(self.number, 0, 0, 1, 1)

        self.address_4 = QLineEdit(self.widget_7)
        self.address_4.setObjectName(u"address_4")
        self.address_4.setMinimumSize(QSize(0, 30))
        self.address_4.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.gridLayout_7.addWidget(self.address_4, 0, 1, 1, 2)

        self.label_14 = QLabel(self.widget_7)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout_7.addWidget(self.label_14, 0, 3, 1, 1)

        self.btn_getData = QPushButton(self.widget_7)
        self.btn_getData.setObjectName(u"btn_getData")
        self.btn_getData.setMinimumSize(QSize(150, 30))
        self.btn_getData.setFont(font)
        self.btn_getData.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_getData.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.btn_getData.setIcon(icon5)

        self.gridLayout_7.addWidget(self.btn_getData, 1, 0, 1, 2)

        self.btn_exportData = QPushButton(self.widget_7)
        self.btn_exportData.setObjectName(u"btn_exportData")
        self.btn_exportData.setMinimumSize(QSize(150, 30))
        self.btn_exportData.setFont(font)
        self.btn_exportData.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_exportData.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.btn_exportData.setIcon(icon5)

        self.gridLayout_7.addWidget(self.btn_exportData, 1, 2, 1, 3)

        self.btn_stopGettingData = QPushButton(self.widget_7)
        self.btn_stopGettingData.setObjectName(u"btn_stopGettingData")
        self.btn_stopGettingData.setMinimumSize(QSize(150, 30))
        self.btn_stopGettingData.setFont(font)
        self.btn_stopGettingData.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_stopGettingData.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.btn_stopGettingData.setIcon(icon5)

        self.gridLayout_7.addWidget(self.btn_stopGettingData, 1, 5, 1, 1)

        self.codingType = QComboBox(self.widget_7)
        self.codingType.addItem("")
        self.codingType.setObjectName(u"codingType")
        self.codingType.setFont(font)
        self.codingType.setAutoFillBackground(False)
        self.codingType.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.codingType.setIconSize(QSize(16, 16))
        self.codingType.setFrame(True)

        self.gridLayout_7.addWidget(self.codingType, 0, 5, 1, 1)

        self.databaseInformation = QPlainTextEdit(self.dataCenter)
        self.databaseInformation.setObjectName(u"databaseInformation")
        self.databaseInformation.setGeometry(QRect(10, 70, 241, 241))
        self.databaseInformation.setMinimumSize(QSize(200, 200))
        self.databaseInformation.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.stackedWidget.addWidget(self.dataCenter)
        self.autoInjection = QWidget()
        self.autoInjection.setObjectName(u"autoInjection")
        self.browse = QPushButton(self.autoInjection)
        self.browse.setObjectName(u"browse")
        self.browse.setGeometry(QRect(670, 50, 150, 30))
        self.browse.setMinimumSize(QSize(150, 30))
        self.browse.setFont(font)
        self.browse.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.browse.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        icon6 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.InputMouse))
        self.browse.setIcon(icon6)
        self.lineEdit_3 = QLineEdit(self.autoInjection)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(20, 50, 640, 30))
        self.lineEdit_3.setMinimumSize(QSize(0, 30))
        self.lineEdit_3.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.webPage = QWebEngineView(self.autoInjection)
        self.webPage.setObjectName(u"webPage")
        self.webPage.setGeometry(QRect(20, 140, 801, 301))
        self.webPage.setUrl(QUrl(u"about:blank"))
        self.frame_title_wid_4 = QFrame(self.autoInjection)
        self.frame_title_wid_4.setObjectName(u"frame_title_wid_4")
        self.frame_title_wid_4.setGeometry(QRect(10, 90, 816, 35))
        self.frame_title_wid_4.setMaximumSize(QSize(16777215, 35))
        self.frame_title_wid_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_title_wid_4.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_26 = QVBoxLayout(self.frame_title_wid_4)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.labelBoxBlenderInstalation_3 = QLabel(self.frame_title_wid_4)
        self.labelBoxBlenderInstalation_3.setObjectName(u"labelBoxBlenderInstalation_3")
        self.labelBoxBlenderInstalation_3.setFont(font)
        self.labelBoxBlenderInstalation_3.setStyleSheet(u"")

        self.verticalLayout_26.addWidget(self.labelBoxBlenderInstalation_3)

        self.label = QLabel(self.autoInjection)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 10, 61, 21))
        self.stackedWidget.addWidget(self.autoInjection)
        self.fileOperation = QWidget()
        self.fileOperation.setObjectName(u"fileOperation")
        self.label_4 = QLabel(self.fileOperation)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(30, 20, 54, 16))
        self.groupBox_2 = QGroupBox(self.fileOperation)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(10, 50, 731, 111))
        self.gridLayout_6 = QGridLayout(self.groupBox_2)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.path = QLineEdit(self.groupBox_2)
        self.path.setObjectName(u"path")
        self.path.setMinimumSize(QSize(0, 30))
        self.path.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.gridLayout_6.addWidget(self.path, 0, 0, 1, 1)

        self.label_11 = QLabel(self.groupBox_2)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_6.addWidget(self.label_11, 0, 1, 1, 1)

        self.fileOperationType_2 = QComboBox(self.groupBox_2)
        self.fileOperationType_2.addItem("")
        self.fileOperationType_2.addItem("")
        self.fileOperationType_2.addItem("")
        self.fileOperationType_2.addItem("")
        self.fileOperationType_2.addItem("")
        self.fileOperationType_2.addItem("")
        self.fileOperationType_2.addItem("")
        self.fileOperationType_2.addItem("")
        self.fileOperationType_2.setObjectName(u"fileOperationType_2")
        self.fileOperationType_2.setFont(font)
        self.fileOperationType_2.setAutoFillBackground(False)
        self.fileOperationType_2.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.fileOperationType_2.setIconSize(QSize(16, 16))
        self.fileOperationType_2.setFrame(True)

        self.gridLayout_6.addWidget(self.fileOperationType_2, 0, 2, 1, 1)

        self.fileOperationType = QComboBox(self.groupBox_2)
        self.fileOperationType.addItem("")
        self.fileOperationType.addItem("")
        self.fileOperationType.addItem("")
        self.fileOperationType.addItem("")
        self.fileOperationType.addItem("")
        self.fileOperationType.addItem("")
        self.fileOperationType.addItem("")
        self.fileOperationType.addItem("")
        self.fileOperationType.setObjectName(u"fileOperationType")
        self.fileOperationType.setFont(font)
        self.fileOperationType.setAutoFillBackground(False)
        self.fileOperationType.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.fileOperationType.setIconSize(QSize(16, 16))
        self.fileOperationType.setFrame(True)

        self.gridLayout_6.addWidget(self.fileOperationType, 0, 3, 1, 1)

        self.btn_stratFileOperation = QPushButton(self.groupBox_2)
        self.btn_stratFileOperation.setObjectName(u"btn_stratFileOperation")
        self.btn_stratFileOperation.setMinimumSize(QSize(150, 30))
        self.btn_stratFileOperation.setFont(font)
        self.btn_stratFileOperation.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_stratFileOperation.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.btn_stratFileOperation.setIcon(icon5)

        self.gridLayout_6.addWidget(self.btn_stratFileOperation, 1, 0, 1, 2)

        self.btn_stopFileOperation = QPushButton(self.groupBox_2)
        self.btn_stopFileOperation.setObjectName(u"btn_stopFileOperation")
        self.btn_stopFileOperation.setMinimumSize(QSize(150, 30))
        self.btn_stopFileOperation.setFont(font)
        self.btn_stopFileOperation.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_stopFileOperation.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.btn_stopFileOperation.setIcon(icon5)

        self.gridLayout_6.addWidget(self.btn_stopFileOperation, 1, 2, 1, 2)

        self.fileOperationResults = QPlainTextEdit(self.fileOperation)
        self.fileOperationResults.setObjectName(u"fileOperationResults")
        self.fileOperationResults.setGeometry(QRect(10, 180, 731, 241))
        self.fileOperationResults.setMinimumSize(QSize(200, 200))
        self.fileOperationResults.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.stackedWidget.addWidget(self.fileOperation)
        self.command = QWidget()
        self.command.setObjectName(u"command")
        self.label_5 = QLabel(self.command)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(30, 20, 71, 21))
        self.groupBox_8 = QGroupBox(self.command)
        self.groupBox_8.setObjectName(u"groupBox_8")
        self.groupBox_8.setGeometry(QRect(40, 70, 741, 121))
        self.gridLayout_8 = QGridLayout(self.groupBox_8)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.commandInput = QLineEdit(self.groupBox_8)
        self.commandInput.setObjectName(u"commandInput")
        self.commandInput.setMinimumSize(QSize(0, 30))
        self.commandInput.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.gridLayout_8.addWidget(self.commandInput, 0, 0, 1, 1)

        self.checkBox_4 = QCheckBox(self.groupBox_8)
        self.checkBox_4.setObjectName(u"checkBox_4")
        self.checkBox_4.setAutoFillBackground(False)
        self.checkBox_4.setStyleSheet(u"")

        self.gridLayout_8.addWidget(self.checkBox_4, 0, 1, 1, 1)

        self.label_15 = QLabel(self.groupBox_8)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout_8.addWidget(self.label_15, 0, 2, 1, 1)

        self.contentCoding = QComboBox(self.groupBox_8)
        self.contentCoding.addItem("")
        self.contentCoding.addItem("")
        self.contentCoding.addItem("")
        self.contentCoding.addItem("")
        self.contentCoding.addItem("")
        self.contentCoding.addItem("")
        self.contentCoding.addItem("")
        self.contentCoding.addItem("")
        self.contentCoding.setObjectName(u"contentCoding")
        self.contentCoding.setFont(font)
        self.contentCoding.setAutoFillBackground(False)
        self.contentCoding.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.contentCoding.setIconSize(QSize(16, 16))
        self.contentCoding.setFrame(True)

        self.gridLayout_8.addWidget(self.contentCoding, 0, 3, 1, 1)

        self.btn_startCommand = QPushButton(self.groupBox_8)
        self.btn_startCommand.setObjectName(u"btn_startCommand")
        self.btn_startCommand.setMinimumSize(QSize(150, 30))
        self.btn_startCommand.setFont(font)
        self.btn_startCommand.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_startCommand.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.btn_startCommand.setIcon(icon5)

        self.gridLayout_8.addWidget(self.btn_startCommand, 1, 0, 1, 1)

        self.btn_stopCommand = QPushButton(self.groupBox_8)
        self.btn_stopCommand.setObjectName(u"btn_stopCommand")
        self.btn_stopCommand.setMinimumSize(QSize(150, 30))
        self.btn_stopCommand.setFont(font)
        self.btn_stopCommand.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_stopCommand.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.btn_stopCommand.setIcon(icon5)

        self.gridLayout_8.addWidget(self.btn_stopCommand, 1, 1, 1, 3)

        self.commandResults = QPlainTextEdit(self.command)
        self.commandResults.setObjectName(u"commandResults")
        self.commandResults.setGeometry(QRect(40, 200, 741, 241))
        self.commandResults.setMinimumSize(QSize(200, 200))
        self.commandResults.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.stackedWidget.addWidget(self.command)
        self.logCenter = QWidget()
        self.logCenter.setObjectName(u"logCenter")
        self.label_6 = QLabel(self.logCenter)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(10, 0, 81, 31))
        self.label_16 = QLabel(self.logCenter)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(10, 40, 121, 31))
        self.groupBox_21 = QGroupBox(self.logCenter)
        self.groupBox_21.setObjectName(u"groupBox_21")
        self.groupBox_21.setGeometry(QRect(0, 30, 831, 441))
        self.packetSendingRecord = QTableWidget(self.groupBox_21)
        if (self.packetSendingRecord.columnCount() < 7):
            self.packetSendingRecord.setColumnCount(7)
        __qtablewidgetitem = QTableWidgetItem()
        self.packetSendingRecord.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.packetSendingRecord.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.packetSendingRecord.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.packetSendingRecord.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.packetSendingRecord.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.packetSendingRecord.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.packetSendingRecord.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        if (self.packetSendingRecord.rowCount() < 16):
            self.packetSendingRecord.setRowCount(16)
        font4 = QFont()
        font4.setFamilies([u"Segoe UI"])
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setFont(font4);
        self.packetSendingRecord.setVerticalHeaderItem(0, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.packetSendingRecord.setVerticalHeaderItem(1, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.packetSendingRecord.setVerticalHeaderItem(2, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.packetSendingRecord.setVerticalHeaderItem(3, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.packetSendingRecord.setVerticalHeaderItem(4, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.packetSendingRecord.setVerticalHeaderItem(5, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.packetSendingRecord.setVerticalHeaderItem(6, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.packetSendingRecord.setVerticalHeaderItem(7, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.packetSendingRecord.setVerticalHeaderItem(8, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.packetSendingRecord.setVerticalHeaderItem(9, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.packetSendingRecord.setVerticalHeaderItem(10, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.packetSendingRecord.setVerticalHeaderItem(11, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.packetSendingRecord.setVerticalHeaderItem(12, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.packetSendingRecord.setVerticalHeaderItem(13, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.packetSendingRecord.setVerticalHeaderItem(14, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.packetSendingRecord.setVerticalHeaderItem(15, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.packetSendingRecord.setItem(0, 0, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.packetSendingRecord.setItem(0, 1, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.packetSendingRecord.setItem(0, 2, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.packetSendingRecord.setItem(0, 3, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.packetSendingRecord.setItem(0, 4, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.packetSendingRecord.setItem(0, 5, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.packetSendingRecord.setItem(0, 6, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.packetSendingRecord.setItem(1, 0, __qtablewidgetitem30)
        self.packetSendingRecord.setObjectName(u"packetSendingRecord")
        self.packetSendingRecord.setGeometry(QRect(10, 60, 816, 160))
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.packetSendingRecord.sizePolicy().hasHeightForWidth())
        self.packetSendingRecord.setSizePolicy(sizePolicy4)
        palette = QPalette()
        brush = QBrush(QColor(221, 221, 221, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(0, 0, 0, 0))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        brush2 = QBrush(QColor(0, 0, 0, 255))
        brush2.setStyle(Qt.NoBrush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush2)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        brush3 = QBrush(QColor(0, 0, 0, 255))
        brush3.setStyle(Qt.NoBrush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        brush4 = QBrush(QColor(0, 0, 0, 255))
        brush4.setStyle(Qt.NoBrush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush)
#endif
        self.packetSendingRecord.setPalette(palette)
        self.packetSendingRecord.setFrameShape(QFrame.Shape.NoFrame)
        self.packetSendingRecord.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.packetSendingRecord.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.packetSendingRecord.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.packetSendingRecord.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.packetSendingRecord.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.packetSendingRecord.setShowGrid(True)
        self.packetSendingRecord.setGridStyle(Qt.PenStyle.SolidLine)
        self.packetSendingRecord.setSortingEnabled(False)
        self.packetSendingRecord.horizontalHeader().setVisible(False)
        self.packetSendingRecord.horizontalHeader().setCascadingSectionResizes(True)
        self.packetSendingRecord.horizontalHeader().setDefaultSectionSize(200)
        self.packetSendingRecord.horizontalHeader().setStretchLastSection(True)
        self.packetSendingRecord.verticalHeader().setVisible(False)
        self.packetSendingRecord.verticalHeader().setCascadingSectionResizes(False)
        self.packetSendingRecord.verticalHeader().setHighlightSections(False)
        self.packetSendingRecord.verticalHeader().setStretchLastSection(True)
        self.log = QPlainTextEdit(self.groupBox_21)
        self.log.setObjectName(u"log")
        self.log.setGeometry(QRect(10, 220, 801, 200))
        self.log.setMinimumSize(QSize(200, 200))
        self.log.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.stackedWidget.addWidget(self.logCenter)

        self.verticalLayout_15.addWidget(self.stackedWidget)


        self.horizontalLayout_4.addWidget(self.pagesContainer)

        self.extraRightBox = QFrame(self.content)
        self.extraRightBox.setObjectName(u"extraRightBox")
        self.extraRightBox.setMinimumSize(QSize(0, 0))
        self.extraRightBox.setMaximumSize(QSize(0, 16777215))
        self.extraRightBox.setFrameShape(QFrame.Shape.NoFrame)
        self.extraRightBox.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.extraRightBox)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.themeSettingsTopDetail = QFrame(self.extraRightBox)
        self.themeSettingsTopDetail.setObjectName(u"themeSettingsTopDetail")
        self.themeSettingsTopDetail.setMaximumSize(QSize(16777215, 3))
        self.themeSettingsTopDetail.setFrameShape(QFrame.Shape.NoFrame)
        self.themeSettingsTopDetail.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_7.addWidget(self.themeSettingsTopDetail)

        self.contentSettings = QFrame(self.extraRightBox)
        self.contentSettings.setObjectName(u"contentSettings")
        self.contentSettings.setFrameShape(QFrame.Shape.NoFrame)
        self.contentSettings.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.contentSettings)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.topMenus = QFrame(self.contentSettings)
        self.topMenus.setObjectName(u"topMenus")
        self.topMenus.setFrameShape(QFrame.Shape.NoFrame)
        self.topMenus.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.topMenus)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.btn_message = QPushButton(self.topMenus)
        self.btn_message.setObjectName(u"btn_message")
        sizePolicy.setHeightForWidth(self.btn_message.sizePolicy().hasHeightForWidth())
        self.btn_message.setSizePolicy(sizePolicy)
        self.btn_message.setMinimumSize(QSize(0, 45))
        self.btn_message.setFont(font)
        self.btn_message.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_message.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_message.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-envelope-open.png);")

        self.verticalLayout_14.addWidget(self.btn_message)

        self.btn_print = QPushButton(self.topMenus)
        self.btn_print.setObjectName(u"btn_print")
        sizePolicy.setHeightForWidth(self.btn_print.sizePolicy().hasHeightForWidth())
        self.btn_print.setSizePolicy(sizePolicy)
        self.btn_print.setMinimumSize(QSize(0, 45))
        self.btn_print.setFont(font)
        self.btn_print.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_print.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_print.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-print.png);")

        self.verticalLayout_14.addWidget(self.btn_print)

        self.btn_logout = QPushButton(self.topMenus)
        self.btn_logout.setObjectName(u"btn_logout")
        sizePolicy.setHeightForWidth(self.btn_logout.sizePolicy().hasHeightForWidth())
        self.btn_logout.setSizePolicy(sizePolicy)
        self.btn_logout.setMinimumSize(QSize(0, 45))
        self.btn_logout.setFont(font)
        self.btn_logout.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_logout.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_logout.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-account-logout.png);")

        self.verticalLayout_14.addWidget(self.btn_logout)


        self.verticalLayout_13.addWidget(self.topMenus, 0, Qt.AlignmentFlag.AlignTop)


        self.verticalLayout_7.addWidget(self.contentSettings)


        self.horizontalLayout_4.addWidget(self.extraRightBox)


        self.verticalLayout_6.addWidget(self.content)

        self.bottomBar = QFrame(self.contentBottom)
        self.bottomBar.setObjectName(u"bottomBar")
        self.bottomBar.setMinimumSize(QSize(0, 22))
        self.bottomBar.setMaximumSize(QSize(16777215, 22))
        self.bottomBar.setFrameShape(QFrame.Shape.NoFrame)
        self.bottomBar.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.bottomBar)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.creditsLabel = QLabel(self.bottomBar)
        self.creditsLabel.setObjectName(u"creditsLabel")
        self.creditsLabel.setMaximumSize(QSize(16777215, 16))
        font5 = QFont()
        font5.setFamilies([u"Segoe UI"])
        font5.setBold(False)
        font5.setItalic(False)
        self.creditsLabel.setFont(font5)
        self.creditsLabel.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.creditsLabel)

        self.version = QLabel(self.bottomBar)
        self.version.setObjectName(u"version")
        self.version.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.version)

        self.frame_size_grip = QFrame(self.bottomBar)
        self.frame_size_grip.setObjectName(u"frame_size_grip")
        self.frame_size_grip.setMinimumSize(QSize(20, 0))
        self.frame_size_grip.setMaximumSize(QSize(20, 16777215))
        self.frame_size_grip.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_size_grip.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_5.addWidget(self.frame_size_grip)


        self.verticalLayout_6.addWidget(self.bottomBar)


        self.verticalLayout_2.addWidget(self.contentBottom)


        self.appLayout.addWidget(self.contentBox)


        self.appMargins.addWidget(self.bgApp)

        MainWindow.setCentralWidget(self.styleSheet)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.titleLeftApp.setText(QCoreApplication.translate("MainWindow", u"PyDracula", None))
        self.titleLeftDescription.setText("")
        self.toggleButton.setText(QCoreApplication.translate("MainWindow", u"\u9690\u85cf\u83dc\u5355\u680f", None))
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"\u81ea\u52a8\u6ce8\u5165", None))
        self.btn_manualInjection.setText(QCoreApplication.translate("MainWindow", u"\u4eba\u5de5\u6ce8\u5165", None))
        self.btn_dataCenter.setText(QCoreApplication.translate("MainWindow", u"\u6570\u636e\u4e2d\u5fc3", None))
        self.btn_command.setText(QCoreApplication.translate("MainWindow", u"\u547d\u4ee4\u64cd\u4f5c", None))
        self.btn_logCenter.setText(QCoreApplication.translate("MainWindow", u"\u65e5\u5fd7\u4e2d\u5fc3", None))
        self.btn_fileOperation.setText(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6\u64cd\u4f5c", None))
        self.btn_save.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58", None))
        self.btn_exit.setText(QCoreApplication.translate("MainWindow", u"\u9000\u51fa", None))
        self.toggleLeftBox.setText(QCoreApplication.translate("MainWindow", u"\u8bbe\u7f6e", None))
        self.extraLabel.setText(QCoreApplication.translate("MainWindow", u"\u6211\u53eb\u9ec4\u6587\u8c6a", None))
#if QT_CONFIG(tooltip)
        self.extraCloseColumnBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close left box", None))
#endif // QT_CONFIG(tooltip)
        self.extraCloseColumnBtn.setText("")
        self.btn_share.setText(QCoreApplication.translate("MainWindow", u"\u5206\u4eab", None))
        self.btn_adjustments.setText(QCoreApplication.translate("MainWindow", u"\u8c03\u6574", None))
        self.btn_more.setText(QCoreApplication.translate("MainWindow", u"\u66f4\u591a", None))
        self.textEdit.setMarkdown("")
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.titleRightInfo.setText(QCoreApplication.translate("MainWindow", u"\u7f51\u7edc\u5b89\u5168\u8bfe\u7a0b\u8bbe\u8ba1", None))
#if QT_CONFIG(tooltip)
        self.settingsTopBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Settings", None))
#endif // QT_CONFIG(tooltip)
        self.settingsTopBtn.setText("")
#if QT_CONFIG(tooltip)
        self.minimizeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.minimizeAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.closeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.closeAppBtn.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u624b\u52a8\u6ce8\u5165\uff1a", None))
        self.btn_exportConfiguration.setText(QCoreApplication.translate("MainWindow", u"\u5bfc\u51fa\u914d\u7f6e", None))
        self.injectionType.setItemText(0, QCoreApplication.translate("MainWindow", u"Bool\u76f2\u6ce8", None))
        self.injectionType.setItemText(1, QCoreApplication.translate("MainWindow", u"Union\u6ce8\u5165", None))
        self.injectionType.setItemText(2, QCoreApplication.translate("MainWindow", u"\u9519\u8bef\u663e\u793a\u6ce8\u5165", None))

        self.retry.setText(QCoreApplication.translate("MainWindow", u"\u91cd\u8bd5", None))
        self.retry.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Type here", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u6ce8\u5165\u7c7b\u578b\uff1a", None))
        self.address_2.setText(QCoreApplication.translate("MainWindow", u"\u7ebf\u7a0b", None))
        self.address_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Type here", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u6570\u636e\u5e93\uff1a", None))
        self.checkBox_3.setText(QCoreApplication.translate("MainWindow", u"SSL", None))
        self.coding.setItemText(0, QCoreApplication.translate("MainWindow", u"UTF-8", None))

        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u7f16\u7801\uff1a", None))
        self.btn_startInjection.setText(QCoreApplication.translate("MainWindow", u"\u8bc6\u522b\u6ce8\u5165", None))
        self.address.setText(QCoreApplication.translate("MainWindow", u"\u5730\u5740", None))
        self.address.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Type here", None))
        self.overtime.setText(QCoreApplication.translate("MainWindow", u"\u8d85\u65f6\u65f6\u95f4", None))
        self.overtime.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Type here", None))
        self.databaseType.setItemText(0, QCoreApplication.translate("MainWindow", u"MySQL", None))
        self.databaseType.setItemText(1, QCoreApplication.translate("MainWindow", u"Access", None))

        self.portID.setText(QCoreApplication.translate("MainWindow", u"\u7aef\u53e3", None))
        self.portID.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Type here", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u6570\u636e\u4e2d\u5fc3", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"\u6570\u636e\u5e93\u4fe1\u606f", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"\u83b7\u53d6\u6570\u636e", None))
        self.number.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb", None))
        self.number.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Type here", None))
        self.address_4.setText(QCoreApplication.translate("MainWindow", u"\u6761\u6570", None))
        self.address_4.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Type here", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"\u7f16\u7801\u7c7b\u578b", None))
        self.btn_getData.setText(QCoreApplication.translate("MainWindow", u"\u83b7\u53d6\u6570\u636e", None))
        self.btn_exportData.setText(QCoreApplication.translate("MainWindow", u"\u5bfc\u51fa\u6570\u636e", None))
        self.btn_stopGettingData.setText(QCoreApplication.translate("MainWindow", u"\u505c\u6b62\u83b7\u53d6", None))
        self.codingType.setItemText(0, QCoreApplication.translate("MainWindow", u"UTF-8", None))

        self.browse.setText(QCoreApplication.translate("MainWindow", u"\u6d4f\u89c8", None))
        self.lineEdit_3.setText(QCoreApplication.translate("MainWindow", u"URL", None))
        self.lineEdit_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Type here", None))
        self.labelBoxBlenderInstalation_3.setText(QCoreApplication.translate("MainWindow", u"\u7f51\u9875\u663e\u793a\uff1a", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u81ea\u52a8\u6ce8\u5165\uff1a", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6\u64cd\u4f5c", None))
        self.path.setText(QCoreApplication.translate("MainWindow", u"\u8def\u5f84", None))
        self.path.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Type here", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6\u7f16\u7801\uff1a", None))
        self.fileOperationType_2.setItemText(0, QCoreApplication.translate("MainWindow", u"GBK", None))
        self.fileOperationType_2.setItemText(1, "")
        self.fileOperationType_2.setItemText(2, "")
        self.fileOperationType_2.setItemText(3, "")
        self.fileOperationType_2.setItemText(4, "")
        self.fileOperationType_2.setItemText(5, "")
        self.fileOperationType_2.setItemText(6, "")
        self.fileOperationType_2.setItemText(7, "")

        self.fileOperationType.setItemText(0, QCoreApplication.translate("MainWindow", u"MySQL Union\u5199\u6587\u4ef6", None))
        self.fileOperationType.setItemText(1, QCoreApplication.translate("MainWindow", u"MySQL Load_File \u8bfb\u6587\u4ef6", None))
        self.fileOperationType.setItemText(2, QCoreApplication.translate("MainWindow", u"SQLServer FileSystemObject\u5199\u6587\u4ef6", None))
        self.fileOperationType.setItemText(3, QCoreApplication.translate("MainWindow", u"SQLServer Sp_MakeWebTask\u5199\u6587\u4ef6", None))
        self.fileOperationType.setItemText(4, QCoreApplication.translate("MainWindow", u"SQLServer\u5229\u7528\u5907\u4efd\u6570\u636e\u5e93\u5199\u6587\u4ef6", None))
        self.fileOperationType.setItemText(5, QCoreApplication.translate("MainWindow", u"SQLServer FileSystemObject\u8bfb\u6587\u4ef6", None))
        self.fileOperationType.setItemText(6, "")
        self.fileOperationType.setItemText(7, "")

        self.btn_stratFileOperation.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb", None))
        self.btn_stopFileOperation.setText(QCoreApplication.translate("MainWindow", u"\u505c\u6b62", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u547d\u4ee4\u6267\u884c", None))
        self.commandInput.setText(QCoreApplication.translate("MainWindow", u"\u547d\u4ee4", None))
        self.commandInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Type here", None))
        self.checkBox_4.setText(QCoreApplication.translate("MainWindow", u"\u56de\u663e\u7ed3\u679c", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"\u5185\u5bb9\u7f16\u7801", None))
        self.contentCoding.setItemText(0, QCoreApplication.translate("MainWindow", u"GBK", None))
        self.contentCoding.setItemText(1, "")
        self.contentCoding.setItemText(2, "")
        self.contentCoding.setItemText(3, "")
        self.contentCoding.setItemText(4, "")
        self.contentCoding.setItemText(5, "")
        self.contentCoding.setItemText(6, "")
        self.contentCoding.setItemText(7, "")

        self.btn_startCommand.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb", None))
        self.btn_stopCommand.setText(QCoreApplication.translate("MainWindow", u"\u7ed3\u675f", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u65e5\u5fd7\u4e2d\u5fc3", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"\u6570\u636e\u5305\u53d1\u5305\u8bb0\u5f55", None))
        ___qtablewidgetitem = self.packetSendingRecord.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem1 = self.packetSendingRecord.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem2 = self.packetSendingRecord.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem3 = self.packetSendingRecord.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem4 = self.packetSendingRecord.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"4", None));
        ___qtablewidgetitem5 = self.packetSendingRecord.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u5217", None));
        ___qtablewidgetitem6 = self.packetSendingRecord.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"5", None));
        ___qtablewidgetitem7 = self.packetSendingRecord.verticalHeaderItem(0)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem8 = self.packetSendingRecord.verticalHeaderItem(1)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem9 = self.packetSendingRecord.verticalHeaderItem(2)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem10 = self.packetSendingRecord.verticalHeaderItem(3)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem11 = self.packetSendingRecord.verticalHeaderItem(4)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem12 = self.packetSendingRecord.verticalHeaderItem(5)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem13 = self.packetSendingRecord.verticalHeaderItem(6)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem14 = self.packetSendingRecord.verticalHeaderItem(7)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem15 = self.packetSendingRecord.verticalHeaderItem(8)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem16 = self.packetSendingRecord.verticalHeaderItem(9)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem17 = self.packetSendingRecord.verticalHeaderItem(10)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem18 = self.packetSendingRecord.verticalHeaderItem(11)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem19 = self.packetSendingRecord.verticalHeaderItem(12)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem20 = self.packetSendingRecord.verticalHeaderItem(13)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem21 = self.packetSendingRecord.verticalHeaderItem(14)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem22 = self.packetSendingRecord.verticalHeaderItem(15)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"New Row", None));

        __sortingEnabled = self.packetSendingRecord.isSortingEnabled()
        self.packetSendingRecord.setSortingEnabled(False)
        ___qtablewidgetitem23 = self.packetSendingRecord.item(0, 0)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"\u53d1\u5305\u5e8f\u53f7", None));
        ___qtablewidgetitem24 = self.packetSendingRecord.item(0, 1)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"Payload", None));
        ___qtablewidgetitem25 = self.packetSendingRecord.item(0, 2)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"\u7528\u65f6\u3010\u6beb\u79d2\u3011", None));
        ___qtablewidgetitem26 = self.packetSendingRecord.item(0, 3)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"\u72b6\u6001\u7801", None));
        ___qtablewidgetitem27 = self.packetSendingRecord.item(0, 4)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"body\u957f\u5ea6", None));
        ___qtablewidgetitem28 = self.packetSendingRecord.item(0, 5)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainWindow", u"\u5ef6\u8fdf\u3010\u6beb\u7c73\u3011", None));
        ___qtablewidgetitem29 = self.packetSendingRecord.item(0, 6)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("MainWindow", u"\u4ee3\u7406", None));
        self.packetSendingRecord.setSortingEnabled(__sortingEnabled)

        self.btn_message.setText(QCoreApplication.translate("MainWindow", u"\u6d88\u606f", None))
        self.btn_print.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5370", None))
        self.btn_logout.setText(QCoreApplication.translate("MainWindow", u"\u9000\u51fa", None))
        self.creditsLabel.setText("")
        self.version.setText(QCoreApplication.translate("MainWindow", u"v1.0.0", None))
    # retranslateUi

