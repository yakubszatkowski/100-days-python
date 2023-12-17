from PySide6.QtWidgets import QMainWindow, QWidget, QStackedLayout
from PySide6.QtCore import Qt, QTimer, QTime
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
        self.main_window.player_name = self.nameinput_lineedit.text()
        self.main_window.switch_window(1)

class TestWidget(QWidget, Ui_test_widget):
    def __init__(self, parent):
        super().__init__()
        self.setupUi(self)
        self.main_window = parent
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.timer_countdown = QTimer(self)
        self.timer_countdown.setInterval(1000)
        self.timer_countdown.timeout.connect(self.countdown)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_timer)

        self.textinput_textedit.textChanged.connect(self.text_changed)

        self.return_button.clicked.connect(self.switch_to_menu)
        self.again_button.clicked.connect(self.choose_text)

    def switch_to_menu(self):
        self.main_window.switch_window(0)

    def choose_text(self, player_name):
        self.timer.stop()
        self.random_text = choice(it_jokes)
        self.word_count = len(self.random_text.split(' '))
        self.results_label.clear()
        self.textinput_textedit.clear()
        self.player_name = player_name

        self.text_label.setText(self.random_text)
        self.textinput_textedit.setEnabled(False)
        self.time = QTime(0, 0)

        self.countdown_timer = 5
        self.countdown_label.setNum(self.countdown_timer)
        self.timer_countdown.start()
        self.countdown()

    def countdown(self):
        if self.countdown_timer > 0:
            self.countdown_label.setNum(self.countdown_timer)
            self.countdown_timer -= 1
        else:
            self.timer_countdown.stop()
            self.textinput_textedit.setEnabled(True)
            self.textinput_textedit.setFocus()
            self.timer.start(10)

    def update_timer(self):
        self.time = self.time.addMSecs(10)
        self.display_time = self.time.toString('mm:ss:zzz')[:-1]
        self.countdown_label.setText(self.display_time)

    def text_changed(self):
        self.current_input = self.textinput_textedit.toPlainText()
        input_length = len(self.current_input)
        text = self.random_text

        colored_text = ''
        for index, character in enumerate(text):
            if index < input_length:
                colored_text += (f'<span style="background-color: {'green' if character == self.current_input[index] 
                else 'red'} ">{character}</span>')
            else:
                colored_text += character

        word_list = colored_text.split()
        count_correct_letters = word_list.count('green')
        self.text_label.setText(colored_text)

        if len(text) == count_correct_letters:
            self.finish_test()

    def finish_test(self):
        self.timer.stop()
        display_time_split = [int(num) for num in self.display_time.split(':')]
        minute_decimal = round((display_time_split[0] + display_time_split[1]/60 + display_time_split[2]/60/100), 2)
        words_per_minute = round((self.word_count / minute_decimal), 2)
        self.results_label.setText(f'You wrote {self.word_count} words in {self.display_time} which is '
                                   f'{words_per_minute} WPM! Good job {self.player_name}!\nPress "again" button when '
                                   f'you are ready to try again!')
        self.textinput_textedit.setEnabled(False)


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle('Speed typing test')
        self.setFixedSize(500,560)

        self.stacked_layout = QStackedLayout()
        self.player_name = None
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
            self.test.choose_text(self.player_name)

#TODO Possible improvements:
# improve graphic interface
# local/online highscores
