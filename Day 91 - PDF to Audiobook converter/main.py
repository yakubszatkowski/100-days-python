from PySide6.QtWidgets import QApplication
from mainwindow import MainWidget
import sys

app = QApplication(sys.argv)
window = MainWidget()

if __name__ == '__main__':
    window.show()
    app.exec()

# pyside6-uic directory_widget.ui > directory_widget.py
    
#TODO
    # create gui that will be able to select .pdf files via directory 
        # learn animation https://www.youtube.com/watch?v=75PG0sloTc8
    # convert pdf text to text variable in python
    # convert text to audio and save it as .mp3
