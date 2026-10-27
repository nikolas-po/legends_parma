# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'route_card_window.ui'
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
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QTabWidget, QVBoxLayout, QWidget)
import login_res_rc

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        if not mainWindow.objectName():
            mainWindow.setObjectName(u"mainWindow")
        mainWindow.resize(1032, 600)
        mainWindow.setStyleSheet(u"#centralwidget { background-color: #F5F0E8; }\n"
"#headerFrame { background-color: #2C2A26; border-bottom: 1px solid rgba(255,255,255,0.2); }\n"
"#headerFrame QLabel { color: #F5F0E8; border: none; }\n"
"#logout_btn { background-color: transparent; color: #F5F0E8; border: 1px solid rgba(255, 255, 255, 0.25); padding: 3px 10px; font-size: 12px; border-radius: 4px; }\n"
"#logout_btn:hover { background-color: rgba(255, 255, 255, 0.08); border: 1px solid rgba(255, 255, 255, 0.4); }\n"
"#logout_btn:pressed { background-color: rgba(255, 255, 255, 0.12); border: 1px solid rgba(255, 255, 255, 0.5); }\n"
"#logout_btn:focus { border: 1px dashed #F5F0E8; }\n"
"\n"
"#leftZone { background-color: #EDE6D9; border-right: 1px solid #D4CBBE; }\n"
"#rightZone { background-color: #FFFFFF; }\n"
"#rightZone QLabel { border: none; background: transparent; }\n"
"#pointsFrame, #reviewsFrame, #infoFrame { background-color: #FFFFFF; border: 1px solid #D4CBBE; }\n"
"#mapFrame { background-color: #EDE6D9; border: 1px solid #D4CBBE; }\n"
""
                        "#mapFrame QLabel { background: #FFFFFF; border: 1px solid #D4CBBE; color: #6B6560; font-size: 11px; padding: 4px 8px; }\n"
"#pointsFrame QLabel#lbl_points_title, #reviewsFrame QLabel#lbl_reviews_title, #rightZone QLabel#lbl_route_props, #rightZone QLabel#lbl_route_desc_title { font-size: 11px; color: #6B6560; }\n"
"#point1Frame, #point2Frame { background: #FFFFFF; border: 1px solid #D4CBBE; }\n"
"#point1Frame QLabel, #point2Frame QLabel { border: none; }\n"
"#point1Frame QLabel#lbl_p1_name, #point2Frame QLabel#lbl_p2_name { font-size: 12px; font-weight: 600; color: #2C2A26; }\n"
"#point1Frame QLabel#lbl_p1_coords, #point2Frame QLabel#lbl_p2_coords { font-size: 11px; font-family: monospace; color: #6B6560; }\n"
"#weatherFrame { background-color: #EDE6D9; border: 1px solid #D4CBBE; }\n"
"#weatherFrame QLabel { border: none; }\n"
"#weatherFrame QLabel#lbl_weather_title { font-size: 11px; color: #6B6560; }\n"
"#weatherFrame QLabel#lbl_temp { font-size: 24px; font-weight: 600; color: #2C2A26; }\n"
"#weatherFrame QL"
                        "abel#lbl_weather_desc { font-size: 13px; font-weight: 600; color: #2C2A26; }\n"
"#weatherFrame QLabel#lbl_weather_cache { font-size: 11px; color: #6B6560; }\n"
"#reviewsFrame QLabel#lbl_stars { font-size: 12px; color: #C4A35A; }\n"
"#reviewItemLayout QLabel#lbl_review_text { font-size: 12px; color: #6B6560; }\n"
"#reviewItemLayout QLabel#lbl_review_author { font-size: 11px; color: #A39E94; }\n"
"#review_line { border: none; border-top: 1px solid #D4CBBE; max-height: 1px; }\n"
"#rightZone QLabel#lbl_route_title { font-size: 15px; font-weight: 600; color: #2C2A26; }\n"
"#rightZone QLabel#lbl_route_desc { font-size: 12px; color: #6B6560; }\n"
"#info_line { border: none; border-top: 1px solid #D4CBBE; max-height: 1px; }\n"
"\n"
"#actionBarFrame { background-color: #FFFFFF; border-top: 1px solid #D4CBBE; }\n"
"#btn_back { padding: 3px 9px; font-size: 12px; color: #6B6560; background: transparent; border: none; }\n"
"#btn_back:hover { background: #F5F0E8; color: #2C2A26; }\n"
"#btn_back:pressed { background: #EDE6D9"
                        "; }\n"
"#btn_back:focus { border: 1px dashed #4A6741; }\n"
"\n"
"#btn_edit, #btn_export, #btn_leave_review, #btn_update_weather { background: #FFFFFF; color: #2C2A26; border: 1px solid #D4CBBE; padding: 3px 9px; font-size: 12px; border-radius: 4px; }\n"
"#btn_edit:hover, #btn_export:hover, #btn_leave_review:hover, #btn_update_weather:hover { background: #F5F0E8; border: 1px solid #4A6741; }\n"
"#btn_edit:pressed, #btn_export:pressed, #btn_leave_review:pressed, #btn_update_weather:pressed { background: #EDE6D9; }\n"
"#btn_edit:disabled, #btn_export:disabled, #btn_leave_review:disabled, #btn_update_weather:disabled { background: #FFFFFF; color: #A39E94; border: 1px solid #E5DFD4; }\n"
"#btn_edit:focus, #btn_export:focus, #btn_leave_review:focus, #btn_update_weather:focus { border: 1px dashed #4A6741; }\n"
"\n"
"#btn_schedule { background: #4A6741; color: #FFFFFF; border: none; padding: 3px 9px; font-size: 12px; border-radius: 4px; }\n"
"#btn_schedule:hover { background: #3D5636; }\n"
"#btn_schedule:pressed { bac"
                        "kground: #334A2E; }\n"
"#btn_schedule:disabled { background: #A8B5A0; }\n"
"#btn_schedule:focus { border: 1px dashed #4A6741; }\n"
"\n"
"#btn_delete { background: #FFFFFF; color: #B54A3A; border: 1px solid #B54A3A; padding: 3px 9px; font-size: 12px; border-radius: 4px; }\n"
"#btn_delete:hover { background: #F5E8E6; }\n"
"#btn_delete:pressed { background: #EBD5D1; }\n"
"#btn_delete:disabled { background: #FFFFFF; color: #D4A39C; border: 1px solid #E5C4BF; }\n"
"#btn_delete:focus { border: 1px dashed #4A6741; }\n"
"\n"
"QTabWidget::panel { border: none; background-color: #FFFFFF; }\n"
"QTabBar { background-color: #FFFFFF; border: none; }\n"
"QTabBar::tab { height: 40px; background-color: #FFFFFF; color: #6B6560; font-size: 12px; font-weight: normal; padding: 0px 30px; border: none; border-bottom: 2px solid transparent; border-top: 1px solid #D4CBBE; text-align: center; }\n"
"QTabBar::tab:hover { color: #2C2A26; }\n"
"QTabBar::tab:selected { color: #2C2A26; font-weight: 600; border-bottom: 2px solid #4A6741; }")
        self.centralwidget = QWidget(mainWindow)
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

        self.mainContentFrame = QFrame(self.centralwidget)
        self.mainContentFrame.setObjectName(u"mainContentFrame")
        self.mainContentFrame.setFrameShape(QFrame.Shape.NoFrame)
        self.mainContentLayout = QHBoxLayout(self.mainContentFrame)
        self.mainContentLayout.setSpacing(0)
        self.mainContentLayout.setObjectName(u"mainContentLayout")
        self.mainContentLayout.setContentsMargins(0, 0, 0, 0)
        self.leftZone = QFrame(self.mainContentFrame)
        self.leftZone.setObjectName(u"leftZone")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.leftZone.sizePolicy().hasHeightForWidth())
        self.leftZone.setSizePolicy(sizePolicy)
        self.leftZone.setFrameShape(QFrame.Shape.NoFrame)
        self.leftZoneLayout = QVBoxLayout(self.leftZone)
        self.leftZoneLayout.setSpacing(14)
        self.leftZoneLayout.setObjectName(u"leftZoneLayout")
        self.leftZoneLayout.setContentsMargins(14, 14, 14, 14)
        self.pointsFrame = QFrame(self.leftZone)
        self.pointsFrame.setObjectName(u"pointsFrame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pointsFrame.sizePolicy().hasHeightForWidth())
        self.pointsFrame.setSizePolicy(sizePolicy1)
        self.pointsLayout = QVBoxLayout(self.pointsFrame)
        self.pointsLayout.setSpacing(8)
        self.pointsLayout.setObjectName(u"pointsLayout")
        self.pointsLayout.setContentsMargins(14, 14, 14, 14)
        self.lbl_points_title = QLabel(self.pointsFrame)
        self.lbl_points_title.setObjectName(u"lbl_points_title")

        self.pointsLayout.addWidget(self.lbl_points_title)

        self.point1Frame = QFrame(self.pointsFrame)
        self.point1Frame.setObjectName(u"point1Frame")
        self.point1Layout = QVBoxLayout(self.point1Frame)
        self.point1Layout.setSpacing(2)
        self.point1Layout.setObjectName(u"point1Layout")
        self.point1Layout.setContentsMargins(8, 7, 8, 7)
        self.lbl_p1_name = QLabel(self.point1Frame)
        self.lbl_p1_name.setObjectName(u"lbl_p1_name")

        self.point1Layout.addWidget(self.lbl_p1_name)

        self.lbl_p1_coords = QLabel(self.point1Frame)
        self.lbl_p1_coords.setObjectName(u"lbl_p1_coords")

        self.point1Layout.addWidget(self.lbl_p1_coords)


        self.pointsLayout.addWidget(self.point1Frame)

        self.point2Frame = QFrame(self.pointsFrame)
        self.point2Frame.setObjectName(u"point2Frame")
        self.point2Layout = QVBoxLayout(self.point2Frame)
        self.point2Layout.setSpacing(2)
        self.point2Layout.setObjectName(u"point2Layout")
        self.point2Layout.setContentsMargins(8, 7, 8, 7)
        self.lbl_p2_name = QLabel(self.point2Frame)
        self.lbl_p2_name.setObjectName(u"lbl_p2_name")

        self.point2Layout.addWidget(self.lbl_p2_name)

        self.lbl_p2_coords = QLabel(self.point2Frame)
        self.lbl_p2_coords.setObjectName(u"lbl_p2_coords")

        self.point2Layout.addWidget(self.lbl_p2_coords)


        self.pointsLayout.addWidget(self.point2Frame)


        self.leftZoneLayout.addWidget(self.pointsFrame)

        self.weatherFrame = QFrame(self.leftZone)
        self.weatherFrame.setObjectName(u"weatherFrame")
        sizePolicy1.setHeightForWidth(self.weatherFrame.sizePolicy().hasHeightForWidth())
        self.weatherFrame.setSizePolicy(sizePolicy1)
        self.weatherLayout = QVBoxLayout(self.weatherFrame)
        self.weatherLayout.setSpacing(6)
        self.weatherLayout.setObjectName(u"weatherLayout")
        self.weatherLayout.setContentsMargins(10, 10, 10, 10)
        self.lbl_weather_title = QLabel(self.weatherFrame)
        self.lbl_weather_title.setObjectName(u"lbl_weather_title")

        self.weatherLayout.addWidget(self.lbl_weather_title)

        self.weatherTopLayout = QHBoxLayout()
        self.weatherTopLayout.setObjectName(u"weatherTopLayout")
        self.weatherInfoLayout = QVBoxLayout()
        self.weatherInfoLayout.setSpacing(2)
        self.weatherInfoLayout.setObjectName(u"weatherInfoLayout")
        self.lbl_temp = QLabel(self.weatherFrame)
        self.lbl_temp.setObjectName(u"lbl_temp")

        self.weatherInfoLayout.addWidget(self.lbl_temp)

        self.lbl_weather_desc = QLabel(self.weatherFrame)
        self.lbl_weather_desc.setObjectName(u"lbl_weather_desc")

        self.weatherInfoLayout.addWidget(self.lbl_weather_desc)


        self.weatherTopLayout.addLayout(self.weatherInfoLayout)

        self.btn_update_weather = QPushButton(self.weatherFrame)
        self.btn_update_weather.setObjectName(u"btn_update_weather")
        self.btn_update_weather.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.weatherTopLayout.addWidget(self.btn_update_weather)


        self.weatherLayout.addLayout(self.weatherTopLayout)

        self.lbl_weather_cache = QLabel(self.weatherFrame)
        self.lbl_weather_cache.setObjectName(u"lbl_weather_cache")

        self.weatherLayout.addWidget(self.lbl_weather_cache)


        self.leftZoneLayout.addWidget(self.weatherFrame)

        self.reviewsFrame = QFrame(self.leftZone)
        self.reviewsFrame.setObjectName(u"reviewsFrame")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(1)
        sizePolicy2.setHeightForWidth(self.reviewsFrame.sizePolicy().hasHeightForWidth())
        self.reviewsFrame.setSizePolicy(sizePolicy2)
        self.reviewsLayout = QVBoxLayout(self.reviewsFrame)
        self.reviewsLayout.setSpacing(8)
        self.reviewsLayout.setObjectName(u"reviewsLayout")
        self.reviewsLayout.setContentsMargins(14, 14, 14, 14)
        self.reviewsHeaderLayout = QHBoxLayout()
        self.reviewsHeaderLayout.setObjectName(u"reviewsHeaderLayout")
        self.lbl_reviews_title = QLabel(self.reviewsFrame)
        self.lbl_reviews_title.setObjectName(u"lbl_reviews_title")

        self.reviewsHeaderLayout.addWidget(self.lbl_reviews_title)

        self.reviews_spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.reviewsHeaderLayout.addItem(self.reviews_spacer)

        self.lbl_stars = QLabel(self.reviewsFrame)
        self.lbl_stars.setObjectName(u"lbl_stars")

        self.reviewsHeaderLayout.addWidget(self.lbl_stars)


        self.reviewsLayout.addLayout(self.reviewsHeaderLayout)

        self.btn_leave_review = QPushButton(self.reviewsFrame)
        self.btn_leave_review.setObjectName(u"btn_leave_review")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.btn_leave_review.sizePolicy().hasHeightForWidth())
        self.btn_leave_review.setSizePolicy(sizePolicy3)
        self.btn_leave_review.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.reviewsLayout.addWidget(self.btn_leave_review)

        self.reviewItemLayout = QVBoxLayout()
        self.reviewItemLayout.setSpacing(4)
        self.reviewItemLayout.setObjectName(u"reviewItemLayout")
        self.lbl_review_text = QLabel(self.reviewsFrame)
        self.lbl_review_text.setObjectName(u"lbl_review_text")

        self.reviewItemLayout.addWidget(self.lbl_review_text)

        self.lbl_review_author = QLabel(self.reviewsFrame)
        self.lbl_review_author.setObjectName(u"lbl_review_author")

        self.reviewItemLayout.addWidget(self.lbl_review_author)

        self.review_line = QFrame(self.reviewsFrame)
        self.review_line.setObjectName(u"review_line")
        self.review_line.setFrameShape(QFrame.Shape.NoFrame)

        self.reviewItemLayout.addWidget(self.review_line)


        self.reviewsLayout.addLayout(self.reviewItemLayout)

        self.reviews_bottom_spacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.reviewsLayout.addItem(self.reviews_bottom_spacer)


        self.leftZoneLayout.addWidget(self.reviewsFrame)


        self.mainContentLayout.addWidget(self.leftZone)

        self.rightZone = QFrame(self.mainContentFrame)
        self.rightZone.setObjectName(u"rightZone")
        sizePolicy.setHeightForWidth(self.rightZone.sizePolicy().hasHeightForWidth())
        self.rightZone.setSizePolicy(sizePolicy)
        self.rightZone.setFrameShape(QFrame.Shape.NoFrame)
        self.rightZoneLayout = QVBoxLayout(self.rightZone)
        self.rightZoneLayout.setSpacing(14)
        self.rightZoneLayout.setObjectName(u"rightZoneLayout")
        self.rightZoneLayout.setContentsMargins(14, 14, 14, 14)
        self.mapFrame = QFrame(self.rightZone)
        self.mapFrame.setObjectName(u"mapFrame")
        sizePolicy2.setHeightForWidth(self.mapFrame.sizePolicy().hasHeightForWidth())
        self.mapFrame.setSizePolicy(sizePolicy2)
        self.mapLayout = QVBoxLayout(self.mapFrame)
        self.mapLayout.setObjectName(u"mapLayout")
        self.lbl_map_placeholder = QLabel(self.mapFrame)
        self.lbl_map_placeholder.setObjectName(u"lbl_map_placeholder")

        self.mapLayout.addWidget(self.lbl_map_placeholder, 0, Qt.AlignmentFlag.AlignCenter)


        self.rightZoneLayout.addWidget(self.mapFrame)

        self.infoFrame = QFrame(self.rightZone)
        self.infoFrame.setObjectName(u"infoFrame")
        sizePolicy2.setHeightForWidth(self.infoFrame.sizePolicy().hasHeightForWidth())
        self.infoFrame.setSizePolicy(sizePolicy2)
        self.infoLayout = QVBoxLayout(self.infoFrame)
        self.infoLayout.setSpacing(8)
        self.infoLayout.setObjectName(u"infoLayout")
        self.infoLayout.setContentsMargins(14, 14, 14, 14)
        self.lbl_route_title = QLabel(self.infoFrame)
        self.lbl_route_title.setObjectName(u"lbl_route_title")

        self.infoLayout.addWidget(self.lbl_route_title)

        self.lbl_route_props = QLabel(self.infoFrame)
        self.lbl_route_props.setObjectName(u"lbl_route_props")

        self.infoLayout.addWidget(self.lbl_route_props)

        self.lbl_route_desc_title = QLabel(self.infoFrame)
        self.lbl_route_desc_title.setObjectName(u"lbl_route_desc_title")
        self.lbl_route_desc_title.setStyleSheet(u"margin-top: 4px;")

        self.infoLayout.addWidget(self.lbl_route_desc_title)

        self.info_line = QFrame(self.infoFrame)
        self.info_line.setObjectName(u"info_line")
        self.info_line.setFrameShape(QFrame.Shape.NoFrame)

        self.infoLayout.addWidget(self.info_line)

        self.lbl_route_desc = QLabel(self.infoFrame)
        self.lbl_route_desc.setObjectName(u"lbl_route_desc")
        self.lbl_route_desc.setWordWrap(True)

        self.infoLayout.addWidget(self.lbl_route_desc)

        self.info_bottom_spacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.infoLayout.addItem(self.info_bottom_spacer)


        self.rightZoneLayout.addWidget(self.infoFrame)


        self.mainContentLayout.addWidget(self.rightZone)


        self.verticalLayout.addWidget(self.mainContentFrame)

        self.actionBarFrame = QFrame(self.centralwidget)
        self.actionBarFrame.setObjectName(u"actionBarFrame")
        self.actionBarFrame.setMinimumSize(QSize(0, 44))
        self.actionBarFrame.setMaximumSize(QSize(16777215, 44))
        self.actionBarLayout = QHBoxLayout(self.actionBarFrame)
        self.actionBarLayout.setSpacing(8)
        self.actionBarLayout.setObjectName(u"actionBarLayout")
        self.actionBarLayout.setContentsMargins(14, 0, 14, 0)
        self.btn_back = QPushButton(self.actionBarFrame)
        self.btn_back.setObjectName(u"btn_back")
        self.btn_back.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.actionBarLayout.addWidget(self.btn_back)

        self.actionBarSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.actionBarLayout.addItem(self.actionBarSpacer)

        self.btn_edit = QPushButton(self.actionBarFrame)
        self.btn_edit.setObjectName(u"btn_edit")
        self.btn_edit.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.actionBarLayout.addWidget(self.btn_edit)

        self.btn_export = QPushButton(self.actionBarFrame)
        self.btn_export.setObjectName(u"btn_export")
        self.btn_export.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.actionBarLayout.addWidget(self.btn_export)

        self.btn_schedule = QPushButton(self.actionBarFrame)
        self.btn_schedule.setObjectName(u"btn_schedule")
        self.btn_schedule.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.actionBarLayout.addWidget(self.btn_schedule)

        self.btn_delete = QPushButton(self.actionBarFrame)
        self.btn_delete.setObjectName(u"btn_delete")
        self.btn_delete.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.actionBarLayout.addWidget(self.btn_delete)


        self.verticalLayout.addWidget(self.actionBarFrame)

        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        sizePolicy3.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy3)
        self.tabWidget.setMinimumSize(QSize(0, 44))
        self.tabWidget.setMaximumSize(QSize(16777215, 44))
        self.tabWidget.setTabPosition(QTabWidget.TabPosition.North)
        self.tabWidget.setUsesScrollButtons(False)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setProperty(u"drawBase", False)
        self.tab_36 = QWidget()
        self.tab_36.setObjectName(u"tab_36")
        self.tabWidget.addTab(self.tab_36, "")
        self.tab_37 = QWidget()
        self.tab_37.setObjectName(u"tab_37")
        self.tabWidget.addTab(self.tab_37, "")
        self.tab_38 = QWidget()
        self.tab_38.setObjectName(u"tab_38")
        self.tabWidget.addTab(self.tab_38, "")
        self.tab_39 = QWidget()
        self.tab_39.setObjectName(u"tab_39")
        self.tabWidget.addTab(self.tab_39, "")
        self.tab_40 = QWidget()
        self.tab_40.setObjectName(u"tab_40")
        self.tabWidget.addTab(self.tab_40, "")
        self.tab_41 = QWidget()
        self.tab_41.setObjectName(u"tab_41")
        self.tabWidget.addTab(self.tab_41, "")
        self.tab_42 = QWidget()
        self.tab_42.setObjectName(u"tab_42")
        self.tabWidget.addTab(self.tab_42, "")

        self.verticalLayout.addWidget(self.tabWidget)

        mainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(mainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(mainWindow)
    # setupUi

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(QCoreApplication.translate("mainWindow", u"RouteCardWindow", None))
        self.logo.setText("")
        self.name.setText(QCoreApplication.translate("mainWindow", u"\u041b\u0435\u0433\u0435\u043d\u0434\u044b \u041f\u0430\u0440\u043c\u044b", None))
        self.name_chart.setText(QCoreApplication.translate("mainWindow", u"\u041a\u0430\u0440\u0442\u043e\u0447\u043a\u0430 \u043c\u0430\u0440\u0448\u0440\u0443\u0442\u0430", None))
        self.status_lb.setText("")
        self.role_lb.setText(QCoreApplication.translate("mainWindow", u"\u0410\u0434\u043c\u0438\u043d\u0438\u0441\u0442\u0440\u0430\u0442\u043e\u0440", None))
        self.logout_btn.setText(QCoreApplication.translate("mainWindow", u"\u0412\u044b\u0439\u0442\u0438", None))
        self.lbl_points_title.setText(QCoreApplication.translate("mainWindow", u"\u0422\u041e\u0427\u041a\u0418 \u041c\u0410\u0420\u0428\u0420\u0423\u0422\u0410", None))
        self.lbl_p1_name.setText(QCoreApplication.translate("mainWindow", u"\u0422\u043e\u0447\u043a\u0430 1", None))
        self.lbl_p1_coords.setText(QCoreApplication.translate("mainWindow", u"61.2583, 54.6215", None))
        self.lbl_p2_name.setText(QCoreApplication.translate("mainWindow", u"\u0422\u043e\u0447\u043a\u0430 2", None))
        self.lbl_p2_coords.setText(QCoreApplication.translate("mainWindow", u"61.2701, 54.6350", None))
        self.lbl_weather_title.setText(QCoreApplication.translate("mainWindow", u"\u041f\u041e\u0413\u041e\u0414\u0410", None))
        self.lbl_temp.setText(QCoreApplication.translate("mainWindow", u"+15\u00b0C", None))
        self.lbl_weather_desc.setText(QCoreApplication.translate("mainWindow", u"\u0422\u0435\u043c\u043f\u0435\u0440\u0430\u0442\u0443\u0440\u0430, \u0432\u0435\u0442\u0435\u0440", None))
        self.btn_update_weather.setText(QCoreApplication.translate("mainWindow", u"\u041e\u0431\u043d\u043e\u0432\u0438\u0442\u044c", None))
        self.lbl_weather_cache.setText(QCoreApplication.translate("mainWindow", u"\u0412\u0440\u0435\u043c\u044f \u043e\u0431\u043d\u043e\u0432\u043b\u0435\u043d\u0438\u044f - \u0438\u0437 \u043a\u0435\u0448\u0430 \u043f\u0440\u0438 \u043e\u0444\u043b\u0430\u0439\u043d", None))
        self.lbl_reviews_title.setText(QCoreApplication.translate("mainWindow", u"\u041e\u0422\u0417\u042b\u0412\u042b", None))
        self.lbl_stars.setText(QCoreApplication.translate("mainWindow", u"\u2605\u2605\u2605\u2605\u2606", None))
        self.btn_leave_review.setText(QCoreApplication.translate("mainWindow", u"\u041e\u0441\u0442\u0430\u0432\u0438\u0442\u044c \u043e\u0442\u0437\u044b\u0432", None))
        self.lbl_review_text.setText(QCoreApplication.translate("mainWindow", u"\u041e\u0442\u043b\u0438\u0447\u043d\u044b\u0439 \u043c\u0430\u0440\u0448\u0440\u0443\u0442, \u043e\u0447\u0435\u043d\u044c \u043a\u0440\u0430\u0441\u0438\u0432\u043e!", None))
        self.lbl_review_author.setText(QCoreApplication.translate("mainWindow", u"\u0418\u0432\u0430\u043d \u0418. \u2022 12.05.2024", None))
        self.lbl_map_placeholder.setText(QCoreApplication.translate("mainWindow", u"\u041a\u0430\u0440\u0442\u0430 \u043c\u0430\u0440\u0448\u0440\u0443\u0442\u0430", None))
        self.lbl_route_title.setText(QCoreApplication.translate("mainWindow", u"\u0421\u0432\u0435\u0434\u0435\u043d\u0438\u044f \u043e \u043c\u0430\u0440\u0448\u0440\u0443\u0442\u0435", None))
        self.lbl_route_props.setText(QCoreApplication.translate("mainWindow", u"\u0422\u0438\u043f \u00b7 \u041f\u0440\u043e\u0442\u044f\u0436\u0451\u043d\u043d\u043e\u0441\u0442\u044c \u00b7 \u0412\u0440\u0435\u043c\u044f \u00b7 \u0420\u0435\u0433\u0438\u043e\u043d", None))
        self.lbl_route_desc_title.setText(QCoreApplication.translate("mainWindow", u"\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435", None))
        self.lbl_route_desc.setText(QCoreApplication.translate("mainWindow", u"\u0416\u0438\u0432\u043e\u043f\u0438\u0441\u043d\u044b\u0439 \u043c\u0430\u0440\u0448\u0440\u0443\u0442 \u043f\u043e \u043b\u0435\u0441\u0430\u043c \u0438 \u0431\u043e\u043b\u043e\u0442\u0430\u043c \u0440\u0435\u0441\u043f\u0443\u0431\u043b\u0438\u043a\u0438 \u041a\u043e\u043c\u0438. \u041e\u0442\u043b\u0438\u0447\u043d\u044b\u0435 \u0432\u0438\u0434\u044b \u0438 \u0447\u0438\u0441\u0442\u044b\u0439 \u0432\u043e\u0437\u0434\u0443\u0445.", None))
        self.btn_back.setText(QCoreApplication.translate("mainWindow", u"\u2039 \u041d\u0430\u0437\u0430\u0434 \u0432 \u043a\u0430\u0442\u0430\u043b\u043e\u0433", None))
        self.btn_edit.setText(QCoreApplication.translate("mainWindow", u"\u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.btn_export.setText(QCoreApplication.translate("mainWindow", u"\u042d\u043a\u0441\u043f\u043e\u0440\u0442 GPX", None))
        self.btn_schedule.setText(QCoreApplication.translate("mainWindow", u"\u0417\u0430\u043f\u043b\u0430\u043d\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u0442\u0443\u0440", None))
        self.btn_delete.setText(QCoreApplication.translate("mainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_36), QCoreApplication.translate("mainWindow", u"\u041a\u0430\u0442\u0430\u043b\u043e\u0433 \u043c\u0430\u0440\u0448\u0440\u0443\u0442\u043e\u0432", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_37), QCoreApplication.translate("mainWindow", u"\u0422\u0443\u0440\u044b", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_38), QCoreApplication.translate("mainWindow", u"\u0418\u043c\u043f\u043e\u0440\u0442 \u0438 \u044d\u043a\u0441\u043f\u043e\u0440\u0442", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_39), QCoreApplication.translate("mainWindow", u"\u0421\u0438\u043d\u0445\u0440\u043e\u043d\u0438\u0437\u0430\u0446\u0438\u044f", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_40), QCoreApplication.translate("mainWindow", u"\u041f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u0438", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_41), QCoreApplication.translate("mainWindow", u"\u0416\u0443\u0440\u043d\u0430\u043b \u0430\u0443\u0434\u0438\u0442\u0430", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_42), QCoreApplication.translate("mainWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438 API \u0438 \u043a\u0435\u0448", None))
    # retranslateUi

