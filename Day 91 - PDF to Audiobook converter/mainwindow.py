from PySide6.QtWidgets import QWidget
from directory_widget import Ui_MainWidget


class MainWidget(QWidget, Ui_MainWidget):
    def __init__(self):
        super(MainWidget, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('PDF to Audiobook converter')
