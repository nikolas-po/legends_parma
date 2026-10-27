# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_review_window.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QLabel, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QTabWidget, QTextEdit, QVBoxLayout,
    QWidget)
import login_res_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1226, 646)
        MainWindow.setStyleSheet(u"#centralwidget { background-color: #F5F0E8; }\n"
"#headerFrame { background-color: #2C2A26; border: none; }\n"
"#headerFrame QLabel { color: #F5F0E8; }\n"
"#logout_btn { background-color: transparent; color: #F5F0E8; border: 1px solid rgba(255, 255, 255, 0.25); padding: 3px 10px; font-size: 12px; border-radius: 4px; }\n"
"#logout_btn:hover { background-color: rgba(255, 255, 255, 0.08); border: 1px solid rgba(255, 255, 255, 0.4); }\n"
"#logout_btn:pressed { background-color: rgba(255, 255, 255, 0.12); border: 1px solid rgba(255, 255, 255, 0.5); }\n"
"#logout_btn:focus { border: 1px dashed #F5F0E8; }\n"
"\n"
"#modalFrame { background-color: #FFFFFF; border: 1px solid #D4CBBE; border-radius: 4px; }\n"
"#lbl_modal_title { font-size: 16px; font-weight: 600; color: #2C2A26; }\n"
"#lbl_rating_field, #lbl_review_field { font-size: 12px; color: #6B6560; }\n"
"\n"
"QLineEdit, QTextEdit, QComboBox {\n"
"    padding: 10px 12px; font-size: 14px; border-radius: 4px; border: 1px solid #D4CBBE; background-color: #FFFFFF; colo"
                        "r: #2C2A26;\n"
"}\n"
"QLineEdit:hover, QTextEdit:hover, QComboBox:hover { border: 1px solid #B8AE9E; }\n"
"QLineEdit:focus, QTextEdit:focus, QComboBox:focus { border: 1px solid #4A6741; }\n"
"QLineEdit[error=\"true\"], QTextEdit[error=\"true\"], QComboBox[error=\"true\"] { border: 1px solid #B54A3A; }\n"
"QLineEdit:disabled, QTextEdit:disabled, QComboBox:disabled { border: 1px dashed #D4CBBE; color: #A39E94; background-color: #F5F0E8; }\n"
"QComboBox QAbstractItemView { background-color: #FFFFFF; border: 1px solid #D4CBBE; selection-background-color: #E8EDE4; selection-color: #2C2A26; }\n"
"\n"
"#btn_publish { background-color: #4A6741; color: #FFFFFF; border: none; padding: 11px 16px; font-size: 14px; font-weight: 600; border-radius: 4px; }\n"
"#btn_publish:hover { background-color: #3D5636; }\n"
"#btn_publish:pressed { background-color: #334A2E; }\n"
"#btn_publish:disabled { background-color: #A8B5A0; }\n"
"#btn_publish:focus { border: 1px dashed #4A6741; }\n"
"\n"
"#btn_cancel { background-color: #FFFFFF; c"
                        "olor: #2C2A26; border: 1px solid #D4CBBE; padding: 11px 16px; font-size: 14px; font-weight: 600; border-radius: 4px; }\n"
"#btn_cancel:hover { background-color: #F5F0E8; border: 1px solid #4A6741; }\n"
"#btn_cancel:pressed { background-color: #EDE6D9; }\n"
"#btn_cancel:disabled { background-color: #FFFFFF; color: #A39E94; border: 1px solid #E5DFD4; }\n"
"#btn_cancel:focus { border: 1px dashed #4A6741; }\n"
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

        self.modalContainerLayout = QVBoxLayout()
        self.modalContainerLayout.setSpacing(0)
        self.modalContainerLayout.setObjectName(u"modalContainerLayout")
        self.modalContainerLayout.setContentsMargins(24, 24, 24, 0)
        self.modalFrame = QFrame(self.centralwidget)
        self.modalFrame.setObjectName(u"modalFrame")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.modalFrame.sizePolicy().hasHeightForWidth())
        self.modalFrame.setSizePolicy(sizePolicy)
        self.modalLayout = QVBoxLayout(self.modalFrame)
        self.modalLayout.setSpacing(14)
        self.modalLayout.setObjectName(u"modalLayout")
        self.modalLayout.setContentsMargins(28, 24, 28, 24)
        self.lbl_modal_title = QLabel(self.modalFrame)
        self.lbl_modal_title.setObjectName(u"lbl_modal_title")

        self.modalLayout.addWidget(self.lbl_modal_title, 0, Qt.AlignmentFlag.AlignHCenter)

        self.ratingLayout = QVBoxLayout()
        self.ratingLayout.setSpacing(5)
        self.ratingLayout.setObjectName(u"ratingLayout")
        self.lbl_rating_field = QLabel(self.modalFrame)
        self.lbl_rating_field.setObjectName(u"lbl_rating_field")

        self.ratingLayout.addWidget(self.lbl_rating_field)

        self.input_rating = QComboBox(self.modalFrame)
        self.input_rating.addItem("")
        self.input_rating.addItem("")
        self.input_rating.addItem("")
        self.input_rating.addItem("")
        self.input_rating.addItem("")
        self.input_rating.setObjectName(u"input_rating")
        self.input_rating.setMaximumSize(QSize(150, 16777215))

        self.ratingLayout.addWidget(self.input_rating)


        self.modalLayout.addLayout(self.ratingLayout)

        self.reviewTextLayout = QVBoxLayout()
        self.reviewTextLayout.setSpacing(5)
        self.reviewTextLayout.setObjectName(u"reviewTextLayout")
        self.lbl_review_field = QLabel(self.modalFrame)
        self.lbl_review_field.setObjectName(u"lbl_review_field")

        self.reviewTextLayout.addWidget(self.lbl_review_field)

        self.input_review = QTextEdit(self.modalFrame)
        self.input_review.setObjectName(u"input_review")
        self.input_review.setMinimumSize(QSize(0, 120))

        self.reviewTextLayout.addWidget(self.input_review)


        self.modalLayout.addLayout(self.reviewTextLayout)

        self.buttonsLayout = QHBoxLayout()
        self.buttonsLayout.setSpacing(8)
        self.buttonsLayout.setObjectName(u"buttonsLayout")
        self.btn_publish = QPushButton(self.modalFrame)
        self.btn_publish.setObjectName(u"btn_publish")
        self.btn_publish.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.buttonsLayout.addWidget(self.btn_publish)

        self.btn_cancel = QPushButton(self.modalFrame)
        self.btn_cancel.setObjectName(u"btn_cancel")
        self.btn_cancel.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.buttonsLayout.addWidget(self.btn_cancel)

        self.buttonsSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.buttonsLayout.addItem(self.buttonsSpacer)


        self.modalLayout.addLayout(self.buttonsLayout)


        self.modalContainerLayout.addWidget(self.modalFrame)


        self.verticalLayout.addLayout(self.modalContainerLayout)

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

        self.verticalLayout.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"AddReviewWindow", None))
        self.logo.setText("")
        self.name.setText(QCoreApplication.translate("MainWindow", u"\u041b\u0435\u0433\u0435\u043d\u0434\u044b \u041f\u0430\u0440\u043c\u044b", None))
        self.name_chart.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u043b\u0435\u043d\u0438\u0435 \u043e\u0442\u0437\u044b\u0432\u0430", None))
        self.status_lb.setText("")
        self.role_lb.setText(QCoreApplication.translate("MainWindow", u"\u0410\u0434\u043c\u0438\u043d\u0438\u0441\u0442\u0440\u0430\u0442\u043e\u0440", None))
        self.logout_btn.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0439\u0442\u0438", None))
        self.lbl_modal_title.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u043b\u0435\u043d\u0438\u0435 \u043e\u0442\u0437\u044b\u0432\u0430", None))
        self.lbl_rating_field.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0446\u0435\u043d\u043a\u0430 1-5 *", None))
        self.input_rating.setItemText(0, QCoreApplication.translate("MainWindow", u"1", None))
        self.input_rating.setItemText(1, QCoreApplication.translate("MainWindow", u"2", None))
        self.input_rating.setItemText(2, QCoreApplication.translate("MainWindow", u"3", None))
        self.input_rating.setItemText(3, QCoreApplication.translate("MainWindow", u"4", None))
        self.input_rating.setItemText(4, QCoreApplication.translate("MainWindow", u"5", None))

        self.lbl_review_field.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0435\u043a\u0441\u0442 \u043e\u0442\u0437\u044b\u0432\u0430 *", None))
        self.input_review.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0434\u0435\u043b\u0438\u0442\u0435\u0441\u044c \u0432\u043f\u0435\u0447\u0430\u0442\u043b\u0435\u043d\u0438\u044f\u043c\u0438...", None))
        self.btn_publish.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043f\u0440\u0430\u0432\u0438\u0442\u044c", None))
        self.btn_cancel.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043c\u0435\u043d\u0430", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_8), QCoreApplication.translate("MainWindow", u"\u041a\u0430\u0442\u0430\u043b\u043e\u0433 \u043c\u0430\u0440\u0448\u0440\u0443\u0442\u043e\u0432", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_9), QCoreApplication.translate("MainWindow", u"\u0422\u0443\u0440\u044b", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_10), QCoreApplication.translate("MainWindow", u"\u0418\u043c\u043f\u043e\u0440\u0442 \u0438 \u044d\u043a\u0441\u043f\u043e\u0440\u0442", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_11), QCoreApplication.translate("MainWindow", u"\u0421\u0438\u043d\u0445\u0440\u043e\u043d\u0438\u0437\u0430\u0446\u0438\u044f", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_12), QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u0438", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_13), QCoreApplication.translate("MainWindow", u"\u0416\u0443\u0440\u043d\u0430\u043b \u0430\u0443\u0434\u0438\u0442\u0430", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_14), QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438 API \u0438 \u043a\u0435\u0448", None))
    # retranslateUi

