from PyQt6.QtWidgets import QMainWindow, QMessageBox
from PyQt6 import QtGui
from ui.base_qt_ui.ui_main_window import Ui_MainWindow
from ui.coordwidget import CoordWidget
from handling_input_data.main import MolMassInputException, VolumeMassInputException, GasInput, GasCalculations, PercentSumError, GasTypeError


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.counter_id: int = 0

        self.setWindowIcon(QtGui.QIcon('logo.png'))

        self.about_program = QMessageBox()
        self.about_program.setWindowTitle('О программе')
        self.about_program.setText('Программа для расчета индивидуальной газовой постоянной смеси газов. Сделано для РХТУ. \n\nАвтор: Хатымов Марат Рустемович\nEmail: maratxat@ya.ru\nTelegram: @i_m_good_man')
        self.ui.manual_button.clicked.connect(self.press_manual_button)

        self.error = QMessageBox()
        self.error.setWindowTitle('Ошибка!')
        self.error.setText('ошибка')

        self.ui.add_input_btn.clicked.connect(self.add_coord_widget)
        self.ui.clear_inputs_btn.clicked.connect(self.clear_area)
        self.ui.calculate_btn.clicked.connect(self.calculate)

        # добавляем самый первый виджет в начале
        self.add_coord_widget()

        # по умолчанию чекбокс массы выставлен
        self.ui.mass_checkbox.setChecked(True)
        self.ui.g_checkbox.setChecked(True)

        # обрабатываем конфликты между чекбоксами
        self.ui.volume_checkbox.clicked.connect(self.press_volume_checkbox)
        self.ui.ml_checkbox.clicked.connect(self.press_ml_checkbox)
        self.ui.percent_checkbox_2.clicked.connect(self.press_percent_checkbox_2)

        self.ui.mass_checkbox.clicked.connect(self.press_mass_checkbox)
        self.ui.g_checkbox.clicked.connect(self.press_g_checkbox)
        self.ui.percent_checkbox.clicked.connect(self.press_percent_checkbox)

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

        self.ui.R_result_label.setText(self.get_clear_part_of_R_result_label())
        self.ui.M_result_label.setText(self.get_clear_part_of_M_result_label())

    def get_clear_part_of_R_result_label(self):
        return self.ui.R_result_label.text().split(':')[0].strip() + ':'

    def get_clear_part_of_M_result_label(self):
        return self.ui.M_result_label.text().split(':')[0].strip() + ':'

    def delete_coordwidget(self, wid: int):
        widget = self.sender()
        self.ui.coordwidget_layout.removeWidget(widget)
        widget.deleteLater()

        self.recount_coord_widgets()

    def recount_coord_widgets(self):
        for i in range(self.ui.coordwidget_layout.count()):
            self.ui.coordwidget_layout.itemAt(i).widget().ui.groupBox.setTitle(f'Газ {str(i+1)}')

    def calculate(self):
        temp_value = self.ui.temp_doubleSpinBox.value()
        p_value = self.ui.pressure_doubleSpinBox.value()

        items = [self.ui.coordwidget_layout.itemAt(i).widget() for i in range(self.ui.coordwidget_layout.count())]

        if not items:
            self.error.setText('Введите газы!')
            self.error.exec()
        else:
            gas_list = []
            for w in items:
                args_list = [w.ui.mol_mass_comboBox.currentText(),
                             w.ui.mass_volume_comboBox.currentText(),
                             w.ui.volume_checkbox.isChecked(),
                             w.ui.percent_checkbox_2.isChecked(),
                             w.ui.ml_checkbox.isChecked(),
                             w.ui.mass_checkbox.isChecked(),
                             w.ui.percent_checkbox.isChecked(),
                             w.ui.g_checkbox.isChecked(),
                             p_value, temp_value
                             ]
                try:
                    gas = GasInput(*args_list).process_input_data()
                    gas_list.append(gas)
                except MolMassInputException as error:
                    self.error.setText(f'{w.ui.groupBox.title()}. {str(error)}')
                    self.error.exec()
                except VolumeMassInputException as error:
                    self.error.setText(f'{w.ui.groupBox.title()}. {str(error)}')
                    self.error.exec()

            # если во всех газах оказались валидные данные
            if len(gas_list) != len(items):
                return
            else:
                gc = GasCalculations(gas_list)
                try:
                    gc.check_gases()
                    self.ui.R_result_label.setText(f'{self.get_clear_part_of_R_result_label()} {gc.R}')
                    self.ui.M_result_label.setText(f'{self.get_clear_part_of_M_result_label()} {gc.M}')
                except PercentSumError as err:
                    self.error.setText(f'Ошибка процентов. {str(err)}')
                    self.error.exec()
                except GasTypeError as err:
                    self.error.setText(f'Ошибка типов газов. {str(err)}')
                    self.error.exec()
                except Exception as err:
                    self.error.setText(f'Возникла ошибка при расчете. Проверьте переданные значения.')
                    self.error.exec()

    def press_manual_button(self):
        self.about_program.exec()

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