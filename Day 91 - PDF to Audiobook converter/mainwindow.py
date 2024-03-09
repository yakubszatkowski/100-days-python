from PySide6.QtWidgets import QWidget
from PySide6.QtCore import QEvent, QVariantAnimation, QAbstractAnimation
from PySide6.QtGui import QColor
from directory_widget import Ui_MainWidget
import functools

def helper_function(widget, color):
    widget.setStyleSheet("background-color: {}".format(color.name()))


class MainWidget(QWidget, Ui_MainWidget):
    def __init__(self):
        super(MainWidget, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('PDF2Sound by yakubszatkowski')

        self.directory_file_button.installEventFilter(self)
        self.convert_button.installEventFilter(self)

    def eventFilter(self, obj, ev):  # button hover
        if ev.type() == QEvent.Enter and obj.isEnabled():
            self.hover_animation(obj, QColor(198, 198, 198), QColor(255, 255, 255))
        elif ev.type() == QEvent.Leave and obj.isEnabled():
            self.hover_animation(obj, QColor(255, 255, 255), QColor(198, 198, 198))

    def hover_animation(self, obj, start_color, target_color):
        anim = QVariantAnimation(
            obj,
            duration=300,
            startValue=start_color,
            endValue=target_color
        )
        anim.valueChanged.connect(functools.partial(helper_function, obj))
        anim.start(QAbstractAnimation.DeleteWhenStopped)
