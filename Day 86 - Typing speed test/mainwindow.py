from PySide6.QtWidgets import QMainWindow, QWidget, QStackedLayout
from PySide6.QtCore import Qt
from ui_menuwidget import Ui_menu_widget
from ui_testwidget import Ui_test_widget

class MenuWidget(QWidget, Ui_menu_widget):
    def __init__(self, parent):
        super().__init__()
        self.setupUi(self)
        self.main_window = parent
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.start_button.clicked.connect(self.start_test)

    def start_test(self):
        self.main_window.switch_window(1)

class TestWidget(QWidget, Ui_test_widget):
    def __init__(self, parent):
        super().__init__()
        self.setupUi(self)
        self.main_window = parent
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.return_button.clicked.connect(self.return_to_menu)

    def return_to_menu(self):
        self.main_window.switch_window(0)

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle('Speed typing test')
        self.setFixedSize(500,560)

        self.stacked_layout = QStackedLayout()
        self.start_menu = MenuWidget(self)
        self.test = TestWidget(self)
        self.stacked_layout.addWidget(self.start_menu)
        self.stacked_layout.addWidget(self.test)

        central_widget = QWidget()
        central_widget.setLayout(self.stacked_layout)
        self.setCentralWidget(central_widget)

    def switch_window(self, index):
        self.stacked_layout.setCurrentIndex(index)

#TODO
# create list of random texts
# pick random text and put it in text_label when entering test
# when entering test enable countdown mechanism - 5 seconds
# after countdown enable input_textedit, start the timer in results_label in s:ms format
# dynamically highlight letters in text_label that match the letters from input_textedit
# add functionality to again_button - it should restart
