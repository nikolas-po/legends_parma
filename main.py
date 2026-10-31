import sys
from PySide6.QtWidgets import (
    QApplication, QHeaderView, QMainWindow, QTableWidget, QFileDialog, QTableWidgetItem
)
from ui.add_review_window_ui import Ui_MainWindow as Ui_AddReview
from ui.audit_log_window_ui import Ui_MainWindow as Ui_Audit
from ui.create_route_window_ui import Ui_MainWindow as Ui_CreateRoute
from ui.create_tour_window_ui import Ui_MainWindow as Ui_CreateTour
from ui.export_data_window_ui import Ui_MainWindow as Ui_Export
from ui.export_gpx_window_ui import Ui_MainWindow as Ui_Gpx
from ui.import_data_window_ui import Ui_MainWindow as Ui_Import
from ui.login_window_ui import Ui_LoginWindow
from ui.register_window_ui import Ui_RegWindow
from ui.route_card_window_ui import Ui_mainWindow as Ui_RouteCard
from ui.route_directory_window_ui import Ui_MainWindow as Ui_Routes
from ui.set_api_hash_window_ui import Ui_MainWindow as Ui_Settings
from ui.sinhr_window_ui import Ui_MainWindow as Ui_Sync
from ui.tour_list_window_ui import Ui_MainWindow as Ui_Tours
from ui.users_window_ui import Ui_MainWindow as Ui_Users
def logout():
    app = QApplication.instance()
    app.login_window = LoginWindow()
    app.login_window.show()
    for widget in QApplication.topLevelWidgets():
        if isinstance(widget, QMainWindow) and widget != app.login_window:
            widget.close()
            widget.deleteLater()
class BaseWindow(QMainWindow):
    TAB_INDEX = 0
    def __init__(self):
        super().__init__()
        self.ui = None
        self.next_window = None
    def setup_common_ui(self):
        self.ui.tabWidget.currentChanged.connect(self.switch_tab)
        for table in self.findChildren(QTableWidget):
            table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.ui.logout_btn.clicked.connect(logout)
    def switch_tab(self, index):
        if index != self.TAB_INDEX:
            self.open_window(TAB_WINDOWS[index])
    def open_window(self, window_class):
        if isinstance(self, window_class):
            return
        self.next_window = window_class()
        self.next_window.setGeometry(self.geometry())
        if self.isMaximized():
            self.next_window.showMaximized()
        else:
            self.next_window.show()
        self.next_window.activateWindow()
        self.next_window.raise_()
        QApplication.processEvents()
        self.close()
class RouteCatalogWindow(BaseWindow):
    TAB_INDEX = 0
    def __init__(self):
        super().__init__()
        self.ui = Ui_Routes()
        self.ui.setupUi(self)
        self.setup_common_ui()
        self.card_window = None
        self.create_window = None
        self.ui.btn_add_route.clicked.connect(self.on_create_clicked)
        self.ui.btn_open.clicked.connect(self.on_open_clicked)
        self.ui.btn_delete.clicked.connect(self.on_delete_clicked)
        self.ui.btn_reset.clicked.connect(lambda: self.ui.searchInput.clear())
        self.fill_table()
    def fill_table(self):
        data = [
            ["1", "Горный перевал", "12.5 км", "Средняя", "Пеший"],
            ["2", "Озёрный круг", "8.2 км", "Лёгкая", "Пеший"],
            ["3", "Скалистый хребет", "18.0 км", "Сложная", "Треккинг"],
            ["4", "Лесная тропа", "6.7 км", "Лёгкая", "Пеший"],
            ["5", "Вулканический маршрут", "22.3 км", "Сложная", "Треккинг"],
        ]
        for row, row_data in enumerate(data):
            self.ui.tableWidget.insertRow(row)
            for col, value in enumerate(row_data):
                self.ui.tableWidget.setItem(row, col, QTableWidgetItem(value))
    def on_create_clicked(self):
        self.create_window = CreateRouteWindow()
        self.create_window.show()
    def on_open_clicked(self):
        self.card_window = RouteCardWindow()
        self.card_window.show()
    def on_delete_clicked(self):
        row = self.ui.tableWidget.currentRow()
        if row >= 0:
            self.ui.tableWidget.removeRow(row)
class TourWindow(BaseWindow):
    TAB_INDEX = 1
    def __init__(self):
        super().__init__()
        self.ui = Ui_Tours()
        self.ui.setupUi(self)
        self.setup_common_ui()
        self.create_window = None
        self.ui.btn_new_tour.clicked.connect(self.on_create_clicked)
        self.fill_table()
    def fill_table(self):
        data = [
            ["1", "Поход на Эльбрус", "12.06.2025", "8", "Запланирован"],
            ["2", "Озёрный уикенд", "20.07.2025", "12", "Открыт"],
            ["3", "Скалолазание в Крыму", "05.08.2025", "6", "Запланирован"],
            ["4", "Лесной квест", "15.09.2025", "15", "Открыт"],
            ["5", "Вулканический тур", "01.10.2025", "10", "Запланирован"],
        ]
        table = self.findChild(QTableWidget)
        if table:
            for row, row_data in enumerate(data):
                table.insertRow(row)
                for col, value in enumerate(row_data):
                    table.setItem(row, col, QTableWidgetItem(value))
    def on_create_clicked(self):
        self.create_window = CreateTourWindow()
        self.create_window.show()
class ImportWindow(BaseWindow):
    TAB_INDEX = 2
    def __init__(self):
        super().__init__()
        self.ui = Ui_Import()
        self.ui.setupUi(self)
        self.setup_common_ui()
        self.ui.btn_import.clicked.connect(self.on_import_clicked)
        self.ui.btn_mode_export.clicked.connect(lambda: self.open_window(ExportWindow))
        self.ui.btn_mode_gpx.clicked.connect(lambda: self.open_window(GpxExportWindow))
    def on_import_clicked(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Выберите файл для импорта", "", "Все файлы (*.*)")
        if file_name:
            self.ui.successBanner.setVisible(True)
class ExportWindow(BaseWindow):
    TAB_INDEX = 2
    def __init__(self):
        super().__init__()
        self.ui = Ui_Export()
        self.ui.setupUi(self)
        self.setup_common_ui()
        self.ui.btn_browse.clicked.connect(self.on_browse_clicked)
        self.ui.btn_export.clicked.connect(self.on_export_clicked)
        self.ui.btn_mode_import.clicked.connect(lambda: self.open_window(ImportWindow))
        self.ui.btn_mode_gpx.clicked.connect(lambda: self.open_window(GpxExportWindow))
    def on_browse_clicked(self):
        path, _ = QFileDialog.getSaveFileName(self, "Сохранить файл", "", "Все файлы (*.*)")
        if path:
            self.ui.inputPath.setText(path)
    def on_export_clicked(self):
        if self.ui.inputPath.text():
            try:
                with open(self.ui.inputPath.text(), 'w', encoding='utf-8') as f:
                    f.write("Экспортированные данные")
                self.ui.successBanner.setVisible(True)
            except Exception:
                self.ui.errorBanner.setVisible(True)
class GpxExportWindow(BaseWindow):
    TAB_INDEX = 2
    def __init__(self):
        super().__init__()
        self.ui = Ui_Gpx()
        self.ui.setupUi(self)
        self.setup_common_ui()
        self.ui.btn_browse.clicked.connect(self.on_browse_clicked)
        self.ui.btn_export.clicked.connect(self.on_export_clicked)
        self.ui.btn_cancel.clicked.connect(self.close)
        self.ui.btn_mode_import.clicked.connect(lambda: self.open_window(ImportWindow))
        self.ui.btn_mode_export.clicked.connect(lambda: self.open_window(ExportWindow))
    def on_browse_clicked(self):
        path, _ = QFileDialog.getSaveFileName(self, "Сохранить GPX", "", "GPX Files (*.gpx)")
        if path:
            self.ui.inputPath.setText(path)
    def on_export_clicked(self):
        if self.ui.inputPath.text():
            try:
                with open(self.ui.inputPath.text(), 'w', encoding='utf-8') as f:
                    f.write("<gpx></gpx>")
                self.ui.successBanner.setVisible(True)
            except Exception:
                self.ui.errorBanner.setVisible(True)
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
        self.fill_table()
    def fill_table(self):
        data = [
            ["1", "ivanov", "Администратор", "ivanov@mail.ru", "Активен"],
            ["2", "petrova", "Модератор", "petrova@mail.ru", "Активен"],
            ["3", "sidorov", "Пользователь", "sidorov@mail.ru", "Активен"],
            ["4", "smirnova", "Пользователь", "smirnova@mail.ru", "Заблокирован"],
            ["5", "kozlov", "Модератор", "kozlov@mail.ru", "Активен"],
        ]
        table = self.findChild(QTableWidget)
        if table:
            for row, row_data in enumerate(data):
                table.insertRow(row)
                for col, value in enumerate(row_data):
                    table.setItem(row, col, QTableWidgetItem(value))
class AuditWindow(BaseWindow):
    TAB_INDEX = 5
    def __init__(self):
        super().__init__()
        self.ui = Ui_Audit()
        self.ui.setupUi(self)
        self.setup_common_ui()
        self.fill_table()
    def fill_table(self):
        data = [
            ["1", "Вход в систему", "ivanov", "31.10.2026 08:15", "Успешный вход"],
            ["2", "Создание маршрута", "petrova", "31.10.2026 09:02", "Добавлен «Горный перевал»"],
            ["3", "Удаление тура", "sidorov", "31.10.2026 10:41", "Удалён тур №3"],
            ["4", "Экспорт GPX", "kozlov", "31.10.2026 11:20", "Файл route_5.gpx"],
            ["5", "Изменение роли", "ivanov", "31.10.2026 12:05", "smirnova → Пользователь"],
        ]
        table = self.findChild(QTableWidget)
        if table:
            for row, row_data in enumerate(data):
                table.insertRow(row)
                for col, value in enumerate(row_data):
                    table.setItem(row, col, QTableWidgetItem(value))
class SettingsWindow(BaseWindow):
    TAB_INDEX = 6
    def __init__(self):
        super().__init__()
        self.ui = Ui_Settings()
        self.ui.setupUi(self)
        self.setup_common_ui()
class RouteCardWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_RouteCard()
        self.ui.setupUi(self)
        self.ui.tabWidget.hide()
        self.ui.logout_btn.hide()
        self.review_window = None
        self.ui.btn_back.clicked.connect(self.close)
        self.ui.btn_leave_review.clicked.connect(self.on_add_review_clicked)
        self.ui.btn_delete.clicked.connect(self.close)
    def on_add_review_clicked(self):
        self.review_window = AddReviewWindow()
        self.review_window.show()
class CreateRouteWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_CreateRoute()
        self.ui.setupUi(self)
        self.ui.tabWidget.setCurrentIndex(0)
        self.ui.tabWidget.tabBar().hide()
        self.ui.logout_btn.hide()
        self.ui.btn_back.clicked.connect(self.close)
        self.ui.btn_cancel.clicked.connect(self.close)
        self.ui.btn_save.clicked.connect(self.close)
class CreateTourWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_CreateTour()
        self.ui.setupUi(self)
        self.ui.tabWidget.setCurrentIndex(1)
        self.ui.tabWidget.tabBar().hide()
        self.ui.logout_btn.hide()
        self.ui.btn_back.clicked.connect(self.close)
        self.ui.btn_cancel.clicked.connect(self.close)
        self.ui.btn_save.clicked.connect(self.close)
class AddReviewWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_AddReview()
        self.ui.setupUi(self)
        self.ui.tabWidget.setCurrentIndex(0)
        self.ui.tabWidget.tabBar().hide()
        self.ui.logout_btn.hide()
        self.ui.btn_cancel.clicked.connect(self.close)
        self.ui.btn_publish.clicked.connect(self.close)
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
        self.ui.reg_btn_2.clicked.connect(self.on_login_clicked)
    def on_login_clicked(self):
        self.login_window = LoginWindow()
        self.login_window.show()
        self.hide()
if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    app.login_window = LoginWindow()
    app.login_window.show()
    sys.exit(app.exec())