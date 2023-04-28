from PyQt6.QtWidgets import QWidget
from PyQt6.QtCore import pyqtSignal
from ui.base_qt_ui.ui_coord_widget import Ui_Form


class CoordWidget(QWidget):

    delete = pyqtSignal(int)

    def __init__(self, id_widget: int, parent=None):
        super(CoordWidget, self).__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.id_widget = id_widget
        # self.ui.groupBox.setTitle(str(id_widget))
        self.ui.delete_button.clicked.connect(self.press_del)
        self.ui.volume_checkbox.clicked.connect(self.press_volume_checkbox)
        self.ui.mass_checkbox.clicked.connect(self.press_mass_checkbox)

    def press_del(self):
        self.ui.groupBox.setParent(None)
        self.delete.emit(self.id_widget)

    def press_volume_checkbox(self):
        """
        Если нажали на выбор объема, до сбрасываем все чекбоксы массы
        :return:
        """
        self.ui.mass_checkbox.setChecked(False)
        self.ui.g_checkbox.setChecked(False)
        self.ui.percent_checkbox.setChecked(False)

    def press_mass_checkbox(self):
        """
        Если нажали на выбор объема, до сбрасываем все чекбоксы объема
        :return:
        """
        self.ui.volume_checkbox.setChecked(False)
        self.ui.ml_checkbox.setChecked(False)
        self.ui.percent_checkbox_2.setChecked(False)


