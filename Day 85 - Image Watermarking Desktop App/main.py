from PySide6.QtWidgets import QApplication
from mainwindow import MainWindow
import sys

app = QApplication(sys.argv)
window = MainWindow()
window.show()

if __name__ == '__main__':
    app.exec()
