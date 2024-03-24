from PySide6.QtWidgets import QApplication
from mainwindow import MainWidget
import sys

app = QApplication(sys.argv)
window = MainWidget()

if __name__ == '__main__':
    window.show()
    app.exec()

# pyside6-uic directory_widget.ui > directory_widget.py
# pyside6-uic progressbar_widget.ui > progressbar_widget.py
# pyside6-rcc resources.qrc -o resource_rc.py

# pyinstaller --windowed --icon=mic.png --runtime-tmpdir=path\to\python\tmp main.py
# pyinstaller --onefile file_name.py

# icon source: https://www.flaticon.com/free-icon/mic_2882877?term=microphone&page=1&position=4&origin=search&related_id=2882877

#TODO
    # Delete the file that is left after interrupted conversion to .mp3
    # Try hover option on QComboBox item with QApplication.processEvents()
