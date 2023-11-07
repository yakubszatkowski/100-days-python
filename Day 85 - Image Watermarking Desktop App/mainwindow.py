from PySide6.QtWidgets import QMainWindow
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt
from ui_mainwindow import Ui_MainWindow

class MainWindow(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('Watermarker')
        self.setAcceptDrops(True)

    def dragEnterEvent(self, event):
        if event.mimeData().hasImage:
            event.accept()
        else:
            event.ignore()

    def dragMoveEvent(self, event):
        if event.mimeData().hasImage:
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        if event.mimeData().hasImage:
            event.setDropAction(Qt.CopyAction)
            file_path = event.mimeData().urls()[0].toLocalFile()
            self.set_image(file_path)
            event.accept()
        else:
            event.ignore()

    def set_image(self, file_path):
        final_image = QPixmap(file_path)
        image_w, image_h = (final_image.width(), final_image.height())
        print(image_w)
        print(image_h)
        self.graphic_window.setPixmap(final_image)
        self.graphic_window.setFixedSize(image_w, image_h)
        self.adjustSize()  # the gui window dont get adjusted


#TODO
# drag and drop picture - gui window adjustments
# loading the picture from toolbar
# placing input label on the picture
# draging placement of the input label around the frame
# rotating the input label
# saving the picture with label on your system
# exporting .exe
