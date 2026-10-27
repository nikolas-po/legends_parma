# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'export_data_window.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QGridLayout, QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QTabWidget, QVBoxLayout, QWidget)
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
"#logout_btn:focus { border: 1px dashed #F5F0E8; }\n"
"\n"
"#formCard { background-color: #FFFFFF; border: 1px solid #D4CBBE; border-radius: 4px; }\n"
"#lbl_form_title { font-size: 16px; font-weight: 600; color: #2C2A26; }\n"
"#lbl_dataset, #lbl_format, #lbl_columns, #lbl_path { font-size: 12px; color: #6B6560; }\n"
"\n"
"QLineEdit, QComboBox { padding: 10px 12px; font-size: 14px; border-radius: 4px; border: 1px solid #D4CBBE; background-color: #FFFFFF; color: #2C2A"
                        "26; }\n"
"QLineEdit:hover, QComboBox:hover { border: 1px solid #B8AE9E; }\n"
"QLineEdit:focus, QComboBox:focus { border: 1px solid #4A6741; }\n"
"QLineEdit[error=\"true\"], QComboBox[error=\"true\"] { border: 1px solid #B54A3A; }\n"
"QLineEdit:disabled, QComboBox:disabled { border: 1px dashed #D4CBBE; color: #A39E94; background-color: #F5F0E8; }\n"
"QComboBox QAbstractItemView { background-color: #FFFFFF; border: 1px solid #D4CBBE; selection-background-color: #E8EDE4; selection-color: #2C2A26; }\n"
"QComboBox QAbstractItemView::item:hover { background-color: #EDE6D9; }\n"
"\n"
"#columnsFrame { background-color: #FFFFFF; border: 1px solid #D4CBBE; border-radius: 4px; }\n"
"QCheckBox { spacing: 6px; font-size: 12px; color: #6B6560; background: transparent; }\n"
"QCheckBox::indicator { width: 15px; height: 15px; border-radius: 3px; border: 1px solid #D4CBBE; background-color: #FFFFFF; }\n"
"QCheckBox::indicator:hover { border: 1px solid #B8AE9E; }\n"
"QCheckBox::indicator:checked { background-color: #4A6741; bord"
                        "er: 1px solid #4A6741; }\n"
"QCheckBox::indicator:disabled { background-color: #E5DFD4; border: 1px solid #E5DFD4; }\n"
"QCheckBox:disabled { color: #A39E94; }\n"
"\n"
"#btn_export { background-color: #4A6741; color: #FFFFFF; border: none; padding: 11px 16px; font-size: 14px; font-weight: 600; border-radius: 4px; }\n"
"#btn_export:hover { background-color: #3D5636; }\n"
"#btn_export:pressed { background-color: #334A2E; }\n"
"#btn_export:disabled { background-color: #A8B5A0; }\n"
"#btn_export:focus { border: 1px dashed #4A6741; }\n"
"\n"
"#btn_browse { background-color: #FFFFFF; color: #2C2A26; border: 1px solid #D4CBBE; padding: 10px 16px; font-size: 14px; border-radius: 4px; }\n"
"#btn_browse:hover { border: 1px solid #4A6741; background-color: #F5F0E8; }\n"
"#btn_browse:pressed { background-color: #EDE6D9; }\n"
"#btn_browse:disabled { background-color: #FFFFFF; color: #A39E94; border: 1px solid #E5DFD4; }\n"
"#btn_browse:focus { border: 1px dashed #4A6741; }\n"
"\n"
"#successBanner { background-color: #E8EDE"
                        "4; border: 1px solid #4A6741; border-radius: 4px; }\n"
"#successBanner QLabel { color: #4A6741; font-size: 12px; border: none; background: transparent; }\n"
"#errorBanner { background-color: #F5E8E6; border: 1px solid #B54A3A; border-radius: 4px; }\n"
"#errorBanner QLabel { color: #B54A3A; font-size: 12px; border: none; background: transparent; }\n"
"\n"
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

        self.datasetLayout = QVBoxLayout()
        self.datasetLayout.setSpacing(5)
        self.datasetLayout.setObjectName(u"datasetLayout")
        self.lbl_dataset = QLabel(self.formCard)
        self.lbl_dataset.setObjectName(u"lbl_dataset")

        self.datasetLayout.addWidget(self.lbl_dataset)

        self.comboDataset = QComboBox(self.formCard)
        self.comboDataset.addItem("")
        self.comboDataset.addItem("")
        self.comboDataset.addItem("")
        self.comboDataset.addItem("")
        self.comboDataset.setObjectName(u"comboDataset")
        self.comboDataset.setMaximumSize(QSize(300, 16777215))

        self.datasetLayout.addWidget(self.comboDataset)


        self.formLayout.addLayout(self.datasetLayout)

        self.formatLayout = QVBoxLayout()
        self.formatLayout.setSpacing(5)
        self.formatLayout.setObjectName(u"formatLayout")
        self.lbl_format = QLabel(self.formCard)
        self.lbl_format.setObjectName(u"lbl_format")

        self.formatLayout.addWidget(self.lbl_format)

        self.comboFormat = QComboBox(self.formCard)
        self.comboFormat.addItem("")
        self.comboFormat.addItem("")
        self.comboFormat.addItem("")
        self.comboFormat.setObjectName(u"comboFormat")
        self.comboFormat.setMaximumSize(QSize(150, 16777215))

        self.formatLayout.addWidget(self.comboFormat)


        self.formLayout.addLayout(self.formatLayout)

        self.columnsLayout = QVBoxLayout()
        self.columnsLayout.setSpacing(5)
        self.columnsLayout.setObjectName(u"columnsLayout")
        self.lbl_columns = QLabel(self.formCard)
        self.lbl_columns.setObjectName(u"lbl_columns")

        self.columnsLayout.addWidget(self.lbl_columns)

        self.columnsFrame = QFrame(self.formCard)
        self.columnsFrame.setObjectName(u"columnsFrame")
        self.columnsFrame.setMinimumSize(QSize(0, 100))
        self.columnsGrid = QGridLayout(self.columnsFrame)
        self.columnsGrid.setSpacing(8)
        self.columnsGrid.setObjectName(u"columnsGrid")
        self.columnsGrid.setContentsMargins(12, 12, 12, 12)
        self.chkCol1 = QCheckBox(self.columnsFrame)
        self.chkCol1.setObjectName(u"chkCol1")
        self.chkCol1.setChecked(True)

        self.columnsGrid.addWidget(self.chkCol1, 0, 0, 1, 1)

        self.chkCol2 = QCheckBox(self.columnsFrame)
        self.chkCol2.setObjectName(u"chkCol2")
        self.chkCol2.setChecked(True)

        self.columnsGrid.addWidget(self.chkCol2, 0, 1, 1, 1)

        self.chkCol3 = QCheckBox(self.columnsFrame)
        self.chkCol3.setObjectName(u"chkCol3")
        self.chkCol3.setChecked(True)

        self.columnsGrid.addWidget(self.chkCol3, 0, 2, 1, 1)

        self.chkCol4 = QCheckBox(self.columnsFrame)
        self.chkCol4.setObjectName(u"chkCol4")
        self.chkCol4.setChecked(True)

        self.columnsGrid.addWidget(self.chkCol4, 1, 0, 1, 1)

        self.chkCol5 = QCheckBox(self.columnsFrame)
        self.chkCol5.setObjectName(u"chkCol5")
        self.chkCol5.setChecked(True)

        self.columnsGrid.addWidget(self.chkCol5, 1, 1, 1, 1)

        self.chkCol6 = QCheckBox(self.columnsFrame)
        self.chkCol6.setObjectName(u"chkCol6")
        self.chkCol6.setChecked(True)

        self.columnsGrid.addWidget(self.chkCol6, 1, 2, 1, 1)


        self.columnsLayout.addWidget(self.columnsFrame)


        self.formLayout.addLayout(self.columnsLayout)

        self.pathLayout = QVBoxLayout()
        self.pathLayout.setSpacing(5)
        self.pathLayout.setObjectName(u"pathLayout")
        self.lbl_path = QLabel(self.formCard)
        self.lbl_path.setObjectName(u"lbl_path")

        self.pathLayout.addWidget(self.lbl_path)

        self.pathInputLayout = QHBoxLayout()
        self.pathInputLayout.setSpacing(8)
        self.pathInputLayout.setObjectName(u"pathInputLayout")
        self.inputPath = QLineEdit(self.formCard)
        self.inputPath.setObjectName(u"inputPath")

        self.pathInputLayout.addWidget(self.inputPath)

        self.btn_browse = QPushButton(self.formCard)
        self.btn_browse.setObjectName(u"btn_browse")
        self.btn_browse.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.pathInputLayout.addWidget(self.btn_browse)


        self.pathLayout.addLayout(self.pathInputLayout)


        self.formLayout.addLayout(self.pathLayout)

        self.btn_export = QPushButton(self.formCard)
        self.btn_export.setObjectName(u"btn_export")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btn_export.sizePolicy().hasHeightForWidth())
        self.btn_export.setSizePolicy(sizePolicy1)
        self.btn_export.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.formLayout.addWidget(self.btn_export)

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


        self.centerLayout.addWidget(self.formCard)

        self.rightSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.centerLayout.addItem(self.rightSpacer)


        self.verticalLayout.addLayout(self.centerLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
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

        self.tabWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"ExportWindow", None))
        self.logo.setText("")
        self.name.setText(QCoreApplication.translate("MainWindow", u"\u041b\u0435\u0433\u0435\u043d\u0434\u044b \u041f\u0430\u0440\u043c\u044b", None))
        self.name_chart.setText(QCoreApplication.translate("MainWindow", u"\u042d\u043a\u0441\u043f\u043e\u0440\u0442 \u0434\u0430\u043d\u043d\u044b\u0445", None))
        self.status_lb.setText("")
        self.role_lb.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044c", None))
        self.logout_btn.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0439\u0442\u0438", None))
        self.lbl_form_title.setText(QCoreApplication.translate("MainWindow", u"\u042d\u043a\u0441\u043f\u043e\u0440\u0442 \u0434\u0430\u043d\u043d\u044b\u0445", None))
        self.lbl_dataset.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0431\u043e\u0440 \u0434\u0430\u043d\u043d\u044b\u0445", None))
        self.comboDataset.setItemText(0, QCoreApplication.translate("MainWindow", u"\u041c\u0430\u0440\u0448\u0440\u0443\u0442\u044b / \u0422\u043e\u0447\u043a\u0438 / \u0417\u0430\u043f\u043e\u0432\u0435\u0434\u043d\u0438\u043a\u0438", None))
        self.comboDataset.setItemText(1, QCoreApplication.translate("MainWindow", u"\u041c\u0430\u0440\u0448\u0440\u0443\u0442\u044b", None))
        self.comboDataset.setItemText(2, QCoreApplication.translate("MainWindow", u"\u0422\u043e\u0447\u043a\u0438", None))
        self.comboDataset.setItemText(3, QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043f\u043e\u0432\u0435\u0434\u043d\u0438\u043a\u0438", None))

        self.lbl_format.setText(QCoreApplication.translate("MainWindow", u"\u0424\u043e\u0440\u043c\u0430\u0442 (CSV / Excel / JSON)", None))
        self.comboFormat.setItemText(0, QCoreApplication.translate("MainWindow", u"CSV", None))
        self.comboFormat.setItemText(1, QCoreApplication.translate("MainWindow", u"Excel", None))
        self.comboFormat.setItemText(2, QCoreApplication.translate("MainWindow", u"JSON", None))

        self.lbl_columns.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043b\u043e\u043d\u043a\u0438", None))
        self.chkCol1.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435", None))
        self.chkCol2.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0438\u043f", None))
        self.chkCol3.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0442\u044f\u0436\u0451\u043d\u043d\u043e\u0441\u0442\u044c", None))
        self.chkCol4.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0440\u0435\u043c\u044f", None))
        self.chkCol5.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0433\u0438\u043e\u043d", None))
        self.chkCol6.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0439\u0442\u0438\u043d\u0433", None))
        self.lbl_path.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0443\u0442\u044c \u043a \u0444\u0430\u0439\u043b\u0443", None))
        self.inputPath.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0423\u043a\u0430\u0436\u0438\u0442\u0435 \u043f\u0443\u0442\u044c \u0441\u043e\u0445\u0440\u0430\u043d\u0435\u043d\u0438\u044f...", None))
        self.btn_browse.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u0437\u043e\u0440...", None))
        self.btn_export.setText(QCoreApplication.translate("MainWindow", u"\u042d\u043a\u0441\u043f\u043e\u0440\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.lbl_success.setText(QCoreApplication.translate("MainWindow", u"\u042d\u043a\u0441\u043f\u043e\u0440\u0442 \u0443\u0441\u043f\u0435\u0448\u043d\u043e \u0437\u0430\u0432\u0435\u0440\u0448\u0451\u043d", None))
        self.lbl_error.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0448\u0438\u0431\u043a\u0430 \u0434\u043e\u0441\u0442\u0443\u043f\u0430 \u0438\u043b\u0438 \u043d\u0435\u0442 \u043c\u0435\u0441\u0442\u0430 \u043d\u0430 \u0434\u0438\u0441\u043a\u0435", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_8), QCoreApplication.translate("MainWindow", u"\u041a\u0430\u0442\u0430\u043b\u043e\u0433 \u043c\u0430\u0440\u0448\u0440\u0443\u0442\u043e\u0432", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_9), QCoreApplication.translate("MainWindow", u"\u0422\u0443\u0440\u044b", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_10), QCoreApplication.translate("MainWindow", u"\u0418\u043c\u043f\u043e\u0440\u0442 \u0438 \u044d\u043a\u0441\u043f\u043e\u0440\u0442", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_11), QCoreApplication.translate("MainWindow", u"\u0421\u0438\u043d\u0445\u0440\u043e\u043d\u0438\u0437\u0430\u0446\u0438\u044f", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_12), QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u0438", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_13), QCoreApplication.translate("MainWindow", u"\u0416\u0443\u0440\u043d\u0430\u043b \u0430\u0443\u0434\u0438\u0442\u0430", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_14), QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438 API \u0438 \u043a\u0435\u0448", None))
    # retranslateUi

