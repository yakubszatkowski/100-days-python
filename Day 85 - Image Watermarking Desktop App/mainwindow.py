from PySide6.QtWidgets import QMainWindow, QFileDialog, QLabel
from PySide6.QtGui import QPixmap, QFont
from PySide6.QtCore import Qt, QTimer
from ui_mainwindow import Ui_MainWindow


class DraggableLabel(QLabel):
    def __init__(self, text, parent):
        super().__init__()
        self.setText(text)
        self.setParent(parent)
        self.map = parent
        self.setFont(QFont('Calibri', 20))
        self.setStyleSheet('''color: rgba(255, 255, 255, 80)''')
        self.setGeometry(60, 120, 232, 33)

    def mousePressEvent(self, event):
        print(self.geometry())
        if event.button() == Qt.LeftButton:
            self.start_position = event.pos()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            self.setStyleSheet('''color: rgba(255, 255, 255, 40);''')
            new_position = self.mapToParent(event.pos() - self.start_position)
            map_area = self.map.rect()
            watermark_area = self.geometry()
            if map_area.contains(watermark_area.translated(new_position-self.pos())):
                self.move(new_position)
            else:
                self.setStyleSheet('''color: rgba(255, 0, 0, 40);''')

    def mouseReleaseEvent(self, event):
        if not event.buttons() == Qt.LeftButton:
            self.setStyleSheet('''color: rgba(255, 255, 255, 80)''')


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('Watermarker')
        self.setAcceptDrops(True)
        self.actionLoad.triggered.connect(self.load_image)
        self.graphic_window.setMaximumSize(1000, 1000)
        self.watermark = DraggableLabel('Enter watermark text', self.graphic_window)
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

    def mouseDoubleClickEvent(self, event):
        self.watermark.setText('Enter watermark text')
        self.watermark.setFont(QFont('Calibri', 20))
        self.watermark.setGeometry(60, 120, 232, 33)

#TODO
# rotating the input label
# saving the picture with label
# exporting .exe of the whole program
