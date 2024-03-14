from PySide6.QtWidgets import QApplication
from mainwindow import MainWidget
import sys

app = QApplication(sys.argv)
window = MainWidget()

if __name__ == '__main__':
    window.show()
    app.exec()

# pyside6-uic directory_widget.ui > directory_widget.py
# pyside6-rcc resources.qrc -o resource_rc.py

#TODO
    # language choice computer's from registry 
        # - implement animation for QComboBox items - QStandardItem
    # save directory
    # loading screen when converting
    # highlight convert button when enabled (after choosing file)
