# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sinhr_window.ui'
##
## Created by: Qt User Interface Compiler version 6.12.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QCheckBox, QFrame,
    QHBoxLayout, QHeaderView, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QTabWidget, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)
import login_res_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1172, 673)
        MainWindow.setStyleSheet(u"#centralwidget { background-color: #F5F0E8; }\n"
"#headerFrame { background-color: #2C2A26; border: none; }\n"
"#headerFrame QLabel { color: #F5F0E8; }\n"
"#logout_btn { background-color: transparent; color: #F5F0E8; border: 1px solid rgba(255, 255, 255, 0.25); padding: 3px 10px; font-size: 12px; border-radius: 4px; }\n"
"#logout_btn:hover { background-color: rgba(255, 255, 255, 0.08); border: 1px solid rgba(255, 255, 255, 0.4); }\n"
"#logout_btn:pressed { background-color: rgba(255, 255, 255, 0.12); border: 1px solid rgba(255, 255, 255, 0.5); }\n"
"#formCard { background-color: #FFFFFF; border: 1px solid #D4CBBE; border-radius: 4px; }\n"
"#lbl_form_title { font-size: 16px; font-weight: 600; color: #2C2A26; }\n"
"#lbl_status { font-size: 12px; }\n"
"#lbl_queue_title { font-size: 11px; font-weight: 600; color: #6B6560; }\n"
"QCheckBox { spacing: 6px; font-size: 12px; color: #6B6560; background: transparent; }\n"
"QCheckBox::indicator { width: 15px; height: 15px; border-radius: 3px; border: 1px solid #D4CBBE; ba"
                        "ckground-color: #FFFFFF; }\n"
"QCheckBox::indicator:hover { border: 1px solid #B8AE9E; }\n"
"QCheckBox::indicator:checked { background-color: #4A6741; border: 1px solid #4A6741; }\n"
"QCheckBox::indicator:disabled { background-color: #E5DFD4; border: 1px solid #E5DFD4; }\n"
"QCheckBox:disabled { color: #A39E94; }\n"
"QHeaderView { background-color: #EDE6D9; }\n"
"QHeaderView::section { background-color: #EDE6D9; color: #6B6560; font-size: 11px; font-weight: 600; border: none; border-bottom: 1px solid #D4CBBE; padding: 7px 10px; }\n"
"QHeaderView::section:vertical { background-color: #EDE6D9; color: #6B6560; border: none; padding: 4px 6px; }\n"
"QTableWidget QHeaderView::section:vertical { background-color: #EDE6D9; color: #6B6560; border: none; padding: 4px 6px; }\n"
"QTableCornerButton::section { background-color: #EDE6D9; border: none; }\n"
"QTableWidget { background-color: #FFFFFF; border: 1px solid #D4CBBE; outline: none; }\n"
"QTableWidget::item { border-bottom: 1px solid #E0DCD3; padding: 7px 10px; color"
                        ": #2C2A26; font-size: 12px; }\n"
"QTableWidget::item:hover { background-color: #EDE6D9; }\n"
"#btn_sync { background-color: #4A6741; color: #FFFFFF; border: none; padding: 11px 16px; font-size: 14px; font-weight: 600; border-radius: 4px; }\n"
"#btn_sync:hover { background-color: #3D5636; }\n"
"#btn_sync:pressed { background-color: #334A2E; }\n"
"#btn_sync:disabled { background-color: #A8B5A0; }\n"
"#btn_sync:focus { border: 1px dashed #4A6741; }\n"
"#offlineBanner { background-color: #F0EEEA; border: 1px solid #D4CBBE; border-radius: 4px; }\n"
"#offlineBanner QLabel { font-size: 12px; color: #6B6560; }\n"
"#offlineDot { background-color: #A39E94; border-radius: 4px; min-width: 8px; max-width: 8px; min-height: 8px; max-height: 8px; }\n"
"#lblLoadingTitle { font-size: 14px; color: #6B6560; }\n"
"#lblLoadingSub { font-size: 12px; color: #A39E94; }\n"
"#lblEmptyTitle { font-size: 14px; color: #6B6560; }\n"
"#lblEmptySub { font-size: 12px; color: #A39E94; }\n"
"#errorFrame { background-color: #FFFFFF; border: 1px s"
                        "olid #B54A3A; border-radius: 4px; }\n"
"#errorFrame QLabel { font-size: 14px; color: #B54A3A; }\n"
"#btnRetry { background-color: #FFFFFF; color: #2C2A26; border: 1px solid #D4CBBE; border-radius: 4px; padding: 6px 16px; font-size: 12px; }\n"
"#btnRetry:hover { border: 1px solid #4A6741; background-color: #F5F0E8; }\n"
"QTabWidget::panel { border: none; background-color: #FFFFFF; }\n"
"QTabBar { background-color: #FFFFFF; border: none; qproperty-drawBase: 0; qproperty-expanding: true; }\n"
"QTabBar::tab { height: 40px; background-color: #FFFFFF; color: #6B6560; font-size: 12px; font-weight: normal; padding: 0px 30px; border: none; border-bottom: 2px solid transparent; border-top: 1px solid #D4CBBE; text-align: center; }\n"
"QTabBar::tab:hover { color: #2C2A26; }\n"
"QTabBar::tab:selected { color: #2C2A26; font-weight: 600; border-bottom: 2px solid #4A6741; }")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.headerFrame = QFrame(self.centralwidget)
        self.headerFrame.setObjectName(u"headerFrame")
        self.headerFrame.setMinimumSize(QSize(0, 40))
        self.headerFrame.setMaximumSize(QSize(16777215, 40))
        self.horizontalLayout = QHBoxLayout(self.headerFrame)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(15, 0, 15, 0)
        self.logo = QPushButton(self.headerFrame)
        self.logo.setObjectName(u"logo")
        self.logo.setMinimumSize(QSize(22, 22))
        self.logo.setMaximumSize(QSize(22, 22))
        self.logo.setStyleSheet(u"QPushButton { background: transparent; margin-right: 12px; border: none; }")
        icon = QIcon()
        icon.addFile(u":/login/icons/logo.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.logo.setIcon(icon)
        self.logo.setIconSize(QSize(18, 18))

        self.horizontalLayout.addWidget(self.logo)

        self.name = QLabel(self.headerFrame)
        self.name.setObjectName(u"name")
        self.name.setStyleSheet(u"font-size: 13px; font-weight: bold; margin-right: 15px;")

        self.horizontalLayout.addWidget(self.name)

        self.name_chart = QLabel(self.headerFrame)
        self.name_chart.setObjectName(u"name_chart")
        self.name_chart.setStyleSheet(u"font-size: 13px; margin-right: 10px;")

        self.horizontalLayout.addWidget(self.name_chart)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.status_lb = QLabel(self.headerFrame)
        self.status_lb.setObjectName(u"status_lb")
        self.status_lb.setMinimumSize(QSize(7, 7))
        self.status_lb.setMaximumSize(QSize(7, 7))
        self.status_lb.setStyleSheet(u"background-color: #4A6741; border-radius: 3px; border: none;")

        self.horizontalLayout.addWidget(self.status_lb)

        self.role_lb = QLabel(self.headerFrame)
        self.role_lb.setObjectName(u"role_lb")
        self.role_lb.setStyleSheet(u"font-size: 12px; margin-right: 15px;")

        self.horizontalLayout.addWidget(self.role_lb)

        self.logout_btn = QPushButton(self.headerFrame)
        self.logout_btn.setObjectName(u"logout_btn")
        self.logout_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout.addWidget(self.logout_btn)


        self.verticalLayout.addWidget(self.headerFrame)

        self.centerLayout = QHBoxLayout()
        self.centerLayout.setSpacing(0)
        self.centerLayout.setObjectName(u"centerLayout")
        self.centerLayout.setContentsMargins(24, 24, 24, 24)
        self.leftSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.centerLayout.addItem(self.leftSpacer)

        self.formCard = QFrame(self.centralwidget)
        self.formCard.setObjectName(u"formCard")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.formCard.sizePolicy().hasHeightForWidth())
        self.formCard.setSizePolicy(sizePolicy)
        self.formCard.setMinimumSize(QSize(640, 0))
        self.formCard.setMaximumSize(QSize(640, 16777215))
        self.formLayout = QVBoxLayout(self.formCard)
        self.formLayout.setSpacing(14)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(24, 24, 24, 24)
        self.lbl_form_title = QLabel(self.formCard)
        self.lbl_form_title.setObjectName(u"lbl_form_title")

        self.formLayout.addWidget(self.lbl_form_title, 0, Qt.AlignHCenter)

        self.offlineBanner = QFrame(self.formCard)
        self.offlineBanner.setObjectName(u"offlineBanner")
        self.offlineBanner.setVisible(False)
        self.offlineLayout = QHBoxLayout(self.offlineBanner)
        self.offlineLayout.setSpacing(8)
        self.offlineLayout.setObjectName(u"offlineLayout")
        self.offlineLayout.setContentsMargins(12, 8, 12, 8)
        self.offlineDot = QLabel(self.offlineBanner)
        self.offlineDot.setObjectName(u"offlineDot")

        self.offlineLayout.addWidget(self.offlineDot)

        self.lbl_offline = QLabel(self.offlineBanner)
        self.lbl_offline.setObjectName(u"lbl_offline")

        self.offlineLayout.addWidget(self.lbl_offline)

        self.offlineSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.offlineLayout.addItem(self.offlineSpacer)


        self.formLayout.addWidget(self.offlineBanner)

        self.lbl_status = QLabel(self.formCard)
        self.lbl_status.setObjectName(u"lbl_status")

        self.formLayout.addWidget(self.lbl_status)

        self.lbl_queue_title = QLabel(self.formCard)
        self.lbl_queue_title.setObjectName(u"lbl_queue_title")

        self.formLayout.addWidget(self.lbl_queue_title)

        self.checkboxesLayout = QVBoxLayout()
        self.checkboxesLayout.setSpacing(8)
        self.checkboxesLayout.setObjectName(u"checkboxesLayout")
        self.chkGeodata = QCheckBox(self.formCard)
        self.chkGeodata.setObjectName(u"chkGeodata")

        self.checkboxesLayout.addWidget(self.chkGeodata)

        self.chkWeather = QCheckBox(self.formCard)
        self.chkWeather.setObjectName(u"chkWeather")

        self.checkboxesLayout.addWidget(self.chkWeather)

        self.chkDescriptions = QCheckBox(self.formCard)
        self.chkDescriptions.setObjectName(u"chkDescriptions")

        self.checkboxesLayout.addWidget(self.chkDescriptions)


        self.formLayout.addLayout(self.checkboxesLayout)

        self.stateStack = QStackedWidget(self.formCard)
        self.stateStack.setObjectName(u"stateStack")
        self.pageNormal = QWidget()
        self.pageNormal.setObjectName(u"pageNormal")
        self.normalLayout = QVBoxLayout(self.pageNormal)
        self.normalLayout.setObjectName(u"normalLayout")
        self.normalLayout.setContentsMargins(0, 0, 0, 0)
        self.tableQueue = QTableWidget(self.pageNormal)
        if (self.tableQueue.columnCount() < 3):
            self.tableQueue.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableQueue.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableQueue.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableQueue.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.tableQueue.setObjectName(u"tableQueue")
        self.tableQueue.setMinimumSize(QSize(0, 150))
        self.tableQueue.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.tableQueue.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tableQueue.setShowGrid(False)
        self.tableQueue.horizontalHeader().setStretchLastSection(True)

        self.normalLayout.addWidget(self.tableQueue)

        self.stateStack.addWidget(self.pageNormal)
        self.pageLoading = QWidget()
        self.pageLoading.setObjectName(u"pageLoading")
        self.loadingLayout = QVBoxLayout(self.pageLoading)
        self.loadingLayout.setObjectName(u"loadingLayout")
        self.loadingLayout.setContentsMargins(0, 0, 0, 0)
        self.loadingSpacerTop = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.loadingLayout.addItem(self.loadingSpacerTop)

        self.lblLoadingTitle = QLabel(self.pageLoading)
        self.lblLoadingTitle.setObjectName(u"lblLoadingTitle")

        self.loadingLayout.addWidget(self.lblLoadingTitle, 0, Qt.AlignHCenter)

        self.lblLoadingSub = QLabel(self.pageLoading)
        self.lblLoadingSub.setObjectName(u"lblLoadingSub")

        self.loadingLayout.addWidget(self.lblLoadingSub, 0, Qt.AlignHCenter)

        self.loadingSpacerBottom = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.loadingLayout.addItem(self.loadingSpacerBottom)

        self.stateStack.addWidget(self.pageLoading)
        self.pageEmpty = QWidget()
        self.pageEmpty.setObjectName(u"pageEmpty")
        self.emptyLayout = QVBoxLayout(self.pageEmpty)
        self.emptyLayout.setObjectName(u"emptyLayout")
        self.emptyLayout.setContentsMargins(0, 0, 0, 0)
        self.emptySpacerTop = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.emptyLayout.addItem(self.emptySpacerTop)

        self.lblEmptyTitle = QLabel(self.pageEmpty)
        self.lblEmptyTitle.setObjectName(u"lblEmptyTitle")

        self.emptyLayout.addWidget(self.lblEmptyTitle, 0, Qt.AlignHCenter)

        self.lblEmptySub = QLabel(self.pageEmpty)
        self.lblEmptySub.setObjectName(u"lblEmptySub")

        self.emptyLayout.addWidget(self.lblEmptySub, 0, Qt.AlignHCenter)

        self.emptySpacerBottom = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.emptyLayout.addItem(self.emptySpacerBottom)

        self.stateStack.addWidget(self.pageEmpty)
        self.pageError = QWidget()
        self.pageError.setObjectName(u"pageError")
        self.errorLayout = QVBoxLayout(self.pageError)
        self.errorLayout.setObjectName(u"errorLayout")
        self.errorLayout.setContentsMargins(0, 0, 0, 0)
        self.errorSpacerTop = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.errorLayout.addItem(self.errorSpacerTop)

        self.errorFrame = QFrame(self.pageError)
        self.errorFrame.setObjectName(u"errorFrame")
        self.errorFrameLayout = QVBoxLayout(self.errorFrame)
        self.errorFrameLayout.setSpacing(12)
        self.errorFrameLayout.setObjectName(u"errorFrameLayout")
        self.errorFrameLayout.setContentsMargins(24, 16, 24, 16)
        self.lblErrorMessage = QLabel(self.errorFrame)
        self.lblErrorMessage.setObjectName(u"lblErrorMessage")

        self.errorFrameLayout.addWidget(self.lblErrorMessage, 0, Qt.AlignHCenter)

        self.btnRetry = QPushButton(self.errorFrame)
        self.btnRetry.setObjectName(u"btnRetry")
        self.btnRetry.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.errorFrameLayout.addWidget(self.btnRetry, 0, Qt.AlignHCenter)


        self.errorLayout.addWidget(self.errorFrame, 0, Qt.AlignHCenter)

        self.errorSpacerBottom = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.errorLayout.addItem(self.errorSpacerBottom)

        self.stateStack.addWidget(self.pageError)

        self.formLayout.addWidget(self.stateStack)

        self.btn_sync = QPushButton(self.formCard)
        self.btn_sync.setObjectName(u"btn_sync")
        self.btn_sync.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.formLayout.addWidget(self.btn_sync, 0, Qt.AlignmentFlag.AlignLeft)


        self.centerLayout.addWidget(self.formCard)

        self.rightSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.centerLayout.addItem(self.rightSpacer)


        self.verticalLayout.addLayout(self.centerLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(1)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy1)
        self.tabWidget.setMinimumSize(QSize(0, 44))
        self.tabWidget.setMaximumSize(QSize(16777215, 44))
        self.tabWidget.setTabPosition(QTabWidget.TabPosition.North)
        self.tabWidget.setUsesScrollButtons(False)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setDocumentMode(True)
        self.tab_8 = QWidget()
        self.tab_8.setObjectName(u"tab_8")
        self.tabWidget.addTab(self.tab_8, "")
        self.tab_9 = QWidget()
        self.tab_9.setObjectName(u"tab_9")
        self.tabWidget.addTab(self.tab_9, "")
        self.tab_10 = QWidget()
        self.tab_10.setObjectName(u"tab_10")
        self.tabWidget.addTab(self.tab_10, "")
        self.tab_11 = QWidget()
        self.tab_11.setObjectName(u"tab_11")
        self.tabWidget.addTab(self.tab_11, "")
        self.tab_12 = QWidget()
        self.tab_12.setObjectName(u"tab_12")
        self.tabWidget.addTab(self.tab_12, "")
        self.tab_13 = QWidget()
        self.tab_13.setObjectName(u"tab_13")
        self.tabWidget.addTab(self.tab_13, "")
        self.tab_14 = QWidget()
        self.tab_14.setObjectName(u"tab_14")
        self.tabWidget.addTab(self.tab_14, "")

        self.verticalLayout.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stateStack.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"SynchronizationWindow", None))
        self.logo.setText("")
        self.name.setText(QCoreApplication.translate("MainWindow", u"\u041b\u0435\u0433\u0435\u043d\u0434\u044b \u041f\u0430\u0440\u043c\u044b", None))
        self.name_chart.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0438\u043d\u0445\u0440\u043e\u043d\u0438\u0437\u0430\u0446\u0438\u044f", None))
        self.status_lb.setText("")
        self.role_lb.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044c", None))
        self.logout_btn.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0439\u0442\u0438", None))
        self.lbl_form_title.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0438\u043d\u0445\u0440\u043e\u043d\u0438\u0437\u0430\u0446\u0438\u044f", None))
        self.offlineDot.setText("")
        self.lbl_offline.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0444\u043b\u0430\u0439\u043d \u2014 \u0434\u0430\u043d\u043d\u044b\u0435 \u0438\u0437 \u043a\u0435\u0448\u0430", None))
        self.lbl_status.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#6B6560;\">\u0421\u0442\u0430\u0442\u0443\u0441:</span> <span style=\" color:#2C2A26;\">\u0413\u043e\u0442\u043e\u0432\u043e \u043a \u0441\u0438\u043d\u0445\u0440\u043e\u043d\u0438\u0437\u0430\u0446\u0438\u0438</span><br/><span style=\" color:#A39E94; font-size:11px;\">\u041f\u043e\u0441\u043b\u0435\u0434\u043d\u044f\u044f \u0441\u0438\u043d\u0445\u0440\u043e\u043d\u0438\u0437\u0430\u0446\u0438\u044f: \u2014</span></p></body></html>", None))
        self.lbl_queue_title.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0427\u0415\u0420\u0415\u0414\u042c \u0417\u0410\u041f\u0420\u041e\u0421\u041e\u0412", None))
        self.chkGeodata.setText(QCoreApplication.translate("MainWindow", u"\u0413\u0435\u043e\u0434\u0430\u043d\u043d\u044b\u0435 (OSM/Overpass)", None))
        self.chkWeather.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0433\u043e\u0434\u0430 (OpenWeather)", None))
        self.chkDescriptions.setText(QCoreApplication.translate("MainWindow", u"\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u044f (Wikipedia)", None))
        ___qtablewidgetitem = self.tableQueue.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0435\u0440\u0432\u0438\u0441", None))
        ___qtablewidgetitem1 = self.tableQueue.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u044a\u0435\u043a\u0442", None))
        ___qtablewidgetitem2 = self.tableQueue.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0430\u0442\u0443\u0441", None))
        self.lblLoadingTitle.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0433\u0440\u0443\u0437\u043a\u0430...", None))
        self.lblLoadingSub.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043d\u0434\u0438\u043a\u0430\u0442\u043e\u0440 \u043f\u0440\u043e\u0433\u0440\u0435\u0441\u0441\u0430", None))
        self.lblEmptyTitle.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0438\u0447\u0435\u0433\u043e \u043d\u0435 \u043d\u0430\u0439\u0434\u0435\u043d\u043e", None))
        self.lblEmptySub.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u0435 \u0444\u0438\u043b\u044c\u0442\u0440\u044b", None))
        self.lblErrorMessage.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0448\u0438\u0431\u043a\u0430 \u043f\u043e\u0434\u043a\u043b\u044e\u0447\u0435\u043d\u0438\u044f \u043a \u0411\u0414", None))
        self.btnRetry.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0432\u0442\u043e\u0440\u0438\u0442\u044c", None))
        self.btn_sync.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0438\u043d\u0445\u0440\u043e\u043d\u0438\u0437\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u0441\u0435\u0439\u0447\u0430\u0441", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_8), QCoreApplication.translate("MainWindow", u"\u041a\u0430\u0442\u0430\u043b\u043e\u0433 \u043c\u0430\u0440\u0448\u0440\u0443\u0442\u043e\u0432", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_9), QCoreApplication.translate("MainWindow", u"\u0422\u0443\u0440\u044b", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_10), QCoreApplication.translate("MainWindow", u"\u0418\u043c\u043f\u043e\u0440\u0442 \u0438 \u044d\u043a\u0441\u043f\u043e\u0440\u0442", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_11), QCoreApplication.translate("MainWindow", u"\u0421\u0438\u043d\u0445\u0440\u043e\u043d\u0438\u0437\u0430\u0446\u0438\u044f", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_12), QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u0438", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_13), QCoreApplication.translate("MainWindow", u"\u0416\u0443\u0440\u043d\u0430\u043b \u0430\u0443\u0434\u0438\u0442\u0430", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_14), QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438 API \u0438 \u043a\u0435\u0448", None))
    # retranslateUi

