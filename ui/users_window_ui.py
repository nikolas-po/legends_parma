# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'users_window.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QFrame, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
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
"#leftPanel { background-color: #FFFFFF; border-right: 1px solid #D4CBBE; }\n"
"#lbl_selected_title { font-size: 14px; font-weight: 600; color: #2C2A26; }\n"
"#lbl_selected_desc { font-size: 12px; color: #6B6560; }\n"
"#btn_change_role { background-color: #FFFFFF; color: #2C2A26; border: 1px solid #D4CBBE; padding: 3px 9px; font-size: 12px; border-radius: 4px; }\n"
"#btn_change_role:hover { background-color: #F5F0E8; border: 1px solid #4A6741; }\n"
"#btn_change_role"
                        ":disabled { background-color: #FFFFFF; color: #A39E94; border: 1px solid #E5DFD4; }\n"
"#btn_change_role:focus { border: 1px dashed #4A6741; }\n"
"#btn_block { background-color: #FFFFFF; color: #B54A3A; border: 1px solid #B54A3A; padding: 3px 9px; font-size: 12px; border-radius: 4px; }\n"
"#btn_block:hover { background-color: #F5E8E6; }\n"
"#btn_block:pressed { background-color: #EBD5D1; }\n"
"#btn_block:disabled { background-color: #FFFFFF; color: #D4A39C; border: 1px solid #E5C4BF; }\n"
"#btn_block:focus { border: 1px dashed #4A6741; }\n"
"#rightPanel { background-color: #FFFFFF; }\n"
"QHeaderView { background-color: #EDE6D9; }\n"
"QHeaderView::section { background-color: #EDE6D9; color: #6B6560; font-size: 11px; font-weight: 600; border: none; border-bottom: 1px solid #D4CBBE; border-right: 1px solid #D4CBBE; padding: 7px 10px; text-align: left; }\n"
"QHeaderView::section:vertical { background-color: #EDE6D9; color: #6B6560; border: none; padding: 4px 6px; }\n"
"QTableWidget { background-color: #FFFFFF; bor"
                        "der: none; outline: none; gridline-color: transparent; }\n"
"QTableWidget::item { border-bottom: 1px solid #E0DCD3; padding: 7px 10px; color: #2C2A26; font-size: 12px; }\n"
"QTableWidget::item:hover { background-color: #EDE6D9; }\n"
"QTableWidget::item:selected { background-color: #E8EDE4; color: #2C2A26; }\n"
"#searchFrame { border-top: 1px solid #D4CBBE; background-color: #FFFFFF; }\n"
"#searchInput { padding: 4px 8px; font-size: 12px; border-radius: 4px; border: 1px solid #D4CBBE; background-color: #FFFFFF; color: #2C2A26; min-width: 160px; max-width: 240px; }\n"
"#searchInput:hover { border: 1px solid #B8AE9E; }\n"
"#searchInput:focus { border: 1px solid #4A6741; }\n"
"#searchInput[error=\"true\"] { border: 1px solid #B54A3A; }\n"
"#searchInput:disabled { border: 1px dashed #D4CBBE; color: #A39E94; background-color: #F5F0E8; }\n"
"#offlineBanner { background-color: #F0EEEA; border: 1px solid #D4CBBE; border-radius: 4px; }\n"
"#offlineBanner QLabel { font-size: 12px; color: #6B6560; }\n"
"#offlineDot { back"
                        "ground-color: #A39E94; border-radius: 4px; min-width: 8px; max-width: 8px; min-height: 8px; max-height: 8px; }\n"
"#lblLoadingTitle { font-size: 14px; color: #6B6560; }\n"
"#lblLoadingSub { font-size: 12px; color: #A39E94; }\n"
"#lblEmptyTitle { font-size: 14px; color: #6B6560; }\n"
"#lblEmptySub { font-size: 12px; color: #A39E94; }\n"
"#errorFrame { background-color: #FFFFFF; border: 1px solid #B54A3A; border-radius: 4px; }\n"
"#errorFrame QLabel { font-size: 14px; color: #B54A3A; }\n"
"#btnRetry { background-color: #FFFFFF; color: #2C2A26; border: 1px solid #D4CBBE; border-radius: 4px; padding: 6px 16px; font-size: 12px; }\n"
"#btnRetry:hover { border: 1px solid #4A6741; background-color: #F5F0E8; }\n"
"QTabWidget::panel { border: none; background-color: #FFFFFF; }\n"
"QTabBar { background-color: #FFFFFF; border: none; qproperty-drawBase: 0; qproperty-expanding: true; }\n"
"QTabBar::tab { height: 40px; background-color: #FFFFFF; color: #6B6560; font-size: 12px; font-weight: normal; padding: 0px 30px; border:"
                        " none; border-bottom: 2px solid transparent; border-top: 1px solid #D4CBBE; text-align: center; }\n"
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

        self.mainLayout = QHBoxLayout()
        self.mainLayout.setSpacing(0)
        self.mainLayout.setObjectName(u"mainLayout")
        self.mainLayout.setContentsMargins(0, 0, 0, 0)
        self.leftPanel = QFrame(self.centralwidget)
        self.leftPanel.setObjectName(u"leftPanel")
        self.leftPanel.setMinimumSize(QSize(280, 0))
        self.leftPanel.setMaximumSize(QSize(280, 16777215))
        self.leftLayout = QVBoxLayout(self.leftPanel)
        self.leftLayout.setSpacing(12)
        self.leftLayout.setObjectName(u"leftLayout")
        self.leftLayout.setContentsMargins(14, 14, 14, 14)
        self.lbl_selected_title = QLabel(self.leftPanel)
        self.lbl_selected_title.setObjectName(u"lbl_selected_title")

        self.leftLayout.addWidget(self.lbl_selected_title)

        self.lbl_selected_desc = QLabel(self.leftPanel)
        self.lbl_selected_desc.setObjectName(u"lbl_selected_desc")

        self.leftLayout.addWidget(self.lbl_selected_desc)

        self.btn_change_role = QPushButton(self.leftPanel)
        self.btn_change_role.setObjectName(u"btn_change_role")
        self.btn_change_role.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.leftLayout.addWidget(self.btn_change_role)

        self.btn_block = QPushButton(self.leftPanel)
        self.btn_block.setObjectName(u"btn_block")
        self.btn_block.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.leftLayout.addWidget(self.btn_block)

        self.leftSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.leftLayout.addItem(self.leftSpacer)


        self.mainLayout.addWidget(self.leftPanel)

        self.rightPanel = QFrame(self.centralwidget)
        self.rightPanel.setObjectName(u"rightPanel")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rightPanel.sizePolicy().hasHeightForWidth())
        self.rightPanel.setSizePolicy(sizePolicy)
        self.rightLayout = QVBoxLayout(self.rightPanel)
        self.rightLayout.setSpacing(0)
        self.rightLayout.setObjectName(u"rightLayout")
        self.rightLayout.setContentsMargins(12, 12, 12, 12)
        self.offlineBanner = QFrame(self.rightPanel)
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


        self.rightLayout.addWidget(self.offlineBanner)

        self.stateStack = QStackedWidget(self.rightPanel)
        self.stateStack.setObjectName(u"stateStack")
        self.pageNormal = QWidget()
        self.pageNormal.setObjectName(u"pageNormal")
        self.normalLayout = QVBoxLayout(self.pageNormal)
        self.normalLayout.setObjectName(u"normalLayout")
        self.normalLayout.setContentsMargins(0, 0, 0, 0)
        self.userTable = QTableWidget(self.pageNormal)
        if (self.userTable.columnCount() < 5):
            self.userTable.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.userTable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.userTable.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.userTable.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.userTable.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.userTable.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.userTable.setObjectName(u"userTable")
        self.userTable.setFrameShape(QFrame.Shape.NoFrame)
        self.userTable.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.userTable.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.userTable.setShowGrid(False)
        self.userTable.horizontalHeader().setStretchLastSection(True)

        self.normalLayout.addWidget(self.userTable)

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

        self.rightLayout.addWidget(self.stateStack)

        self.searchFrame = QFrame(self.rightPanel)
        self.searchFrame.setObjectName(u"searchFrame")
        self.searchFrame.setMinimumSize(QSize(0, 50))
        self.searchFrame.setMaximumSize(QSize(16777215, 50))
        self.searchLayout = QHBoxLayout(self.searchFrame)
        self.searchLayout.setSpacing(12)
        self.searchLayout.setObjectName(u"searchLayout")
        self.searchLayout.setContentsMargins(14, 0, 14, 0)
        self.searchInput = QLineEdit(self.searchFrame)
        self.searchInput.setObjectName(u"searchInput")

        self.searchLayout.addWidget(self.searchInput)

        self.searchSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.searchLayout.addItem(self.searchSpacer)


        self.rightLayout.addWidget(self.searchFrame)


        self.mainLayout.addWidget(self.rightPanel)


        self.verticalLayout.addLayout(self.mainLayout)

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
        self.tabWidget.setCurrentIndex(4)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"UsersWindow", None))
        self.logo.setText("")
        self.name.setText(QCoreApplication.translate("MainWindow", u"\u041b\u0435\u0433\u0435\u043d\u0434\u044b \u041f\u0430\u0440\u043c\u044b", None))
        self.name_chart.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u0438", None))
        self.status_lb.setText("")
        self.role_lb.setText(QCoreApplication.translate("MainWindow", u"\u0410\u0434\u043c\u0438\u043d\u0438\u0441\u0442\u0440\u0430\u0442\u043e\u0440", None))
        self.logout_btn.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0439\u0442\u0438", None))
        self.lbl_selected_title.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0440\u0430\u043d\u043d\u044b\u0439 \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044c", None))
        self.lbl_selected_desc.setText(QCoreApplication.translate("MainWindow", u"\u0420\u043e\u043b\u044c: \u041f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044c / \u0410\u0434\u043c\u0438\u043d\u0438\u0441\u0442\u0440\u0430\u0442\u043e\u0440", None))
        self.btn_change_role.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c \u0440\u043e\u043b\u044c", None))
        self.btn_block.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0431\u043b\u043e\u043a\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.offlineDot.setText("")
        self.lbl_offline.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0444\u043b\u0430\u0439\u043d \u2014 \u0434\u0430\u043d\u043d\u044b\u0435 \u0438\u0437 \u043a\u0435\u0448\u0430", None))
        ___qtablewidgetitem = self.userTable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u041b\u043e\u0433\u0438\u043d", None))
        ___qtablewidgetitem1 = self.userTable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043c\u044f", None))
        ___qtablewidgetitem2 = self.userTable.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\u0420\u043e\u043b\u044c", None))
        ___qtablewidgetitem3 = self.userTable.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0430\u0442\u0443\u0441", None))
        ___qtablewidgetitem4 = self.userTable.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0441\u043b\u0435\u0434\u043d\u0438\u0439 \u0432\u0445\u043e\u0434", None))
        self.lblLoadingTitle.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0433\u0440\u0443\u0437\u043a\u0430...", None))
        self.lblLoadingSub.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043d\u0434\u0438\u043a\u0430\u0442\u043e\u0440 \u043f\u0440\u043e\u0433\u0440\u0435\u0441\u0441\u0430", None))
        self.lblEmptyTitle.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0438\u0447\u0435\u0433\u043e \u043d\u0435 \u043d\u0430\u0439\u0434\u0435\u043d\u043e", None))
        self.lblEmptySub.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u0435 \u0444\u0438\u043b\u044c\u0442\u0440\u044b", None))
        self.lblErrorMessage.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0448\u0438\u0431\u043a\u0430 \u043f\u043e\u0434\u043a\u043b\u044e\u0447\u0435\u043d\u0438\u044f \u043a \u0411\u0414", None))
        self.btnRetry.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0432\u0442\u043e\u0440\u0438\u0442\u044c", None))
        self.searchInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0438\u0441\u043a \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_8), QCoreApplication.translate("MainWindow", u"\u041a\u0430\u0442\u0430\u043b\u043e\u0433 \u043c\u0430\u0440\u0448\u0440\u0443\u0442\u043e\u0432", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_9), QCoreApplication.translate("MainWindow", u"\u0422\u0443\u0440\u044b", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_10), QCoreApplication.translate("MainWindow", u"\u0418\u043c\u043f\u043e\u0440\u0442 \u0438 \u044d\u043a\u0441\u043f\u043e\u0440\u0442", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_11), QCoreApplication.translate("MainWindow", u"\u0421\u0438\u043d\u0445\u0440\u043e\u043d\u0438\u0437\u0430\u0446\u0438\u044f", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_12), QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u0438", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_13), QCoreApplication.translate("MainWindow", u"\u0416\u0443\u0440\u043d\u0430\u043b \u0430\u0443\u0434\u0438\u0442\u0430", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_14), QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438 API \u0438 \u043a\u0435\u0448", None))
    # retranslateUi

