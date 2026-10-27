# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'create_tour_window.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QFrame,
    QHBoxLayout, QLabel, QLineEdit, QListWidget,
    QListWidgetItem, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QTabWidget, QVBoxLayout, QWidget)
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
"#formContainer { background-color: #F5F0E8; }\n"
"#btn_back { font-size: 12px; color: #6B6560; background: transparent; border: none; text-align: left; padding: 4px 8px; border-radius: 4px; }\n"
"#btn_back:hover { background: #EDE6D9; }\n"
"#btn_back:focus { border: 1px dashed #4A6741; }\n"
"#lbl_form_title { font-size: 16px; font-weight: 600; color: #2C2A26; }\n"
"\n"
"#formCard { background-color: #FFFFFF"
                        "; border: 1px solid #D4CBBE; border-radius: 4px; }\n"
"#sectionTitle { font-size: 14px; font-weight: 600; color: #2C2A26; }\n"
"#hintLabel { font-size: 11px; color: #A39E94; }\n"
"#fieldLabel { font-size: 12px; color: #6B6560; }\n"
"\n"
"QLineEdit, QDateEdit, QComboBox {\n"
"    padding: 10px 12px; font-size: 14px; border-radius: 4px; border: 1px solid #D4CBBE; background-color: #FFFFFF; color: #2C2A26; min-height: 20px;\n"
"}\n"
"QDateEdit::drop-down {\n"
"    subcontrol-origin: padding; subcontrol-position: top right; width: 28px; border-left: 1px solid #D4CBBE; background-color: #F5F0E8; border-top-right-radius: 4px; border-bottom-right-radius: 4px;\n"
"}\n"
"QLineEdit:hover, QDateEdit:hover, QComboBox:hover { border: 1px solid #B8AE9E; }\n"
"QLineEdit:focus, QDateEdit:focus, QComboBox:focus { border: 1px solid #4A6741; }\n"
"QLineEdit[error=\"true\"], QDateEdit[error=\"true\"], QComboBox[error=\"true\"] { border: 1px solid #B54A3A; }\n"
"QLineEdit:disabled, QDateEdit:disabled, QComboBox:disabled { border: "
                        "1px dashed #D4CBBE; color: #A39E94; background-color: #F5F0E8; }\n"
"\n"
"QComboBox QAbstractItemView { background-color: #FFFFFF; border: 1px solid #D4CBBE; selection-background-color: #E8EDE4; selection-color: #2C2A26; }\n"
"QComboBox QAbstractItemView::item:hover { background-color: #EDE6D9; }\n"
"\n"
"QListWidget { background-color: #FFFFFF; border: 1px solid #D4CBBE; border-radius: 4px; outline: none; }\n"
"QListWidget::item { padding: 8px 10px; font-size: 12px; color: #2C2A26; border-bottom: 1px solid #F0F0F0; }\n"
"QListWidget::item:hover { background-color: #EDE6D9; }\n"
"QListWidget::item:selected { background-color: #E8EDE4; color: #2C2A26; }\n"
"QListWidget[error=\"true\"] { border: 1px solid #B54A3A; }\n"
"QListWidget:disabled { border: 1px dashed #D4CBBE; color: #A39E94; background-color: #F5F0E8; }\n"
"\n"
"#actionBar { border-top: 1px solid #D4CBBE; }\n"
"\n"
"#btn_save { background-color: #4A6741; color: #FFFFFF; border: none; padding: 11px 16px; font-size: 14px; font-weight: 600; border-radius"
                        ": 4px; }\n"
"#btn_save:hover { background-color: #3D5636; }\n"
"#btn_save:pressed { background-color: #334A2E; }\n"
"#btn_save:disabled { background-color: #A8B5A0; }\n"
"#btn_save:focus { border: 1px dashed #4A6741; }\n"
"\n"
"#btn_cancel { background-color: #FFFFFF; color: #2C2A26; border: 1px solid #D4CBBE; padding: 11px 16px; font-size: 14px; font-weight: 600; border-radius: 4px; }\n"
"#btn_cancel:hover { background-color: #F5F0E8; border: 1px solid #4A6741; }\n"
"#btn_cancel:pressed { background-color: #EDE6D9; }\n"
"#btn_cancel:disabled { background-color: #FFFFFF; color: #A39E94; border: 1px solid #E5DFD4; }\n"
"#btn_cancel:focus { border: 1px dashed #4A6741; }\n"
"\n"
"QTabWidget::panel { border: none; background-color: #FFFFFF; }\n"
"QTabBar { background-color: #FFFFFF; border: none; }\n"
"QTabBar::tab { height: 40px; background-color: #FFFFFF; color: #6B6560; font-size: 12px; font-weight: normal; padding: 0px 30px; border: none; border-bottom: 2px solid transparent; border-top: 1px solid #D4CBBE; tex"
                        "t-align: center; }\n"
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

        self.formContainer = QFrame(self.centralwidget)
        self.formContainer.setObjectName(u"formContainer")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.formContainer.sizePolicy().hasHeightForWidth())
        self.formContainer.setSizePolicy(sizePolicy)
        self.formContainerLayout = QVBoxLayout(self.formContainer)
        self.formContainerLayout.setSpacing(14)
        self.formContainerLayout.setObjectName(u"formContainerLayout")
        self.formContainerLayout.setContentsMargins(24, 16, 24, 16)
        self.btn_back = QPushButton(self.formContainer)
        self.btn_back.setObjectName(u"btn_back")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btn_back.sizePolicy().hasHeightForWidth())
        self.btn_back.setSizePolicy(sizePolicy1)
        self.btn_back.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.formContainerLayout.addWidget(self.btn_back)

        self.lbl_form_title = QLabel(self.formContainer)
        self.lbl_form_title.setObjectName(u"lbl_form_title")

        self.formContainerLayout.addWidget(self.lbl_form_title)

        self.formCard = QFrame(self.formContainer)
        self.formCard.setObjectName(u"formCard")
        sizePolicy.setHeightForWidth(self.formCard.sizePolicy().hasHeightForWidth())
        self.formCard.setSizePolicy(sizePolicy)
        self.formCardLayout = QHBoxLayout(self.formCard)
        self.formCardLayout.setSpacing(24)
        self.formCardLayout.setObjectName(u"formCardLayout")
        self.formCardLayout.setContentsMargins(14, 14, 14, 14)
        self.leftColumnLayout = QVBoxLayout()
        self.leftColumnLayout.setSpacing(8)
        self.leftColumnLayout.setObjectName(u"leftColumnLayout")
        self.sectionTitle = QLabel(self.formCard)
        self.sectionTitle.setObjectName(u"sectionTitle")

        self.leftColumnLayout.addWidget(self.sectionTitle)

        self.hintLabel = QLabel(self.formCard)
        self.hintLabel.setObjectName(u"hintLabel")

        self.leftColumnLayout.addWidget(self.hintLabel)

        self.listRoutes = QListWidget(self.formCard)
        QListWidgetItem(self.listRoutes)
        QListWidgetItem(self.listRoutes)
        QListWidgetItem(self.listRoutes)
        self.listRoutes.setObjectName(u"listRoutes")
        sizePolicy.setHeightForWidth(self.listRoutes.sizePolicy().hasHeightForWidth())
        self.listRoutes.setSizePolicy(sizePolicy)

        self.leftColumnLayout.addWidget(self.listRoutes)


        self.formCardLayout.addLayout(self.leftColumnLayout)

        self.rightColumnFrame = QFrame(self.formCard)
        self.rightColumnFrame.setObjectName(u"rightColumnFrame")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(1)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.rightColumnFrame.sizePolicy().hasHeightForWidth())
        self.rightColumnFrame.setSizePolicy(sizePolicy2)
        self.rightColumnFrame.setFrameShape(QFrame.Shape.NoFrame)
        self.rightColumnLayout = QVBoxLayout(self.rightColumnFrame)
        self.rightColumnLayout.setSpacing(14)
        self.rightColumnLayout.setObjectName(u"rightColumnLayout")
        self.rightColumnLayout.setContentsMargins(0, 0, 0, 0)
        self.sectionTitle1 = QLabel(self.rightColumnFrame)
        self.sectionTitle1.setObjectName(u"sectionTitle1")

        self.rightColumnLayout.addWidget(self.sectionTitle1)

        self.nameLayout = QVBoxLayout()
        self.nameLayout.setSpacing(5)
        self.nameLayout.setObjectName(u"nameLayout")
        self.fieldLabel = QLabel(self.rightColumnFrame)
        self.fieldLabel.setObjectName(u"fieldLabel")

        self.nameLayout.addWidget(self.fieldLabel)

        self.inputName = QLineEdit(self.rightColumnFrame)
        self.inputName.setObjectName(u"inputName")

        self.nameLayout.addWidget(self.inputName)


        self.rightColumnLayout.addLayout(self.nameLayout)

        self.datesLayout = QHBoxLayout()
        self.datesLayout.setSpacing(10)
        self.datesLayout.setObjectName(u"datesLayout")
        self.startDateLayout = QVBoxLayout()
        self.startDateLayout.setSpacing(5)
        self.startDateLayout.setObjectName(u"startDateLayout")
        self.fieldLabel1 = QLabel(self.rightColumnFrame)
        self.fieldLabel1.setObjectName(u"fieldLabel1")

        self.startDateLayout.addWidget(self.fieldLabel1)

        self.dateStart = QDateEdit(self.rightColumnFrame)
        self.dateStart.setObjectName(u"dateStart")
        self.dateStart.setCalendarPopup(True)

        self.startDateLayout.addWidget(self.dateStart)


        self.datesLayout.addLayout(self.startDateLayout)

        self.endDateLayout = QVBoxLayout()
        self.endDateLayout.setSpacing(5)
        self.endDateLayout.setObjectName(u"endDateLayout")
        self.fieldLabel2 = QLabel(self.rightColumnFrame)
        self.fieldLabel2.setObjectName(u"fieldLabel2")

        self.endDateLayout.addWidget(self.fieldLabel2)

        self.dateEnd = QDateEdit(self.rightColumnFrame)
        self.dateEnd.setObjectName(u"dateEnd")
        self.dateEnd.setCalendarPopup(True)

        self.endDateLayout.addWidget(self.dateEnd)


        self.datesLayout.addLayout(self.endDateLayout)


        self.rightColumnLayout.addLayout(self.datesLayout)

        self.statusLayout = QVBoxLayout()
        self.statusLayout.setSpacing(5)
        self.statusLayout.setObjectName(u"statusLayout")
        self.fieldLabel3 = QLabel(self.rightColumnFrame)
        self.fieldLabel3.setObjectName(u"fieldLabel3")

        self.statusLayout.addWidget(self.fieldLabel3)

        self.comboStatus = QComboBox(self.rightColumnFrame)
        self.comboStatus.addItem("")
        self.comboStatus.addItem("")
        self.comboStatus.addItem("")
        self.comboStatus.addItem("")
        self.comboStatus.setObjectName(u"comboStatus")

        self.statusLayout.addWidget(self.comboStatus)


        self.rightColumnLayout.addLayout(self.statusLayout)

        self.rightSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.rightColumnLayout.addItem(self.rightSpacer)

        self.actionBar = QFrame(self.rightColumnFrame)
        self.actionBar.setObjectName(u"actionBar")
        self.actionBar.setFrameShape(QFrame.Shape.NoFrame)
        self.actionButtonsLayout = QHBoxLayout(self.actionBar)
        self.actionButtonsLayout.setSpacing(8)
        self.actionButtonsLayout.setObjectName(u"actionButtonsLayout")
        self.actionButtonsLayout.setContentsMargins(0, 12, 0, 0)
        self.btn_save = QPushButton(self.actionBar)
        self.btn_save.setObjectName(u"btn_save")
        self.btn_save.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.actionButtonsLayout.addWidget(self.btn_save)

        self.btn_cancel = QPushButton(self.actionBar)
        self.btn_cancel.setObjectName(u"btn_cancel")
        self.btn_cancel.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.actionButtonsLayout.addWidget(self.btn_cancel)

        self.actionSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.actionButtonsLayout.addItem(self.actionSpacer)


        self.rightColumnLayout.addWidget(self.actionBar)


        self.formCardLayout.addWidget(self.rightColumnFrame)


        self.formContainerLayout.addWidget(self.formCard)


        self.verticalLayout.addWidget(self.formContainer)

        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy3)
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
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"CreateTourWindow", None))
        self.logo.setText("")
        self.name.setText(QCoreApplication.translate("MainWindow", u"\u041b\u0435\u0433\u0435\u043d\u0434\u044b \u041f\u0430\u0440\u043c\u044b", None))
        self.name_chart.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0437\u0434\u0430\u043d\u0438\u0435 \u0442\u0443\u0440\u0430", None))
        self.status_lb.setText("")
        self.role_lb.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044c", None))
        self.logout_btn.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0439\u0442\u0438", None))
        self.btn_back.setText(QCoreApplication.translate("MainWindow", u"\u2039 \u041d\u0430\u0437\u0430\u0434", None))
        self.lbl_form_title.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0437\u0434\u0430\u043d\u0438\u0435 \u0442\u0443\u0440\u0430", None))
        self.sectionTitle.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0430\u0440\u0448\u0440\u0443\u0442\u044b \u0432 \u0442\u0443\u0440\u0435 *", None))
        self.hintLabel.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0438\u043d\u0438\u043c\u0443\u043c \u043e\u0434\u0438\u043d \u043c\u0430\u0440\u0448\u0440\u0443\u0442", None))

        __sortingEnabled = self.listRoutes.isSortingEnabled()
        self.listRoutes.setSortingEnabled(False)
        ___qlistwidgetitem = self.listRoutes.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0430\u0440\u0448\u0440\u0443\u0442 1", None))
        ___qlistwidgetitem1 = self.listRoutes.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0430\u0440\u0448\u0440\u0443\u0442 2", None))
        ___qlistwidgetitem2 = self.listRoutes.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0430\u0440\u0448\u0440\u0443\u0442 3", None))
        self.listRoutes.setSortingEnabled(__sortingEnabled)

        self.sectionTitle1.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0441\u043d\u043e\u0432\u043d\u0430\u044f \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f", None))
        self.fieldLabel.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0442\u0443\u0440\u0430 *", None))
        self.fieldLabel1.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u0442\u0430 \u043d\u0430\u0447\u0430\u043b\u0430 *", None))
        self.dateStart.setDisplayFormat(QCoreApplication.translate("MainWindow", u"dd.MM.yyyy", None))
        self.fieldLabel2.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u0442\u0430 \u043e\u043a\u043e\u043d\u0447\u0430\u043d\u0438\u044f *", None))
        self.dateEnd.setDisplayFormat(QCoreApplication.translate("MainWindow", u"dd.MM.yyyy", None))
        self.fieldLabel3.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0430\u0442\u0443\u0441", None))
        self.comboStatus.setItemText(0, QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043f\u043b\u0430\u043d\u0438\u0440\u043e\u0432\u0430\u043d", None))
        self.comboStatus.setItemText(1, QCoreApplication.translate("MainWindow", u"\u0412 \u043f\u0440\u043e\u0446\u0435\u0441\u0441\u0435", None))
        self.comboStatus.setItemText(2, QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0432\u0435\u0440\u0448\u0451\u043d", None))
        self.comboStatus.setItemText(3, QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043c\u0435\u043d\u0451\u043d", None))

        self.btn_save.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.btn_cancel.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043c\u0435\u043d\u0430", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_8), QCoreApplication.translate("MainWindow", u"\u041a\u0430\u0442\u0430\u043b\u043e\u0433 \u043c\u0430\u0440\u0448\u0440\u0443\u0442\u043e\u0432", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_9), QCoreApplication.translate("MainWindow", u"\u0422\u0443\u0440\u044b", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_10), QCoreApplication.translate("MainWindow", u"\u0418\u043c\u043f\u043e\u0440\u0442 \u0438 \u044d\u043a\u0441\u043f\u043e\u0440\u0442", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_11), QCoreApplication.translate("MainWindow", u"\u0421\u0438\u043d\u0445\u0440\u043e\u043d\u0438\u0437\u0430\u0446\u0438\u044f", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_12), QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u0438", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_13), QCoreApplication.translate("MainWindow", u"\u0416\u0443\u0440\u043d\u0430\u043b \u0430\u0443\u0434\u0438\u0442\u0430", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_14), QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438 API \u0438 \u043a\u0435\u0448", None))
    # retranslateUi

