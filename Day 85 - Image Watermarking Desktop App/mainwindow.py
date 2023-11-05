from PySide6.QtWidgets import QMainWindow
from ui_mainwindow import Ui_MainWindow
from PySide6.QtGui import QFont, QFontDatabase

class MainWindow(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle('Watermarker')
        self.setupUi(self)

        # # Editing label fonts
        # font_id = QFontDatabase.addApplicationFont('Roboto-Medium.ttf')
        # families = QFontDatabase.applicationFontFamilies(font_id)
        # font = QFont(families[0])
        # self.title_label.setFont(font)
        # self.font_size_label.setFont(font)
        # self.watermark_input_text.setFont(font)
        # self.spin_box.setFont(font)
        # self.save_button.setFont(font)

