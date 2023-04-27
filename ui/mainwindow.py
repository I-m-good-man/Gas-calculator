from PyQt6.QtWidgets import QMainWindow

from ui.base_qt_ui.ui_main_window import Ui_MainWindow
from ui.coordwidget import CoordWidget


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.counter_id: int = 0

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

    def delete_coordwidget(self, wid: int):
        widget = self.sender()
        self.ui.coordwidget_layout.removeWidget(widget)
        widget.deleteLater()

        self.recount_coord_widgets()

    

