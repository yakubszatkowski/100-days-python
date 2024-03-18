# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'progressbar_widget.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QProgressBar, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_progress_widget(object):
    def setupUi(self, progress_widget):
        if not progress_widget.objectName():
            progress_widget.setObjectName(u"progress_widget")
        progress_widget.resize(400, 80)
        progress_widget.setMaximumSize(QSize(16777215, 80))
        progress_widget.setStyleSheet(u"#progress_widget {\n"
"   background-color: rgb(20, 20, 20);\n"
"}\n"
"\n"
"QLabel {\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QProgressBar {\n"
"	background-color: rgb(198, 198, 198);\n"
"	color: rgb(0, 0, 0);\n"
"	text-align: center;\n"
"\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"     background-color: rgb(255, 255, 255);\n"
"}")
        self.verticalLayout = QVBoxLayout(progress_widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.progres_label = QLabel(progress_widget)
        self.progres_label.setObjectName(u"progres_label")
        font = QFont()
        font.setFamilies([u"Calibri Light"])
        font.setPointSize(16)
        self.progres_label.setFont(font)

        self.verticalLayout.addWidget(self.progres_label, 0, Qt.AlignHCenter)

        self.progress_bar = QProgressBar(progress_widget)
        self.progress_bar.setObjectName(u"progress_bar")
        self.progress_bar.setValue(24)

        self.verticalLayout.addWidget(self.progress_bar)


        self.retranslateUi(progress_widget)

        QMetaObject.connectSlotsByName(progress_widget)
    # setupUi

    def retranslateUi(self, progress_widget):
        progress_widget.setWindowTitle(QCoreApplication.translate("progress_widget", u"Form", None))
        self.progres_label.setText(QCoreApplication.translate("progress_widget", u"hello", None))
    # retranslateUi

