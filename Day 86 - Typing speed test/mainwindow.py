from PySide6.QtWidgets import QMainWindow, QWidget, QStackedLayout
from PySide6.QtCore import Qt, QTimer
from ui_menuwidget import Ui_menu_widget
from ui_testwidget import Ui_test_widget
from random import choice
from jokes_list import it_jokes


class MenuWidget(QWidget, Ui_menu_widget):
    def __init__(self, parent):
        super().__init__()
        self.setupUi(self)
        self.main_window = parent
        self.setAttribute(Qt.WA_StyledBackground, True)

        self.start_button.clicked.connect(self.switch_to_test)
        self.start_button.setShortcut('Return')

    def switch_to_test(self):
        self.main_window.switch_window(1)

class TestWidget(QWidget, Ui_test_widget):
    def __init__(self, parent):
        super().__init__()
        self.setupUi(self)
        self.main_window = parent
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.countdown)

        self.return_button.clicked.connect(self.switch_to_menu)
        self.again_button.clicked.connect(self.choose_text)

    def switch_to_menu(self):
        self.main_window.switch_window(0)

    def choose_text(self):
        random_text = choice(it_jokes)
        self.text_label.setText(random_text)
        self.textinput_textedit.setEnabled(False)

        self.countdown_timer = 5
        self.countdown_label.setNum(self.countdown_timer)
        self.timer.start(1000)
        self.countdown()

    def countdown(self):
        if self.countdown_timer > 0:
            self.countdown_label.setNum(self.countdown_timer)
            self.countdown_timer -= 1
        else:
            self.countdown_label.setText('Start!')
            self.textinput_textedit.setEnabled(True)

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

        self.stacked_layout.currentChanged.connect(self.switch_to_test)

    def switch_window(self, index):
        self.stacked_layout.setCurrentIndex(index)

    def switch_to_test(self, index):
        if index == 1:
            self.test.choose_text()


#TODO
# dynamically highlight letters in text_label that match the letters from input_textedit
# start the timer in results_label in s:ms format
# when every letter is highlighted stop the timer, disable the input_textedit, in results show time, words written, words per minute
