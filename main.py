import sys

from PySide6.QtWidgets import (
    QApplication,
    QHeaderView,
    QMainWindow,
    QSizePolicy,
    QTableWidget,
)

from ui.audit_log_window_ui import Ui_MainWindow as Ui_Audit
from ui.import_data_window_ui import Ui_MainWindow as Ui_Import
from ui.login_window_ui import Ui_LoginWindow
from ui.register_window_ui import Ui_RegWindow
from ui.route_directory_window_ui import Ui_MainWindow as Ui_Routes
from ui.set_api_hash_window_ui import Ui_MainWindow as Ui_Settings
from ui.sinhr_window_ui import Ui_MainWindow as Ui_Sync
from ui.tour_list_window_ui import Ui_MainWindow as Ui_Tours
from ui.users_window_ui import Ui_MainWindow as Ui_Users


class BaseWindow(QMainWindow):
    TAB_INDEX = 0

    def __init__(self):
        super().__init__()
        self.ui = None
        self.next_window = None
        self.login_window = None

    def setup_common_ui(self):
        tabs = self.ui.tabWidget
        tabs.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        tab_bar = tabs.tabBar()
        tab_bar.setExpanding(True)
        tab_bar.setDocumentMode(True)
        tab_bar.setDrawBase(False)
        tabs.setCurrentIndex(self.TAB_INDEX)  # до connect — сигнал не сработает
        tabs.currentChanged.connect(self.switch_tab)

        # Таблицы называются по-разному (tableWidget, auditTable, ...) — берём все
        for table in self.findChildren(QTableWidget):
            table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

        self.ui.logout_btn.clicked.connect(self.on_logout)

    def switch_tab(self, index):
        if index == self.TAB_INDEX:
            return

        self.next_window = TAB_WINDOWS[index]()
        self.next_window.setGeometry(self.geometry())
        if self.isMaximized():
            self.next_window.showMaximized()
        else:
            self.next_window.show()
        QApplication.processEvents()  # дать новому окну отрисоваться до закрытия старого
        self.close()

    def on_logout(self):
        self.login_window = LoginWindow()
        self.login_window.show()
        self.close()


class RouteCatalogWindow(BaseWindow):
    TAB_INDEX = 0

    def __init__(self):
        super().__init__()
        self.ui = Ui_Routes()
        self.ui.setupUi(self)
        self.setup_common_ui()


class TourWindow(BaseWindow):
    TAB_INDEX = 1

    def __init__(self):
        super().__init__()
        self.ui = Ui_Tours()
        self.ui.setupUi(self)
        self.setup_common_ui()


class ImportWindow(BaseWindow):
    TAB_INDEX = 2

    def __init__(self):
        super().__init__()
        self.ui = Ui_Import()
        self.ui.setupUi(self)
        self.setup_common_ui()


class SyncWindow(BaseWindow):
    TAB_INDEX = 3

    def __init__(self):
        super().__init__()
        self.ui = Ui_Sync()
        self.ui.setupUi(self)
        self.setup_common_ui()


class UsersWindow(BaseWindow):
    TAB_INDEX = 4

    def __init__(self):
        super().__init__()
        self.ui = Ui_Users()
        self.ui.setupUi(self)
        self.setup_common_ui()


class AuditWindow(BaseWindow):
    TAB_INDEX = 5

    def __init__(self):
        super().__init__()
        self.ui = Ui_Audit()
        self.ui.setupUi(self)
        self.setup_common_ui()


class SettingsWindow(BaseWindow):
    TAB_INDEX = 6

    def __init__(self):
        super().__init__()
        self.ui = Ui_Settings()
        self.ui.setupUi(self)
        self.setup_common_ui()


TAB_WINDOWS = [
    RouteCatalogWindow,
    TourWindow,
    ImportWindow,
    SyncWindow,
    UsersWindow,
    AuditWindow,
    SettingsWindow,
]


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
        self.register_window = RegisterWindow()
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


class RegisterWindow(QMainWindow):
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


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")

    window = LoginWindow()
    window.show()

    sys.exit(app.exec())