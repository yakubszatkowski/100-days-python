from PySide6.QtWidgets import QApplication
from mainwindow import MainWindow
import sys

app = QApplication(sys.argv)
window = MainWindow()
window.show()

if __name__ == '__main__':
    app.exec()

# pyside6-uic mainwindow.ui > ui_mainwindow.py
# pyside6-rcc resource.qrc -o resource_rc.py