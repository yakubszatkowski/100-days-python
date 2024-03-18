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

#TODO
    # loading screen when converting - progress bar attached to both red_pdf and convert_to_audio
    # highlight convert button when enabled (after choosing file)
