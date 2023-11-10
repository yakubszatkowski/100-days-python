from PySide6.QtWidgets import QMainWindow, QFileDialog
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt, QTimer
from ui_mainwindow import Ui_MainWindow

class MainWindow(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('Watermarker')
        self.setAcceptDrops(True)
        self.actionLoad.triggered.connect(self.load_image)
        self.graphic_window.setMaximumSize(1000,1000)

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

    def sizing_n_upload(self, final_image):
        image_w, image_h = (final_image.width(), final_image.height())
        self.graphic_window.setFixedSize(image_w, image_h)
        self.graphic_window.setPixmap(final_image)
        QTimer.singleShot(0, self.adjustSize)

    def set_image(self, file_path):
        image = QPixmap(file_path)
        self.sizing_n_upload(image)

    def load_image(self):
        file_path = QFileDialog.getOpenFileName(self, 'Open File', '', 'Image Files (*.png *.jpg *.jpeg)')
        image = QPixmap(file_path[0])
        self.sizing_n_upload(image)


#TODO
# what if image is too big?
# loading the picture from toolbar
# similar resizing? try different resizing?
# hover over QMenu options

# placing input label on the picture
# dragging placement of the input label around the frame
# rotating the input label
# saving the picture with label on your system
# exporting .exe
