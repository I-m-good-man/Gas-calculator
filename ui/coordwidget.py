from PyQt6.QtWidgets import QWidget
from ui.base_qt_ui.ui_coord_widget import Ui_Form


class CoordWidget(QWidget):
    def __init__(self, id_widget: int, parent=None):
        super(CoordWidget, self).__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.id_widget = id_widget
        # self.ui.groupBox.setTitle(str(id_widget))
        self.ui.delete_button.clicked.connect(self.press_del)

    def press_del(self):
        self.ui.groupBox.setParent(None)
        # self.delete.emit(self.id_widget)
