# Form implementation generated from reading ui file 'C:\Users\marat\PycharmProjects\scientific_calculator\ui\base_qt_ui\ui_main_window.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(907, 506)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.base_layout = QtWidgets.QVBoxLayout()
        self.base_layout.setObjectName("base_layout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.manual_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.manual_button.setObjectName("manual_button")
        self.horizontalLayout.addWidget(self.manual_button)
        self.clear_inputs_btn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.clear_inputs_btn.setObjectName("clear_inputs_btn")
        self.horizontalLayout.addWidget(self.clear_inputs_btn)
        self.add_input_btn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.add_input_btn.setObjectName("add_input_btn")
        self.horizontalLayout.addWidget(self.add_input_btn)
        self.calculate_btn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.calculate_btn.setObjectName("calculate_btn")
        self.horizontalLayout.addWidget(self.calculate_btn)
        self.base_layout.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.temp_label = QtWidgets.QLabel(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.temp_label.setFont(font)
        self.temp_label.setObjectName("temp_label")
        self.horizontalLayout_3.addWidget(self.temp_label, 0, QtCore.Qt.AlignmentFlag.AlignLeft)
        self.temp_doubleSpinBox = QtWidgets.QDoubleSpinBox(parent=self.centralwidget)
        self.temp_doubleSpinBox.setDecimals(0)
        self.temp_doubleSpinBox.setMinimum(-100000.0)
        self.temp_doubleSpinBox.setMaximum(100000000000.0)
        self.temp_doubleSpinBox.setProperty("value", 273.0)
        self.temp_doubleSpinBox.setObjectName("temp_doubleSpinBox")
        self.horizontalLayout_3.addWidget(self.temp_doubleSpinBox)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.pressure_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.pressure_label.setObjectName("pressure_label")
        self.horizontalLayout_3.addWidget(self.pressure_label, 0, QtCore.Qt.AlignmentFlag.AlignLeft)
        self.pressure_doubleSpinBox = QtWidgets.QDoubleSpinBox(parent=self.centralwidget)
        self.pressure_doubleSpinBox.setDecimals(0)
        self.pressure_doubleSpinBox.setMinimum(-100000.0)
        self.pressure_doubleSpinBox.setMaximum(100000000000.0)
        self.pressure_doubleSpinBox.setProperty("value", 101300.0)
        self.pressure_doubleSpinBox.setObjectName("pressure_doubleSpinBox")
        self.horizontalLayout_3.addWidget(self.pressure_doubleSpinBox)
        self.base_layout.addLayout(self.horizontalLayout_3)
        self.inputs_area = QtWidgets.QScrollArea(parent=self.centralwidget)
        self.inputs_area.setWidgetResizable(True)
        self.inputs_area.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignTop)
        self.inputs_area.setObjectName("inputs_area")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setEnabled(True)
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 885, 347))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy)
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setContentsMargins(9, 3, -1, 3)
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setObjectName("verticalLayout")
        self.coordwidget_layout = QtWidgets.QVBoxLayout()
        self.coordwidget_layout.setSpacing(3)
        self.coordwidget_layout.setObjectName("coordwidget_layout")
        self.verticalLayout.addLayout(self.coordwidget_layout)
        self.inputs_area.setWidget(self.scrollAreaWidgetContents)
        self.base_layout.addWidget(self.inputs_area)
        self.M_result_label = QtWidgets.QLabel(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.M_result_label.setFont(font)
        self.M_result_label.setObjectName("M_result_label")
        self.base_layout.addWidget(self.M_result_label)
        self.R_result_label = QtWidgets.QLabel(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.R_result_label.setFont(font)
        self.R_result_label.setObjectName("R_result_label")
        self.base_layout.addWidget(self.R_result_label)
        self.horizontalLayout_2.addLayout(self.base_layout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Калькулятор для газов"))
        self.manual_button.setText(_translate("MainWindow", "О программе"))
        self.clear_inputs_btn.setText(_translate("MainWindow", "Очистить поля"))
        self.add_input_btn.setText(_translate("MainWindow", "Добавить газ"))
        self.calculate_btn.setText(_translate("MainWindow", "Расчёт"))
        self.temp_label.setText(_translate("MainWindow", "Температура T [К]"))
        self.pressure_label.setText(_translate("MainWindow", "Давление p [Па]"))
        self.M_result_label.setText(_translate("MainWindow", "Молярная масса M [г/моль]: "))
        self.R_result_label.setText(_translate("MainWindow", "Индивидуальная газовая постоянная R [Дж/(К*кг)]: "))
