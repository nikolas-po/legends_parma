import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QStackedWidget, QWidget, QHeaderView
)

from ui.login_window_ui import Ui_LoginWindow
from ui.register_window_ui import Ui_RegWindow
from ui.route_directory_window_ui import Ui_MainWindow as Ui_Route


class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_LoginWindow()
        self.ui.setupUi(self)

        self.register_window = None
        self.catalog_window = None

        self.ui.reg_btn.clicked.connect(self.on_reg_clicked)
        self.ui.guest_btn.clicked.connect(self.on_guest_clicked)
        self.ui.login_btn.clicked.connect(self.on_login_clicked)

    def on_reg_clicked(self):
        self.register_window = RegisterWIndow()
        self.register_window.show()

        self.hide()

    def on_guest_clicked(self):
        self.catalog_window = RouteCatalogWindow()
        self.catalog_window.show()

        self.hide()

    def on_login_clicked(self):
        self.catalog_window = RouteCatalogWindow()
        self.catalog_window.show()

        self.hide()


class RegisterWIndow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_RegWindow()
        self.ui.setupUi(self)

        self.login_window = None

        self.ui.log_btn.clicked.connect(self.on_login_clicked)

    def on_login_clicked(self):

        self.login_window = LoginWindow()
        self.login_window.show()

        self.hide()


class RouteCatalogWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Route()
        self.ui.setupUi(self)

        self.login_window = None

        self.ui.logout_btn.clicked.connect(self.on_logout_clicked)

        tab_bar = self.ui.tabWidget.tabBar()
        tab_bar.setExpanding(True)          # главная строка
        tab_bar.setDocumentMode(True)       # убирает лишние отступы
        tab_bar.setDrawBase(False)

        self.ui.tabWidget.setDocumentMode(True)


        header = self.ui.tableWidget.horizontalHeader()
        header.setStretchLastSection(True)          # главный момент
        header.setDefaultSectionSize(130)           # можно оставить или убрать
        header.setSectionResizeMode(QHeaderView.Stretch)  # если хотите, чтобы ВСЕ столбцы тянулись одинаково
    def on_logout_clicked(self):

        self.login_window = LoginWindow()
        self.login_window.show()

        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = LoginWindow()
    window.show()

    sys.exit(app.exec())
