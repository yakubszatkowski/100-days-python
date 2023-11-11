from PySide6.QtWidgets import QMainWindow, QFileDialog, QLabel
from PySide6.QtGui import QPixmap, QFont
from PySide6.QtCore import Qt, QTimer
from ui_mainwindow import Ui_MainWindow

class DraggableLabel(QLabel):
    def __int__(self):
        super().__init__()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.start_position = event.pos()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            self.move(self.mapToParent(event.pos() - self.start_position))

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('Watermarker')
        self.setAcceptDrops(True)
        self.actionLoad.triggered.connect(self.load_image)
        self.graphic_window.setMaximumSize(1000, 1000)
        self.watermark = DraggableLabel('Enter watermark text', self.graphic_window)
        self.watermark.setFont(QFont('Calibri', 20))
        self.watermark_input_text.textChanged.connect(self.watermark_text_change)
        self.spin_box.valueChanged.connect(self.watermark_text_change)

    def watermark_text_change(self):
        if self.watermark_input_text.text() == '':
            self.watermark.setText('Enter watermark text')
        else:
            self.watermark.setText(self.watermark_input_text.text())
        self.watermark.setFont(QFont('Calibri', self.spin_box.value()))
        self.watermark.adjustSize()

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
        if final_image.height() > 1000 or final_image.width() > 1000:
            image = final_image.scaled(1000, 1000, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        else:
            image = final_image
        self.graphic_window.setPixmap(image)
        QTimer.singleShot(0, self.adjustSize)

    def set_image(self, file_path):
        image = QPixmap(file_path)
        self.sizing_n_upload(image)

    def load_image(self):
        file_path = QFileDialog.getOpenFileName(self, 'Open File', '', 'Image Files (*.png *.jpg *.jpeg)')
        image = QPixmap(file_path[0])
        self.sizing_n_upload(image)


#TODO
# make input label draggable only across the qpixmap
# rotating the input label
# saving the picture with label on your system
# exporting .exe
