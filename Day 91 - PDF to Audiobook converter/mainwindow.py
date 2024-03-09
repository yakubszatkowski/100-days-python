from PySide6.QtWidgets import QWidget, QFileDialog
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
        self.pdf_to_convert = None

        self.directory_file_button.installEventFilter(self)
        self.directory_file_button.clicked.connect(self.load_pdf)
        self.convert_button.installEventFilter(self)
        self.convert_button.clicked.connect(self.convert_pdf)
        

    def eventFilter(self, obj, ev):  # button hover
        if ev.type() == QEvent.Enter and obj.isEnabled(): # when hover
            self.hover_animation(obj, QColor(198, 198, 198), QColor(255, 255, 255))
        elif ev.type() == QEvent.Leave and obj.isEnabled(): # when leaving hover
            self.hover_animation(obj, QColor(255, 255, 255), QColor(198, 198, 198))
        return super().eventFilter(obj, ev)

    def hover_animation(self, obj, start_color, target_color):
        anim = QVariantAnimation(
            obj,
            duration=300,
            startValue=start_color,
            endValue=target_color
        )
        anim.valueChanged.connect(functools.partial(helper_function, obj))
        anim.start(QAbstractAnimation.DeleteWhenStopped)

    def load_pdf(self):
        file_path = QFileDialog.getOpenFileName(self, 'Open File', '', 'PDF Files (*.pdf)')[0]
        file_name = file_path.split('/')[-1]
        self.file_name.setText(file_name)
        self.pdf_to_convert = file_path
        self.convert_button.setEnabled(True)

    def convert_pdf(self):
        print('convert function here')
