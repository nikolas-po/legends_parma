# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'create_route_window.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDoubleSpinBox, QFrame,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QTabWidget,
    QTextEdit, QVBoxLayout, QWidget)
import login_res_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.ApplicationModal)
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
"#leftFormCard, #rightFormCard { backg"
                        "round-color: #FFFFFF; border: 1px solid #D4CBBE; padding: 14px; }\n"
"#section_title_points, #section_title_main { font-size: 11px; font-weight: 600; color: #6B6560; text-transform: uppercase; }\n"
"#hintLabel { font-size: 11px; color: #A39E94; }\n"
"#lbl_point_name, #lbl_lat, #lbl_lon, #lbl_alt, #lbl_reserve, #lbl_route_name, #lbl_type, #lbl_region, #lbl_length, #lbl_time, #lbl_desc { font-size: 12px; color: #6B6560; }\n"
"#listTitle { font-size: 14px; font-weight: 600; color: #2C2A26; }\n"
"\n"
"QLineEdit, QTextEdit, QComboBox, QDoubleSpinBox {\n"
"    padding: 10px 12px; font-size: 14px; border-radius: 4px; border: 1px solid #D4CBBE; background-color: #FFFFFF; color: #2C2A26;\n"
"}\n"
"QLineEdit:hover, QTextEdit:hover, QComboBox:hover, QDoubleSpinBox:hover { border: 1px solid #B8AE9E; }\n"
"QLineEdit:focus, QTextEdit:focus, QComboBox:focus, QDoubleSpinBox:focus { border: 1px solid #4A6741; }\n"
"QLineEdit[error=\"true\"], QTextEdit[error=\"true\"], QComboBox[error=\"true\"], QDoubleSpinBox[error=\"true\"] {"
                        " border: 1px solid #B54A3A; }\n"
"QLineEdit:disabled, QTextEdit:disabled, QComboBox:disabled, QDoubleSpinBox:disabled { border: 1px dashed #D4CBBE; color: #A39E94; background-color: #F5F0E8; }\n"
"\n"
"QComboBox QAbstractItemView { background-color: #FFFFFF; border: 1px solid #D4CBBE; selection-background-color: #E8EDE4; selection-color: #2C2A26; }\n"
"QComboBox QAbstractItemView::item:hover { background-color: #EDE6D9; }\n"
"\n"
"#btn_add_point { background-color: #FFFFFF; color: #2C2A26; border: 1px solid #D4CBBE; padding: 3px 9px; font-size: 12px; border-radius: 4px; }\n"
"#btn_add_point:hover { border: 1px solid #4A6741; }\n"
"#btn_add_point:pressed { background-color: #EDE6D9; }\n"
"#btn_add_point:disabled { background-color: #FFFFFF; color: #A39E94; border: 1px solid #E5DFD4; }\n"
"#btn_add_point:focus { border: 1px dashed #4A6741; }\n"
"\n"
"#btn_save { background-color: #4A6741; color: #FFFFFF; border: none; padding: 11px 16px; font-size: 14px; font-weight: 600; border-radius: 4px; }\n"
"#btn_save:hove"
                        "r { background-color: #3D5636; }\n"
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
"#actionBar { border-top: 1px solid #D4CBBE; }\n"
"\n"
"QTabWidget::panel { border: none; background-color: #FFFFFF; }\n"
"QTabBar { background-color: #FFFFFF; border: none; qproperty-drawBase: 0; qproperty-expanding: true; }\n"
"QTabBar::tab { height: 40px; background-color: #FFFFFF; color: #6B6560; font-size: 12px; font-weight: normal; padding: 0px 30px; border: "
                        "none; border-bottom: 2px solid transparent; border-top: 1px solid #D4CBBE; text-align: center; }\n"
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
        self.formContainer.setFrameShape(QFrame.Shape.NoFrame)
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

        self.mainFormLayout = QHBoxLayout()
        self.mainFormLayout.setSpacing(14)
        self.mainFormLayout.setObjectName(u"mainFormLayout")
        self.leftFormCard = QFrame(self.formContainer)
        self.leftFormCard.setObjectName(u"leftFormCard")
        sizePolicy.setHeightForWidth(self.leftFormCard.sizePolicy().hasHeightForWidth())
        self.leftFormCard.setSizePolicy(sizePolicy)
        self.leftFormLayout = QVBoxLayout(self.leftFormCard)
        self.leftFormLayout.setSpacing(10)
        self.leftFormLayout.setObjectName(u"leftFormLayout")
        self.leftFormLayout.setContentsMargins(14, 14, 14, 14)
        self.section_title_points = QLabel(self.leftFormCard)
        self.section_title_points.setObjectName(u"section_title_points")

        self.leftFormLayout.addWidget(self.section_title_points)

        self.hintLabel = QLabel(self.leftFormCard)
        self.hintLabel.setObjectName(u"hintLabel")

        self.leftFormLayout.addWidget(self.hintLabel)

        self.pointInputLayout = QVBoxLayout()
        self.pointInputLayout.setSpacing(5)
        self.pointInputLayout.setObjectName(u"pointInputLayout")
        self.lbl_point_name = QLabel(self.leftFormCard)
        self.lbl_point_name.setObjectName(u"lbl_point_name")

        self.pointInputLayout.addWidget(self.lbl_point_name)

        self.input_point_name = QLineEdit(self.leftFormCard)
        self.input_point_name.setObjectName(u"input_point_name")

        self.pointInputLayout.addWidget(self.input_point_name)


        self.leftFormLayout.addLayout(self.pointInputLayout)

        self.pointCoordLayout = QHBoxLayout()
        self.pointCoordLayout.setSpacing(10)
        self.pointCoordLayout.setObjectName(u"pointCoordLayout")
        self.latLayout = QVBoxLayout()
        self.latLayout.setSpacing(5)
        self.latLayout.setObjectName(u"latLayout")
        self.lbl_lat = QLabel(self.leftFormCard)
        self.lbl_lat.setObjectName(u"lbl_lat")

        self.latLayout.addWidget(self.lbl_lat)

        self.input_lat = QDoubleSpinBox(self.leftFormCard)
        self.input_lat.setObjectName(u"input_lat")
        self.input_lat.setDecimals(6)
        self.input_lat.setMinimum(-90.000000000000000)
        self.input_lat.setMaximum(90.000000000000000)

        self.latLayout.addWidget(self.input_lat)


        self.pointCoordLayout.addLayout(self.latLayout)

        self.lonLayout = QVBoxLayout()
        self.lonLayout.setSpacing(5)
        self.lonLayout.setObjectName(u"lonLayout")
        self.lbl_lon = QLabel(self.leftFormCard)
        self.lbl_lon.setObjectName(u"lbl_lon")

        self.lonLayout.addWidget(self.lbl_lon)

        self.input_lon = QDoubleSpinBox(self.leftFormCard)
        self.input_lon.setObjectName(u"input_lon")
        self.input_lon.setDecimals(6)
        self.input_lon.setMinimum(-180.000000000000000)
        self.input_lon.setMaximum(180.000000000000000)

        self.lonLayout.addWidget(self.input_lon)


        self.pointCoordLayout.addLayout(self.lonLayout)

        self.altLayout = QVBoxLayout()
        self.altLayout.setSpacing(5)
        self.altLayout.setObjectName(u"altLayout")
        self.lbl_alt = QLabel(self.leftFormCard)
        self.lbl_alt.setObjectName(u"lbl_alt")

        self.altLayout.addWidget(self.lbl_alt)

        self.input_alt = QDoubleSpinBox(self.leftFormCard)
        self.input_alt.setObjectName(u"input_alt")
        self.input_alt.setMaximum(99999.000000000000000)

        self.altLayout.addWidget(self.input_alt)


        self.pointCoordLayout.addLayout(self.altLayout)


        self.leftFormLayout.addLayout(self.pointCoordLayout)

        self.reserveLayout = QVBoxLayout()
        self.reserveLayout.setSpacing(5)
        self.reserveLayout.setObjectName(u"reserveLayout")
        self.lbl_reserve = QLabel(self.leftFormCard)
        self.lbl_reserve.setObjectName(u"lbl_reserve")

        self.reserveLayout.addWidget(self.lbl_reserve)

        self.input_reserve = QLineEdit(self.leftFormCard)
        self.input_reserve.setObjectName(u"input_reserve")

        self.reserveLayout.addWidget(self.input_reserve)


        self.leftFormLayout.addLayout(self.reserveLayout)

        self.btn_add_point = QPushButton(self.leftFormCard)
        self.btn_add_point.setObjectName(u"btn_add_point")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btn_add_point.sizePolicy().hasHeightForWidth())
        self.btn_add_point.setSizePolicy(sizePolicy2)
        self.btn_add_point.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.leftFormLayout.addWidget(self.btn_add_point)

        self.listTitle = QLabel(self.leftFormCard)
        self.listTitle.setObjectName(u"listTitle")

        self.leftFormLayout.addWidget(self.listTitle)

        self.list_points = QTextEdit(self.leftFormCard)
        self.list_points.setObjectName(u"list_points")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(1)
        sizePolicy3.setHeightForWidth(self.list_points.sizePolicy().hasHeightForWidth())
        self.list_points.setSizePolicy(sizePolicy3)
        self.list_points.setReadOnly(True)

        self.leftFormLayout.addWidget(self.list_points)


        self.mainFormLayout.addWidget(self.leftFormCard)

        self.rightColumnFrame = QFrame(self.formContainer)
        self.rightColumnFrame.setObjectName(u"rightColumnFrame")
        sizePolicy.setHeightForWidth(self.rightColumnFrame.sizePolicy().hasHeightForWidth())
        self.rightColumnFrame.setSizePolicy(sizePolicy)
        self.rightColumnFrame.setFrameShape(QFrame.Shape.NoFrame)
        self.rightColumnLayout = QVBoxLayout(self.rightColumnFrame)
        self.rightColumnLayout.setSpacing(8)
        self.rightColumnLayout.setObjectName(u"rightColumnLayout")
        self.rightColumnLayout.setContentsMargins(0, 0, 0, 0)
        self.rightFormCard = QFrame(self.rightColumnFrame)
        self.rightFormCard.setObjectName(u"rightFormCard")
        sizePolicy3.setHeightForWidth(self.rightFormCard.sizePolicy().hasHeightForWidth())
        self.rightFormCard.setSizePolicy(sizePolicy3)
        self.rightFormLayout = QVBoxLayout(self.rightFormCard)
        self.rightFormLayout.setSpacing(10)
        self.rightFormLayout.setObjectName(u"rightFormLayout")
        self.rightFormLayout.setContentsMargins(14, 14, 14, 14)
        self.section_title_main = QLabel(self.rightFormCard)
        self.section_title_main.setObjectName(u"section_title_main")

        self.rightFormLayout.addWidget(self.section_title_main)

        self.mainNameLayout = QVBoxLayout()
        self.mainNameLayout.setSpacing(5)
        self.mainNameLayout.setObjectName(u"mainNameLayout")
        self.lbl_route_name = QLabel(self.rightFormCard)
        self.lbl_route_name.setObjectName(u"lbl_route_name")

        self.mainNameLayout.addWidget(self.lbl_route_name)

        self.input_route_name = QLineEdit(self.rightFormCard)
        self.input_route_name.setObjectName(u"input_route_name")

        self.mainNameLayout.addWidget(self.input_route_name)


        self.rightFormLayout.addLayout(self.mainNameLayout)

        self.typeRegionLayout = QHBoxLayout()
        self.typeRegionLayout.setSpacing(10)
        self.typeRegionLayout.setObjectName(u"typeRegionLayout")
        self.typeLayout = QVBoxLayout()
        self.typeLayout.setSpacing(5)
        self.typeLayout.setObjectName(u"typeLayout")
        self.lbl_type = QLabel(self.rightFormCard)
        self.lbl_type.setObjectName(u"lbl_type")

        self.typeLayout.addWidget(self.lbl_type)

        self.combo_type = QComboBox(self.rightFormCard)
        self.combo_type.setObjectName(u"combo_type")

        self.typeLayout.addWidget(self.combo_type)


        self.typeRegionLayout.addLayout(self.typeLayout)

        self.regionLayout = QVBoxLayout()
        self.regionLayout.setSpacing(5)
        self.regionLayout.setObjectName(u"regionLayout")
        self.lbl_region = QLabel(self.rightFormCard)
        self.lbl_region.setObjectName(u"lbl_region")

        self.regionLayout.addWidget(self.lbl_region)

        self.input_region = QLineEdit(self.rightFormCard)
        self.input_region.setObjectName(u"input_region")

        self.regionLayout.addWidget(self.input_region)


        self.typeRegionLayout.addLayout(self.regionLayout)


        self.rightFormLayout.addLayout(self.typeRegionLayout)

        self.lengthTimeLayout = QHBoxLayout()
        self.lengthTimeLayout.setSpacing(10)
        self.lengthTimeLayout.setObjectName(u"lengthTimeLayout")
        self.lengthLayout = QVBoxLayout()
        self.lengthLayout.setSpacing(5)
        self.lengthLayout.setObjectName(u"lengthLayout")
        self.lbl_length = QLabel(self.rightFormCard)
        self.lbl_length.setObjectName(u"lbl_length")

        self.lengthLayout.addWidget(self.lbl_length)

        self.input_length = QDoubleSpinBox(self.rightFormCard)
        self.input_length.setObjectName(u"input_length")
        self.input_length.setMaximum(99999.000000000000000)

        self.lengthLayout.addWidget(self.input_length)


        self.lengthTimeLayout.addLayout(self.lengthLayout)

        self.timeLayout = QVBoxLayout()
        self.timeLayout.setSpacing(5)
        self.timeLayout.setObjectName(u"timeLayout")
        self.lbl_time = QLabel(self.rightFormCard)
        self.lbl_time.setObjectName(u"lbl_time")

        self.timeLayout.addWidget(self.lbl_time)

        self.input_time = QDoubleSpinBox(self.rightFormCard)
        self.input_time.setObjectName(u"input_time")
        self.input_time.setMaximum(99999.000000000000000)

        self.timeLayout.addWidget(self.input_time)


        self.lengthTimeLayout.addLayout(self.timeLayout)


        self.rightFormLayout.addLayout(self.lengthTimeLayout)

        self.descLayout = QVBoxLayout()
        self.descLayout.setSpacing(5)
        self.descLayout.setObjectName(u"descLayout")
        self.lbl_desc = QLabel(self.rightFormCard)
        self.lbl_desc.setObjectName(u"lbl_desc")

        self.descLayout.addWidget(self.lbl_desc)

        self.input_desc = QTextEdit(self.rightFormCard)
        self.input_desc.setObjectName(u"input_desc")
        sizePolicy3.setHeightForWidth(self.input_desc.sizePolicy().hasHeightForWidth())
        self.input_desc.setSizePolicy(sizePolicy3)

        self.descLayout.addWidget(self.input_desc)


        self.rightFormLayout.addLayout(self.descLayout)


        self.rightColumnLayout.addWidget(self.rightFormCard)

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


        self.mainFormLayout.addWidget(self.rightColumnFrame)


        self.formContainerLayout.addLayout(self.mainFormLayout)


        self.verticalLayout.addWidget(self.formContainer)

        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy4.setHorizontalStretch(1)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy4)
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

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"CreateRouteWindow", None))
        self.logo.setText("")
        self.name.setText(QCoreApplication.translate("MainWindow", u"\u041b\u0435\u0433\u0435\u043d\u0434\u044b \u041f\u0430\u0440\u043c\u044b", None))
        self.name_chart.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0437\u0434\u0430\u043d\u0438\u0435 \u043c\u0430\u0440\u0448\u0440\u0443\u0442\u0430", None))
        self.status_lb.setText("")
        self.role_lb.setText(QCoreApplication.translate("MainWindow", u"\u0410\u0434\u043c\u0438\u043d\u0438\u0441\u0442\u0440\u0430\u0442\u043e\u0440", None))
        self.logout_btn.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0439\u0442\u0438", None))
        self.btn_back.setText(QCoreApplication.translate("MainWindow", u"\u2039 \u041d\u0430\u0437\u0430\u0434", None))
        self.lbl_form_title.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0437\u0434\u0430\u043d\u0438\u0435 \u043c\u0430\u0440\u0448\u0440\u0443\u0442\u0430", None))
        self.section_title_points.setText(QCoreApplication.translate("MainWindow", u"\u0422\u041e\u0427\u041a\u0418 \u041c\u0410\u0420\u0428\u0420\u0423\u0422\u0410", None))
        self.hintLabel.setText(QCoreApplication.translate("MainWindow", u"\u0422\u043e\u0447\u043a\u0438 \u043c\u043e\u0436\u043d\u043e \u0434\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u043f\u043e\u0437\u0436\u0435; \u0431\u0435\u0437 \u0442\u043e\u0447\u0435\u043a GPX \u043d\u0435\u0434\u043e\u0441\u0442\u0443\u043f\u0435\u043d", None))
        self.lbl_point_name.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0442\u043e\u0447\u043a\u0438", None))
        self.lbl_lat.setText(QCoreApplication.translate("MainWindow", u"\u0428\u0438\u0440\u043e\u0442\u0430 (-90..90)", None))
        self.lbl_lon.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u043b\u0433\u043e\u0442\u0430 (-180..180)", None))
        self.lbl_alt.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0441\u043e\u0442\u0430, \u043c", None))
        self.lbl_reserve.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043f\u043e\u0432\u0435\u0434\u043d\u0438\u043a *", None))
        self.btn_add_point.setText(QCoreApplication.translate("MainWindow", u"+ \u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0442\u043e\u0447\u043a\u0443", None))
        self.listTitle.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u043b\u0435\u043d\u043d\u044b\u0435 \u0442\u043e\u0447\u043a\u0438", None))
        self.section_title_main.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0421\u041d\u041e\u0412\u041d\u0410\u042f \u0418\u041d\u0424\u041e\u0420\u041c\u0410\u0426\u0418\u042f", None))
        self.lbl_route_name.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 *", None))
        self.lbl_type.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0438\u043f * (\u041f\u0435\u0448\u0438\u0439 / \u0412\u043e\u0434\u043d\u044b\u0439 / \u0413\u043e\u0440\u043d\u044b\u0439)", None))
        self.lbl_region.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0433\u0438\u043e\u043d *", None))
        self.lbl_length.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0442\u044f\u0436\u0451\u043d\u043d\u043e\u0441\u0442\u044c, \u043a\u043c *", None))
        self.lbl_time.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0440\u0435\u043c\u044f \u043f\u0440\u043e\u0445\u043e\u0436\u0434\u0435\u043d\u0438\u044f, \u0447 *", None))
        self.lbl_desc.setText(QCoreApplication.translate("MainWindow", u"\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435", None))
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

