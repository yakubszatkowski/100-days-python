from PySide6.QtWidgets import QMainWindow, QFileDialog, QLabel, QWidget, QVBoxLayout
from PySide6.QtGui import QPixmap, QFont, QCursor
from PySide6.QtCore import Qt, QTimer
from ui_mainwindow import Ui_MainWindow


class RotationLabel(QLabel):
    def __init__(self, input_parent):
        super().__init__()
        self.watermark_label = input_parent
        self.setParent(self.watermark_label)
        self.setText('⟳')
        self.setStyleSheet(f'''color: rgba(255, 255, 255, 100)''') # border: 4px dashed #aaa
        self.move(self.watermark_label.geometry().width()-10, -5)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.start_position = event.pos()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            self.setStyleSheet('''color: red;''')

class DraggableLabel(QLabel):
    def __init__(self, text, parent, widget):
        super().__init__()
        self.setText(text)
        self.setParent(parent)
        self.map = parent
        self.setFont(QFont('Calibri', 20))
        self.setStyleSheet('''color: rgba(255, 255, 255, 100)''')
        self.body = widget

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.start_position = event.pos()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            self.setStyleSheet('''color: rgba(255, 255, 255, 40);''')
            new_position = self.map.mapFromGlobal(event.globalPos() - self.start_position)
            map_area = self.map.rect()
            watermark_area = self.geometry()
            if map_area.contains(watermark_area.translated(new_position)):
                self.body.move(new_position)
            else:
                self.setStyleSheet('''color: rgba(255, 0, 0, 40);''')

    def mouseReleaseEvent(self, event):
        if not event.buttons() == Qt.LeftButton:
            self.setStyleSheet('''color: rgba(255, 255, 255, 100)''')


class LabelWithRotator(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.setParent(parent)
        self.watermark_text = DraggableLabel('Enter watermark text', parent, self)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.watermark_text)
        self.setLayout(self.layout)


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('Watermarker')
        self.setAcceptDrops(True)
        self.actionLoad.triggered.connect(self.load_image)
        self.graphic_window.setMaximumSize(1000, 1000)

        self.watermark = LabelWithRotator(self.graphic_window)

        self.watermark_input_text.textChanged.connect(self.watermark_text_change)
        self.spin_box.valueChanged.connect(self.watermark_text_change)

    def watermark_text_change(self):
        if self.watermark_input_text.text() == '':
            self.watermark.watermark_text.setText('Enter watermark text')
        else:
            self.watermark.watermark_text.setText(self.watermark_input_text.text())
        self.watermark.watermark_text.setFont(QFont('Calibri', self.spin_box.value()))
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

    def sizing_n_upload(self, image):
        if image.height() > 1000 or image.width() > 1000:
            image = image.scaled(1000, 1000, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        else:
            pass
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
        self.watermark.watermark_text.setText('Enter watermark text')
        self.watermark.watermark_text.setFont(QFont('Calibri', 20))
        self.watermark.setGeometry(60, 120, 250, 52)
        self.watermark_input_text.setText('')
        self.spin_box.setValue(20)

#TODO
# make rotator size dynamic with label size, figure out where to put it (middle top or right top)
# rotating the input label
# cursor changing to grab/rotate icon
# saving the picture with label
# exporting .exe of the whole program
