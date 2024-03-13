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
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_MainWidget(object):
    def setupUi(self, MainWidget):
        if not MainWidget.objectName():
            MainWidget.setObjectName(u"MainWidget")
        MainWidget.setEnabled(True)
        MainWidget.resize(300, 300)
        MainWidget.setMinimumSize(QSize(300, 300))
        MainWidget.setMaximumSize(QSize(300, 300))
        MainWidget.setStyleSheet(u"#MainWidget {\n"
"   background-color: rgb(20, 20, 20);\n"
"}\n"
"\n"
"QLabel {\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton {\n"
"	background-color: rgb(198,198,198);\n"
"	border: 1px solid transparent;\n"
"	margin: 2px;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"	background-color: rgb(158,158,158);\n"
"}\n"
"\n"
"QComboBox {\n"
"	background-color: rgb(198,198,198);\n"
"	margin: 5px;\n"
"	border: none;\n"
"	padding-left: 4px;\n"
"}\n"
"\n"
"QComboBox:disabled {\n"
"	background-color: rgb(158,158,158);\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    background-color: rgb(198,198,198);\n"
"	selection-background-color: red;\n"
"}\n"
"\n"
"\n"
"")
        self.layoutWidget = QWidget(MainWidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(34, 10, 231, 281))
        self.main_layout = QVBoxLayout(self.layoutWidget)
        self.main_layout.setObjectName(u"main_layout")
        self.main_layout.setContentsMargins(0, 20, 0, 20)
        self.title_label_2 = QLabel(self.layoutWidget)
        self.title_label_2.setObjectName(u"title_label_2")
        font = QFont()
        font.setFamilies([u"Onyx"])
        font.setPointSize(26)
        self.title_label_2.setFont(font)

        self.main_layout.addWidget(self.title_label_2, 0, Qt.AlignHCenter)

        self.title_label = QLabel(self.layoutWidget)
        self.title_label.setObjectName(u"title_label")
        font1 = QFont()
        font1.setFamilies([u"Calibri Light"])
        font1.setPointSize(12)
        self.title_label.setFont(font1)

        self.main_layout.addWidget(self.title_label, 0, Qt.AlignHCenter)

        self.file_name = QLabel(self.layoutWidget)
        self.file_name.setObjectName(u"file_name")
        font2 = QFont()
        font2.setFamilies([u"Calibri Light"])
        self.file_name.setFont(font2)

        self.main_layout.addWidget(self.file_name, 0, Qt.AlignHCenter)

        self.directory_file_button = QPushButton(self.layoutWidget)
        self.directory_file_button.setObjectName(u"directory_file_button")
        self.directory_file_button.setEnabled(True)
        self.directory_file_button.setMinimumSize(QSize(120, 0))
        self.directory_file_button.setMaximumSize(QSize(150, 16777215))
        self.directory_file_button.setFont(font2)

        self.main_layout.addWidget(self.directory_file_button, 0, Qt.AlignHCenter)

        self.convert_layout = QHBoxLayout()
        self.convert_layout.setObjectName(u"convert_layout")
        self.convert_button = QPushButton(self.layoutWidget)
        self.convert_button.setObjectName(u"convert_button")
        self.convert_button.setEnabled(False)
        self.convert_button.setMaximumSize(QSize(150, 16777215))
        self.convert_button.setFont(font2)

        self.convert_layout.addWidget(self.convert_button)

        self.language_combo_box = QComboBox(self.layoutWidget)
        self.language_combo_box.addItem("")
        self.language_combo_box.addItem("")
        self.language_combo_box.addItem("")
        self.language_combo_box.setObjectName(u"language_combo_box")
        self.language_combo_box.setEnabled(True)
        self.language_combo_box.setMaximumSize(QSize(150, 25))
        self.language_combo_box.setFont(font2)

        self.convert_layout.addWidget(self.language_combo_box)


        self.main_layout.addLayout(self.convert_layout)

        self.main_layout.setStretch(0, 2)
        self.main_layout.setStretch(1, 2)
        self.main_layout.setStretch(2, 1)
        self.main_layout.setStretch(3, 1)

        self.retranslateUi(MainWidget)

        QMetaObject.connectSlotsByName(MainWidget)
    # setupUi

    def retranslateUi(self, MainWidget):
        MainWidget.setWindowTitle(QCoreApplication.translate("MainWidget", u"Form", None))
        self.title_label_2.setText(QCoreApplication.translate("MainWidget", u"PDF2Sound", None))
        self.title_label.setText(QCoreApplication.translate("MainWidget", u"<html><head/><body><p align=\"center\">PDF to Audiobook converter</p></body></html>", None))
        self.file_name.setText("")
        self.directory_file_button.setText(QCoreApplication.translate("MainWidget", u"Select file", None))
        self.convert_button.setText(QCoreApplication.translate("MainWidget", u"Convert", None))
        self.language_combo_box.setItemText(0, QCoreApplication.translate("MainWidget", u"1", None))
        self.language_combo_box.setItemText(1, QCoreApplication.translate("MainWidget", u"2", None))
        self.language_combo_box.setItemText(2, QCoreApplication.translate("MainWidget", u"3", None))

    # retranslateUi

