# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'route_directory_window.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QCheckBox, QComboBox,
    QFrame, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QTabWidget, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)
import login_res_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1160, 696)
        MainWindow.setStyleSheet(u"#centralwidget { background-color: #F5F0E8; }\n"
"#headerFrame { background-color: #2C2A26; border-bottom: 1px solid rgba(255,255,255,0.2); }\n"
"#headerFrame QLabel { color: #F5F0E8; border: none; }\n"
"#logout_btn { background-color: transparent; color: #F5F0E8; border: 1px solid rgba(255, 255, 255, 0.25); padding: 3px 10px; font-size: 12px; border-radius: 4px; }\n"
"#logout_btn:hover { background-color: rgba(255, 255, 255, 0.08); border: 1px solid rgba(255, 255, 255, 0.4); }\n"
"#logout_btn:pressed { background-color: rgba(255, 255, 255, 0.12); border: 1px solid rgba(255, 255, 255, 0.5); }\n"
"#leftPanel { background-color: #F5F0E8; border-right: 1px solid #D4CBBE; }\n"
"#lbl_title { font-size: 12px; color: #6B6560; }\n"
"#lbl_desc { font-size: 11px; color: #6B6560; }\n"
"#btn_open { background-color: #4A6741; color: #FFFFFF; border: none; padding: 3px 9px; font-size: 12px; border-radius: 4px; }\n"
"#btn_open:hover { background-color: #3D5636; }\n"
"#btn_open:pressed { background-color: #334A2E; }\n"
"#btn_"
                        "open:disabled { background-color: #A8B5A0; }\n"
"#btn_edit { background-color: #FFFFFF; color: #2C2A26; border: 1px solid #D4CBBE; padding: 3px 9px; font-size: 12px; border-radius: 4px; }\n"
"#btn_edit:hover { background-color: #F5F0E8; border: 1px solid #4A6741; }\n"
"#btn_edit:pressed { background-color: #EDE6D9; border: 1px solid #3D5636; }\n"
"#btn_edit:disabled { background-color: #FFFFFF; color: #A39E94; border: 1px solid #E5DFD4; }\n"
"#btn_delete { background-color: #FFFFFF; color: #B54A3A; border: 1px solid #B54A3A; padding: 3px 9px; font-size: 12px; border-radius: 4px; }\n"
"#btn_delete:hover { background-color: #F5E8E6; color: #B54A3A; border: 1px solid #B54A3A; }\n"
"#btn_delete:pressed { background-color: #EBD5D1; color: #9A3E30; border: 1px solid #9A3E30; }\n"
"#btn_delete:disabled { background-color: #FFFFFF; color: #D4A39C; border: 1px solid #E5C4BF; }\n"
"QRadioButton { spacing: 6px; font-size: 12px; color: #6B6560; }\n"
"QRadioButton::indicator { width: 15px; height: 15px; }\n"
"QRadioButton:"
                        ":indicator:unchecked { border: 1px solid #D4CBBE; border-radius: 8px; background-color: #FFFFFF; }\n"
"QRadioButton::indicator:checked { border: 4px solid #4A6741; border-radius: 8px; background-color: #FFFFFF; }\n"
"#rightPanel { background-color: #F5F0E8; }\n"
"#offlineBanner { background-color: #F0EEEA; border: 1px solid #D4CBBE; border-radius: 4px; }\n"
"#offlineBanner QLabel { font-size: 12px; color: #6B6560; }\n"
"#offlineDot { background-color: #A39E94; border-radius: 4px; min-width: 8px; max-width: 8px; min-height: 8px; max-height: 8px; }\n"
"#filterPanel { background-color: #F5F0E8; border-top: 1px solid #D4CBBE; }\n"
"#filterPanel QLineEdit { padding: 4px 8px; font-size: 12px; border-radius: 4px; border: 1px solid #D4CBBE; background-color: #FFFFFF; color: #2C2A26; }\n"
"#filterPanel QLineEdit:hover { border: 1px solid #B8AE9E; }\n"
"#filterPanel QLineEdit:focus { border: 1px solid #4A6741; }\n"
"#filterPanel QLineEdit[error=\"true\"] { border: 1px solid #B54A3A; }\n"
"#filterPanel QLineEdit:disabled"
                        " { border: 1px dashed #D4CBBE; color: #A39E94; background-color: #F5F0E8; }\n"
"#filterPanel QLineEdit#searchInput { min-width: 160px; max-width: 240px; }\n"
"#filterPanel QComboBox { padding: 4px 8px; font-size: 12px; border-radius: 4px; border: 1px solid #D4CBBE; background-color: #FFFFFF; color: #2C2A26; min-width: 120px; }\n"
"#filterPanel QComboBox:hover { border: 1px solid #B8AE9E; }\n"
"#filterPanel QComboBox:on { border: 1px solid #4A6741; }\n"
"#filterPanel QComboBox:disabled { border: 1px dashed #D4CBBE; color: #A39E94; background-color: #F5F0E8; }\n"
"#filterPanel QComboBox QAbstractItemView { background-color: #FFFFFF; border: 1px solid #D4CBBE; selection-background-color: #E8EDE4; selection-color: #2C2A26; }\n"
"#filterPanel QComboBox QAbstractItemView::item:hover { background-color: #EDE6D9; }\n"
"#btn_add_route { background-color: #4A6741; color: #FFFFFF; border: none; padding: 3px 9px; font-size: 12px; border-radius: 4px; }\n"
"#btn_add_route:hover { background-color: #3D5636; }\n"
"#btn_add_ro"
                        "ute:pressed { background-color: #334A2E; }\n"
"#btn_add_route:disabled { background-color: #A8B5A0; }\n"
"#btn_add_route:focus { border: 1px dashed #4A6741; }\n"
"#btn_reset { background-color: #FFFFFF; color: #2C2A26; border: 1px solid #D4CBBE; padding: 3px 9px; font-size: 12px; border-radius: 4px; }\n"
"#btn_reset:hover { background-color: #F5F0E8; border: 1px solid #4A6741; }\n"
"#btn_reset:pressed { background-color: #EDE6D9; border: 1px solid #3D5636; }\n"
"#btn_reset:disabled { background-color: #FFFFFF; color: #A39E94; border: 1px solid #E5DFD4; }\n"
"#btn_reset:focus { border: 1px dashed #4A6741; }\n"
"#chk_deleted { spacing: 6px; font-size: 12px; color: #6B6560; }\n"
"#chk_deleted::indicator { width: 15px; height: 15px; border-radius: 3px; border: 1px solid #D4CBBE; background-color: #FFFFFF; }\n"
"#chk_deleted::indicator:hover { border: 1px solid #B8AE9E; }\n"
"#chk_deleted::indicator:checked { background-color: #4A6741; border: 1px solid #4A6741; }\n"
"#chk_deleted::indicator:pressed { background-co"
                        "lor: #334A2E; border: 1px solid #334A2E; }\n"
"#chk_deleted::indicator:disabled { background-color: #E5DFD4; border: 1px solid #E5DFD4; }\n"
"#chk_deleted:disabled { color: #A39E94; }\n"
"#tableWidget { background-color: #FFFFFF; alternate-background-color: #FAF8F3; border: 1px solid #D4CBBE; outline: none; }\n"
"QHeaderView { background-color: #EDE6D9; }\n"
"QHeaderView::section { font-size: 11px; font-weight: 600; color: #6B6560; background-color: #EDE6D9; padding: 7px 10px; border: none; border-bottom: 1px solid #D4CBBE; border-right: 1px solid #D4CBBE; }\n"
"QHeaderView::section:vertical { background-color: #EDE6D9; color: #6B6560; border: none; padding: 4px 6px; }\n"
"QTableWidget QHeaderView::section:vertical { background-color: #EDE6D9; color: #6B6560; border: none; padding: 4px 6px; }\n"
"QTableCornerButton::section { background-color: #EDE6D9; border: none; }\n"
"QTableWidget::item { font-size: 12px; color: #2C2A26; padding: 7px 10px; border-bottom: 1px solid #D4CBBE; }\n"
"QTableWidget::item:hover { "
                        "background-color: #EDE6D9; }\n"
"QTableWidget::item:selected { background-color: #E8EDE4; color: #2C2A26; }\n"
"#footerLabel { font-size: 11px; color: #6B6560; }\n"
"#lblLoadingTitle { font-size: 14px; color: #6B6560; }\n"
"#lblLoadingSub { font-size: 12px; color: #A39E94; }\n"
"#lblEmptyTitle { font-size: 14px; color: #6B6560; }\n"
"#lblEmptySub { font-size: 12px; color: #A39E94; }\n"
"#errorFrame { background-color: #FFFFFF; border: 1px solid #B54A3A; border-radius: 4px; }\n"
"#errorFrame QLabel { font-size: 14px; color: #B54A3A; }\n"
"#btnRetry { background-color: #FFFFFF; color: #2C2A26; border: 1px solid #D4CBBE; border-radius: 4px; padding: 6px 16px; font-size: 12px; }\n"
"#btnRetry:hover { border: 1px solid #4A6741; background-color: #F5F0E8; }\n"
"QTabWidget::panel { border: none; background-color: #FFFFFF; }\n"
"QTabBar { background-color: #FFFFFF; border: none; qproperty-expanding: true; qproperty-drawBase: 0; }\n"
"QTabBar::tab { height: 40px; background-color: #FFFFFF; color: #6B6560; font-size: 12"
                        "px; font-weight: normal; padding: 0px 10px; border: none; border-bottom: 2px solid transparent; border-top: 1px solid #D4CBBE; text-align: center; }\n"
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
        self.logo.setStyleSheet(u"QPushButton { background: transparent; margin-right: 12px; }")
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
        self.status_lb.setStyleSheet(u"background-color: #4A6741; border-radius: 3px;")

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

        self.centralFrame = QFrame(self.centralwidget)
        self.centralFrame.setObjectName(u"centralFrame")
        self.centralFrame.setFrameShape(QFrame.Shape.NoFrame)
        self.horizontalLayout_main = QHBoxLayout(self.centralFrame)
        self.horizontalLayout_main.setSpacing(0)
        self.horizontalLayout_main.setObjectName(u"horizontalLayout_main")
        self.horizontalLayout_main.setContentsMargins(0, 0, 0, 0)
        self.leftPanel = QFrame(self.centralFrame)
        self.leftPanel.setObjectName(u"leftPanel")
        self.leftPanel.setMinimumSize(QSize(280, 260))
        self.leftPanel.setMaximumSize(QSize(280, 16777215))
        self.verticalLayout_2 = QVBoxLayout(self.leftPanel)
        self.verticalLayout_2.setSpacing(12)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(14, 14, 14, 14)
        self.lbl_title = QLabel(self.leftPanel)
        self.lbl_title.setObjectName(u"lbl_title")

        self.verticalLayout_2.addWidget(self.lbl_title)

        self.lbl_desc = QLabel(self.leftPanel)
        self.lbl_desc.setObjectName(u"lbl_desc")

        self.verticalLayout_2.addWidget(self.lbl_desc)

        self.lbl_name = QLabel(self.leftPanel)
        self.lbl_name.setObjectName(u"lbl_name")

        self.verticalLayout_2.addWidget(self.lbl_name)

        self.lbl_type = QLabel(self.leftPanel)
        self.lbl_type.setObjectName(u"lbl_type")

        self.verticalLayout_2.addWidget(self.lbl_type)

        self.lbl_length = QLabel(self.leftPanel)
        self.lbl_length.setObjectName(u"lbl_length")

        self.verticalLayout_2.addWidget(self.lbl_length)

        self.leftSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.leftSpacer)

        self.leftButtonsLayout = QHBoxLayout()
        self.leftButtonsLayout.setSpacing(6)
        self.leftButtonsLayout.setObjectName(u"leftButtonsLayout")
        self.btn_open = QPushButton(self.leftPanel)
        self.btn_open.setObjectName(u"btn_open")
        self.btn_open.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.leftButtonsLayout.addWidget(self.btn_open)

        self.btn_edit = QPushButton(self.leftPanel)
        self.btn_edit.setObjectName(u"btn_edit")
        self.btn_edit.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.leftButtonsLayout.addWidget(self.btn_edit)

        self.btn_delete = QPushButton(self.leftPanel)
        self.btn_delete.setObjectName(u"btn_delete")
        self.btn_delete.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.leftButtonsLayout.addWidget(self.btn_delete)


        self.verticalLayout_2.addLayout(self.leftButtonsLayout)


        self.horizontalLayout_main.addWidget(self.leftPanel)

        self.rightPanel = QFrame(self.centralFrame)
        self.rightPanel.setObjectName(u"rightPanel")
        self.rightPanel.setFrameShape(QFrame.Shape.NoFrame)
        self.verticalLayout_right = QVBoxLayout(self.rightPanel)
        self.verticalLayout_right.setSpacing(0)
        self.verticalLayout_right.setObjectName(u"verticalLayout_right")
        self.verticalLayout_right.setContentsMargins(12, 12, 12, 12)
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


        self.verticalLayout_right.addWidget(self.offlineBanner)

        self.stateStack = QStackedWidget(self.rightPanel)
        self.stateStack.setObjectName(u"stateStack")
        self.pageNormal = QWidget()
        self.pageNormal.setObjectName(u"pageNormal")
        self.normalLayout = QVBoxLayout(self.pageNormal)
        self.normalLayout.setObjectName(u"normalLayout")
        self.normalLayout.setContentsMargins(0, 0, 0, 0)
        self.tableWidget = QTableWidget(self.pageNormal)
        if (self.tableWidget.columnCount() < 6):
            self.tableWidget.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setFrameShape(QFrame.Shape.NoFrame)
        self.tableWidget.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tableWidget.setShowGrid(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(130)
        self.tableWidget.horizontalHeader().setStretchLastSection(False)

        self.normalLayout.addWidget(self.tableWidget)

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

        self.verticalLayout_right.addWidget(self.stateStack)

        self.footerLabel = QLabel(self.rightPanel)
        self.footerLabel.setObjectName(u"footerLabel")
        self.footerLabel.setStyleSheet(u"margin-top: 8px; margin-bottom: 8px; margin-left: 2px;")

        self.verticalLayout_right.addWidget(self.footerLabel)

        self.filterPanel = QFrame(self.rightPanel)
        self.filterPanel.setObjectName(u"filterPanel")
        self.filterPanel.setFrameShape(QFrame.Shape.NoFrame)
        self.filterLayout = QHBoxLayout(self.filterPanel)
        self.filterLayout.setSpacing(8)
        self.filterLayout.setObjectName(u"filterLayout")
        self.filterLayout.setContentsMargins(0, 8, 0, 8)
        self.searchInput = QLineEdit(self.filterPanel)
        self.searchInput.setObjectName(u"searchInput")

        self.filterLayout.addWidget(self.searchInput)

        self.typeSelect = QComboBox(self.filterPanel)
        self.typeSelect.addItem("")
        self.typeSelect.setObjectName(u"typeSelect")

        self.filterLayout.addWidget(self.typeSelect)

        self.regionSelect = QComboBox(self.filterPanel)
        self.regionSelect.addItem("")
        self.regionSelect.setObjectName(u"regionSelect")

        self.filterLayout.addWidget(self.regionSelect)

        self.btn_reset = QPushButton(self.filterPanel)
        self.btn_reset.setObjectName(u"btn_reset")
        self.btn_reset.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.filterLayout.addWidget(self.btn_reset)

        self.horizontalSpacer_right = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.filterLayout.addItem(self.horizontalSpacer_right)

        self.btn_add_route = QPushButton(self.filterPanel)
        self.btn_add_route.setObjectName(u"btn_add_route")
        self.btn_add_route.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.filterLayout.addWidget(self.btn_add_route)

        self.chk_deleted = QCheckBox(self.filterPanel)
        self.chk_deleted.setObjectName(u"chk_deleted")
        self.chk_deleted.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.filterLayout.addWidget(self.chk_deleted)


        self.verticalLayout_right.addWidget(self.filterPanel)


        self.horizontalLayout_main.addWidget(self.rightPanel)


        self.verticalLayout.addWidget(self.centralFrame)

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
        self.tab_1 = QWidget()
        self.tab_1.setObjectName(u"tab_1")
        self.tabWidget.addTab(self.tab_1, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.tabWidget.addTab(self.tab_5, "")
        self.tab_6 = QWidget()
        self.tab_6.setObjectName(u"tab_6")
        self.tabWidget.addTab(self.tab_6, "")
        self.tab_7 = QWidget()
        self.tab_7.setObjectName(u"tab_7")
        self.tabWidget.addTab(self.tab_7, "")

        self.verticalLayout.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stateStack.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"RouteCatalogWindow", None))
        self.logo.setText("")
        self.name.setText(QCoreApplication.translate("MainWindow", u"\u041b\u0435\u0433\u0435\u043d\u0434\u044b \u041f\u0430\u0440\u043c\u044b", None))
        self.name_chart.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u0442\u0430\u043b\u043e\u0433 \u043c\u0430\u0440\u0448\u0440\u0443\u0442\u043e\u0432", None))
        self.status_lb.setText("")
        self.role_lb.setText(QCoreApplication.translate("MainWindow", u"\u0410\u0434\u043c\u0438\u043d\u0438\u0441\u0442\u0440\u0430\u0442\u043e\u0440", None))
        self.logout_btn.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0439\u0442\u0438", None))
        self.lbl_title.setText(QCoreApplication.translate("MainWindow", u"\u0412\u042b\u0411\u0420\u0410\u041d\u041d\u042b\u0419 \u041c\u0410\u0420\u0428\u0420\u0423\u0422", None))
        self.lbl_desc.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0440\u0430\u0442\u043a\u0438\u0435 \u0441\u0432\u0435\u0434\u0435\u043d\u0438\u044f", None))
        self.lbl_name.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11px; color:#6B6560;\">\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435:</span> <span style=\" font-size:12px; color:#2C2A26;\">\u2014</span></p></body></html>", None))
        self.lbl_type.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11px; color:#6B6560;\">\u0422\u0438\u043f:</span> <span style=\" font-size:12px; color:#2C2A26;\">\u2014</span></p></body></html>", None))
        self.lbl_length.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11px; color:#6B6560;\">\u041f\u0440\u043e\u0442\u044f\u0436\u0451\u043d\u043d\u043e\u0441\u0442\u044c:</span> <span style=\" font-size:12px; color:#2C2A26;\">\u2014</span></p></body></html>", None))
        self.btn_open.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c", None))
        self.btn_edit.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.btn_delete.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.offlineDot.setText("")
        self.lbl_offline.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0444\u043b\u0430\u0439\u043d \u2014 \u0434\u0430\u043d\u043d\u044b\u0435 \u0438\u0437 \u043a\u0435\u0448\u0430", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435", None))
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0438\u043f", None))
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0442\u044f\u0436\u0451\u043d\u043d\u043e\u0441\u0442\u044c, \u043a\u043c", None))
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0440\u0435\u043c\u044f, \u0447", None))
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0433\u0438\u043e\u043d", None))
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0439\u0442\u0438\u043d\u0433", None))
        self.lblLoadingTitle.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0433\u0440\u0443\u0437\u043a\u0430...", None))
        self.lblLoadingSub.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043d\u0434\u0438\u043a\u0430\u0442\u043e\u0440 \u043f\u0440\u043e\u0433\u0440\u0435\u0441\u0441\u0430", None))
        self.lblEmptyTitle.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0438\u0447\u0435\u0433\u043e \u043d\u0435 \u043d\u0430\u0439\u0434\u0435\u043d\u043e", None))
        self.lblEmptySub.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u0435 \u0444\u0438\u043b\u044c\u0442\u0440\u044b", None))
        self.lblErrorMessage.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0448\u0438\u0431\u043a\u0430 \u043f\u043e\u0434\u043a\u043b\u044e\u0447\u0435\u043d\u0438\u044f \u043a \u0411\u0414", None))
        self.btnRetry.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0432\u0442\u043e\u0440\u0438\u0442\u044c", None))
        self.footerLabel.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043a\u0430\u0437\u0430\u043d\u043e N \u0438\u0437 M", None))
        self.searchInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0438\u0441\u043a \u043f\u043e \u043d\u0430\u0437\u0432\u0430\u043d\u0438\u044e", None))
        self.typeSelect.setItemText(0, QCoreApplication.translate("MainWindow", u"\u0422\u0438\u043f", None))

        self.regionSelect.setItemText(0, QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0433\u0438\u043e\u043d", None))

        self.btn_reset.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0431\u0440\u043e\u0441\u0438\u0442\u044c", None))
        self.btn_add_route.setText(QCoreApplication.translate("MainWindow", u"+ \u041d\u043e\u0432\u044b\u0439 \u043c\u0430\u0440\u0448\u0440\u0443\u0442", None))
        self.chk_deleted.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043a\u0430\u0437\u044b\u0432\u0430\u0442\u044c \u0443\u0434\u0430\u043b\u0451\u043d\u043d\u044b\u0435", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), QCoreApplication.translate("MainWindow", u"\u041a\u0430\u0442\u0430\u043b\u043e\u0433 \u043c\u0430\u0440\u0448\u0440\u0443\u0442\u043e\u0432", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"\u0422\u0443\u0440\u044b", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"\u0418\u043c\u043f\u043e\u0440\u0442 \u0438 \u044d\u043a\u0441\u043f\u043e\u0440\u0442", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"\u0421\u0438\u043d\u0445\u0440\u043e\u043d\u0438\u0437\u0430\u0446\u0438\u044f", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u0438", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), QCoreApplication.translate("MainWindow", u"\u0416\u0443\u0440\u043d\u0430\u043b \u0430\u0443\u0434\u0438\u0442\u0430", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_7), QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438 API \u0438 \u043a\u0435\u0448", None))
    # retranslateUi

