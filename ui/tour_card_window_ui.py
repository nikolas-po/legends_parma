# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tour_card_window.ui'
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
    QHeaderView, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QTabWidget, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)
import login_res_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1172, 673)
        MainWindow.setStyleSheet(u"#centralwidget { background-color: #F5F0E8; }\n"
"#headerFrame { background-color: #2C2A26; border-bottom: 1px solid rgba(255,255,255,0.2); }\n"
"#headerFrame QLabel { color: #F5F0E8; border: none; }\n"
"#logout_btn { background-color: transparent; color: #F5F0E8; border: 1px solid rgba(255, 255, 255, 0.25); padding: 3px 10px; font-size: 12px; border-radius: 4px; }\n"
"#logout_btn:hover { background-color: rgba(255, 255, 255, 0.08); border: 1px solid rgba(255, 255, 255, 0.4); }\n"
"#logout_btn:pressed { background-color: rgba(255, 255, 255, 0.12); border: 1px solid rgba(255, 255, 255, 0.5); }\n"
"#logout_btn:focus { border: 1px dashed #F5F0E8; }\n"
"#toolbarFrame { background-color: #FFFFFF; border-bottom: 1px solid #D4CBBE; }\n"
"#btn_back { padding: 3px 9px; font-size: 12px; color: #6B6560; background: transparent; border: none; }\n"
"#btn_back:hover { background: #F5F0E8; color: #2C2A26; }\n"
"#lbl_toolbar_title { font-size: 14px; font-weight: 600; color: #2C2A26; margin-left: 8px; }\n"
"#btn_change_status,"
                        " #btn_edit { background: #FFFFFF; color: #2C2A26; border: 1px solid #D4CBBE; padding: 4px 10px; font-size: 12px; border-radius: 4px; }\n"
"#btn_change_status:hover, #btn_edit:hover { background: #F5F0E8; border: 1px solid #4A6741; }\n"
"#leftPanel { background-color: #F5F0E8; }\n"
"#rightPanel { background-color: #FFFFFF; border-left: 1px solid #D4CBBE; }\n"
"#lbl_main_title { font-size: 18px; font-weight: 600; color: #2C2A26; }\n"
"#lbl_meta { font-size: 12px; color: #6B6560; }\n"
"#routesFrame, #descFrame { background-color: #FFFFFF; border: 1px solid #D4CBBE; border-radius: 4px; }\n"
"QLabel[styleClass=\"sectionTitle\"] { font-size: 11px; font-weight: 600; color: #6B6560; margin-bottom: 8px; }\n"
"#lbl_desc_text { font-size: 13px; color: #2C2A26; }\n"
"QTableWidget { background-color: #FFFFFF; border: none; outline: none; gridline-color: #D4CBBE; }\n"
"QHeaderView { background-color: #EDE6D9; }\n"
"QHeaderView::section { background-color: #EDE6D9; color: #6B6560; font-size: 11px; font-weight: 600; border: n"
                        "one; border-bottom: 1px solid #D4CBBE; border-right: 1px solid #D4CBBE; padding: 7px 10px; text-align: left; }\n"
"QHeaderView::section:vertical { background-color: #EDE6D9; color: #6B6560; border: none; padding: 4px 6px; }\n"
"QTableWidget QHeaderView::section:vertical { background-color: #EDE6D9; color: #6B6560; border: none; padding: 4px 6px; }\n"
"QTableCornerButton::section { background-color: #EDE6D9; border: none; }\n"
"QTableWidget::item { border-bottom: 1px solid #D4CBBE; padding: 7px 10px; color: #2C2A26; font-size: 12px; }\n"
"QTableWidget::item:hover { background-color: #EDE6D9; }\n"
"QTableWidget::item:selected { background-color: #E8EDE4; color: #2C2A26; }\n"
"QTableWidget QPushButton { background-color: #FFFFFF; color: #2C2A26; border: 1px solid #D4CBBE; border-radius: 4px; padding: 3px 9px; font-size: 12px; }\n"
"QTableWidget QPushButton:hover { border: 1px solid #4A6741; background-color: #F5F0E8; }\n"
"QLabel[styleClass=\"statLabel\"] { font-size: 11px; color: #6B6560; }\n"
"QLabel[styleClass"
                        "=\"statValue\"] { font-size: 13px; color: #2C2A26; }\n"
"#lbl_status_badge { font-size: 12px; color: #4A6741; background-color: #E8EDE4; border: 1px solid #4A6741; padding: 2px 8px; border-radius: 3px; }\n"
"#btn_cancel_tour { background-color: #FFFFFF; color: #B54A3A; border: 1px solid #B54A3A; padding: 6px 12px; font-size: 13px; border-radius: 4px; font-weight: 600; }\n"
"#btn_cancel_tour:hover { background-color: #F5E8E6; }\n"
"QTabWidget::panel { border: none; background-color: #FFFFFF; }\n"
"QTabBar { background-color: #FFFFFF; border: none; }\n"
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

        self.toolbarFrame = QFrame(self.centralwidget)
        self.toolbarFrame.setObjectName(u"toolbarFrame")
        self.toolbarFrame.setMinimumSize(QSize(0, 48))
        self.toolbarFrame.setMaximumSize(QSize(16777215, 48))
        self.toolbarLayout = QHBoxLayout(self.toolbarFrame)
        self.toolbarLayout.setSpacing(8)
        self.toolbarLayout.setObjectName(u"toolbarLayout")
        self.toolbarLayout.setContentsMargins(16, 0, 16, 0)
        self.btn_back = QPushButton(self.toolbarFrame)
        self.btn_back.setObjectName(u"btn_back")
        self.btn_back.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.toolbarLayout.addWidget(self.btn_back)

        self.lbl_toolbar_title = QLabel(self.toolbarFrame)
        self.lbl_toolbar_title.setObjectName(u"lbl_toolbar_title")

        self.toolbarLayout.addWidget(self.lbl_toolbar_title)

        self.toolbarSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.toolbarLayout.addItem(self.toolbarSpacer)

        self.btn_change_status = QPushButton(self.toolbarFrame)
        self.btn_change_status.setObjectName(u"btn_change_status")
        self.btn_change_status.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.toolbarLayout.addWidget(self.btn_change_status)

        self.btn_edit = QPushButton(self.toolbarFrame)
        self.btn_edit.setObjectName(u"btn_edit")
        self.btn_edit.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.toolbarLayout.addWidget(self.btn_edit)


        self.verticalLayout.addWidget(self.toolbarFrame)

        self.mainContentFrame = QFrame(self.centralwidget)
        self.mainContentFrame.setObjectName(u"mainContentFrame")
        self.mainContentFrame.setFrameShape(QFrame.Shape.NoFrame)
        self.mainContentLayout = QHBoxLayout(self.mainContentFrame)
        self.mainContentLayout.setSpacing(0)
        self.mainContentLayout.setObjectName(u"mainContentLayout")
        self.mainContentLayout.setContentsMargins(0, 0, 0, 0)
        self.leftPanel = QFrame(self.mainContentFrame)
        self.leftPanel.setObjectName(u"leftPanel")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.leftPanel.sizePolicy().hasHeightForWidth())
        self.leftPanel.setSizePolicy(sizePolicy)
        self.leftLayout = QVBoxLayout(self.leftPanel)
        self.leftLayout.setSpacing(16)
        self.leftLayout.setObjectName(u"leftLayout")
        self.leftLayout.setContentsMargins(20, 16, 20, 16)
        self.lbl_main_title = QLabel(self.leftPanel)
        self.lbl_main_title.setObjectName(u"lbl_main_title")

        self.leftLayout.addWidget(self.lbl_main_title)

        self.lbl_meta = QLabel(self.leftPanel)
        self.lbl_meta.setObjectName(u"lbl_meta")

        self.leftLayout.addWidget(self.lbl_meta)

        self.routesFrame = QFrame(self.leftPanel)
        self.routesFrame.setObjectName(u"routesFrame")
        self.routesLayout = QVBoxLayout(self.routesFrame)
        self.routesLayout.setSpacing(8)
        self.routesLayout.setObjectName(u"routesLayout")
        self.routesLayout.setContentsMargins(12, 12, 12, 12)
        self.lbl_routes_section_title = QLabel(self.routesFrame)
        self.lbl_routes_section_title.setObjectName(u"lbl_routes_section_title")

        self.routesLayout.addWidget(self.lbl_routes_section_title)

        self.routesTable = QTableWidget(self.routesFrame)
        if (self.routesTable.columnCount() < 5):
            self.routesTable.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.routesTable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.routesTable.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.routesTable.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.routesTable.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.routesTable.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.routesTable.setObjectName(u"routesTable")
        self.routesTable.setFrameShape(QFrame.Shape.NoFrame)
        self.routesTable.setShowGrid(True)
        self.routesTable.setSelectionMode(QAbstractItemView.SelectionMode.NoSelection)
        self.routesTable.horizontalHeader().setStretchLastSection(False)
        self.routesTable.verticalHeader().setVisible(False)

        self.routesLayout.addWidget(self.routesTable)


        self.leftLayout.addWidget(self.routesFrame)

        self.descFrame = QFrame(self.leftPanel)
        self.descFrame.setObjectName(u"descFrame")
        self.descLayout = QVBoxLayout(self.descFrame)
        self.descLayout.setSpacing(8)
        self.descLayout.setObjectName(u"descLayout")
        self.descLayout.setContentsMargins(12, 12, 12, 12)
        self.lbl_desc_section_title = QLabel(self.descFrame)
        self.lbl_desc_section_title.setObjectName(u"lbl_desc_section_title")

        self.descLayout.addWidget(self.lbl_desc_section_title)

        self.lbl_desc_text = QLabel(self.descFrame)
        self.lbl_desc_text.setObjectName(u"lbl_desc_text")
        self.lbl_desc_text.setWordWrap(True)

        self.descLayout.addWidget(self.lbl_desc_text)

        self.descSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.descLayout.addItem(self.descSpacer)


        self.leftLayout.addWidget(self.descFrame)

        self.leftBottomSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.leftLayout.addItem(self.leftBottomSpacer)


        self.mainContentLayout.addWidget(self.leftPanel)

        self.rightPanel = QFrame(self.mainContentFrame)
        self.rightPanel.setObjectName(u"rightPanel")
        self.rightPanel.setMinimumSize(QSize(320, 0))
        self.rightPanel.setMaximumSize(QSize(320, 16777215))
        self.rightLayout = QVBoxLayout(self.rightPanel)
        self.rightLayout.setSpacing(12)
        self.rightLayout.setObjectName(u"rightLayout")
        self.rightLayout.setContentsMargins(16, 16, 16, 16)
        self.statStatusLayout = QVBoxLayout()
        self.statStatusLayout.setSpacing(4)
        self.statStatusLayout.setObjectName(u"statStatusLayout")
        self.lbl_stat_status_label = QLabel(self.rightPanel)
        self.lbl_stat_status_label.setObjectName(u"lbl_stat_status_label")

        self.statStatusLayout.addWidget(self.lbl_stat_status_label)

        self.lbl_status_badge = QLabel(self.rightPanel)
        self.lbl_status_badge.setObjectName(u"lbl_status_badge")
        self.lbl_status_badge.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.statStatusLayout.addWidget(self.lbl_status_badge)


        self.rightLayout.addLayout(self.statStatusLayout)

        self.statStartLayout = QVBoxLayout()
        self.statStartLayout.setSpacing(4)
        self.statStartLayout.setObjectName(u"statStartLayout")
        self.lbl_stat_start_label = QLabel(self.rightPanel)
        self.lbl_stat_start_label.setObjectName(u"lbl_stat_start_label")

        self.statStartLayout.addWidget(self.lbl_stat_start_label)

        self.lbl_stat_start_value = QLabel(self.rightPanel)
        self.lbl_stat_start_value.setObjectName(u"lbl_stat_start_value")

        self.statStartLayout.addWidget(self.lbl_stat_start_value)


        self.rightLayout.addLayout(self.statStartLayout)

        self.statEndLayout = QVBoxLayout()
        self.statEndLayout.setSpacing(4)
        self.statEndLayout.setObjectName(u"statEndLayout")
        self.lbl_stat_end_label = QLabel(self.rightPanel)
        self.lbl_stat_end_label.setObjectName(u"lbl_stat_end_label")

        self.statEndLayout.addWidget(self.lbl_stat_end_label)

        self.lbl_stat_end_value = QLabel(self.rightPanel)
        self.lbl_stat_end_value.setObjectName(u"lbl_stat_end_value")

        self.statEndLayout.addWidget(self.lbl_stat_end_value)


        self.rightLayout.addLayout(self.statEndLayout)

        self.statOrgLayout = QVBoxLayout()
        self.statOrgLayout.setSpacing(4)
        self.statOrgLayout.setObjectName(u"statOrgLayout")
        self.lbl_stat_org_label = QLabel(self.rightPanel)
        self.lbl_stat_org_label.setObjectName(u"lbl_stat_org_label")

        self.statOrgLayout.addWidget(self.lbl_stat_org_label)

        self.lbl_stat_org_value = QLabel(self.rightPanel)
        self.lbl_stat_org_value.setObjectName(u"lbl_stat_org_value")

        self.statOrgLayout.addWidget(self.lbl_stat_org_value)


        self.rightLayout.addLayout(self.statOrgLayout)

        self.statCountLayout = QVBoxLayout()
        self.statCountLayout.setSpacing(4)
        self.statCountLayout.setObjectName(u"statCountLayout")
        self.lbl_stat_count_label = QLabel(self.rightPanel)
        self.lbl_stat_count_label.setObjectName(u"lbl_stat_count_label")

        self.statCountLayout.addWidget(self.lbl_stat_count_label)

        self.lbl_stat_count_value = QLabel(self.rightPanel)
        self.lbl_stat_count_value.setObjectName(u"lbl_stat_count_value")

        self.statCountLayout.addWidget(self.lbl_stat_count_value)


        self.rightLayout.addLayout(self.statCountLayout)

        self.rightSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.rightLayout.addItem(self.rightSpacer)

        self.btn_cancel_tour = QPushButton(self.rightPanel)
        self.btn_cancel_tour.setObjectName(u"btn_cancel_tour")
        self.btn_cancel_tour.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.rightLayout.addWidget(self.btn_cancel_tour)


        self.mainContentLayout.addWidget(self.rightPanel)


        self.verticalLayout.addWidget(self.mainContentFrame)

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
        self.tabWidget.setProperty(u"drawBase", False)
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

        self.verticalLayout.addWidget(self.tabWidget, 0, Qt.AlignmentFlag.AlignHCenter)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"TourCardWindow", None))
        self.logo.setText("")
        self.name.setText(QCoreApplication.translate("MainWindow", u"\u041b\u0435\u0433\u0435\u043d\u0434\u044b \u041f\u0430\u0440\u043c\u044b", None))
        self.name_chart.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u0440\u0442\u043e\u0447\u043a\u0430 \u0442\u0443\u0440\u0430", None))
        self.status_lb.setText("")
        self.role_lb.setText(QCoreApplication.translate("MainWindow", u"\u0410\u0434\u043c\u0438\u043d\u0438\u0441\u0442\u0440\u0430\u0442\u043e\u0440", None))
        self.logout_btn.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0439\u0442\u0438", None))
        self.btn_back.setText(QCoreApplication.translate("MainWindow", u"\u2039 \u041d\u0430\u0437\u0430\u0434", None))
        self.lbl_toolbar_title.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0430\u043d\u0430\u0440\u0430\u0433\u0430 \u2014 \u0441\u0435\u043d\u0442\u044f\u0431\u0440\u044c", None))
        self.btn_change_status.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c \u0441\u0442\u0430\u0442\u0443\u0441", None))
        self.btn_edit.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.lbl_main_title.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0430\u043d\u0430\u0440\u0430\u0433\u0430 \u2014 \u0441\u0435\u043d\u0442\u044f\u0431\u0440\u044c", None))
        self.lbl_meta.setText(QCoreApplication.translate("MainWindow", u"15.09.2026 \u2014 20.09.2026 \u00b7 \u041e\u0440\u0433\u0430\u043d\u0438\u0437\u0430\u0442\u043e\u0440: admin", None))
        self.lbl_routes_section_title.setProperty(u"styleClass", QCoreApplication.translate("MainWindow", u"sectionTitle", None))
        self.lbl_routes_section_title.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0410\u0420\u0428\u0420\u0423\u0422\u042b \u0422\u0423\u0420\u0410", None))
        ___qtablewidgetitem = self.routesTable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435", None))
        ___qtablewidgetitem1 = self.routesTable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0438\u043f", None))
        ___qtablewidgetitem2 = self.routesTable.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043c", None))
        ___qtablewidgetitem3 = self.routesTable.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"\u0427", None))
        self.lbl_desc_section_title.setProperty(u"styleClass", QCoreApplication.translate("MainWindow", u"sectionTitle", None))
        self.lbl_desc_section_title.setText(QCoreApplication.translate("MainWindow", u"\u041e\u041f\u0418\u0421\u0410\u041d\u0418\u0415", None))
        self.lbl_desc_text.setText(QCoreApplication.translate("MainWindow", u"\u0413\u0440\u0443\u043f\u043f\u043e\u0432\u043e\u0439 \u0432\u044b\u0445\u043e\u0434 \u043d\u0430 \u041c\u0430\u043d\u0430\u0440\u0430\u0433\u0443. \u0421\u0431\u043e\u0440 \u0443 \u0431\u0430\u0437\u044b \u00ab\u0416\u0435\u043b\u0430\u043d\u043d\u0430\u044f\u00bb.", None))
        self.lbl_stat_status_label.setProperty(u"styleClass", QCoreApplication.translate("MainWindow", u"statLabel", None))
        self.lbl_stat_status_label.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0430\u0442\u0443\u0441", None))
        self.lbl_status_badge.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043f\u043b\u0430\u043d\u0438\u0440\u043e\u0432\u0430\u043d", None))
        self.lbl_stat_start_label.setProperty(u"styleClass", QCoreApplication.translate("MainWindow", u"statLabel", None))
        self.lbl_stat_start_label.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0447\u0430\u043b\u043e", None))
        self.lbl_stat_start_value.setProperty(u"styleClass", QCoreApplication.translate("MainWindow", u"statValue", None))
        self.lbl_stat_start_value.setText(QCoreApplication.translate("MainWindow", u"15.09.2026", None))
        self.lbl_stat_end_label.setProperty(u"styleClass", QCoreApplication.translate("MainWindow", u"statLabel", None))
        self.lbl_stat_end_label.setText(QCoreApplication.translate("MainWindow", u"\u041e\u043a\u043e\u043d\u0447\u0430\u043d\u0438\u0435", None))
        self.lbl_stat_end_value.setProperty(u"styleClass", QCoreApplication.translate("MainWindow", u"statValue", None))
        self.lbl_stat_end_value.setText(QCoreApplication.translate("MainWindow", u"20.09.2026", None))
        self.lbl_stat_org_label.setProperty(u"styleClass", QCoreApplication.translate("MainWindow", u"statLabel", None))
        self.lbl_stat_org_label.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0440\u0433\u0430\u043d\u0438\u0437\u0430\u0442\u043e\u0440", None))
        self.lbl_stat_org_value.setProperty(u"styleClass", QCoreApplication.translate("MainWindow", u"statValue", None))
        self.lbl_stat_org_value.setText(QCoreApplication.translate("MainWindow", u"admin", None))
        self.lbl_stat_count_label.setProperty(u"styleClass", QCoreApplication.translate("MainWindow", u"statLabel", None))
        self.lbl_stat_count_label.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0430\u0440\u0448\u0440\u0443\u0442\u043e\u0432", None))
        self.lbl_stat_count_value.setProperty(u"styleClass", QCoreApplication.translate("MainWindow", u"statValue", None))
        self.lbl_stat_count_value.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.btn_cancel_tour.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043c\u0435\u043d\u0438\u0442\u044c \u0442\u0443\u0440", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_8), QCoreApplication.translate("MainWindow", u"\u041a\u0430\u0442\u0430\u043b\u043e\u0433 \u043c\u0430\u0440\u0448\u0440\u0443\u0442\u043e\u0432", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_9), QCoreApplication.translate("MainWindow", u"\u0422\u0443\u0440\u044b", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_10), QCoreApplication.translate("MainWindow", u"\u0418\u043c\u043f\u043e\u0440\u0442 \u0438 \u044d\u043a\u0441\u043f\u043e\u0440\u0442", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_11), QCoreApplication.translate("MainWindow", u"\u0421\u0438\u043d\u0445\u0440\u043e\u043d\u0438\u0437\u0430\u0446\u0438\u044f", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_12), QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u0438", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_13), QCoreApplication.translate("MainWindow", u"\u0416\u0443\u0440\u043d\u0430\u043b \u0430\u0443\u0434\u0438\u0442\u0430", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_14), QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438 API \u0438 \u043a\u0435\u0448", None))
    # retranslateUi

