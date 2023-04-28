# Form implementation generated from reading ui file 'C:\Users\marat\PycharmProjects\scientific_calculator\ui\base_qt_ui\ui_coord_widget.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(643, 268)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupBox = QtWidgets.QGroupBox(parent=Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMinimumSize(QtCore.QSize(0, 120))
        self.groupBox.setMaximumSize(QtCore.QSize(16777215, 120))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.input_data = QtWidgets.QHBoxLayout()
        self.input_data.setObjectName("input_data")
        self.mol_mass_input = QtWidgets.QVBoxLayout()
        self.mol_mass_input.setObjectName("mol_mass_input")
        self.mol_mass_label = QtWidgets.QLabel(parent=self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        self.mol_mass_label.setFont(font)
        self.mol_mass_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.mol_mass_label.setObjectName("mol_mass_label")
        self.mol_mass_input.addWidget(self.mol_mass_label)
        self.mol_mass_comboBox = QtWidgets.QComboBox(parent=self.groupBox)
        self.mol_mass_comboBox.setObjectName("mol_mass_comboBox")
        self.mol_mass_input.addWidget(self.mol_mass_comboBox)
        self.input_data.addLayout(self.mol_mass_input)
        self.mass_or_volume_input = QtWidgets.QVBoxLayout()
        self.mass_or_volume_input.setObjectName("mass_or_volume_input")
        self.mass_or_volume_choice = QtWidgets.QHBoxLayout()
        self.mass_or_volume_choice.setObjectName("mass_or_volume_choice")
        self.volume_choice = QtWidgets.QVBoxLayout()
        self.volume_choice.setObjectName("volume_choice")
        self.volume_checkbox = QtWidgets.QCheckBox(parent=self.groupBox)
        self.volume_checkbox.setObjectName("volume_checkbox")
        self.volume_choice.addWidget(self.volume_checkbox)
        self.volume_units_choice = QtWidgets.QHBoxLayout()
        self.volume_units_choice.setObjectName("volume_units_choice")
        self.percent_checkbox_2 = QtWidgets.QCheckBox(parent=self.groupBox)
        self.percent_checkbox_2.setObjectName("percent_checkbox_2")
        self.volume_units_choice.addWidget(self.percent_checkbox_2)
        self.ml_checkbox = QtWidgets.QCheckBox(parent=self.groupBox)
        self.ml_checkbox.setObjectName("ml_checkbox")
        self.volume_units_choice.addWidget(self.ml_checkbox)
        self.volume_choice.addLayout(self.volume_units_choice)
        self.mass_or_volume_choice.addLayout(self.volume_choice)
        self.mass_choice = QtWidgets.QVBoxLayout()
        self.mass_choice.setObjectName("mass_choice")
        self.mass_checkbox = QtWidgets.QCheckBox(parent=self.groupBox)
        self.mass_checkbox.setObjectName("mass_checkbox")
        self.mass_choice.addWidget(self.mass_checkbox)
        self.mass_units_choice = QtWidgets.QHBoxLayout()
        self.mass_units_choice.setObjectName("mass_units_choice")
        self.percent_checkbox = QtWidgets.QCheckBox(parent=self.groupBox)
        self.percent_checkbox.setObjectName("percent_checkbox")
        self.mass_units_choice.addWidget(self.percent_checkbox)
        self.g_checkbox = QtWidgets.QCheckBox(parent=self.groupBox)
        self.g_checkbox.setObjectName("g_checkbox")
        self.mass_units_choice.addWidget(self.g_checkbox)
        self.mass_choice.addLayout(self.mass_units_choice)
        self.mass_or_volume_choice.addLayout(self.mass_choice)
        self.mass_or_volume_input.addLayout(self.mass_or_volume_choice)
        self.mass_volume_comboBox = QtWidgets.QComboBox(parent=self.groupBox)
        self.mass_volume_comboBox.setObjectName("mass_volume_comboBox")
        self.mass_or_volume_input.addWidget(self.mass_volume_comboBox)
        self.input_data.addLayout(self.mass_or_volume_input)
        self.delete_button = QtWidgets.QPushButton(parent=self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.delete_button.setFont(font)
        self.delete_button.setObjectName("delete_button")
        self.input_data.addWidget(self.delete_button)
        self.verticalLayout_2.addLayout(self.input_data)
        self.horizontalLayout.addWidget(self.groupBox)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.groupBox.setTitle(_translate("Form", "GroupBox"))
        self.mol_mass_label.setText(_translate("Form", "Молярная масса газа (г./моль)"))
        self.volume_checkbox.setText(_translate("Form", "V - Объем"))
        self.percent_checkbox_2.setText(_translate("Form", "%"))
        self.ml_checkbox.setText(_translate("Form", "мл."))
        self.mass_checkbox.setText(_translate("Form", "m - Масса"))
        self.percent_checkbox.setText(_translate("Form", "%"))
        self.g_checkbox.setText(_translate("Form", "гр."))
        self.delete_button.setText(_translate("Form", "Удалить"))
