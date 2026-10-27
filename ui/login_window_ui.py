# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login_window.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)
import login_res_rc

class Ui_LoginWindow(object):
    def setupUi(self, LoginWindow):
        if not LoginWindow.objectName():
            LoginWindow.setObjectName(u"LoginWindow")
        LoginWindow.resize(788, 561)
        LoginWindow.setStyleSheet(u"QMainWindow {\n"
"    background-color: #F5F0E8;\n"
"    color: #2C2A26;\n"
"}")
        self.centralwidget = QWidget(LoginWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.mainGlobalLayout = QHBoxLayout(self.centralwidget)
        self.mainGlobalLayout.setSpacing(0)
        self.mainGlobalLayout.setObjectName(u"mainGlobalLayout")
        self.mainGlobalLayout.setContentsMargins(0, 0, 0, 0)
        self.leftPanel = QFrame(self.centralwidget)
        self.leftPanel.setObjectName(u"leftPanel")
        self.leftPanel.setFrameShape(QFrame.Shape.NoFrame)
        self.leftPanel.setStyleSheet(u"#leftPanel { background-color: #FFFFFF; border: 1px solid #D4CBBE; }")
        self.leftLayout = QVBoxLayout(self.leftPanel)
        self.leftLayout.setSpacing(16)
        self.leftLayout.setObjectName(u"leftLayout")
        self.leftLayout.setContentsMargins(50, 70, 50, 50)
        self.loginsystem = QLabel(self.leftPanel)
        self.loginsystem.setObjectName(u"loginsystem")
        self.loginsystem.setStyleSheet(u"background: transparent; font-size:20px; font-weight:600; color:#2C2A26;")
        self.loginsystem.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.leftLayout.addWidget(self.loginsystem)

        self.topFormSpacer = QSpacerItem(20, 30, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.leftLayout.addItem(self.topFormSpacer)

        self.inputs = QVBoxLayout()
        self.inputs.setSpacing(16)
        self.inputs.setObjectName(u"inputs")
        self.login = QVBoxLayout()
        self.login.setSpacing(5)
        self.login.setObjectName(u"login")
        self.login_lb = QLabel(self.leftPanel)
        self.login_lb.setObjectName(u"login_lb")
        self.login_lb.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.login_lb.setStyleSheet(u"background: transparent; font-size:12px; color:#6B6560; margin-bottom:5px;")

        self.login.addWidget(self.login_lb)

        self.login_in = QLineEdit(self.leftPanel)
        self.login_in.setObjectName(u"login_in")
        self.login_in.setMinimumSize(QSize(0, 35))
        self.login_in.setStyleSheet(u"QLineEdit { background-color: #FFFFFF; color: #2C2A26; border: 1px solid #D4CBBE; border-radius: 4px; padding: 0 10px; width:332px; height:auto; }\n"
"QLineEdit:hover { border: 1px solid #B8AE9E; }\n"
"QLineEdit:focus { border: 1px solid #4A6741; }\n"
"QLineEdit[error=\"true\"] { border: 1px solid #B54A3A; }\n"
"QLineEdit:disabled { border: 1px dashed #D4CBBE; color: #A39E94; background-color: #F5F0E8; }")

        self.login.addWidget(self.login_in)


        self.inputs.addLayout(self.login)

        self.passw = QVBoxLayout()
        self.passw.setSpacing(5)
        self.passw.setObjectName(u"passw")
        self.pasw_lb = QLabel(self.leftPanel)
        self.pasw_lb.setObjectName(u"pasw_lb")
        self.pasw_lb.setStyleSheet(u"background: transparent; font-size:12px; color:#6B6560; margin-bottom:5px;")

        self.passw.addWidget(self.pasw_lb)

        self.passw_in = QLineEdit(self.leftPanel)
        self.passw_in.setObjectName(u"passw_in")
        self.passw_in.setEchoMode(QLineEdit.EchoMode.Password)
        self.passw_in.setMinimumSize(QSize(0, 35))
        self.passw_in.setStyleSheet(u"QLineEdit { background-color: #FFFFFF; color: #2C2A26; border: 1px solid #D4CBBE; border-radius: 4px; padding: 0 10px; width:332px; height:auto; }\n"
"QLineEdit:hover { border: 1px solid #B8AE9E; }\n"
"QLineEdit:focus { border: 1px solid #4A6741; }\n"
"QLineEdit[error=\"true\"] { border: 1px solid #B54A3A; }\n"
"QLineEdit:disabled { border: 1px dashed #D4CBBE; color: #A39E94; background-color: #F5F0E8; }")

        self.passw.addWidget(self.passw_in)


        self.inputs.addLayout(self.passw)


        self.leftLayout.addLayout(self.inputs)

        self.checkBox_remember = QCheckBox(self.leftPanel)
        self.checkBox_remember.setObjectName(u"checkBox_remember")
        self.checkBox_remember.setStyleSheet(u"QCheckBox { background: transparent; font-size: 13px; color: #6B6560; }\n"
"QCheckBox::indicator { width: 15px; height: 15px; border: 1px solid #D4CBBE; background-color: #FFFFFF; }\n"
"QCheckBox::indicator:hover { border: 1px solid #3D5636; }\n"
"QCheckBox::indicator:checked { background-color: #4A6741; border: 1px solid #4A6741; }\n"
"QCheckBox::indicator:pressed { background-color: #334A2E; }\n"
"QCheckBox::indicator:disabled { background-color: #E5DFD4; border: 1px solid #E5DFD4; }\n"
"QCheckBox:disabled { color: #A39E94; }")

        self.leftLayout.addWidget(self.checkBox_remember)

        self.login_btn = QPushButton(self.leftPanel)
        self.login_btn.setObjectName(u"login_btn")
        self.login_btn.setMinimumSize(QSize(0, 32))
        self.login_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.login_btn.setStyleSheet(u"QPushButton { background-color: #4A6741; color: #FFFFFF; font-size: 14px; font-weight: 600; border-radius: 4px; border: none; width:332px; height:auto; }\n"
"QPushButton:hover { background-color: #3D5636; }\n"
"QPushButton:pressed { background-color: #334A2E; }\n"
"QPushButton:disabled { background-color: #A8B5A0; color: #FFFFFF; }\n"
"QPushButton:focus { border: 1px dashed #4A6741; }")

        self.leftLayout.addWidget(self.login_btn)

        self.link_btns = QVBoxLayout()
        self.link_btns.setObjectName(u"link_btns")
        self.guest_btn = QPushButton(self.leftPanel)
        self.guest_btn.setObjectName(u"guest_btn")
        self.guest_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.guest_btn.setStyleSheet(u"QPushButton { background: transparent; border: none; color: #3D6B4F; text-align: center; font-size: 13px; }\n"
"QPushButton:hover { color: #2F543D; text-decoration: underline; }\n"
"QPushButton:pressed { color: #254432; }\n"
"QPushButton:focus { border: 1px dashed #4A6741; }\n"
"QPushButton:disabled { color: #A39E94; }")

        self.link_btns.addWidget(self.guest_btn)

        self.reg_btn = QPushButton(self.leftPanel)
        self.reg_btn.setObjectName(u"reg_btn")
        self.reg_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.reg_btn.setStyleSheet(u"QPushButton { background: transparent; border: none; color: #3D6B4F; text-align: center; font-size: 13px; }\n"
"QPushButton:hover { color: #2F543D; text-decoration: underline; }\n"
"QPushButton:pressed { color: #254432; }\n"
"QPushButton:focus { border: 1px dashed #4A6741; }\n"
"QPushButton:disabled { color: #A39E94; }")

        self.link_btns.addWidget(self.reg_btn)


        self.leftLayout.addLayout(self.link_btns)

        self.leftBottomSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.leftLayout.addItem(self.leftBottomSpacer)


        self.mainGlobalLayout.addWidget(self.leftPanel)

        self.dividerLine = QFrame(self.centralwidget)
        self.dividerLine.setObjectName(u"dividerLine")
        self.dividerLine.setMinimumSize(QSize(1, 0))
        self.dividerLine.setMaximumSize(QSize(1, 16777215))
        self.dividerLine.setFrameShape(QFrame.Shape.NoFrame)
        self.dividerLine.setStyleSheet(u"#dividerLine { background-color: #D4CBBE; }")

        self.mainGlobalLayout.addWidget(self.dividerLine)

        self.rightPanel = QFrame(self.centralwidget)
        self.rightPanel.setObjectName(u"rightPanel")
        self.rightPanel.setFrameShape(QFrame.Shape.NoFrame)
        self.rightPanel.setStyleSheet(u"#rightPanel { background-color: #EDE6D9; }")
        self.rightLayout = QVBoxLayout(self.rightPanel)
        self.rightLayout.setSpacing(0)
        self.rightLayout.setObjectName(u"rightLayout")
        self.rightLayout.setContentsMargins(20, 20, 20, 20)
        self.rightTopSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.rightLayout.addItem(self.rightTopSpacer)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.logo = QLabel(self.rightPanel)
        self.logo.setObjectName(u"logo")
        self.logo.setMinimumSize(QSize(64, 64))
        self.logo.setMaximumSize(QSize(64, 64))
        self.logo.setStyleSheet(u"QLabel { background-color: #FFFFFF; border-radius: 4px; } QLabel:hover { border: 2px solid #B8934A; } QLabel:pressed { border: 2px solid #A6823F; }")
        self.logo.setPixmap(QPixmap(u":/login/icons/logo.png"))
        self.logo.setScaledContents(True)
        self.logo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.logo, 0, 0, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.name = QLabel(self.rightPanel)
        self.name.setObjectName(u"name")
        self.name.setStyleSheet(u"background: transparent; font-size:26px; font-weight:600; color:#C4A35A")
        self.name.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.name, 2, 0, 1, 1)

        self.description = QLabel(self.rightPanel)
        self.description.setObjectName(u"description")
        self.description.setStyleSheet(u"background: transparent; color:#6B6560; font-size:14px;")
        self.description.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.description, 3, 0, 1, 1)


        self.rightLayout.addLayout(self.gridLayout)

        self.rightBottomSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.rightLayout.addItem(self.rightBottomSpacer)


        self.mainGlobalLayout.addWidget(self.rightPanel)

        self.mainGlobalLayout.setStretch(0, 1)
        self.mainGlobalLayout.setStretch(2, 1)
        LoginWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(LoginWindow)

        QMetaObject.connectSlotsByName(LoginWindow)
    # setupUi

    def retranslateUi(self, LoginWindow):
        LoginWindow.setWindowTitle(QCoreApplication.translate("LoginWindow", u"LoginWindow", None))
        self.loginsystem.setText(QCoreApplication.translate("LoginWindow", u"\u0412\u0445\u043e\u0434 \u0432 \u0441\u0438\u0441\u0442\u0435\u043c\u0443", None))
        self.login_lb.setText(QCoreApplication.translate("LoginWindow", u"\u041b\u043e\u0433\u0438\u043d", None))
        self.pasw_lb.setText(QCoreApplication.translate("LoginWindow", u"\u041f\u0430\u0440\u043e\u043b\u044c", None))
        self.checkBox_remember.setText(QCoreApplication.translate("LoginWindow", u"\u0417\u0430\u043f\u043e\u043c\u043d\u0438\u0442\u044c \u043c\u0435\u043d\u044f", None))
        self.login_btn.setText(QCoreApplication.translate("LoginWindow", u"\u0412\u043e\u0439\u0442\u0438", None))
        self.guest_btn.setText(QCoreApplication.translate("LoginWindow", u"\u041f\u0440\u043e\u0434\u043e\u043b\u0436\u0438\u0442\u044c \u043a\u0430\u043a \u0433\u043e\u0441\u0442\u044c", None))
        self.reg_btn.setText(QCoreApplication.translate("LoginWindow", u"\u041d\u0435\u0442 \u0430\u043a\u043a\u0430\u0443\u043d\u0442\u0430? \u0417\u0430\u0440\u0435\u0433\u0438\u0441\u0442\u0440\u0438\u0440\u043e\u0432\u0430\u0442\u044c\u0441\u044f", None))
        self.logo.setText("")
        self.name.setText(QCoreApplication.translate("LoginWindow", u"\u041b\u0435\u0433\u0435\u043d\u0434\u044b \u041f\u0430\u0440\u043c\u044b", None))
        self.description.setText(QCoreApplication.translate("LoginWindow", u"\u0423\u0447\u0451\u0442 \u0438 \u043f\u043b\u0430\u043d\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435 \u0442\u0443\u0440\u0438\u0441\u0442\u0438\u0447\u0435\u0441\u043a\u0438\u0445 \u043c\u0430\u0440\u0448\u0440\u0443\u0442\u043e\u0432\n"
"\u0420\u0435\u0441\u043f\u0443\u0431\u043b\u0438\u043a\u0438 \u041a\u043e\u043c\u0438", None))
    # retranslateUi

