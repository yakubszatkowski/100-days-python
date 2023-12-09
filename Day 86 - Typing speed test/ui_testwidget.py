# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'testwidget.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QPlainTextEdit,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_test_widget(object):
    def setupUi(self, test_widget):
        if not test_widget.objectName():
            test_widget.setObjectName(u"test_widget")
        test_widget.setEnabled(True)
        test_widget.resize(500, 560)
        test_widget.setStyleSheet(u"#test_widget {\n"
"background-color:qradialgradient(spread:pad, cx:0.483682, cy:0.307, radius:0.5, fx:0.478, fy:0, stop:0 rgba(173, 185, 207, 255), stop:1 rgba(255, 255, 255, 255))\n"
"}")
        self.verticalLayout = QVBoxLayout(test_widget)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(15, 30, 15, 30)
        self.countdown_label = QLabel(test_widget)
        self.countdown_label.setObjectName(u"countdown_label")
        font = QFont()
        font.setPointSize(20)
        self.countdown_label.setFont(font)

        self.verticalLayout.addWidget(self.countdown_label, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.typingtext_label = QLabel(test_widget)
        self.typingtext_label.setObjectName(u"typingtext_label")
        font1 = QFont()
        font1.setPointSize(16)
        self.typingtext_label.setFont(font1)
        self.typingtext_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.typingtext_label.setWordWrap(True)

        self.verticalLayout.addWidget(self.typingtext_label)

        self.plainTextEdit = QPlainTextEdit(test_widget)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setEnabled(False)

        self.verticalLayout.addWidget(self.plainTextEdit)

        self.results_label = QLabel(test_widget)
        self.results_label.setObjectName(u"results_label")

        self.verticalLayout.addWidget(self.results_label, 0, Qt.AlignHCenter)

        self.buttons = QHBoxLayout()
        self.buttons.setSpacing(10)
        self.buttons.setObjectName(u"buttons")
        self.buttons.setContentsMargins(50, -1, 50, -1)
        self.again_button = QPushButton(test_widget)
        self.again_button.setObjectName(u"again_button")

        self.buttons.addWidget(self.again_button)

        self.return_button = QPushButton(test_widget)
        self.return_button.setObjectName(u"return_button")

        self.buttons.addWidget(self.return_button)


        self.verticalLayout.addLayout(self.buttons)

        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 2)
        self.verticalLayout.setStretch(2, 2)

        self.retranslateUi(test_widget)

        QMetaObject.connectSlotsByName(test_widget)
    # setupUi

    def retranslateUi(self, test_widget):
        test_widget.setWindowTitle(QCoreApplication.translate("test_widget", u"Form", None))
        self.countdown_label.setText(QCoreApplication.translate("test_widget", u"Countdown", None))
        self.typingtext_label.setText(QCoreApplication.translate("test_widget", u"Here is example text", None))
        self.results_label.setText(QCoreApplication.translate("test_widget", u"Result", None))
        self.again_button.setText(QCoreApplication.translate("test_widget", u"Again", None))
        self.return_button.setText(QCoreApplication.translate("test_widget", u"Return", None))
    # retranslateUi

