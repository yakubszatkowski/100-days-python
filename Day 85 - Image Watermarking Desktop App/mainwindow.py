from PySide6.QtWidgets import (QMainWindow, QFileDialog, QLabel, QWidget, QGridLayout, QApplication, QGraphicsScene,
                               QGraphicsProxyWidget, QGraphicsTextItem)
from PySide6.QtGui import QFont, QPixmap, QColor, QColorConstants
from PySide6.QtCore import Qt, Signal, QPoint, QObject
from ui_mainwindow import Ui_MainWindow

class RotationLabel(QLabel):
    position_change = Signal(int)
    def __init__(self, parent):
        super().__init__()
        # self.setParent(parent)
        self.setText('⟳')
        self.setStyleSheet(f'''color: rgba(255, 255, 255, 100)''') #
        self.setFont(QFont('Calibri', 12))
        self.setMaximumSize(20,20)

class DraggableLabel(QGraphicsTextItem):
    def __init__(self):
        super().__init__()
        self.setPlainText('Example text')
        self.setFont(QFont('Calibri', 20))
        self.setOpacity(0.5)
        self.setDefaultTextColor(QColor(QColorConstants.White))
        # self.rotator = RotationLabel()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.start_position = event.pos()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            QApplication.setOverrideCursor(Qt.ClosedHandCursor)
            self.setOpacity(0.25)
            delta = event.pos() - self.start_position
            new_position = self.pos() + delta

            self.setPos(new_position)

    def mouseReleaseEvent(self, event):
        if not event.buttons() == Qt.LeftButton:
            QApplication.setOverrideCursor(Qt.ArrowCursor)
            self.setOpacity(0.5)

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

        self.scene = CustomScene(self)
        self.graphic_window.setScene(self.scene)
        self.graphic_window.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.graphic_window.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

        self.set_watermark()

        self.actionLoad.triggered.connect(self.load_image)


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

        self.set_watermark()

    def set_image(self, file_path):
        image = QPixmap(file_path)
        self.sizing_n_upload(image)

    def load_image(self):
        file_path = QFileDialog.getOpenFileName(self, 'Open File', '', 'Image Files (*.png *.jpg *.jpeg)')
        image = QPixmap(file_path[0])
        self.sizing_n_upload(image)

    def set_watermark(self):
        self.watermark = DraggableLabel()
        # self.rotator = RotationLabel(self.scene)
        self.scene.addItem(self.watermark)


#TODO
# put watermark text - that stays whenever there is image or not - done
# make watermark text movable with mouse movement (drag) - done
# make watermark text possible to rotate with mouse movement (drag rotator object)
# save the image with the watermark text
