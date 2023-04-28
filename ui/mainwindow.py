from PyQt6.QtWidgets import QMainWindow, QMessageBox

from ui.base_qt_ui.ui_main_window import Ui_MainWindow
from ui.coordwidget import CoordWidget
from handling_input_data.main import MolMassInputException, VolumeMassInputException, GasInput


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.counter_id: int = 0

        self.error = QMessageBox()
        self.error.setWindowTitle('Ошибка!')
        self.error.setText('ошибка')

        self.ui.add_input_btn.clicked.connect(self.add_coord_widget)
        self.ui.clear_inputs_btn.clicked.connect(self.clear_area)
        self.ui.calculate_btn.clicked.connect(self.calculate)

    def add_coord_widget(self):
        self.counter_id += 1
        coord_widget = CoordWidget(self.counter_id)
        self.ui.coordwidget_layout.addWidget(coord_widget)
        coord_widget.delete.connect(self.delete_coordwidget)

        self.recount_coord_widgets()

    def clear_area(self):
        while self.ui.coordwidget_layout.count() > 0:
            item = self.ui.coordwidget_layout.takeAt(0)
            item.widget().deleteLater()

        self.ui.temp_doubleSpinBox.setProperty("value", 273.0)
        self.ui.pressure_doubleSpinBox.setProperty("value", 101300.0)

    def delete_coordwidget(self, wid: int):
        widget = self.sender()
        self.ui.coordwidget_layout.removeWidget(widget)
        widget.deleteLater()

        self.recount_coord_widgets()

    def calculate(self):
        temp_value = self.ui.temp_doubleSpinBox.value()
        p_value = self.ui.pressure_doubleSpinBox.value()

        print(temp_value, p_value)
        items = [self.ui.coordwidget_layout.itemAt(i).widget() for i in range(self.ui.coordwidget_layout.count())]

        if not items:
            self.error.setText('Введите газы!')
            self.error.exec()
        else:
            for w in items:
                GasInput()
                print(w.id_widget)

    def recount_coord_widgets(self):
        for i in range(self.ui.coordwidget_layout.count()):
            self.ui.coordwidget_layout.itemAt(i).widget().ui.groupBox.setTitle(str(i+1))
