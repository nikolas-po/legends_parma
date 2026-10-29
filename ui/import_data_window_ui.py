# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'import_data_window.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QFrame,
    QHBoxLayout, QHeaderView, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QTabWidget,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)
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
"\n"
"#formCard { background-color: #FFFFFF; border: 1px solid #D4CBBE; border-radius: 4px; }\n"
"#lbl_form_title { font-size: 16px; font-weight: 600; color: #2C2A26; }\n"
"#dropArea { background-color: #FFFFFF; border: 2px dashed #D4CBBE; border-radius: 4px; }\n"
"#dropArea QLabel { border: none; background: transparent; }\n"
"#lbl_drop_main { font-size: 14px; color: #2C2A26; }\n"
"#lbl_drop_sub { font-size: 12px; color: #A39E94; }\n"
"#fieldLabel { font-size: 12px"
                        "; color: #6B6560; }\n"
"\n"
"QComboBox { padding: 10px 12px; font-size: 14px; border-radius: 4px; border: 1px solid #D4CBBE; background-color: #FFFFFF; color: #2C2A26; }\n"
"QComboBox:hover { border: 1px solid #B8AE9E; }\n"
"QComboBox:focus { border: 1px solid #4A6741; }\n"
"QComboBox[error=\"true\"] { border: 1px solid #B54A3A; }\n"
"QComboBox:disabled { border: 1px dashed #D4CBBE; color: #A39E94; background-color: #F5F0E8; }\n"
"QComboBox QAbstractItemView { background-color: #FFFFFF; border: 1px solid #D4CBBE; selection-background-color: #E8EDE4; selection-color: #2C2A26; }\n"
"QComboBox QAbstractItemView::item:hover { background-color: #EDE6D9; }\n"
"\n"
"#btn_import { background-color: #4A6741; color: #FFFFFF; border: none; padding: 11px 16px; font-size: 14px; font-weight: 600; border-radius: 4px; }\n"
"#btn_import:hover { background-color: #3D5636; }\n"
"#btn_import:pressed { background-color: #334A2E; }\n"
"#btn_import:disabled { background-color: #A8B5A0; }\n"
"#btn_import:focus { border: 1px dashed #4"
                        "A6741; }\n"
"\n"
"#successBanner { background-color: #E8EDE4; border: 1px solid #4A6741; border-radius: 4px; }\n"
"#successBanner QLabel { color: #4A6741; font-size: 12px; border: none; background: transparent; }\n"
"#errorBanner { background-color: #F5E8E6; border: 1px solid #B54A3A; border-radius: 4px; }\n"
"#errorBanner QLabel { color: #B54A3A; font-size: 12px; border: none; background: transparent; }\n"
"\n"
"QTableWidget { background-color: #FFFFFF; border: 1px solid #D4CBBE; outline: none; }\n"
"QHeaderView::section { background-color: #EDE6D9; color: #6B6560; font-size: 11px; font-weight: 600; border: none; border-bottom: 1px solid #D4CBBE; padding: 7px 10px; }\n"
"QTableWidget::item { border-bottom: 1px solid #D4CBBE; padding: 7px 10px; color: #2C2A26; font-size: 12px; }\n"
"\n"
"#modeBar { background: transparent; border: none; }\n"
"#btn_mode_import, #btn_mode_export, #btn_mode_gpx { background-color: #FFFFFF; color: #6B6560; border: 1px solid #D4CBBE; padding: 7px 16px; font-size: 12px; border-radiu"
                        "s: 4px; }\n"
"#btn_mode_import:hover, #btn_mode_export:hover, #btn_mode_gpx:hover { color: #2C2A26; border: 1px solid #4A6741; }\n"
"#btn_mode_import:checked, #btn_mode_export:checked, #btn_mode_gpx:checked { background-color: #4A6741; color: #FFFFFF; border: 1px solid #4A6741; font-weight: 600; }\n"
"\n"
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

        self.modeBar = QFrame(self.centralwidget)
        self.modeBar.setObjectName(u"modeBar")
        self.modeLayout = QHBoxLayout(self.modeBar)
        self.modeLayout.setSpacing(8)
        self.modeLayout.setObjectName(u"modeLayout")
        self.modeLayout.setContentsMargins(24, 12, 24, 0)
        self.btn_mode_import = QPushButton(self.modeBar)
        self.btn_mode_import.setObjectName(u"btn_mode_import")
        self.btn_mode_import.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_mode_import.setCheckable(True)
        self.btn_mode_import.setChecked(True)
        self.btn_mode_import.setAutoExclusive(True)

        self.modeLayout.addWidget(self.btn_mode_import)

        self.btn_mode_export = QPushButton(self.modeBar)
        self.btn_mode_export.setObjectName(u"btn_mode_export")
        self.btn_mode_export.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_mode_export.setCheckable(True)
        self.btn_mode_export.setChecked(False)
        self.btn_mode_export.setAutoExclusive(True)

        self.modeLayout.addWidget(self.btn_mode_export)

        self.btn_mode_gpx = QPushButton(self.modeBar)
        self.btn_mode_gpx.setObjectName(u"btn_mode_gpx")
        self.btn_mode_gpx.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_mode_gpx.setCheckable(True)
        self.btn_mode_gpx.setChecked(False)
        self.btn_mode_gpx.setAutoExclusive(True)

        self.modeLayout.addWidget(self.btn_mode_gpx)

        self.modeSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.modeLayout.addItem(self.modeSpacer)


        self.verticalLayout.addWidget(self.modeBar)

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

        self.dropArea = QFrame(self.formCard)
        self.dropArea.setObjectName(u"dropArea")
        self.dropArea.setMinimumSize(QSize(0, 120))
        self.dropArea.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.dropLayout = QVBoxLayout(self.dropArea)
        self.dropLayout.setSpacing(8)
        self.dropLayout.setObjectName(u"dropLayout")
        self.lbl_drop_main = QLabel(self.dropArea)
        self.lbl_drop_main.setObjectName(u"lbl_drop_main")

        self.dropLayout.addWidget(self.lbl_drop_main)

        self.lbl_drop_sub = QLabel(self.dropArea)
        self.lbl_drop_sub.setObjectName(u"lbl_drop_sub")

        self.dropLayout.addWidget(self.lbl_drop_sub)


        self.formLayout.addWidget(self.dropArea)

        self.typeLayout = QVBoxLayout()
        self.typeLayout.setSpacing(5)
        self.typeLayout.setObjectName(u"typeLayout")
        self.fieldLabel = QLabel(self.formCard)
        self.fieldLabel.setObjectName(u"fieldLabel")

        self.typeLayout.addWidget(self.fieldLabel)

        self.comboType = QComboBox(self.formCard)
        self.comboType.addItem("")
        self.comboType.addItem("")
        self.comboType.addItem("")
        self.comboType.addItem("")
        self.comboType.setObjectName(u"comboType")
        self.comboType.setMaximumSize(QSize(250, 16777215))

        self.typeLayout.addWidget(self.comboType)


        self.formLayout.addLayout(self.typeLayout)

        self.btn_import = QPushButton(self.formCard)
        self.btn_import.setObjectName(u"btn_import")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btn_import.sizePolicy().hasHeightForWidth())
        self.btn_import.setSizePolicy(sizePolicy1)
        self.btn_import.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.formLayout.addWidget(self.btn_import)

        self.successBanner = QFrame(self.formCard)
        self.successBanner.setObjectName(u"successBanner")
        self.successBanner.setVisible(False)
        self.successLayout = QHBoxLayout(self.successBanner)
        self.successLayout.setObjectName(u"successLayout")
        self.successLayout.setContentsMargins(12, 8, 12, 8)
        self.lbl_success = QLabel(self.successBanner)
        self.lbl_success.setObjectName(u"lbl_success")

        self.successLayout.addWidget(self.lbl_success)


        self.formLayout.addWidget(self.successBanner)

        self.errorBanner = QFrame(self.formCard)
        self.errorBanner.setObjectName(u"errorBanner")
        self.errorBanner.setVisible(False)
        self.errorLayout = QHBoxLayout(self.errorBanner)
        self.errorLayout.setObjectName(u"errorLayout")
        self.errorLayout.setContentsMargins(12, 8, 12, 8)
        self.lbl_error = QLabel(self.errorBanner)
        self.lbl_error.setObjectName(u"lbl_error")

        self.errorLayout.addWidget(self.lbl_error)


        self.formLayout.addWidget(self.errorBanner)

        self.errorTable = QTableWidget(self.formCard)
        if (self.errorTable.columnCount() < 3):
            self.errorTable.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.errorTable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.errorTable.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.errorTable.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.errorTable.setObjectName(u"errorTable")
        self.errorTable.setMinimumSize(QSize(0, 150))
        self.errorTable.setVisible(False)
        self.errorTable.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.errorTable.setShowGrid(False)

        self.formLayout.addWidget(self.errorTable)


        self.centerLayout.addWidget(self.formCard)

        self.rightSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.centerLayout.addItem(self.rightSpacer)


        self.verticalLayout.addLayout(self.centerLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(1)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy2)
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

        self.tabWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"ImportWindow", None))
        self.logo.setText("")
        self.name.setText(QCoreApplication.translate("MainWindow", u"\u041b\u0435\u0433\u0435\u043d\u0434\u044b \u041f\u0430\u0440\u043c\u044b", None))
        self.name_chart.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043c\u043f\u043e\u0440\u0442 \u0434\u0430\u043d\u043d\u044b\u0445", None))
        self.status_lb.setText("")
        self.role_lb.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044c", None))
        self.logout_btn.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0439\u0442\u0438", None))
        self.btn_mode_import.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043c\u043f\u043e\u0440\u0442", None))
        self.btn_mode_export.setText(QCoreApplication.translate("MainWindow", u"\u042d\u043a\u0441\u043f\u043e\u0440\u0442", None))
        self.btn_mode_gpx.setText(QCoreApplication.translate("MainWindow", u"\u042d\u043a\u0441\u043f\u043e\u0440\u0442 GPX", None))
        self.lbl_form_title.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043c\u043f\u043e\u0440\u0442 \u0434\u0430\u043d\u043d\u044b\u0445", None))
        self.lbl_drop_main.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0440\u0435\u0442\u0430\u0449\u0438\u0442\u0435 \u0444\u0430\u0439\u043b (CSV, Excel, JSON)", None))
        self.lbl_drop_sub.setText(QCoreApplication.translate("MainWindow", u"\u0438\u043b\u0438 \u043d\u0430\u0436\u043c\u0438\u0442\u0435 \u0434\u043b\u044f \u0432\u044b\u0431\u043e\u0440\u0430", None))
        self.fieldLabel.setText(QCoreApplication.translate("MainWindow", u"\u0427\u0442\u043e \u0438\u043c\u043f\u043e\u0440\u0442\u0438\u0440\u0443\u0435\u043c", None))
        self.comboType.setItemText(0, QCoreApplication.translate("MainWindow", u"\u041c\u0430\u0440\u0448\u0440\u0443\u0442\u044b / \u0422\u043e\u0447\u043a\u0438 / \u0417\u0430\u043f\u043e\u0432\u0435\u0434\u043d\u0438\u043a\u0438", None))
        self.comboType.setItemText(1, QCoreApplication.translate("MainWindow", u"\u041c\u0430\u0440\u0448\u0440\u0443\u0442\u044b", None))
        self.comboType.setItemText(2, QCoreApplication.translate("MainWindow", u"\u0422\u043e\u0447\u043a\u0438", None))
        self.comboType.setItemText(3, QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043f\u043e\u0432\u0435\u0434\u043d\u0438\u043a\u0438", None))

        self.btn_import.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043c\u043f\u043e\u0440\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.lbl_success.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u043b\u0435\u043d\u043e 10 \u00b7 \u043e\u0431\u043d\u043e\u0432\u043b\u0435\u043d\u043e 2 \u00b7 \u043f\u0440\u043e\u043f\u0443\u0449\u0435\u043d\u043e 0", None))
        self.lbl_error.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0440\u043e\u043a\u0430 5, \u043f\u043e\u043b\u0435 \"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435\": \u043d\u0435 \u043c\u043e\u0436\u0435\u0442 \u0431\u044b\u0442\u044c \u043f\u0443\u0441\u0442\u044b\u043c", None))
        ___qtablewidgetitem = self.errorTable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0440\u043e\u043a\u0430", None))
        ___qtablewidgetitem1 = self.errorTable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043b\u0435", None))
        ___qtablewidgetitem2 = self.errorTable.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0438\u0447\u0438\u043d\u0430", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_8), QCoreApplication.translate("MainWindow", u"\u041a\u0430\u0442\u0430\u043b\u043e\u0433 \u043c\u0430\u0440\u0448\u0440\u0443\u0442\u043e\u0432", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_9), QCoreApplication.translate("MainWindow", u"\u0422\u0443\u0440\u044b", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_10), QCoreApplication.translate("MainWindow", u"\u0418\u043c\u043f\u043e\u0440\u0442 \u0438 \u044d\u043a\u0441\u043f\u043e\u0440\u0442", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_11), QCoreApplication.translate("MainWindow", u"\u0421\u0438\u043d\u0445\u0440\u043e\u043d\u0438\u0437\u0430\u0446\u0438\u044f", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_12), QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u0438", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_13), QCoreApplication.translate("MainWindow", u"\u0416\u0443\u0440\u043d\u0430\u043b \u0430\u0443\u0434\u0438\u0442\u0430", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_14), QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438 API \u0438 \u043a\u0435\u0448", None))
    # retranslateUi

