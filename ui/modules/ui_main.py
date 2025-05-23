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
        MainWindow.resize(940, 560)
        MainWindow.setMinimumSize(QSize(940, 560))
        MainWindow.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
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
        self.leftMenuBg.setLineWidth(0)
        self.verticalLayout_3 = QVBoxLayout(self.leftMenuBg)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
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
        self.titleLeftApp.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
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
        self.leftMenuFrame.setToolTipDuration(0)
        self.leftMenuFrame.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.leftMenuFrame.setAutoFillBackground(False)
        self.leftMenuFrame.setFrameShape(QFrame.Shape.NoFrame)
        self.leftMenuFrame.setFrameShadow(QFrame.Shadow.Plain)
        self.leftMenuFrame.setLineWidth(0)
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
        self.btn_home.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.btn_home.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_home.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-home.png);")

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
        self.btn_dataCenter.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-airplane-mode.png);")

        self.verticalLayout_8.addWidget(self.btn_dataCenter)

        self.btn_command = QPushButton(self.topMenu)
        self.btn_command.setObjectName(u"btn_command")
        sizePolicy.setHeightForWidth(self.btn_command.sizePolicy().hasHeightForWidth())
        self.btn_command.setSizePolicy(sizePolicy)
        self.btn_command.setMinimumSize(QSize(0, 45))
        self.btn_command.setFont(font)
        self.btn_command.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_command.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_command.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-align-center.png);")

        self.verticalLayout_8.addWidget(self.btn_command)

        self.btn_fileOperation = QPushButton(self.topMenu)
        self.btn_fileOperation.setObjectName(u"btn_fileOperation")
        sizePolicy.setHeightForWidth(self.btn_fileOperation.sizePolicy().hasHeightForWidth())
        self.btn_fileOperation.setSizePolicy(sizePolicy)
        self.btn_fileOperation.setMinimumSize(QSize(0, 45))
        self.btn_fileOperation.setFont(font)
        self.btn_fileOperation.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_fileOperation.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_fileOperation.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-cart.png);")

        self.verticalLayout_8.addWidget(self.btn_fileOperation)

        self.btn_logCenter = QPushButton(self.topMenu)
        self.btn_logCenter.setObjectName(u"btn_logCenter")
        sizePolicy.setHeightForWidth(self.btn_logCenter.sizePolicy().hasHeightForWidth())
        self.btn_logCenter.setSizePolicy(sizePolicy)
        self.btn_logCenter.setMinimumSize(QSize(0, 45))
        self.btn_logCenter.setFont(font)
        self.btn_logCenter.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_logCenter.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_logCenter.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-cast.png);")

        self.verticalLayout_8.addWidget(self.btn_logCenter)

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

        self.verticalMenuLayout.addWidget(self.bottomMenu, 0, Qt.AlignmentFlag.AlignBottom)

        self.toggleBox.raise_()
        self.bottomMenu.raise_()
        self.topMenu.raise_()

        self.verticalLayout_3.addWidget(self.leftMenuFrame)


        self.appLayout.addWidget(self.leftMenuBg)

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
        self.leftBox.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.leftBox.setFrameShape(QFrame.Shape.NoFrame)
        self.leftBox.setFrameShadow(QFrame.Shadow.Raised)
        self.leftBox.setLineWidth(39)
        self.horizontalLayout_3 = QHBoxLayout(self.leftBox)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(12, -1, -1, -1)
        self.titleRightInfo = QLabel(self.leftBox)
        self.titleRightInfo.setObjectName(u"titleRightInfo")
        self.titleRightInfo.setFont(font)
        self.titleRightInfo.setLineWidth(26)
        self.titleRightInfo.setMidLineWidth(23)
        self.titleRightInfo.setMargin(5)
        self.titleRightInfo.setIndent(2)
        self.titleRightInfo.setOpenExternalLinks(False)
        self.titleRightInfo.setTextInteractionFlags(Qt.TextInteractionFlag.NoTextInteraction)

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
        icon = QIcon()
        icon.addFile(u":/icons/images/icons/icon_settings.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.settingsTopBtn.setIcon(icon)
        self.settingsTopBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.settingsTopBtn)

        self.minimizeAppBtn = QPushButton(self.rightButtons)
        self.minimizeAppBtn.setObjectName(u"minimizeAppBtn")
        self.minimizeAppBtn.setMinimumSize(QSize(28, 28))
        self.minimizeAppBtn.setMaximumSize(QSize(28, 28))
        self.minimizeAppBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/icons/images/icons/icon_minimize.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.minimizeAppBtn.setIcon(icon1)
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
        icon2 = QIcon()
        icon2.addFile(u":/icons/images/icons/icon_maximize.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.maximizeRestoreAppBtn.setIcon(icon2)
        self.maximizeRestoreAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.maximizeRestoreAppBtn)

        self.closeAppBtn = QPushButton(self.rightButtons)
        self.closeAppBtn.setObjectName(u"closeAppBtn")
        self.closeAppBtn.setMinimumSize(QSize(28, 28))
        self.closeAppBtn.setMaximumSize(QSize(28, 28))
        self.closeAppBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/icons/images/icons/icon_close.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.closeAppBtn.setIcon(icon3)
        self.closeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.closeAppBtn)


        self.horizontalLayout.addWidget(self.rightButtons, 0, Qt.AlignmentFlag.AlignRight)


        self.verticalLayout_2.addWidget(self.contentTopBg)

        self.contentBottom = QFrame(self.contentBox)
        self.contentBottom.setObjectName(u"contentBottom")
        self.contentBottom.setFrameShape(QFrame.Shape.NoFrame)
        self.contentBottom.setFrameShadow(QFrame.Shadow.Plain)
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
        self.verticalLayout_15.setSpacing(6)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(9, -1, -1, -1)
        self.stackedWidget = QStackedWidget(self.pagesContainer)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.stackedWidget.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.stackedWidget.setAutoFillBackground(False)
        self.stackedWidget.setStyleSheet(u"background: transparent;")
        self.stackedWidget.setLineWidth(0)
        self.home = QWidget()
        self.home.setObjectName(u"home")
        self.home.setStyleSheet(u"background-image: url(:/images/images/images/PyDracula_vertical.png);\n"
"background-position: center;\n"
"background-repeat: no-repeat;")
        self.stackedWidget.addWidget(self.home)
        self.manualInjection = QWidget()
        self.manualInjection.setObjectName(u"manualInjection")
        self.horizontalLayoutWidget = QWidget(self.manualInjection)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(20, 20, 701, 51))
        self.horizontalLayout_10 = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.requestMethod = QComboBox(self.horizontalLayoutWidget)
        self.requestMethod.addItem("")
        self.requestMethod.addItem("")
        self.requestMethod.addItem("")
        self.requestMethod.addItem("")
        self.requestMethod.addItem("")
        self.requestMethod.addItem("")
        self.requestMethod.addItem("")
        self.requestMethod.setObjectName(u"requestMethod")
        self.requestMethod.setMinimumSize(QSize(0, 34))
        self.requestMethod.setFont(font)
        self.requestMethod.setAutoFillBackground(False)
        self.requestMethod.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.requestMethod.setIconSize(QSize(16, 16))
        self.requestMethod.setFrame(True)

        self.horizontalLayout_10.addWidget(self.requestMethod)

        self.autoUrl = QLineEdit(self.horizontalLayoutWidget)
        self.autoUrl.setObjectName(u"autoUrl")
        self.autoUrl.setMinimumSize(QSize(0, 34))
        self.autoUrl.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.autoUrl.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.autoUrl.setMaxLength(78)

        self.horizontalLayout_10.addWidget(self.autoUrl)

        self.https = QCheckBox(self.horizontalLayoutWidget)
        self.https.setObjectName(u"https")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.https.sizePolicy().hasHeightForWidth())
        self.https.setSizePolicy(sizePolicy3)
        self.https.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.https.setAutoFillBackground(False)
        self.https.setStyleSheet(u"")

        self.horizontalLayout_10.addWidget(self.https)

        self.btn_startInjection = QPushButton(self.horizontalLayoutWidget)
        self.btn_startInjection.setObjectName(u"btn_startInjection")
        self.btn_startInjection.setMinimumSize(QSize(100, 34))
        self.btn_startInjection.setFont(font)
        self.btn_startInjection.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_startInjection.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.horizontalLayout_10.addWidget(self.btn_startInjection)

        self.groupBox_2 = QGroupBox(self.manualInjection)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(20, 90, 701, 341))
        self.horizontalLayoutWidget_4 = QWidget(self.groupBox_2)
        self.horizontalLayoutWidget_4.setObjectName(u"horizontalLayoutWidget_4")
        self.horizontalLayoutWidget_4.setGeometry(QRect(20, 30, 661, 61))
        self.horizontalLayout_13 = QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.horizontalLayoutWidget_4)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_13.addWidget(self.label_3)

        self.injectionType = QComboBox(self.horizontalLayoutWidget_4)
        self.injectionType.addItem("")
        self.injectionType.addItem("")
        self.injectionType.addItem("")
        self.injectionType.addItem("")
        self.injectionType.addItem("")
        self.injectionType.addItem("")
        self.injectionType.addItem("")
        self.injectionType.setObjectName(u"injectionType")
        self.injectionType.setFont(font)
        self.injectionType.setAutoFillBackground(False)
        self.injectionType.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.injectionType.setIconSize(QSize(16, 16))
        self.injectionType.setFrame(True)

        self.horizontalLayout_13.addWidget(self.injectionType)

        self.label_10 = QLabel(self.horizontalLayoutWidget_4)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_13.addWidget(self.label_10)

        self.databaseType = QComboBox(self.horizontalLayoutWidget_4)
        self.databaseType.addItem("")
        self.databaseType.addItem("")
        self.databaseType.addItem("")
        self.databaseType.addItem("")
        self.databaseType.addItem("")
        self.databaseType.addItem("")
        self.databaseType.addItem("")
        self.databaseType.addItem("")
        self.databaseType.addItem("")
        self.databaseType.addItem("")
        self.databaseType.addItem("")
        self.databaseType.addItem("")
        self.databaseType.addItem("")
        self.databaseType.addItem("")
        self.databaseType.addItem("")
        self.databaseType.addItem("")
        self.databaseType.addItem("")
        self.databaseType.addItem("")
        self.databaseType.addItem("")
        self.databaseType.addItem("")
        self.databaseType.addItem("")
        self.databaseType.addItem("")
        self.databaseType.addItem("")
        self.databaseType.addItem("")
        self.databaseType.setObjectName(u"databaseType")
        self.databaseType.setFont(font)
        self.databaseType.setAutoFillBackground(False)
        self.databaseType.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.databaseType.setIconSize(QSize(16, 16))
        self.databaseType.setFrame(True)

        self.horizontalLayout_13.addWidget(self.databaseType)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_18 = QLabel(self.horizontalLayoutWidget_4)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_12.addWidget(self.label_18)

        self.injectionLevel = QComboBox(self.horizontalLayoutWidget_4)
        self.injectionLevel.addItem("")
        self.injectionLevel.addItem("")
        self.injectionLevel.addItem("")
        self.injectionLevel.addItem("")
        self.injectionLevel.addItem("")
        self.injectionLevel.setObjectName(u"injectionLevel")
        self.injectionLevel.setFont(font)
        self.injectionLevel.setAutoFillBackground(False)
        self.injectionLevel.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.injectionLevel.setIconSize(QSize(16, 16))
        self.injectionLevel.setFrame(True)

        self.horizontalLayout_12.addWidget(self.injectionLevel)

        self.label_17 = QLabel(self.horizontalLayoutWidget_4)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_12.addWidget(self.label_17)

        self.riskLevel = QComboBox(self.horizontalLayoutWidget_4)
        self.riskLevel.addItem("")
        self.riskLevel.addItem("")
        self.riskLevel.addItem("")
        self.riskLevel.setObjectName(u"riskLevel")
        self.riskLevel.setFont(font)
        self.riskLevel.setAutoFillBackground(False)
        self.riskLevel.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.riskLevel.setIconSize(QSize(16, 16))
        self.riskLevel.setFrame(True)

        self.horizontalLayout_12.addWidget(self.riskLevel)


        self.horizontalLayout_13.addLayout(self.horizontalLayout_12)

        self.verticalLayoutWidget_7 = QWidget(self.groupBox_2)
        self.verticalLayoutWidget_7.setObjectName(u"verticalLayoutWidget_7")
        self.verticalLayoutWidget_7.setGeometry(QRect(20, 110, 661, 211))
        self.verticalLayout_17 = QVBoxLayout(self.verticalLayoutWidget_7)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.paramList = QListWidget(self.verticalLayoutWidget_7)
        self.paramList.setObjectName(u"paramList")

        self.verticalLayout_17.addWidget(self.paramList)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.paramInput = QLineEdit(self.verticalLayoutWidget_7)
        self.paramInput.setObjectName(u"paramInput")
        self.paramInput.setMinimumSize(QSize(0, 30))
        self.paramInput.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.horizontalLayout_11.addWidget(self.paramInput)

        self.btn_addParam = QPushButton(self.verticalLayoutWidget_7)
        self.btn_addParam.setObjectName(u"btn_addParam")
        self.btn_addParam.setMinimumSize(QSize(81, 30))
        self.btn_addParam.setFont(font)
        self.btn_addParam.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_addParam.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.horizontalLayout_11.addWidget(self.btn_addParam)

        self.btn_deleteParam = QPushButton(self.verticalLayoutWidget_7)
        self.btn_deleteParam.setObjectName(u"btn_deleteParam")
        self.btn_deleteParam.setMinimumSize(QSize(80, 30))
        self.btn_deleteParam.setFont(font)
        self.btn_deleteParam.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_deleteParam.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.horizontalLayout_11.addWidget(self.btn_deleteParam)


        self.verticalLayout_17.addLayout(self.horizontalLayout_11)

        self.stackedWidget.addWidget(self.manualInjection)
        self.dataCenter = QWidget()
        self.dataCenter.setObjectName(u"dataCenter")
        self.verticalLayoutWidget_5 = QWidget(self.dataCenter)
        self.verticalLayoutWidget_5.setObjectName(u"verticalLayoutWidget_5")
        self.verticalLayoutWidget_5.setGeometry(QRect(20, 20, 181, 411))
        self.verticalLayout_12 = QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_12.setSpacing(10)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.databaseInformation = QTableWidget(self.verticalLayoutWidget_5)
        if (self.databaseInformation.columnCount() < 2):
            self.databaseInformation.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.databaseInformation.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.databaseInformation.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        if (self.databaseInformation.rowCount() < 8):
            self.databaseInformation.setRowCount(8)
        font4 = QFont()
        font4.setFamilies([u"Segoe UI"])
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font4);
        self.databaseInformation.setVerticalHeaderItem(0, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.databaseInformation.setVerticalHeaderItem(1, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.databaseInformation.setVerticalHeaderItem(2, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.databaseInformation.setVerticalHeaderItem(3, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.databaseInformation.setVerticalHeaderItem(4, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.databaseInformation.setVerticalHeaderItem(5, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.databaseInformation.setVerticalHeaderItem(6, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.databaseInformation.setVerticalHeaderItem(7, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.databaseInformation.setItem(0, 0, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.databaseInformation.setItem(0, 1, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.databaseInformation.setItem(1, 0, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.databaseInformation.setItem(2, 0, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.databaseInformation.setItem(3, 0, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.databaseInformation.setItem(4, 0, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.databaseInformation.setItem(5, 0, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.databaseInformation.setItem(6, 0, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.databaseInformation.setItem(7, 0, __qtablewidgetitem18)
        self.databaseInformation.setObjectName(u"databaseInformation")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.databaseInformation.sizePolicy().hasHeightForWidth())
        self.databaseInformation.setSizePolicy(sizePolicy4)
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
        brush3 = QBrush(QColor(221, 221, 221, 128))
        brush3.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush3)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        brush4 = QBrush(QColor(0, 0, 0, 255))
        brush4.setStyle(Qt.NoBrush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush3)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        brush5 = QBrush(QColor(0, 0, 0, 255))
        brush5.setStyle(Qt.NoBrush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush5)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush3)
#endif
        self.databaseInformation.setPalette(palette)
        self.databaseInformation.setToolTipDuration(0)
        self.databaseInformation.setFrameShape(QFrame.Shape.NoFrame)
        self.databaseInformation.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.databaseInformation.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.databaseInformation.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.databaseInformation.setAutoScrollMargin(6)
        self.databaseInformation.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.databaseInformation.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.databaseInformation.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.databaseInformation.setShowGrid(True)
        self.databaseInformation.setGridStyle(Qt.PenStyle.SolidLine)
        self.databaseInformation.setSortingEnabled(False)
        self.databaseInformation.setRowCount(8)
        self.databaseInformation.setColumnCount(2)
        self.databaseInformation.horizontalHeader().setVisible(False)
        self.databaseInformation.horizontalHeader().setCascadingSectionResizes(True)
        self.databaseInformation.horizontalHeader().setMinimumSectionSize(20)
        self.databaseInformation.horizontalHeader().setDefaultSectionSize(50)
        self.databaseInformation.horizontalHeader().setStretchLastSection(True)
        self.databaseInformation.verticalHeader().setVisible(False)
        self.databaseInformation.verticalHeader().setCascadingSectionResizes(True)
        self.databaseInformation.verticalHeader().setMinimumSectionSize(30)
        self.databaseInformation.verticalHeader().setDefaultSectionSize(30)
        self.databaseInformation.verticalHeader().setHighlightSections(False)
        self.databaseInformation.verticalHeader().setStretchLastSection(False)

        self.verticalLayout_12.addWidget(self.databaseInformation)

        self.btn_getData = QPushButton(self.verticalLayoutWidget_5)
        self.btn_getData.setObjectName(u"btn_getData")
        self.btn_getData.setMinimumSize(QSize(100, 30))
        self.btn_getData.setFont(font)
        self.btn_getData.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_getData.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.verticalLayout_12.addWidget(self.btn_getData)

        self.verticalLayoutWidget_6 = QWidget(self.dataCenter)
        self.verticalLayoutWidget_6.setObjectName(u"verticalLayoutWidget_6")
        self.verticalLayoutWidget_6.setGeometry(QRect(220, 20, 501, 411))
        self.verticalLayout_16 = QVBoxLayout(self.verticalLayoutWidget_6)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setSpacing(6)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.databaseTree = QTreeView(self.verticalLayoutWidget_6)
        self.databaseTree.setObjectName(u"databaseTree")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.databaseTree.sizePolicy().hasHeightForWidth())
        self.databaseTree.setSizePolicy(sizePolicy5)
        self.databaseTree.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout_8.addWidget(self.databaseTree)

        self.tableInformation = QTableWidget(self.verticalLayoutWidget_6)
        if (self.tableInformation.columnCount() < 6):
            self.tableInformation.setColumnCount(6)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tableInformation.setHorizontalHeaderItem(0, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tableInformation.setHorizontalHeaderItem(1, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tableInformation.setHorizontalHeaderItem(2, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tableInformation.setHorizontalHeaderItem(3, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tableInformation.setHorizontalHeaderItem(4, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.tableInformation.setHorizontalHeaderItem(5, __qtablewidgetitem24)
        if (self.tableInformation.rowCount() < 16):
            self.tableInformation.setRowCount(16)
        __qtablewidgetitem25 = QTableWidgetItem()
        __qtablewidgetitem25.setFont(font4);
        self.tableInformation.setVerticalHeaderItem(0, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.tableInformation.setVerticalHeaderItem(1, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.tableInformation.setVerticalHeaderItem(2, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.tableInformation.setVerticalHeaderItem(3, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.tableInformation.setVerticalHeaderItem(4, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.tableInformation.setVerticalHeaderItem(5, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        self.tableInformation.setVerticalHeaderItem(6, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        self.tableInformation.setVerticalHeaderItem(7, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        self.tableInformation.setVerticalHeaderItem(8, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        self.tableInformation.setVerticalHeaderItem(9, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        self.tableInformation.setVerticalHeaderItem(10, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        self.tableInformation.setVerticalHeaderItem(11, __qtablewidgetitem36)
        __qtablewidgetitem37 = QTableWidgetItem()
        self.tableInformation.setVerticalHeaderItem(12, __qtablewidgetitem37)
        __qtablewidgetitem38 = QTableWidgetItem()
        self.tableInformation.setVerticalHeaderItem(13, __qtablewidgetitem38)
        __qtablewidgetitem39 = QTableWidgetItem()
        self.tableInformation.setVerticalHeaderItem(14, __qtablewidgetitem39)
        __qtablewidgetitem40 = QTableWidgetItem()
        self.tableInformation.setVerticalHeaderItem(15, __qtablewidgetitem40)
        __qtablewidgetitem41 = QTableWidgetItem()
        self.tableInformation.setItem(0, 0, __qtablewidgetitem41)
        __qtablewidgetitem42 = QTableWidgetItem()
        self.tableInformation.setItem(0, 1, __qtablewidgetitem42)
        __qtablewidgetitem43 = QTableWidgetItem()
        self.tableInformation.setItem(0, 2, __qtablewidgetitem43)
        __qtablewidgetitem44 = QTableWidgetItem()
        self.tableInformation.setItem(0, 3, __qtablewidgetitem44)
        __qtablewidgetitem45 = QTableWidgetItem()
        self.tableInformation.setItem(0, 4, __qtablewidgetitem45)
        __qtablewidgetitem46 = QTableWidgetItem()
        self.tableInformation.setItem(0, 5, __qtablewidgetitem46)
        __qtablewidgetitem47 = QTableWidgetItem()
        self.tableInformation.setItem(1, 0, __qtablewidgetitem47)
        self.tableInformation.setObjectName(u"tableInformation")
        sizePolicy4.setHeightForWidth(self.tableInformation.sizePolicy().hasHeightForWidth())
        self.tableInformation.setSizePolicy(sizePolicy4)
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Text, brush)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        brush6 = QBrush(QColor(0, 0, 0, 255))
        brush6.setStyle(Qt.NoBrush)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush6)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Active, QPalette.PlaceholderText, brush3)
#endif
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        brush7 = QBrush(QColor(0, 0, 0, 255))
        brush7.setStyle(Qt.NoBrush)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush7)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush3)
#endif
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        brush8 = QBrush(QColor(0, 0, 0, 255))
        brush8.setStyle(Qt.NoBrush)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush8)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush3)
#endif
        self.tableInformation.setPalette(palette1)
        self.tableInformation.setFrameShape(QFrame.Shape.NoFrame)
        self.tableInformation.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.tableInformation.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.tableInformation.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tableInformation.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.tableInformation.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tableInformation.setShowGrid(True)
        self.tableInformation.setGridStyle(Qt.PenStyle.SolidLine)
        self.tableInformation.setSortingEnabled(False)
        self.tableInformation.horizontalHeader().setVisible(False)
        self.tableInformation.horizontalHeader().setCascadingSectionResizes(True)
        self.tableInformation.horizontalHeader().setDefaultSectionSize(200)
        self.tableInformation.horizontalHeader().setStretchLastSection(True)
        self.tableInformation.verticalHeader().setVisible(False)
        self.tableInformation.verticalHeader().setCascadingSectionResizes(False)
        self.tableInformation.verticalHeader().setHighlightSections(False)
        self.tableInformation.verticalHeader().setStretchLastSection(True)

        self.horizontalLayout_8.addWidget(self.tableInformation)


        self.verticalLayout_16.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.btn_getDatabaseContent = QPushButton(self.verticalLayoutWidget_6)
        self.btn_getDatabaseContent.setObjectName(u"btn_getDatabaseContent")
        self.btn_getDatabaseContent.setMinimumSize(QSize(150, 30))
        self.btn_getDatabaseContent.setFont(font)
        self.btn_getDatabaseContent.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_getDatabaseContent.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.horizontalLayout_9.addWidget(self.btn_getDatabaseContent)

        self.btn_exportData = QPushButton(self.verticalLayoutWidget_6)
        self.btn_exportData.setObjectName(u"btn_exportData")
        self.btn_exportData.setMinimumSize(QSize(150, 30))
        self.btn_exportData.setFont(font)
        self.btn_exportData.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_exportData.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.horizontalLayout_9.addWidget(self.btn_exportData)


        self.verticalLayout_16.addLayout(self.horizontalLayout_9)

        self.stackedWidget.addWidget(self.dataCenter)
        self.autoInjection = QWidget()
        self.autoInjection.setObjectName(u"autoInjection")
        self.verticalLayoutWidget_3 = QWidget(self.autoInjection)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(20, 20, 701, 411))
        self.verticalLayout_10 = QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_10.setSpacing(12)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.url = QLineEdit(self.verticalLayoutWidget_3)
        self.url.setObjectName(u"url")
        self.url.setMinimumSize(QSize(0, 30))
        self.url.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.horizontalLayout_7.addWidget(self.url)

        self.browse = QPushButton(self.verticalLayoutWidget_3)
        self.browse.setObjectName(u"browse")
        self.browse.setMinimumSize(QSize(80, 30))
        self.browse.setFont(font)
        self.browse.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.browse.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.horizontalLayout_7.addWidget(self.browse)

        self.detection = QPushButton(self.verticalLayoutWidget_3)
        self.detection.setObjectName(u"detection")
        self.detection.setMinimumSize(QSize(80, 30))
        self.detection.setFont(font)
        self.detection.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.detection.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.horizontalLayout_7.addWidget(self.detection)


        self.verticalLayout_10.addLayout(self.horizontalLayout_7)

        self.webPage = QWebEngineView(self.verticalLayoutWidget_3)
        self.webPage.setObjectName(u"webPage")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.webPage.sizePolicy().hasHeightForWidth())
        self.webPage.setSizePolicy(sizePolicy6)
        self.webPage.setFocusPolicy(Qt.FocusPolicy.WheelFocus)
        self.webPage.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.webPage.setAutoFillBackground(False)
        self.webPage.setUrl(QUrl(u"about:blank"))

        self.verticalLayout_10.addWidget(self.webPage)

        self.stackedWidget.addWidget(self.autoInjection)
        self.fileOperation = QWidget()
        self.fileOperation.setObjectName(u"fileOperation")
        self.verticalLayoutWidget_2 = QWidget(self.fileOperation)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(20, 20, 701, 411))
        self.verticalLayout_5 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_5.setSpacing(10)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.path_2 = QLineEdit(self.verticalLayoutWidget_2)
        self.path_2.setObjectName(u"path_2")
        self.path_2.setMinimumSize(QSize(0, 30))
        self.path_2.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.gridLayout_5.addWidget(self.path_2, 0, 0, 1, 1)

        self.fileOperationType = QComboBox(self.verticalLayoutWidget_2)
        self.fileOperationType.addItem("")
        self.fileOperationType.addItem("")
        self.fileOperationType.setObjectName(u"fileOperationType")
        self.fileOperationType.setFont(font)
        self.fileOperationType.setAutoFillBackground(False)
        self.fileOperationType.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.fileOperationType.setIconSize(QSize(16, 16))
        self.fileOperationType.setFrame(True)

        self.gridLayout_5.addWidget(self.fileOperationType, 0, 1, 2, 1)

        self.path = QLineEdit(self.verticalLayoutWidget_2)
        self.path.setObjectName(u"path")
        self.path.setMinimumSize(QSize(0, 30))
        self.path.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.gridLayout_5.addWidget(self.path, 1, 0, 1, 1)

        self.btn_startFileOperation = QPushButton(self.verticalLayoutWidget_2)
        self.btn_startFileOperation.setObjectName(u"btn_startFileOperation")
        self.btn_startFileOperation.setMinimumSize(QSize(100, 30))
        self.btn_startFileOperation.setFont(font)
        self.btn_startFileOperation.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_startFileOperation.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.gridLayout_5.addWidget(self.btn_startFileOperation, 0, 2, 2, 1)


        self.verticalLayout_5.addLayout(self.gridLayout_5)

        self.fileOperationResults = QPlainTextEdit(self.verticalLayoutWidget_2)
        self.fileOperationResults.setObjectName(u"fileOperationResults")
        self.fileOperationResults.setMinimumSize(QSize(200, 200))
        self.fileOperationResults.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.fileOperationResults.setTextInteractionFlags(Qt.TextInteractionFlag.TextSelectableByKeyboard|Qt.TextInteractionFlag.TextSelectableByMouse)

        self.verticalLayout_5.addWidget(self.fileOperationResults)

        self.stackedWidget.addWidget(self.fileOperation)
        self.command = QWidget()
        self.command.setObjectName(u"command")
        self.verticalLayoutWidget = QWidget(self.command)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(20, 20, 701, 411))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setSpacing(18)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.commandInput = QLineEdit(self.verticalLayoutWidget)
        self.commandInput.setObjectName(u"commandInput")
        sizePolicy.setHeightForWidth(self.commandInput.sizePolicy().hasHeightForWidth())
        self.commandInput.setSizePolicy(sizePolicy)
        self.commandInput.setMinimumSize(QSize(0, 30))
        self.commandInput.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.horizontalLayout_6.addWidget(self.commandInput)

        self.echoResults = QCheckBox(self.verticalLayoutWidget)
        self.echoResults.setObjectName(u"echoResults")
        self.echoResults.setAutoFillBackground(False)
        self.echoResults.setStyleSheet(u"")

        self.horizontalLayout_6.addWidget(self.echoResults)

        self.btn_startCommand = QPushButton(self.verticalLayoutWidget)
        self.btn_startCommand.setObjectName(u"btn_startCommand")
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.btn_startCommand.sizePolicy().hasHeightForWidth())
        self.btn_startCommand.setSizePolicy(sizePolicy7)
        self.btn_startCommand.setMinimumSize(QSize(100, 30))
        self.btn_startCommand.setFont(font)
        self.btn_startCommand.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_startCommand.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.horizontalLayout_6.addWidget(self.btn_startCommand)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.commandResults = QPlainTextEdit(self.verticalLayoutWidget)
        self.commandResults.setObjectName(u"commandResults")
        self.commandResults.setMinimumSize(QSize(200, 200))
        self.commandResults.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.verticalLayout.addWidget(self.commandResults)

        self.stackedWidget.addWidget(self.command)
        self.logCenter = QWidget()
        self.logCenter.setObjectName(u"logCenter")
        self.verticalLayoutWidget_4 = QWidget(self.logCenter)
        self.verticalLayoutWidget_4.setObjectName(u"verticalLayoutWidget_4")
        self.verticalLayoutWidget_4.setGeometry(QRect(20, 20, 701, 411))
        self.verticalLayout_11 = QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.packetSendingRecord = QTableWidget(self.verticalLayoutWidget_4)
        if (self.packetSendingRecord.columnCount() < 5):
            self.packetSendingRecord.setColumnCount(5)
        __qtablewidgetitem48 = QTableWidgetItem()
        self.packetSendingRecord.setHorizontalHeaderItem(0, __qtablewidgetitem48)
        __qtablewidgetitem49 = QTableWidgetItem()
        self.packetSendingRecord.setHorizontalHeaderItem(1, __qtablewidgetitem49)
        __qtablewidgetitem50 = QTableWidgetItem()
        self.packetSendingRecord.setHorizontalHeaderItem(2, __qtablewidgetitem50)
        __qtablewidgetitem51 = QTableWidgetItem()
        self.packetSendingRecord.setHorizontalHeaderItem(3, __qtablewidgetitem51)
        __qtablewidgetitem52 = QTableWidgetItem()
        self.packetSendingRecord.setHorizontalHeaderItem(4, __qtablewidgetitem52)
        if (self.packetSendingRecord.rowCount() < 1):
            self.packetSendingRecord.setRowCount(1)
        __qtablewidgetitem53 = QTableWidgetItem()
        __qtablewidgetitem53.setFont(font4);
        self.packetSendingRecord.setVerticalHeaderItem(0, __qtablewidgetitem53)
        __qtablewidgetitem54 = QTableWidgetItem()
        self.packetSendingRecord.setItem(0, 0, __qtablewidgetitem54)
        __qtablewidgetitem55 = QTableWidgetItem()
        self.packetSendingRecord.setItem(0, 1, __qtablewidgetitem55)
        __qtablewidgetitem56 = QTableWidgetItem()
        self.packetSendingRecord.setItem(0, 2, __qtablewidgetitem56)
        __qtablewidgetitem57 = QTableWidgetItem()
        self.packetSendingRecord.setItem(0, 3, __qtablewidgetitem57)
        __qtablewidgetitem58 = QTableWidgetItem()
        self.packetSendingRecord.setItem(0, 4, __qtablewidgetitem58)
        self.packetSendingRecord.setObjectName(u"packetSendingRecord")
        sizePolicy4.setHeightForWidth(self.packetSendingRecord.sizePolicy().hasHeightForWidth())
        self.packetSendingRecord.setSizePolicy(sizePolicy4)
        palette2 = QPalette()
        palette2.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette2.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette2.setBrush(QPalette.Active, QPalette.Text, brush)
        palette2.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        brush9 = QBrush(QColor(0, 0, 0, 255))
        brush9.setStyle(Qt.NoBrush)
        palette2.setBrush(QPalette.Active, QPalette.Base, brush9)
        palette2.setBrush(QPalette.Active, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Active, QPalette.PlaceholderText, brush)
#endif
        palette2.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette2.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        brush10 = QBrush(QColor(0, 0, 0, 255))
        brush10.setStyle(Qt.NoBrush)
        palette2.setBrush(QPalette.Inactive, QPalette.Base, brush10)
        palette2.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush)
#endif
        palette2.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette2.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        brush11 = QBrush(QColor(0, 0, 0, 255))
        brush11.setStyle(Qt.NoBrush)
        palette2.setBrush(QPalette.Disabled, QPalette.Base, brush11)
        palette2.setBrush(QPalette.Disabled, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush)
#endif
        self.packetSendingRecord.setPalette(palette2)
        self.packetSendingRecord.setFrameShape(QFrame.Shape.NoFrame)
        self.packetSendingRecord.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.packetSendingRecord.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.packetSendingRecord.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.packetSendingRecord.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.packetSendingRecord.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.packetSendingRecord.setShowGrid(True)
        self.packetSendingRecord.setGridStyle(Qt.PenStyle.SolidLine)
        self.packetSendingRecord.setSortingEnabled(False)
        self.packetSendingRecord.setRowCount(1)
        self.packetSendingRecord.setColumnCount(5)
        self.packetSendingRecord.horizontalHeader().setVisible(False)
        self.packetSendingRecord.horizontalHeader().setCascadingSectionResizes(True)
        self.packetSendingRecord.horizontalHeader().setMinimumSectionSize(20)
        self.packetSendingRecord.horizontalHeader().setDefaultSectionSize(142)
        self.packetSendingRecord.horizontalHeader().setHighlightSections(True)
        self.packetSendingRecord.horizontalHeader().setProperty(u"showSortIndicator", False)
        self.packetSendingRecord.horizontalHeader().setStretchLastSection(False)
        self.packetSendingRecord.verticalHeader().setVisible(False)
        self.packetSendingRecord.verticalHeader().setCascadingSectionResizes(False)
        self.packetSendingRecord.verticalHeader().setHighlightSections(False)
        self.packetSendingRecord.verticalHeader().setStretchLastSection(True)

        self.verticalLayout_11.addWidget(self.packetSendingRecord)

        self.log = QPlainTextEdit(self.verticalLayoutWidget_4)
        self.log.setObjectName(u"log")
        self.log.setMinimumSize(QSize(200, 200))
        self.log.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.verticalLayout_11.addWidget(self.log)

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
        self.titleLeftApp.setText(QCoreApplication.translate("MainWindow", u"SQL\u6ce8\u5165\u5de5\u5177", None))
        self.titleLeftDescription.setText("")
        self.toggleButton.setText(QCoreApplication.translate("MainWindow", u"\u9690\u85cf\u83dc\u5355\u680f", None))
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"\u81ea\u52a8\u6ce8\u5165", None))
        self.btn_manualInjection.setText(QCoreApplication.translate("MainWindow", u"\u4eba\u5de5\u6ce8\u5165", None))
        self.btn_dataCenter.setText(QCoreApplication.translate("MainWindow", u"\u6570\u636e\u4e2d\u5fc3", None))
        self.btn_command.setText(QCoreApplication.translate("MainWindow", u"\u547d\u4ee4\u6267\u884c", None))
        self.btn_fileOperation.setText(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6\u64cd\u4f5c", None))
        self.btn_logCenter.setText(QCoreApplication.translate("MainWindow", u"\u65e5\u5fd7\u4e2d\u5fc3", None))
        self.btn_exit.setText(QCoreApplication.translate("MainWindow", u"\u9000\u51fa", None))
        self.titleRightInfo.setText(QCoreApplication.translate("MainWindow", u"\u7f51\u7edc\u5b89\u5168\u8bbe\u8ba1", None))
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
        self.requestMethod.setItemText(0, QCoreApplication.translate("MainWindow", u"GET", None))
        self.requestMethod.setItemText(1, QCoreApplication.translate("MainWindow", u"POST", None))
        self.requestMethod.setItemText(2, QCoreApplication.translate("MainWindow", u"PUT", None))
        self.requestMethod.setItemText(3, QCoreApplication.translate("MainWindow", u"DELETE", None))
        self.requestMethod.setItemText(4, QCoreApplication.translate("MainWindow", u"PATCH", None))
        self.requestMethod.setItemText(5, QCoreApplication.translate("MainWindow", u"HEAD", None))
        self.requestMethod.setItemText(6, QCoreApplication.translate("MainWindow", u"OPTIONS", None))

        self.requestMethod.setCurrentText(QCoreApplication.translate("MainWindow", u"GET", None))
        self.requestMethod.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u7f51\u9875\u8bf7\u6c42\u65b9\u5f0f", None))
        self.autoUrl.setText("")
        self.autoUrl.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u8bf7\u8f93\u5165\u8981\u6ce8\u5165\u7684\u7f51\u5740", None))
        self.https.setText(QCoreApplication.translate("MainWindow", u"HTTPS", None))
        self.btn_startInjection.setText(QCoreApplication.translate("MainWindow", u"\u8bc6\u522b\u6ce8\u5165", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"\u6ce8\u5165\u53c2\u6570", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u6ce8\u5165\u7c7b\u578b", None))
        self.injectionType.setItemText(0, QCoreApplication.translate("MainWindow", u"\u81ea\u52a8\u68c0\u6d4b", None))
        self.injectionType.setItemText(1, QCoreApplication.translate("MainWindow", u"\u5e03\u5c14\u76f2\u6ce8", None))
        self.injectionType.setItemText(2, QCoreApplication.translate("MainWindow", u"\u62a5\u9519\u6ce8\u5165", None))
        self.injectionType.setItemText(3, QCoreApplication.translate("MainWindow", u"\u5185\u8054\u6ce8\u5165", None))
        self.injectionType.setItemText(4, QCoreApplication.translate("MainWindow", u"\u5806\u53e0\u6ce8\u5165", None))
        self.injectionType.setItemText(5, QCoreApplication.translate("MainWindow", u"\u65f6\u95f4\u76f2\u6ce8", None))
        self.injectionType.setItemText(6, QCoreApplication.translate("MainWindow", u"\u8054\u5408\u6ce8\u5165", None))

        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u6570\u636e\u5e93", None))
        self.databaseType.setItemText(0, QCoreApplication.translate("MainWindow", u"\u81ea\u52a8\u68c0\u6d4b", None))
        self.databaseType.setItemText(1, QCoreApplication.translate("MainWindow", u"MySQL", None))
        self.databaseType.setItemText(2, QCoreApplication.translate("MainWindow", u"Access", None))
        self.databaseType.setItemText(3, QCoreApplication.translate("MainWindow", u"Oracle", None))
        self.databaseType.setItemText(4, QCoreApplication.translate("MainWindow", u"Microsoft SQL Server", None))
        self.databaseType.setItemText(5, QCoreApplication.translate("MainWindow", u"SAP MaxDB", None))
        self.databaseType.setItemText(6, QCoreApplication.translate("MainWindow", u"PostgreSQL", None))
        self.databaseType.setItemText(7, QCoreApplication.translate("MainWindow", u"SQLite", None))
        self.databaseType.setItemText(8, QCoreApplication.translate("MainWindow", u"Sybase", None))
        self.databaseType.setItemText(9, QCoreApplication.translate("MainWindow", u"Informix", None))
        self.databaseType.setItemText(10, QCoreApplication.translate("MainWindow", u"HSQLDB", None))
        self.databaseType.setItemText(11, QCoreApplication.translate("MainWindow", u"H2", None))
        self.databaseType.setItemText(12, QCoreApplication.translate("MainWindow", u"MonetDB", None))
        self.databaseType.setItemText(13, QCoreApplication.translate("MainWindow", u"Apache Derby", None))
        self.databaseType.setItemText(14, QCoreApplication.translate("MainWindow", u"Vertica", None))
        self.databaseType.setItemText(15, QCoreApplication.translate("MainWindow", u"Mckoi", None))
        self.databaseType.setItemText(16, QCoreApplication.translate("MainWindow", u"Presto", None))
        self.databaseType.setItemText(17, QCoreApplication.translate("MainWindow", u"Altibase", None))
        self.databaseType.setItemText(18, QCoreApplication.translate("MainWindow", u"MimerSQL", None))
        self.databaseType.setItemText(19, QCoreApplication.translate("MainWindow", u"ClickHouse", None))
        self.databaseType.setItemText(20, QCoreApplication.translate("MainWindow", u"CrateDB", None))
        self.databaseType.setItemText(21, QCoreApplication.translate("MainWindow", u"FrontBase", None))
        self.databaseType.setItemText(22, QCoreApplication.translate("MainWindow", u"Raima Database Manager", None))
        self.databaseType.setItemText(23, QCoreApplication.translate("MainWindow", u"Virtuoso", None))

        self.label_18.setText(QCoreApplication.translate("MainWindow", u"\u98ce\u9669\u7b49\u7ea7", None))
        self.injectionLevel.setItemText(0, QCoreApplication.translate("MainWindow", u"1", None))
        self.injectionLevel.setItemText(1, QCoreApplication.translate("MainWindow", u"2", None))
        self.injectionLevel.setItemText(2, QCoreApplication.translate("MainWindow", u"3", None))
        self.injectionLevel.setItemText(3, QCoreApplication.translate("MainWindow", u"4", None))
        self.injectionLevel.setItemText(4, QCoreApplication.translate("MainWindow", u"5", None))

        self.label_17.setText(QCoreApplication.translate("MainWindow", u"\u6ce8\u5165\u7b49\u7ea7", None))
        self.riskLevel.setItemText(0, QCoreApplication.translate("MainWindow", u"1", None))
        self.riskLevel.setItemText(1, QCoreApplication.translate("MainWindow", u"2", None))
        self.riskLevel.setItemText(2, QCoreApplication.translate("MainWindow", u"3", None))

        self.paramInput.setText("")
        self.paramInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u8bf7\u8f93\u5165\u6dfb\u52a0\u7684\u53c2\u6570\u540d", None))
        self.btn_addParam.setText(QCoreApplication.translate("MainWindow", u"\u6dfb\u52a0\u53c2\u6570", None))
        self.btn_deleteParam.setText(QCoreApplication.translate("MainWindow", u"\u5220\u9664\u53c2\u6570", None))
        ___qtablewidgetitem = self.databaseInformation.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem1 = self.databaseInformation.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem2 = self.databaseInformation.verticalHeaderItem(0)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem3 = self.databaseInformation.verticalHeaderItem(1)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem4 = self.databaseInformation.verticalHeaderItem(2)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem5 = self.databaseInformation.verticalHeaderItem(3)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem6 = self.databaseInformation.verticalHeaderItem(4)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem7 = self.databaseInformation.verticalHeaderItem(5)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem8 = self.databaseInformation.verticalHeaderItem(6)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem9 = self.databaseInformation.verticalHeaderItem(7)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"New Row", None));

        __sortingEnabled = self.databaseInformation.isSortingEnabled()
        self.databaseInformation.setSortingEnabled(False)
        ___qtablewidgetitem10 = self.databaseInformation.item(0, 0)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"\u4fe1\u606f", None));
        ___qtablewidgetitem11 = self.databaseInformation.item(0, 1)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"\u503c", None));
        ___qtablewidgetitem12 = self.databaseInformation.item(1, 0)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"\u6570\u636e\u5e93", None));
        ___qtablewidgetitem13 = self.databaseInformation.item(2, 0)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"\u7248\u672c", None));
        ___qtablewidgetitem14 = self.databaseInformation.item(3, 0)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"\u64cd\u4f5c\u7cfb\u7edf", None));
        ___qtablewidgetitem15 = self.databaseInformation.item(4, 0)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"\u4e3b\u673a\u540d", None));
        ___qtablewidgetitem16 = self.databaseInformation.item(5, 0)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"\u5f53\u524d\u7528\u6237", None));
        ___qtablewidgetitem17 = self.databaseInformation.item(6, 0)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"\u5f53\u524d\u6570\u636e\u5e93", None));
        ___qtablewidgetitem18 = self.databaseInformation.item(7, 0)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"\u6307\u7eb9", None));
        self.databaseInformation.setSortingEnabled(__sortingEnabled)

        self.btn_getData.setText(QCoreApplication.translate("MainWindow", u"\u83b7\u53d6\u6570\u636e\u5e93\u4fe1\u606f", None))
        ___qtablewidgetitem19 = self.tableInformation.horizontalHeaderItem(0)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem20 = self.tableInformation.horizontalHeaderItem(1)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem21 = self.tableInformation.horizontalHeaderItem(2)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem22 = self.tableInformation.horizontalHeaderItem(3)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem23 = self.tableInformation.horizontalHeaderItem(4)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"4", None));
        ___qtablewidgetitem24 = self.tableInformation.horizontalHeaderItem(5)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"5", None));
        ___qtablewidgetitem25 = self.tableInformation.verticalHeaderItem(0)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem26 = self.tableInformation.verticalHeaderItem(1)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem27 = self.tableInformation.verticalHeaderItem(2)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem28 = self.tableInformation.verticalHeaderItem(3)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem29 = self.tableInformation.verticalHeaderItem(4)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem30 = self.tableInformation.verticalHeaderItem(5)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem31 = self.tableInformation.verticalHeaderItem(6)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem32 = self.tableInformation.verticalHeaderItem(7)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem33 = self.tableInformation.verticalHeaderItem(8)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem34 = self.tableInformation.verticalHeaderItem(9)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem35 = self.tableInformation.verticalHeaderItem(10)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem36 = self.tableInformation.verticalHeaderItem(11)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem37 = self.tableInformation.verticalHeaderItem(12)
        ___qtablewidgetitem37.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem38 = self.tableInformation.verticalHeaderItem(13)
        ___qtablewidgetitem38.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem39 = self.tableInformation.verticalHeaderItem(14)
        ___qtablewidgetitem39.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem40 = self.tableInformation.verticalHeaderItem(15)
        ___qtablewidgetitem40.setText(QCoreApplication.translate("MainWindow", u"New Row", None));

        __sortingEnabled1 = self.tableInformation.isSortingEnabled()
        self.tableInformation.setSortingEnabled(False)
        self.tableInformation.setSortingEnabled(__sortingEnabled1)

        self.btn_getDatabaseContent.setText(QCoreApplication.translate("MainWindow", u"\u83b7\u53d6\u6570\u636e\u5e93\u5185\u5bb9", None))
        self.btn_exportData.setText(QCoreApplication.translate("MainWindow", u"\u5bfc\u51fa\u6570\u636e", None))
        self.url.setText("")
        self.url.setPlaceholderText(QCoreApplication.translate("MainWindow", u"URL", None))
        self.browse.setText(QCoreApplication.translate("MainWindow", u"\u6d4f\u89c8", None))
        self.detection.setText(QCoreApplication.translate("MainWindow", u"\u68c0\u6d4b", None))
        self.path_2.setText("")
        self.path_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u8bf7\u8f93\u5165\u8981\u8bfb\u53d6\u6216\u5199\u5165\u7684\u8def\u5f84", None))
        self.fileOperationType.setItemText(0, QCoreApplication.translate("MainWindow", u"\u8bfb\u53d6\u6587\u4ef6", None))
        self.fileOperationType.setItemText(1, QCoreApplication.translate("MainWindow", u"\u5199\u5165\u6587\u4ef6", None))

        self.path.setText("")
        self.path.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u8bf7\u8f93\u5165\u8981\u8bfb\u53d6\u6216\u5199\u5165\u7684\u8def\u5f84", None))
        self.btn_startFileOperation.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb", None))
        self.commandInput.setText("")
        self.commandInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u8bf7\u8f93\u5165\u547d\u4ee4", None))
        self.echoResults.setText(QCoreApplication.translate("MainWindow", u"\u56de\u663e\u7ed3\u679c", None))
        self.btn_startCommand.setText(QCoreApplication.translate("MainWindow", u"\u6267\u884c", None))
        ___qtablewidgetitem41 = self.packetSendingRecord.horizontalHeaderItem(0)
        ___qtablewidgetitem41.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem42 = self.packetSendingRecord.horizontalHeaderItem(1)
        ___qtablewidgetitem42.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem43 = self.packetSendingRecord.horizontalHeaderItem(2)
        ___qtablewidgetitem43.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem44 = self.packetSendingRecord.horizontalHeaderItem(3)
        ___qtablewidgetitem44.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem45 = self.packetSendingRecord.horizontalHeaderItem(4)
        ___qtablewidgetitem45.setText(QCoreApplication.translate("MainWindow", u"4", None));
        ___qtablewidgetitem46 = self.packetSendingRecord.verticalHeaderItem(0)
        ___qtablewidgetitem46.setText(QCoreApplication.translate("MainWindow", u"New Row", None));

        __sortingEnabled2 = self.packetSendingRecord.isSortingEnabled()
        self.packetSendingRecord.setSortingEnabled(False)
        ___qtablewidgetitem47 = self.packetSendingRecord.item(0, 0)
        ___qtablewidgetitem47.setText(QCoreApplication.translate("MainWindow", u"\u65f6\u95f4", None));
        ___qtablewidgetitem48 = self.packetSendingRecord.item(0, 1)
        ___qtablewidgetitem48.setText(QCoreApplication.translate("MainWindow", u"\u7f51\u7ad9", None));
        ___qtablewidgetitem49 = self.packetSendingRecord.item(0, 2)
        ___qtablewidgetitem49.setText(QCoreApplication.translate("MainWindow", u"\u7c7b\u578b", None));
        ___qtablewidgetitem50 = self.packetSendingRecord.item(0, 3)
        ___qtablewidgetitem50.setText(QCoreApplication.translate("MainWindow", u"Payload", None));
        ___qtablewidgetitem51 = self.packetSendingRecord.item(0, 4)
        ___qtablewidgetitem51.setText(QCoreApplication.translate("MainWindow", u"\u76f8\u4f3c\u5ea6", None));
        self.packetSendingRecord.setSortingEnabled(__sortingEnabled2)

        self.btn_message.setText(QCoreApplication.translate("MainWindow", u"\u6d88\u606f", None))
        self.btn_print.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5370", None))
        self.btn_logout.setText(QCoreApplication.translate("MainWindow", u"\u9000\u51fa", None))
        self.creditsLabel.setText("")
        self.version.setText(QCoreApplication.translate("MainWindow", u"v1.0.0", None))
    # retranslateUi

