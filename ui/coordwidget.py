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

        self.ui.mol_mass_comboBox.setEditable(True)
        self.ui.mol_mass_label.setToolTip('Молярная масса газа.\nОсобенности ввода:\n1) Десятичная дробь может вводится как через запятую, так и через точку.\n    Пример: 1,5; 2.6\n2) Если был сделан выбор из предложенных вариантов, то не нужно ничего стирать. Программа сама определит число.\n    Пример: O2: 32, He: 4')
        self.base_gases = ['H: 1,008', 'H2: 2,016', 'NH3: 17,031', 'CO: 28,01', 'H2O: 18,016', 'CO2: 44,009', 'N2: 28,016', 'O2: 31,998', 'He: 4,003', 'Ar: 39,944', 'Ne: 20,183', 'Cl2: 70,914', 'NO2: 46,0055', 'NO: 30,008', 'O3: 48,00']
        self.ui.mol_mass_comboBox.addItems(self.base_gases)
        self.ui.mass_volume_comboBox.setEditable(True)

        self.ui.delete_button.clicked.connect(self.press_del)

    def press_del(self):
        self.ui.groupBox.setParent(None)
        self.delete.emit(self.id_widget)
