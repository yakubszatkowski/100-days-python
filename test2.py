from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import Qt, Signal, QPoint

# class CustomLabel(QtWidgets.QLabel):
#     def __init__(self):
#         super().__init__()
#         self.setText("Stack Overflow")
#
#     def mousePressEvent(self, ev):
#         if ev.button() == Qt.LeftButton:
#             self.start_position = ev.pos()
#
#     def mouseMoveEvent(self, ev):
#         if ev.buttons() == Qt.LeftButton:
#             delta = ev.pos() - self.start_position
#             new_position = self.pos() + delta
#             self.move(new_position)


def main():
    import sys

    app = QtWidgets.QApplication(sys.argv)

    label = QtWidgets.QLabel("Stack Overflow", alignment=QtCore.Qt.AlignCenter)

    graphicsview = QtWidgets.QGraphicsView()
    scene = QtWidgets.QGraphicsScene()
    graphicsview.setScene(scene)

    proxy = QtWidgets.QGraphicsProxyWidget()
    proxy.setWidget(label)
    proxy.setTransformOriginPoint(proxy.boundingRect().center())
    scene.addItem(proxy)

    slider = QtWidgets.QSlider(minimum=0, maximum=359, orientation=QtCore.Qt.Horizontal)
    slider.valueChanged.connect(proxy.setRotation)
    # proxy.setRotation(50)

    label_text = QtWidgets.QLabel(
        "{}°".format(slider.value()), alignment=QtCore.Qt.AlignCenter
    )
    slider.valueChanged.connect(
        lambda value: label_text.setText("{}°".format(slider.value()))
    )

    slider.setValue(45)

    w = QtWidgets.QWidget()
    lay = QtWidgets.QVBoxLayout(w)
    lay.addWidget(graphicsview)
    lay.addWidget(slider)
    lay.addWidget(label_text)
    w.resize(640, 480)
    w.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()