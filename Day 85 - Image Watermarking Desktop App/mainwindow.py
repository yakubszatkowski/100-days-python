from PySide6.QtWidgets import QMainWindow, QLabel
from PySide6.QtGui import QPixmap
from ui_mainwindow import Ui_MainWindow

class MainWindow(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('Watermarker')
        self.setAcceptDrops(True)
        self.graphic_window.setPixmap(QPixmap('pics/cat2.jpeg'))

#TODO
# drag and drop
# animations/transitions
# resizing widgets when window gets resized