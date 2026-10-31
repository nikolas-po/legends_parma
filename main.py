import sys
from PySide6.QtWidgets import (
    QApplication, QHeaderView, QMainWindow, QTableWidget, QFileDialog,
    QTableWidgetItem
)
from PySide6.QtCore import Qt
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
from ui.tour_card_window_ui import Ui_MainWindow as Ui_TourCard
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
        self.ui.btn_edit.clicked.connect(self.on_edit_clicked)
        self.ui.btn_delete.clicked.connect(self.on_delete_clicked)
        self.ui.btn_reset.clicked.connect(lambda: self.ui.searchInput.clear())
        self.fill_table()

    def fill_table(self):
        data = [
            ["Маньпупунёр", "Пеший", "14.5", "8", "Троицко-Печорский", "4.9"],
            ["Плато Парма", "Пеший", "9.2", "5", "Усть-Куломский", "4.6"],
            ["По реке Печора", "Водный", "32.0", "12", "Печорский", "4.8"],
            ["Югыд ва — тропа", "Треккинг", "18.7", "9", "Вуктыл", "4.7"],
            ["Леса вокруг Ухты", "Вело", "22.3", "6", "Ухта", "4.4"],
        ]
        for row, row_data in enumerate(data):
            self.ui.tableWidget.insertRow(row)
            for col, value in enumerate(row_data):
                self.ui.tableWidget.setItem(row, col, QTableWidgetItem(value))

    def on_create_clicked(self):
        self.create_window = CreateRouteWindow()
        self.create_window.show()

    def on_open_clicked(self):
        row = self.ui.tableWidget.currentRow()
        if row < 0:
            return
        data = {
            "name": self.ui.tableWidget.item(row, 0).text(),
            "type": self.ui.tableWidget.item(row, 1).text(),
            "length": self.ui.tableWidget.item(row, 2).text(),
            "time": self.ui.tableWidget.item(row, 3).text(),
            "region": self.ui.tableWidget.item(row, 4).text(),
        }
        self.card_window = RouteCardWindow(data)
        self.card_window.show()

    def on_edit_clicked(self):
        row = self.ui.tableWidget.currentRow()
        if row < 0:
            return
        name = self.ui.tableWidget.item(row, 0).text()
        self.create_window = CreateRouteWindow(name)
        self.create_window.show()

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
        self.card_window = None
        self.ui.btn_new_tour.clicked.connect(self.on_create_clicked)
        self.ui.btn_edit_left.clicked.connect(self.on_edit_clicked)
        self.ui.btn_open_left.clicked.connect(self.on_open_clicked)
        self.fill_table()

    def fill_table(self):
        data = [
            ["К столбы Маньпупунёра", "12.06.2025", "18.06.2025", "Активный"],
            ["Сплав по Печоре", "20.07.2025", "27.07.2025", "Открыт"],
            ["Парма и Югыд ва", "05.08.2025", "12.08.2025", "Запланирован"],
            ["Ухта — лесные тропы", "15.09.2025", "19.09.2025", "Открыт"],
            ["Осенний Воркута", "01.10.2025", "07.10.2025", "Запланирован"],
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

    def on_edit_clicked(self):
        table = self.findChild(QTableWidget)
        row = table.currentRow()
        if row < 0:
            return
        name = table.item(row, 0).text()
        self.create_window = CreateTourWindow(name)
        self.create_window.show()

    def on_open_clicked(self):
        self.card_window = TourCardWindow()
        self.card_window.show()


class ImportWindow(BaseWindow):
    TAB_INDEX = 2

    def __init__(self):
        super().__init__()
        self.ui = Ui_Import()
        self.ui.setupUi(self)
        self.setup_common_ui()

        self.ui.btn_mode_export.clicked.connect(lambda: self.open_window(ExportWindow))
        self.ui.btn_mode_gpx.clicked.connect(lambda: self.open_window(GpxExportWindow))

        self.ui.dropArea.setAcceptDrops(True)
        self.ui.dropArea.mousePressEvent = self.on_drop_area_clicked
        self.ui.dropArea.dragEnterEvent = self.on_drag_enter
        self.ui.dropArea.dropEvent = self.on_drop

    def on_drop_area_clicked(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            QFileDialog.getOpenFileName(
                self, "Выберите файл для импорта", "", "Все файлы (*.*)"
            )

    def on_drag_enter(self, event):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()
        else:
            event.ignore()

    def on_drop(self, event):
        urls = event.mimeData().urls()
        if urls:
            self.ui.lbl_drop_main.setText(urls[0].toLocalFile())


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
        self.fill_table()

    def fill_table(self):
        data = [
            ["OSM / Overpass", "Маньпупунёр", "Готово"],
            ["OpenWeather", "Плато Парма", "В очереди"],
            ["Wikipedia", "Печора", "Ошибка"],
            ["OSM / Overpass", "Югыд ва", "Готово"],
            ["OpenWeather", "Ухта", "В очереди"],
        ]
        table = self.ui.tableQueue
        for row, row_data in enumerate(data):
            table.insertRow(row)
            for col, value in enumerate(row_data):
                table.setItem(row, col, QTableWidgetItem(value))


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
            ["admin", "Алексей Иванов", "Администратор", "Активен", "30.10.2026"],
            ["petrova", "Мария Петрова", "Модератор", "Активен", "29.10.2026"],
            ["sidorov", "Игорь Сидоров", "Пользователь", "Активен", "28.10.2026"],
            ["smirnova", "Елена Смирнова", "Пользователь", "Заблокирован", "15.10.2026"],
            ["kozlov", "Дмитрий Козлов", "Модератор", "Активен", "31.10.2026"],
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
        self.ui.btn_export.clicked.connect(self.on_export_csv)
        self.fill_table()

    def fill_table(self):
        data = [
            ["31.10.2026 08:15", "admin", "Вход", "Система", "Успех", "Успешный вход"],
            ["31.10.2026 09:02", "petrova", "Создание", "Маршрут", "Успех", "Добавлен «Маньпупунёр»"],
            ["31.10.2026 10:41", "sidorov", "Удаление", "Тур", "Успех", "Удалён тур «Парма»"],
            ["31.10.2026 11:20", "kozlov", "Экспорт", "GPX", "Успех", "Файл manpupuner.gpx"],
            ["31.10.2026 12:05", "admin", "Изменение роли", "Пользователь", "Успех", "smirnova → Пользователь"],
        ]
        table = self.ui.auditTable
        for row, row_data in enumerate(data):
            table.insertRow(row)
            for col, value in enumerate(row_data):
                table.setItem(row, col, QTableWidgetItem(value))

    def on_export_csv(self):
        QFileDialog.getSaveFileName(
            self, "Выгрузить журнал в CSV", "audit_log.csv", "CSV Files (*.csv)"
        )


class SettingsWindow(BaseWindow):
    TAB_INDEX = 6

    def __init__(self):
        super().__init__()
        self.ui = Ui_Settings()
        self.ui.setupUi(self)
        self.setup_common_ui()


class RouteCardWindow(QMainWindow):
    def __init__(self, data=None):
        super().__init__()
        self.ui = Ui_RouteCard()
        self.ui.setupUi(self)
        self.ui.tabWidget.hide()
        self.ui.logout_btn.hide()
        self.review_window = None
        self.edit_window = None
        self.ui.btn_back.clicked.connect(self.close)
        self.ui.btn_leave_review.clicked.connect(self.on_add_review_clicked)
        self.ui.btn_edit.clicked.connect(self.on_edit_clicked)
        self.ui.btn_export.clicked.connect(self.on_export_gpx_clicked)
        self.ui.btn_delete.clicked.connect(self.close)
        if data:
            self.fill_data(data)

    def fill_data(self, data):
        if data.get("name"):
            self.ui.lbl_route_title.setText(data["name"])
        parts = []
        if data.get("type"):
            parts.append(data["type"])
        if data.get("length"):
            parts.append(f"{data['length']} км")
        if data.get("time"):
            parts.append(f"{data['time']} ч")
        if data.get("region"):
            parts.append(data["region"])
        if parts:
            self.ui.lbl_route_props.setText(" · ".join(parts))

    def on_add_review_clicked(self):
        self.review_window = AddReviewWindow()
        self.review_window.show()

    def on_edit_clicked(self):
        name = self.ui.lbl_route_title.text()
        self.edit_window = CreateRouteWindow(name)
        self.edit_window.show()

    def on_export_gpx_clicked(self):
        QFileDialog.getSaveFileName(
            self, "Экспорт GPX", "route.gpx", "GPX Files (*.gpx)"
        )


class TourCardWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_TourCard()
        self.ui.setupUi(self)
        self.ui.tabWidget.hide()
        self.ui.logout_btn.hide()
        self.edit_window = None
        self.ui.btn_back.clicked.connect(self.close)
        self.ui.btn_edit.clicked.connect(self.on_edit_clicked)
        self.ui.btn_change_status.clicked.connect(self.on_change_status_clicked)
        self.ui.btn_cancel_tour.clicked.connect(self.close)
        self.fill_routes_table()

    def fill_routes_table(self):
        data = [
            ["Маньпупунёр", "Пеший", "14.5", "8"],
            ["Плато Парма", "Пеший", "9.2", "5"],
            ["По реке Печора", "Водный", "32.0", "12"],
        ]
        table = self.ui.routesTable
        table.setColumnCount(4)
        table.setHorizontalHeaderLabels(["Название", "Тип", "Км", "Ч"])
        table.verticalHeader().setVisible(False)
        table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        for row, row_data in enumerate(data):
            table.insertRow(row)
            for col, value in enumerate(row_data):
                table.setItem(row, col, QTableWidgetItem(value))

    def on_edit_clicked(self):
        name = self.ui.lbl_main_title.text()
        self.edit_window = CreateTourWindow(name)
        self.edit_window.show()

    def on_change_status_clicked(self):
        pass


class CreateRouteWindow(QMainWindow):
    def __init__(self, name=None):
        super().__init__()
        self.ui = Ui_CreateRoute()
        self.ui.setupUi(self)
        self.ui.tabWidget.setCurrentIndex(0)
        self.ui.tabWidget.tabBar().hide()
        self.ui.logout_btn.hide()
        self.ui.btn_back.clicked.connect(self.close)
        self.ui.btn_cancel.clicked.connect(self.close)
        self.ui.btn_save.clicked.connect(self.close)
        if name:
            self.ui.input_route_name.setText(name)


class CreateTourWindow(QMainWindow):
    def __init__(self, name=None):
        super().__init__()
        self.ui = Ui_CreateTour()
        self.ui.setupUi(self)
        self.ui.tabWidget.setCurrentIndex(1)
        self.ui.tabWidget.tabBar().hide()
        self.ui.logout_btn.hide()
        self.ui.btn_back.clicked.connect(self.close)
        self.ui.btn_cancel.clicked.connect(self.close)
        self.ui.btn_save.clicked.connect(self.close)
        if name:
            self.ui.inputName.setText(name)


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