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

        self.ui.volume_checkbox.setToolTip('Объём. Выберите ввод в процентах или в мл.\nОсобенности ввода:\n1) Единицы измерения писать не нужно, записывается только число.\n2) Десятичная дробь может вводится как через запятую, так и через точку.\n    Пример: 1,5; 2.6')
        self.ui.mass_checkbox.setToolTip('Масса. Выберите ввод в процентах или в г.\nОсобенности ввода:\n1) Единицы измерения писать не нужно, записывается только число.\n2) Десятичная дробь может вводится как через запятую, так и через точку.\n    Пример: 1,5; 2.6')

        self.ui.mol_mass_comboBox.setEditable(True)
        self.ui.mol_mass_label.setToolTip('Молярная масса газа.\nОсобенности ввода:\n1) Десятичная дробь может вводится как через запятую, так и через точку.\n    Пример: 1,5; 2.6\n2) Если был сделан выбор из предложенных вариантов, то не нужно ничего стирать. Программа сама определит число.\n    Пример: O2: 32, He: 4')
        self.base_gases = ['H: 1,008', 'H2: 2,016', 'NH3: 17,031', 'CO: 28,01', 'H2O: 18,016', 'CO2: 44,009', 'N2: 28,016', 'O2: 31,998', 'He: 4,003', 'Ar: 39,944', 'Ne: 20,183', 'Cl2: 70,914', 'NO2: 46', 'NO: 30,008', 'O3: 48,00']
        self.ui.mol_mass_comboBox.addItems(self.base_gases)
        self.ui.mass_volume_comboBox.setEditable(True)

        self.ui.delete_button.clicked.connect(self.press_del)

        # по умолчанию чекбокс массы выставлен
        self.ui.mass_checkbox.setChecked(True)
        self.ui.g_checkbox.setChecked(True)

        # делаем подробный выбор подчекбоксов объема и массы недоступными, пока не выберут чекбокс объема или массы
        self.ui.ml_checkbox.setCheckable(False)
        self.ui.percent_checkbox_2.setCheckable(False)

        # обрабатываем конфликты между чекбоксами
        self.ui.volume_checkbox.clicked.connect(self.press_volume_checkbox)
        self.ui.ml_checkbox.clicked.connect(self.press_ml_checkbox)
        self.ui.percent_checkbox_2.clicked.connect(self.press_percent_checkbox_2)

        self.ui.mass_checkbox.clicked.connect(self.press_mass_checkbox)
        self.ui.g_checkbox.clicked.connect(self.press_g_checkbox)
        self.ui.percent_checkbox.clicked.connect(self.press_percent_checkbox)

    def press_del(self):
        self.ui.groupBox.setParent(None)
        self.delete.emit(self.id_widget)

    def press_volume_checkbox(self):
        """
        Если нажали на выбор объема, то обрабатываем чекбоксы
        :return:
        """
        # чекбокс массы - false
        self.ui.mass_checkbox.setChecked(False)

        # чекбоксы за подробный выбор массы делаем false и некликабельными
        self.ui.g_checkbox.setChecked(False)
        self.ui.g_checkbox.setCheckable(False)
        self.ui.percent_checkbox.setChecked(False)
        self.ui.percent_checkbox.setCheckable(False)


        # делаем кликабельными чекбоксы объема и выбираем один чекбокс
        self.ui.ml_checkbox.setCheckable(True)
        self.ui.ml_checkbox.setChecked(True)
        self.ui.percent_checkbox_2.setCheckable(True)

    def press_g_checkbox(self):
        """
        Если чекбокс прцоентов был уже выбран, то его обнуляем
        :return:
        """
        if self.ui.percent_checkbox.checkState():
            self.ui.percent_checkbox.setChecked(False)

    def press_percent_checkbox(self):
        """
        Если чекбокс граммов был уже выбран, то его обнуляем
        :return:
        """
        if self.ui.g_checkbox.checkState():
            self.ui.g_checkbox.setChecked(False)

    def press_mass_checkbox(self):
        """
        Если нажали на выбор массы, то обрабатываем чекбоксы
        :return:
        """
        # чекбокс объема - false
        self.ui.volume_checkbox.setChecked(False)

        # чекбоксы за подробный выбор объема делаем false и некликабельными
        self.ui.ml_checkbox.setChecked(False)
        self.ui.ml_checkbox.setCheckable(False)
        self.ui.percent_checkbox_2.setChecked(False)
        self.ui.percent_checkbox_2.setCheckable(False)

        # делаем кликабельными чекбоксы массы и выбираем один чекбокс
        self.ui.g_checkbox.setCheckable(True)
        self.ui.g_checkbox.setChecked(True)
        self.ui.percent_checkbox.setCheckable(True)

    def press_ml_checkbox(self):
        """
        Если чекбокс процентов был уже выбран, то его обнуляем
        :return:
        """
        if self.ui.percent_checkbox_2.checkState():
            self.ui.percent_checkbox_2.setChecked(False)

    def press_percent_checkbox_2(self):
        """
        Если чекбокс мл был уже выбран, то его обнуляем
        :return:
        """
        if self.ui.ml_checkbox.checkState():
            self.ui.ml_checkbox.setChecked(False)
