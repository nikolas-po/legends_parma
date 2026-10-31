# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'audit_log_window.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QDateEdit,
    QFrame, QHBoxLayout, QHeaderView, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QTabWidget, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)
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
"#contentFrame { background-color: #F5F0E8; }\n"
"QHeaderView { background-color: #EDE6D9; }\n"
"QHeaderView::section { background-color: #EDE6D9; color: #6B6560; font-size: 11px; font-weight: 600; border: none; border-bottom: 1px solid #D4CBBE; border-right: 1px solid #D4CBBE; padding: 7px 10px; text-align: left; }\n"
"QHeaderView::section:vertical { background-color: #EDE6D9; color: #6B6560; border: none; padding: 4px 6px; }\n"
"QTableWidget { background-color: #F"
                        "FFFFF; border: 1px solid #D4CBBE; outline: none; gridline-color: transparent; }\n"
"QTableWidget::item { border-bottom: 1px solid #D4CBBE; padding: 7px 10px; color: #2C2A26; font-size: 12px; }\n"
"QTableWidget::item:hover { background-color: #EDE6D9; }\n"
"QTableWidget::item:selected { background-color: #E8EDE4; color: #2C2A26; }\n"
"#filterFrame { background-color: transparent; }\n"
"#filterFrame QLabel { font-size: 13px; font-weight: 500; color: #6B6560; }\n"
"QDateEdit, QComboBox { padding: 8px 12px; font-size: 13px; border-radius: 4px; border: 1px solid #D4CBBE; background-color: #FFFFFF; color: #2C2A26; min-height: 20px; }\n"
"QDateEdit::drop-down { subcontrol-origin: padding; subcontrol-position: top right; width: 28px; border-left: 1px solid #D4CBBE; background-color: #F5F0E8; border-top-right-radius: 4px; border-bottom-right-radius: 4px; }\n"
"QDateEdit:hover, QComboBox:hover { border: 1px solid #B8AE9E; }\n"
"QDateEdit:focus, QComboBox:focus { border: 1px solid #4A6741; }\n"
"QDateEdit[error=\"true\"]"
                        ", QComboBox[error=\"true\"] { border: 1px solid #B54A3A; }\n"
"QDateEdit:disabled, QComboBox:disabled { border: 1px dashed #D4CBBE; color: #A39E94; background-color: #F5F0E8; }\n"
"QComboBox QAbstractItemView { background-color: #FFFFFF; border: 1px solid #D4CBBE; selection-background-color: #E8EDE4; selection-color: #2C2A26; }\n"
"QComboBox QAbstractItemView::item:hover { background-color: #EDE6D9; }\n"
"#btn_apply, #btn_export { padding: 8px 16px; font-size: 13px; border-radius: 4px; background-color: #FFFFFF; color: #2C2A26; border: 1px solid #D4CBBE; min-height: 20px; }\n"
"#btn_apply:hover, #btn_export:hover { border: 1px solid #4A6741; background-color: #F5F0E8; }\n"
"#btn_apply:pressed, #btn_export:pressed { background-color: #EDE6D9; }\n"
"#btn_apply:disabled, #btn_export:disabled { background-color: #FFFFFF; color: #A39E94; border: 1px solid #E5DFD4; }\n"
"#btn_apply:focus, #btn_export:focus { border: 1px dashed #4A6741; }\n"
"#offlineBanner { background-color: #F0EEEA; border: 1px solid #D4CBBE; bord"
                        "er-radius: 4px; }\n"
"#offlineBanner QLabel { font-size: 12px; color: #6B6560; }\n"
"#offlineDot { background-color: #A39E94; border-radius: 4px; min-width: 8px; max-width: 8px; min-height: 8px; max-height: 8px; }\n"
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
"QTabBar::tab { height: 40px; back"
                        "ground-color: #FFFFFF; color: #6B6560; font-size: 12px; font-weight: normal; padding: 0px 30px; border: none; border-bottom: 2px solid transparent; border-top: 1px solid #D4CBBE; text-align: center; }\n"
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

        self.contentFrame = QFrame(self.centralwidget)
        self.contentFrame.setObjectName(u"contentFrame")
        self.contentLayout = QVBoxLayout(self.contentFrame)
        self.contentLayout.setSpacing(10)
        self.contentLayout.setObjectName(u"contentLayout")
        self.contentLayout.setContentsMargins(12, 12, 12, 12)
        self.offlineBanner = QFrame(self.contentFrame)
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


        self.contentLayout.addWidget(self.offlineBanner)

        self.stateStack = QStackedWidget(self.contentFrame)
        self.stateStack.setObjectName(u"stateStack")
        self.pageNormal = QWidget()
        self.pageNormal.setObjectName(u"pageNormal")
        self.normalLayout = QVBoxLayout(self.pageNormal)
        self.normalLayout.setObjectName(u"normalLayout")
        self.normalLayout.setContentsMargins(0, 0, 0, 0)
        self.auditTable = QTableWidget(self.pageNormal)
        if (self.auditTable.columnCount() < 6):
            self.auditTable.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.auditTable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.auditTable.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.auditTable.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.auditTable.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.auditTable.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.auditTable.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.auditTable.setObjectName(u"auditTable")
        self.auditTable.setFrameShape(QFrame.Shape.NoFrame)
        self.auditTable.setShowGrid(False)
        self.auditTable.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.auditTable.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.auditTable.horizontalHeader().setStretchLastSection(True)

        self.normalLayout.addWidget(self.auditTable)

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

        self.contentLayout.addWidget(self.stateStack)

        self.filterFrame = QFrame(self.contentFrame)
        self.filterFrame.setObjectName(u"filterFrame")
        self.filterLayout = QHBoxLayout(self.filterFrame)
        self.filterLayout.setSpacing(8)
        self.filterLayout.setObjectName(u"filterLayout")
        self.filterLayout.setContentsMargins(0, 0, 0, 0)
        self.lblDateFrom = QLabel(self.filterFrame)
        self.lblDateFrom.setObjectName(u"lblDateFrom")

        self.filterLayout.addWidget(self.lblDateFrom)

        self.dateFrom = QDateEdit(self.filterFrame)
        self.dateFrom.setObjectName(u"dateFrom")
        self.dateFrom.setMinimumSize(QSize(140, 36))
        self.dateFrom.setCalendarPopup(True)

        self.filterLayout.addWidget(self.dateFrom)

        self.lblDateTo = QLabel(self.filterFrame)
        self.lblDateTo.setObjectName(u"lblDateTo")

        self.filterLayout.addWidget(self.lblDateTo)

        self.dateTo = QDateEdit(self.filterFrame)
        self.dateTo.setObjectName(u"dateTo")
        self.dateTo.setMinimumSize(QSize(140, 36))
        self.dateTo.setCalendarPopup(True)

        self.filterLayout.addWidget(self.dateTo)

        self.comboUser = QComboBox(self.filterFrame)
        self.comboUser.addItem("")
        self.comboUser.setObjectName(u"comboUser")
        self.comboUser.setMinimumSize(QSize(140, 36))

        self.filterLayout.addWidget(self.comboUser)

        self.comboAction = QComboBox(self.filterFrame)
        self.comboAction.addItem("")
        self.comboAction.setObjectName(u"comboAction")
        self.comboAction.setMinimumSize(QSize(140, 36))

        self.filterLayout.addWidget(self.comboAction)

        self.filterSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.filterLayout.addItem(self.filterSpacer)

        self.btn_apply = QPushButton(self.filterFrame)
        self.btn_apply.setObjectName(u"btn_apply")
        self.btn_apply.setMinimumSize(QSize(0, 36))
        self.btn_apply.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.filterLayout.addWidget(self.btn_apply)

        self.btn_export = QPushButton(self.filterFrame)
        self.btn_export.setObjectName(u"btn_export")
        self.btn_export.setMinimumSize(QSize(0, 36))
        self.btn_export.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.filterLayout.addWidget(self.btn_export)


        self.contentLayout.addWidget(self.filterFrame)


        self.verticalLayout.addWidget(self.contentFrame)

        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
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
        self.tabWidget.setCurrentIndex(5)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"AuditLog_Window", None))
        self.logo.setText("")
        self.name.setText(QCoreApplication.translate("MainWindow", u"\u041b\u0435\u0433\u0435\u043d\u0434\u044b \u041f\u0430\u0440\u043c\u044b", None))
        self.name_chart.setText(QCoreApplication.translate("MainWindow", u"\u0416\u0443\u0440\u043d\u0430\u043b \u0430\u0443\u0434\u0438\u0442\u0430", None))
        self.status_lb.setText("")
        self.role_lb.setText(QCoreApplication.translate("MainWindow", u"\u0410\u0434\u043c\u0438\u043d\u0438\u0441\u0442\u0440\u0430\u0442\u043e\u0440", None))
        self.logout_btn.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0439\u0442\u0438", None))
        self.offlineDot.setText("")
        self.lbl_offline.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0444\u043b\u0430\u0439\u043d \u2014 \u0434\u0430\u043d\u043d\u044b\u0435 \u0438\u0437 \u043a\u0435\u0448\u0430", None))
        ___qtablewidgetitem = self.auditTable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u0442\u0430/\u0432\u0440\u0435\u043c\u044f", None))
        ___qtablewidgetitem1 = self.auditTable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044c", None))
        ___qtablewidgetitem2 = self.auditTable.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0435\u0439\u0441\u0442\u0432\u0438\u0435", None))
        ___qtablewidgetitem3 = self.auditTable.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u044a\u0435\u043a\u0442", None))
        ___qtablewidgetitem4 = self.auditTable.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442", None))
        ___qtablewidgetitem5 = self.auditTable.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0435\u0442\u0430\u043b\u0438", None))
        self.lblLoadingTitle.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0433\u0440\u0443\u0437\u043a\u0430...", None))
        self.lblLoadingSub.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043d\u0434\u0438\u043a\u0430\u0442\u043e\u0440 \u043f\u0440\u043e\u0433\u0440\u0435\u0441\u0441\u0430", None))
        self.lblEmptyTitle.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0438\u0447\u0435\u0433\u043e \u043d\u0435 \u043d\u0430\u0439\u0434\u0435\u043d\u043e", None))
        self.lblEmptySub.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u0435 \u0444\u0438\u043b\u044c\u0442\u0440\u044b", None))
        self.lblErrorMessage.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0448\u0438\u0431\u043a\u0430 \u043f\u043e\u0434\u043a\u043b\u044e\u0447\u0435\u043d\u0438\u044f \u043a \u0411\u0414", None))
        self.btnRetry.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0432\u0442\u043e\u0440\u0438\u0442\u044c", None))
        self.lblDateFrom.setText(QCoreApplication.translate("MainWindow", u"\u0421", None))
        self.dateFrom.setDisplayFormat(QCoreApplication.translate("MainWindow", u"dd.MM.yyyy", None))
        self.lblDateTo.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e", None))
        self.dateTo.setDisplayFormat(QCoreApplication.translate("MainWindow", u"dd.MM.yyyy", None))
        self.comboUser.setItemText(0, QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044c", None))

        self.comboAction.setItemText(0, QCoreApplication.translate("MainWindow", u"\u0414\u0435\u0439\u0441\u0442\u0432\u0438\u0435", None))

        self.btn_apply.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0438\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.btn_export.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0433\u0440\u0443\u0437\u0438\u0442\u044c CSV", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_8), QCoreApplication.translate("MainWindow", u"\u041a\u0430\u0442\u0430\u043b\u043e\u0433 \u043c\u0430\u0440\u0448\u0440\u0443\u0442\u043e\u0432", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_9), QCoreApplication.translate("MainWindow", u"\u0422\u0443\u0440\u044b", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_10), QCoreApplication.translate("MainWindow", u"\u0418\u043c\u043f\u043e\u0440\u0442 \u0438 \u044d\u043a\u0441\u043f\u043e\u0440\u0442", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_11), QCoreApplication.translate("MainWindow", u"\u0421\u0438\u043d\u0445\u0440\u043e\u043d\u0438\u0437\u0430\u0446\u0438\u044f", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_12), QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u0438", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_13), QCoreApplication.translate("MainWindow", u"\u0416\u0443\u0440\u043d\u0430\u043b \u0430\u0443\u0434\u0438\u0442\u0430", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_14), QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438 API \u0438 \u043a\u0435\u0448", None))
    # retranslateUi

