from PySide6.QtWidgets import QWidget
from PySide6.QtCore import QEvent, QPropertyAnimation
from PySide6.QtGui import QColor
from directory_widget import Ui_MainWidget


class MainWidget(QWidget, Ui_MainWidget):
    def __init__(self):
        super(MainWidget, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('PDF2Sound by yakubszatkowski')

        self.directory_file_button.installEventFilter(self)
        self.convert_button.installEventFilter(self)

    def eventFilter(self, obj, ev):  # button hover
        if ev.type() == QEvent.Enter and obj.isEnabled():
            print("you've just hovered over button")
        elif ev.type() == QEvent.Leave and obj.isEnabled():
            print("you've left")

    def hover_animation(self, obj):
        pass
