# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'directory_widget.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_MainWidget(object):
    def setupUi(self, MainWidget):
        if not MainWidget.objectName():
            MainWidget.setObjectName(u"MainWidget")
        MainWidget.resize(300, 300)
        MainWidget.setMinimumSize(QSize(300, 300))
        MainWidget.setMaximumSize(QSize(300, 300))
        MainWidget.setStyleSheet(u"# background-color: rgb(20, 20, 20);\n"
"\n"
"QPushButton {\n"
"	width: 20px;\n"
"}\n"
"\n"
"\n"
"")
        self.widget = QWidget(MainWidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(34, 10, 231, 281))
        self.main_layout = QVBoxLayout(self.widget)
        self.main_layout.setObjectName(u"main_layout")
        self.main_layout.setContentsMargins(0, 20, 0, 20)
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")

        self.main_layout.addWidget(self.label, 0, Qt.AlignHCenter)

        self.title_label = QLabel(self.widget)
        self.title_label.setObjectName(u"title_label")

        self.main_layout.addWidget(self.title_label, 0, Qt.AlignHCenter)

        self.directory_file_button = QPushButton(self.widget)
        self.directory_file_button.setObjectName(u"directory_file_button")
        self.directory_file_button.setMinimumSize(QSize(120, 0))
        self.directory_file_button.setMaximumSize(QSize(150, 16777215))

        self.main_layout.addWidget(self.directory_file_button, 0, Qt.AlignHCenter)

        self.file_name = QLabel(self.widget)
        self.file_name.setObjectName(u"file_name")

        self.main_layout.addWidget(self.file_name, 0, Qt.AlignHCenter)

        self.convert_button = QPushButton(self.widget)
        self.convert_button.setObjectName(u"convert_button")
        self.convert_button.setMinimumSize(QSize(120, 0))
        self.convert_button.setMaximumSize(QSize(150, 16777215))

        self.main_layout.addWidget(self.convert_button, 0, Qt.AlignHCenter)

        self.main_layout.setStretch(0, 1)
        self.main_layout.setStretch(1, 3)
        self.main_layout.setStretch(2, 1)
        self.main_layout.setStretch(4, 1)

        self.retranslateUi(MainWidget)

        QMetaObject.connectSlotsByName(MainWidget)
    # setupUi

    def retranslateUi(self, MainWidget):
        MainWidget.setWindowTitle(QCoreApplication.translate("MainWidget", u"Form", None))
        self.label.setText(QCoreApplication.translate("MainWidget", u"PDF2Sound", None))
        self.title_label.setText(QCoreApplication.translate("MainWidget", u"<html><head/><body><p align=\"center\">PDF to Audiobook<br>converter</p></body></html>", None))
        self.directory_file_button.setText(QCoreApplication.translate("MainWidget", u"Choose pdf file", None))
        self.file_name.setText("")
        self.convert_button.setText(QCoreApplication.translate("MainWidget", u"Convert", None))
    # retranslateUi

