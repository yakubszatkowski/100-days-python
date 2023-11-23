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
        self.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsMovable | QGraphicsItem.ItemSendsScenePositionChanges)

    def itemChange(self, change, value):
        if change == QGraphicsItem.ItemPositionChange:
            self.rotator_geo = self.boundingRect()
            self.scene_geo = self.scene().sceneRect()
            w = self.rotator_geo.width()
            h = self.rotator_geo.height()
            top_left = value - QPointF(20,0)
            bottom_right = value + QPointF(w, h)
            if not self.scene_geo.contains(top_left) or not self.scene_geo.contains(bottom_right):
                y = value.y()
                x = value.x()
                if y < self.scene_geo.top():
                    y = self.scene_geo.top()
                if y > self.scene_geo.bottom() - h:
                    y = self.scene_geo.bottom() - h
                if x < self.scene_geo.left():
                    x = self.scene_geo.left()
                if x > self.scene_geo.right() - w:
                    x = self.scene_geo.right() - w
                value.setX(x)
                value.setY(y)
                self.position_change.emit(value)
                return value
            self.position_change.emit(value)
        return super().itemChange(change, value)

class DraggableLabel(QGraphicsTextItem):
    def __init__(self):
        super().__init__()
        self.setPlainText('Enter watermark text')
        self.setFont(QFont('Calibri', 20))
        self.setOpacity(0.5)
        self.setDefaultTextColor(QColor(QColorConstants.White))
        self.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsMovable | QGraphicsItem.ItemSendsScenePositionChanges)

    def itemChange(self, change, value):
        if change == QGraphicsItem.ItemPositionChange:
            self.label_geo = self.boundingRect()
            self.scene_geo = self.scene().sceneRect()
            w = self.label_geo.width()
            h = self.label_geo.height()
            top_left = value - QPointF(20, 0)
            bottom_right = value + QPointF(w, h)
            if not self.scene_geo.contains(top_left) or not self.scene_geo.contains(bottom_right):
                y = value.y()
                x = value.x()
                if y < self.scene_geo.top():
                    y = self.scene_geo.top()
                if y > self.scene_geo.bottom() - h:
                    y = self.scene_geo.bottom() - h
                if x < self.scene_geo.left():
                    x = self.scene_geo.left()
                if x > self.scene_geo.right() - w:
                    x = self.scene_geo.right() - w
                value.setX(x)
                value.setY(y)
                return value
        return super().itemChange(change, value)

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
        self.rotator.position_change.connect(self.rotate_watermark)

        # self.watermark.textChanged.connect(self.watermark_text_change)
        self.spin_box.valueChanged.connect(self.watermark_text_change)
        self.watermark_input_text.textChanged.connect(self.watermark_text_change)


    def watermark_text_change(self):
        if self.watermark_input_text.text() == '':
            self.watermark.setPlainText('Enter watermark text')
            print(self.watermark.toPlainText())
        else:
            self.watermark.setPlainText(self.watermark_input_text.text())
        self.watermark.setFont(QFont('Calibri', self.spin_box.value()))
        self.watermark.adjustSize()
        self.watermark.setTransformOriginPoint(self.watermark.boundingRect().center())

    def rotate_watermark(self, position):
        item_position = self.watermark.transformOriginPoint()
        angle = math.atan2(item_position.y() - position.y(), item_position.x() - position.x()) / math.pi * 180 + 31
        self.watermark.setRotation(angle)
        self.rotator.setRotation(-angle)

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
        self.rotator.setTransformOriginPoint(self.rotator.boundingRect().center())
        self.scene.addItem(self.watermark)
        self.scene.addItem(self.rotator)
        if image:
            self.watermark.setPos((image.width() - self.watermark.boundingRect().width()) / 2,
                                  (image.height() - self.watermark.boundingRect().height()) / 2)
        else:
            self.watermark.setPos((350 - self.watermark.boundingRect().width()) / 2,
                                  (304 - self.watermark.boundingRect().height()) / 2)



#TODO
# save pic
# help from actionbar
# get .exe
