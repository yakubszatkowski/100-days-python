from PySide6.QtWidgets import QMainWindow, QFileDialog, QGraphicsScene, QGraphicsTextItem, QGraphicsItem
from PySide6.QtGui import QFont, QPixmap, QColor, QColorConstants
from PySide6.QtCore import Qt, Signal, QPointF
from ui_mainwindow import Ui_MainWindow
import math

class RotationLabel(QGraphicsTextItem):
    position_change = Signal(QPointF)
    def __init__(self):
        super().__init__()
        self.setPlainText('⟳')
        self.setFont(QFont('Calibri', 20))
        self.setOpacity(0.5)
        self.setPos(10, 0)
        self.setDefaultTextColor(QColor(QColorConstants.White))
        self.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsMovable)


class DraggableLabel(QGraphicsTextItem):
    def __init__(self):
        super().__init__()
        self.setPlainText('Example text')
        self.setFont(QFont('Calibri', 20))
        self.setOpacity(0.5)
        self.setDefaultTextColor(QColor(QColorConstants.White))
        self.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsMovable)

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

        self.scene = CustomScene(self)
        self.graphic_window.setScene(self.scene)
        self.scene.setSceneRect(0, 0, 350, 304)
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
        self.set_watermark(image)

    def set_image(self, file_path):
        image = QPixmap(file_path)
        self.sizing_n_upload(image)

    def load_image(self):
        file_path = QFileDialog.getOpenFileName(self, 'Open File', '', 'Image Files (*.png *.jpg *.jpeg)')
        image = QPixmap(file_path[0])
        self.sizing_n_upload(image)

    def set_watermark(self, image=None):
        self.watermark = DraggableLabel()
        self.watermark.setTransformOriginPoint(self.watermark.boundingRect().center())
        self.rotator = RotationLabel()
        self.scene.addItem(self.watermark)
        self.scene.addItem(self.rotator)
        if image:
            self.watermark.setPos((image.width() - self.watermark.boundingRect().width()) / 2,
                                  (image.height() - self.watermark.boundingRect().height()) / 2)
        else:
            self.watermark.setPos((350 - self.watermark.boundingRect().width()) / 2,
                                  (304 - self.watermark.boundingRect().height()) / 2)

#TODO
# make watermark text possible to rotate with mouse movement
# save the image with the watermark text
