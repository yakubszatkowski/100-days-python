from PySide6.QtWidgets import QMainWindow, QFileDialog, QLabel, QWidget, QGridLayout, QApplication, QGraphicsScene, QGraphicsProxyWidget
from PySide6.QtGui import QFont, QPixmap
from PySide6.QtCore import Qt, QPoint, Signal
from ui_mainwindow import Ui_MainWindow


class RotationLabel(QLabel):
    rotation_change = Signal(int)

    def __init__(self, parent, widget):
        super().__init__()
        self.watermark_label = widget
        self.map = parent
        self.setText('⟳')
        self.setStyleSheet(f'''color: rgba(255, 255, 255, 100)''') #
        self.setFont(QFont('Calibri', 12))
        self.setMaximumSize(20,20)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.start_position = event.pos()

    def mouseMoveEvent(self, event):  # Shorter text
        if event.buttons() == Qt.LeftButton:
            self.setStyleSheet('''color: white;''')
            QApplication.setOverrideCursor(Qt.SizeVerCursor)
            rotation_position = self.map.mapFromGlobal(event.globalPos() - self.start_position - QPoint(0, 100))
            rotation_angle = rotation_position.y()/5
            self.rotation_change.emit(rotation_angle)

    def mouseReleaseEvent(self, event):
        self.setStyleSheet(f'''color: rgba(255, 255, 255, 100)''')
        QApplication.setOverrideCursor(Qt.ArrowCursor)


class DraggableLabel(QLabel):
    def __init__(self, text, parent, widget):
        super().__init__()
        self.setText(text)
        self.setParent(parent)
        self.map = parent
        self.setFont(QFont('Calibri', 20))
        self.setStyleSheet('''color: rgba(255, 255, 255, 100);''')
        self.body = widget

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.start_position = event.pos()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            QApplication.setOverrideCursor(Qt.ClosedHandCursor)
            self.setStyleSheet('''color: rgba(255, 255, 255, 40)''')
            new_position = self.map.mapFromGlobal(event.globalPos() - self.start_position)
            map_area = self.map.rect()
            watermark_area = self.geometry()
            if map_area.contains(watermark_area.translated(new_position)):
                self.body.move(new_position)
            else:
                self.setStyleSheet('''color: rgba(255, 0, 0, 40)''')

    def mouseReleaseEvent(self, event):
        if not event.buttons() == Qt.LeftButton:
            QApplication.setOverrideCursor(Qt.ArrowCursor)
            self.setStyleSheet('''color: rgba(255, 255, 255, 100)''')


class LabelWithRotator(QWidget):
    def __init__(self, parent):
        super().__init__()
        # self.setParent(parent)
        self.setStyleSheet("background:transparent;")
        self.watermark_text = DraggableLabel('Enter watermark text', parent, self)
        self.rotator = RotationLabel(parent, self)
        self.layout = QGridLayout()
        self.layout.addWidget(self.watermark_text, 0, 0)
        self.layout.addWidget(self.rotator, 0, 1, Qt.AlignTop)
        self.layout.setSpacing(0)
        self.setLayout(self.layout)


class CustomScene(QGraphicsScene):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent

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
            self.parent.set_image(file_path)
            event.accept()
        else:
            event.ignore()


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('Watermarker')
        self.setAcceptDrops(True)
        self.graphic_window.setAcceptDrops(True)

        self.watermark = LabelWithRotator(self.graphic_window)
        self.scene = CustomScene(self)
        self.graphic_window.setScene(self.scene)

        self.proxy = QGraphicsProxyWidget()
        self.proxy.setWidget(self.watermark)
        self.scene.addItem(self.proxy)
        self.proxy.setTransformOriginPoint(self.proxy.boundingRect().center())
        self.watermark.rotator.rotation_change.connect(self.update_rotation)

        self.actionLoad.triggered.connect(self.load_image)
        self.watermark_input_text.textChanged.connect(self.watermark_text_change)
        self.spin_box.valueChanged.connect(self.watermark_text_change)

    def update_rotation(self, rotation_angle):
        self.proxy.setRotation(rotation_angle)
        print(rotation_angle)

    def watermark_text_change(self):
        if self.watermark_input_text.text() == '':
            self.watermark.watermark_text.setText('Enter watermark text')
        else:
            self.watermark.watermark_text.setText(self.watermark_input_text.text())
        self.watermark.watermark_text.setFont(QFont('Calibri', self.spin_box.value()))
        self.watermark.adjustSize()

    def dragEnterEvent(self, event):
        self.scene.dragEnterEvent(event)

    def dragMoveEvent(self, event):
        self.scene.dragMoveEvent(event)

    def dropEvent(self, event):
        self.scene.dropEvent(event)

    def sizing_n_upload(self, image):
        if image.height() > 800 or image.width() > 800:
            image = image.scaled(800, 800, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        else:
            pass
        self.scene.clear()
        self.scene.addPixmap(image)

        self.graphic_window.setFixedSize(image.width(), image.height())
        self.scene.setSceneRect(0, 0, image.width(), image.height())
        self.setFixedSize(image.width() + 50, image.height() + 146)

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
        self.watermark.watermark_text.setAlignment(Qt.AlignCenter)
        self.watermark.move(0,0)
        self.watermark_input_text.setText('')
        self.spin_box.setValue(20)

#TODO
# address bug where scroll bar appears as the label moves
# saving the picture with label
# exporting .exe of the whole program
