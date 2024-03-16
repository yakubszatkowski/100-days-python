from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from directory_widget import Ui_MainWidget
from convert_to_audio import read_pdf, convert_to_audio
import functools, pyttsx3


def helper_function(widget, color):
    widget.setStyleSheet("background-color: {}".format(color.name()))


class ComboBoxDelegate(QStyledItemDelegate):
    def paint(self, painter, option, index):
        if option.state & QStyle.State_MouseOver:   # if hover
            background_color = QColor(255, 255, 255)  
        else:                                       # leaving hover
            background_color = QColor(198, 198, 198)  
        painter.fillRect(option.rect, background_color)
        painter.drawText(option.rect, index.data())


class MainWidget(QWidget, Ui_MainWidget):
    def __init__(self):
        super(MainWidget, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('PDF2Sound by yakubszatkowski')

        self.directory_file_button.installEventFilter(self)
        self.directory_file_button.clicked.connect(self.load_pdf)
        self.convert_button.installEventFilter(self)
        self.convert_button.clicked.connect(self.convert_pdf)
        self.language_combo_box.installEventFilter(self)
        delegate = ComboBoxDelegate(self.language_combo_box)
        self.language_combo_box.setItemDelegate(delegate)

        self.engine = pyttsx3.init()
        self.voices = self.engine.getProperty('voices')
        for voice in self.voices:
            language = voice.name.split('- ')[1]
            if '(' in language:
                language = language.split('(')[0]
            self.language_combo_box.addItem(language)
        self.engine.runAndWait()


    def eventFilter(self, obj, ev):  # QObject hover
        if ev.type() == QEvent.Enter and obj.isEnabled(): # when hovering
            self.qobj_hover_animation(obj, QColor(198, 198, 198), QColor(255, 255, 255))
        elif ev.type() == QEvent.Leave and obj.isEnabled(): # when leaving hovering
            self.qobj_hover_animation(obj, QColor(255, 255, 255), QColor(198, 198, 198))
        return super().eventFilter(obj, ev)


    def qobj_hover_animation(self, obj, start_color, target_color):
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
        if file_path:
            self.book_title = file_path.split('/')[-1].split('.')[0]
            self.file_name.setText(self.book_title)
            self.pdf_to_convert = file_path
            self.convert_button.setEnabled(True)
            self.language_combo_box.setEnabled(True)


    def convert_pdf(self):
        pdf_contents = read_pdf(self.pdf_to_convert)
        convert_to_audio(pdf_contents, self.book_title)
