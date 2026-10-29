# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'set_api_hash_window.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QSpinBox, QTabWidget, QVBoxLayout,
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
"#logout_btn:focus { border: 1px dashed #F5F0E8; }\n"
"\n"
"#contentFrame { background-color: #F5F0E8; }\n"
"#leftPanel, #rightPanel { background-color: #FFFFFF; border: 1px solid #D4CBBE; border-radius: 4px; }\n"
"#title_cache, #title_api { font-size: 14px; font-weight: 600; color: #2C2A26; }\n"
"#lbl_ttl, #lbl_api_key, #lbl_osm, #lbl_timeout { font-size: 12px; color: #6B6560; }\n"
"#lbl_stats { font-size: 12px; color: #6B6560; }\n"
"\n"
"QLineEdit, QSpinBox {\n"
""
                        "    padding: 10px 12px; font-size: 14px; border-radius: 4px; border: 1px solid #D4CBBE; background-color: #FFFFFF; color: #2C2A26;\n"
"}\n"
"QLineEdit:hover, QSpinBox:hover { border: 1px solid #B8AE9E; }\n"
"QLineEdit:focus, QSpinBox:focus { border: 1px solid #4A6741; }\n"
"QLineEdit[error=\"true\"], QSpinBox[error=\"true\"] { border: 1px solid #B54A3A; }\n"
"QLineEdit:disabled, QSpinBox:disabled { border: 1px dashed #D4CBBE; color: #A39E94; background-color: #F5F0E8; }\n"
"\n"
"#btn_clear_cache { background-color: #FFFFFF; color: #B54A3A; border: 1px solid #B54A3A; padding: 11px 16px; font-size: 14px; border-radius: 4px; }\n"
"#btn_clear_cache:hover { background-color: #F5E8E6; }\n"
"#btn_clear_cache:pressed { background-color: #EBD5D1; }\n"
"#btn_clear_cache:disabled { background-color: #FFFFFF; color: #D4A39C; border: 1px solid #E5C4BF; }\n"
"#btn_clear_cache:focus { border: 1px dashed #4A6741; }\n"
"\n"
"#btn_save_cache, #btn_check_conn { background-color: #FFFFFF; color: #2C2A26; border: 1px solid #D4CBBE"
                        "; padding: 11px 16px; font-size: 14px; border-radius: 4px; }\n"
"#btn_save_cache:hover, #btn_check_conn:hover { border: 1px solid #4A6741; background-color: #F5F0E8; }\n"
"#btn_save_cache:pressed, #btn_check_conn:pressed { background-color: #EDE6D9; }\n"
"#btn_save_cache:disabled, #btn_check_conn:disabled { background-color: #FFFFFF; color: #A39E94; border: 1px solid #E5DFD4; }\n"
"#btn_save_cache:focus, #btn_check_conn:focus { border: 1px dashed #4A6741; }\n"
"\n"
"#btn_save_api { background-color: #4A6741; color: #FFFFFF; border: none; padding: 11px 16px; font-size: 14px; font-weight: 600; border-radius: 4px; }\n"
"#btn_save_api:hover { background-color: #3D5636; }\n"
"#btn_save_api:pressed { background-color: #334A2E; }\n"
"#btn_save_api:disabled { background-color: #A8B5A0; }\n"
"#btn_save_api:focus { border: 1px dashed #4A6741; }\n"
"\n"
"QTabWidget::panel { border: none; background-color: #FFFFFF; }\n"
"QTabBar { background-color: #FFFFFF; border: none; qproperty-drawBase: 0; qproperty-expanding: true; }"
                        "\n"
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

        self.contentFrame = QFrame(self.centralwidget)
        self.contentFrame.setObjectName(u"contentFrame")
        self.contentLayout = QVBoxLayout(self.contentFrame)
        self.contentLayout.setSpacing(0)
        self.contentLayout.setObjectName(u"contentLayout")
        self.contentLayout.setContentsMargins(16, 16, 16, 16)
        self.lbl_form_title = QLabel(self.contentFrame)
        self.lbl_form_title.setObjectName(u"lbl_form_title")
        self.lbl_form_title.setStyleSheet(u"font-size: 16px; font-weight: 600; color: #2C2A26; margin-bottom: 14px;")

        self.contentLayout.addWidget(self.lbl_form_title)

        self.mainLayout = QHBoxLayout()
        self.mainLayout.setSpacing(14)
        self.mainLayout.setObjectName(u"mainLayout")
        self.leftPanel = QFrame(self.contentFrame)
        self.leftPanel.setObjectName(u"leftPanel")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.leftPanel.sizePolicy().hasHeightForWidth())
        self.leftPanel.setSizePolicy(sizePolicy)
        self.leftLayout = QVBoxLayout(self.leftPanel)
        self.leftLayout.setSpacing(14)
        self.leftLayout.setObjectName(u"leftLayout")
        self.leftLayout.setContentsMargins(14, 14, 14, 14)
        self.title_cache = QLabel(self.leftPanel)
        self.title_cache.setObjectName(u"title_cache")

        self.leftLayout.addWidget(self.title_cache)

        self.ttlLayout = QVBoxLayout()
        self.ttlLayout.setSpacing(5)
        self.ttlLayout.setObjectName(u"ttlLayout")
        self.lbl_ttl = QLabel(self.leftPanel)
        self.lbl_ttl.setObjectName(u"lbl_ttl")

        self.ttlLayout.addWidget(self.lbl_ttl)

        self.input_ttl = QSpinBox(self.leftPanel)
        self.input_ttl.setObjectName(u"input_ttl")
        self.input_ttl.setMaximum(999999)
        self.input_ttl.setValue(86400)

        self.ttlLayout.addWidget(self.input_ttl)


        self.leftLayout.addLayout(self.ttlLayout)

        self.statsLayout = QVBoxLayout()
        self.statsLayout.setSpacing(5)
        self.statsLayout.setObjectName(u"statsLayout")
        self.lbl_stats = QLabel(self.leftPanel)
        self.lbl_stats.setObjectName(u"lbl_stats")

        self.statsLayout.addWidget(self.lbl_stats)

        self.statsValue = QLabel(self.leftPanel)
        self.statsValue.setObjectName(u"statsValue")

        self.statsLayout.addWidget(self.statsValue)


        self.leftLayout.addLayout(self.statsLayout)

        self.leftSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.leftLayout.addItem(self.leftSpacer)

        self.btn_clear_cache = QPushButton(self.leftPanel)
        self.btn_clear_cache.setObjectName(u"btn_clear_cache")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btn_clear_cache.sizePolicy().hasHeightForWidth())
        self.btn_clear_cache.setSizePolicy(sizePolicy1)
        self.btn_clear_cache.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.leftLayout.addWidget(self.btn_clear_cache)

        self.btn_save_cache = QPushButton(self.leftPanel)
        self.btn_save_cache.setObjectName(u"btn_save_cache")
        sizePolicy1.setHeightForWidth(self.btn_save_cache.sizePolicy().hasHeightForWidth())
        self.btn_save_cache.setSizePolicy(sizePolicy1)
        self.btn_save_cache.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.leftLayout.addWidget(self.btn_save_cache)


        self.mainLayout.addWidget(self.leftPanel)

        self.rightPanel = QFrame(self.contentFrame)
        self.rightPanel.setObjectName(u"rightPanel")
        sizePolicy.setHeightForWidth(self.rightPanel.sizePolicy().hasHeightForWidth())
        self.rightPanel.setSizePolicy(sizePolicy)
        self.rightLayout = QVBoxLayout(self.rightPanel)
        self.rightLayout.setSpacing(14)
        self.rightLayout.setObjectName(u"rightLayout")
        self.rightLayout.setContentsMargins(14, 14, 14, 14)
        self.title_api = QLabel(self.rightPanel)
        self.title_api.setObjectName(u"title_api")

        self.rightLayout.addWidget(self.title_api)

        self.apiKeyLayout = QVBoxLayout()
        self.apiKeyLayout.setSpacing(5)
        self.apiKeyLayout.setObjectName(u"apiKeyLayout")
        self.lbl_api_key = QLabel(self.rightPanel)
        self.lbl_api_key.setObjectName(u"lbl_api_key")

        self.apiKeyLayout.addWidget(self.lbl_api_key)

        self.input_api_key = QLineEdit(self.rightPanel)
        self.input_api_key.setObjectName(u"input_api_key")
        self.input_api_key.setEchoMode(QLineEdit.EchoMode.Password)

        self.apiKeyLayout.addWidget(self.input_api_key)


        self.rightLayout.addLayout(self.apiKeyLayout)

        self.osmLayout = QVBoxLayout()
        self.osmLayout.setSpacing(5)
        self.osmLayout.setObjectName(u"osmLayout")
        self.lbl_osm = QLabel(self.rightPanel)
        self.lbl_osm.setObjectName(u"lbl_osm")

        self.osmLayout.addWidget(self.lbl_osm)

        self.input_osm = QLineEdit(self.rightPanel)
        self.input_osm.setObjectName(u"input_osm")

        self.osmLayout.addWidget(self.input_osm)


        self.rightLayout.addLayout(self.osmLayout)

        self.timeoutLayout = QVBoxLayout()
        self.timeoutLayout.setSpacing(5)
        self.timeoutLayout.setObjectName(u"timeoutLayout")
        self.lbl_timeout = QLabel(self.rightPanel)
        self.lbl_timeout.setObjectName(u"lbl_timeout")

        self.timeoutLayout.addWidget(self.lbl_timeout)

        self.input_timeout = QSpinBox(self.rightPanel)
        self.input_timeout.setObjectName(u"input_timeout")
        self.input_timeout.setMaximum(999)
        self.input_timeout.setValue(10)

        self.timeoutLayout.addWidget(self.input_timeout)


        self.rightLayout.addLayout(self.timeoutLayout)

        self.rightSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.rightLayout.addItem(self.rightSpacer)

        self.rightButtonsLayout = QHBoxLayout()
        self.rightButtonsLayout.setSpacing(8)
        self.rightButtonsLayout.setObjectName(u"rightButtonsLayout")
        self.btn_check_conn = QPushButton(self.rightPanel)
        self.btn_check_conn.setObjectName(u"btn_check_conn")
        self.btn_check_conn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.rightButtonsLayout.addWidget(self.btn_check_conn)

        self.btn_save_api = QPushButton(self.rightPanel)
        self.btn_save_api.setObjectName(u"btn_save_api")
        self.btn_save_api.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.rightButtonsLayout.addWidget(self.btn_save_api)

        self.rightBtnSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.rightButtonsLayout.addItem(self.rightBtnSpacer)


        self.rightLayout.addLayout(self.rightButtonsLayout)


        self.mainLayout.addWidget(self.rightPanel)


        self.contentLayout.addLayout(self.mainLayout)


        self.verticalLayout.addWidget(self.contentFrame)

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

        self.tabWidget.setCurrentIndex(6)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"SettingsAPI_Window", None))
        self.logo.setText("")
        self.name.setText(QCoreApplication.translate("MainWindow", u"\u041b\u0435\u0433\u0435\u043d\u0434\u044b \u041f\u0430\u0440\u043c\u044b", None))
        self.name_chart.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438 API \u0438 \u043a\u0435\u0448", None))
        self.status_lb.setText("")
        self.role_lb.setText(QCoreApplication.translate("MainWindow", u"\u0410\u0434\u043c\u0438\u043d\u0438\u0441\u0442\u0440\u0430\u0442\u043e\u0440", None))
        self.logout_btn.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0439\u0442\u0438", None))
        self.lbl_form_title.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438 API \u0438 \u043a\u0435\u0448\u0430", None))
        self.title_cache.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0435\u0448", None))
        self.lbl_ttl.setText(QCoreApplication.translate("MainWindow", u"TTL, \u0441\u0435\u043a\u0443\u043d\u0434\u044b", None))
        self.lbl_stats.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0430\u0442\u0438\u0441\u0442\u0438\u043a\u0430 \u043a\u0435\u0448\u0430", None))
        self.statsValue.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043f\u0438\u0441\u0435\u0439: \u2014 \u00b7 \u0420\u0430\u0437\u043c\u0435\u0440: \u2014", None))
        self.btn_clear_cache.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0447\u0438\u0441\u0442\u0438\u0442\u044c \u043a\u0435\u0448", None))
        self.btn_save_cache.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.title_api.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438 API", None))
        self.lbl_api_key.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043b\u044e\u0447 OpenWeather (\u043c\u0430\u0441\u043a\u0430)", None))
        self.lbl_osm.setText(QCoreApplication.translate("MainWindow", u"Endpoint OSM / Overpass", None))
        self.lbl_timeout.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0430\u0439\u043c\u0430\u0443\u0442, \u0441", None))
        self.btn_check_conn.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0432\u0435\u0440\u0438\u0442\u044c \u0441\u043e\u0435\u0434\u0438\u043d\u0435\u043d\u0438\u0435", None))
        self.btn_save_api.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_8), QCoreApplication.translate("MainWindow", u"\u041a\u0430\u0442\u0430\u043b\u043e\u0433 \u043c\u0430\u0440\u0448\u0440\u0443\u0442\u043e\u0432", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_9), QCoreApplication.translate("MainWindow", u"\u0422\u0443\u0440\u044b", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_10), QCoreApplication.translate("MainWindow", u"\u0418\u043c\u043f\u043e\u0440\u0442 \u0438 \u044d\u043a\u0441\u043f\u043e\u0440\u0442", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_11), QCoreApplication.translate("MainWindow", u"\u0421\u0438\u043d\u0445\u0440\u043e\u043d\u0438\u0437\u0430\u0446\u0438\u044f", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_12), QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u0438", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_13), QCoreApplication.translate("MainWindow", u"\u0416\u0443\u0440\u043d\u0430\u043b \u0430\u0443\u0434\u0438\u0442\u0430", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_14), QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438 API \u0438 \u043a\u0435\u0448", None))
    # retranslateUi

