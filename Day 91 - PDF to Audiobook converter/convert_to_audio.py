from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from progressbar_widget import Ui_progress_widget
from pydub import AudioSegment
import fitz, pyttsx3, math


class SplashScreen(QSplashScreen, Ui_progress_widget):
    def __init__(self):
        super(SplashScreen, self).__init__()
        self.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)

    def read_pdf(self, file_path):
        self.show()
        self.text = ''
        max_percent = 50
        self.progres_label.setText('Conversion pdf to text')
        with fitz.open(file_path) as doc:
            page_count = doc.page_count
            current_page = 0
            for page in doc:
                current_page += 1
                progress_percent = math.floor((current_page / page_count)*max_percent)
                self.text += chr(12) + page.get_text()
                self.progress_bar.setValue(progress_percent)
                # print(progress_percent)
                QApplication.processEvents()
        self.progres_label.setText('Conversion pdf to text completed')


    def convert_to_audio(self, language, save_file_path):
        save_path = f'{save_file_path}'

        text_length = len(self.text)
        print(text_length)

        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        choosen_voice = None
        for voice in voices:
            if language in voice.name:
                choosen_voice = voice
                # print(voice)
        
        engine.setProperty('voice', choosen_voice.id)
        engine.setProperty('rate', 150)
        engine.setProperty('volume', 1.0)

        engine.save_to_file(self.text, save_path)
        engine.runAndWait()
        self.text = ''
