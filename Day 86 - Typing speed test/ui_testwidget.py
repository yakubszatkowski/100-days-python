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
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(test_widget.sizePolicy().hasHeightForWidth())
        test_widget.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(12)
        test_widget.setFont(font)
        test_widget.setStyleSheet(u"#test_widget {background-color:qradialgradient(spread:pad, cx:0.483682, cy:0.307, radius:0.5, fx:0.478, fy:0, stop:0 rgba(173, 185, 207, 255), stop:1 rgba(255, 255, 255, 255))}")
        self.verticalLayout = QVBoxLayout(test_widget)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(15, 30, 15, 30)
        self.countdown_label = QLabel(test_widget)
        self.countdown_label.setObjectName(u"countdown_label")
        font1 = QFont()
        font1.setPointSize(26)
        self.countdown_label.setFont(font1)

        self.verticalLayout.addWidget(self.countdown_label, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.text_label = QLabel(test_widget)
        self.text_label.setObjectName(u"text_label")
        font2 = QFont()
        font2.setPointSize(20)
        self.text_label.setFont(font2)
        self.text_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.text_label.setWordWrap(True)

        self.verticalLayout.addWidget(self.text_label)

        self.textinput_textedit = QPlainTextEdit(test_widget)
        self.textinput_textedit.setObjectName(u"textinput_textedit")
        self.textinput_textedit.setEnabled(True)
        self.textinput_textedit.setMaximumSize(QSize(16777215, 167))
        font3 = QFont()
        font3.setPointSize(16)
        self.textinput_textedit.setFont(font3)

        self.verticalLayout.addWidget(self.textinput_textedit)

        self.results_label = QLabel(test_widget)
        self.results_label.setObjectName(u"results_label")

        self.verticalLayout.addWidget(self.results_label, 0, Qt.AlignHCenter)

        self.buttons_layout = QHBoxLayout()
        self.buttons_layout.setSpacing(10)
        self.buttons_layout.setObjectName(u"buttons_layout")
        self.buttons_layout.setContentsMargins(50, -1, 50, -1)
        self.again_button = QPushButton(test_widget)
        self.again_button.setObjectName(u"again_button")

        self.buttons_layout.addWidget(self.again_button)

        self.return_button = QPushButton(test_widget)
        self.return_button.setObjectName(u"return_button")

        self.buttons_layout.addWidget(self.return_button)


        self.verticalLayout.addLayout(self.buttons_layout)

        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 2)
        self.verticalLayout.setStretch(2, 2)

        self.retranslateUi(test_widget)

        QMetaObject.connectSlotsByName(test_widget)
    # setupUi

    def retranslateUi(self, test_widget):
        test_widget.setWindowTitle(QCoreApplication.translate("test_widget", u"Form", None))
        self.countdown_label.setText(QCoreApplication.translate("test_widget", u"Countdown", None))
        self.text_label.setText(QCoreApplication.translate("test_widget", u"Here is example text", None))
        self.results_label.setText(QCoreApplication.translate("test_widget", u"Result", None))
        self.again_button.setText(QCoreApplication.translate("test_widget", u"Again", None))
        self.return_button.setText(QCoreApplication.translate("test_widget", u"Return", None))
    # retranslateUi

