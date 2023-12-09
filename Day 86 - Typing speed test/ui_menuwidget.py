# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'menuwidget.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)
import resource_rc
import resource_rc

class Ui_menu_widget(object):
    def setupUi(self, menu_widget):
        if not menu_widget.objectName():
            menu_widget.setObjectName(u"menu_widget")
        menu_widget.resize(500, 560)
        menu_widget.setStyleSheet(u"#menu_widget {\n"
"background-color:qradialgradient(spread:pad, cx:0.483682, cy:0.307, radius:0.5, fx:0.478, fy:0, stop:0 rgba(173, 185, 207, 255), stop:1 rgba(255, 255, 255, 255))\n"
"}\n"
"\n"
"\n"
"")
        self.verticalLayout = QVBoxLayout(menu_widget)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(15, 30, 15, 30)
        self.title_label = QLabel(menu_widget)
        self.title_label.setObjectName(u"title_label")
        font = QFont()
        font.setPointSize(20)
        self.title_label.setFont(font)

        self.verticalLayout.addWidget(self.title_label, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.picture_label = QLabel(menu_widget)
        self.picture_label.setObjectName(u"picture_label")
        self.picture_label.setMaximumSize(QSize(380, 300))
        self.picture_label.setPixmap(QPixmap(u":/resources/Day 86 - Typing speed test/img/icon.png"))
        self.picture_label.setScaledContents(True)
        self.picture_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.picture_label.setMargin(0)

        self.verticalLayout.addWidget(self.picture_label, 0, Qt.AlignHCenter)

        self.entername_label = QLabel(menu_widget)
        self.entername_label.setObjectName(u"entername_label")
        font1 = QFont()
        font1.setPointSize(12)
        self.entername_label.setFont(font1)

        self.verticalLayout.addWidget(self.entername_label, 0, Qt.AlignHCenter)

        self.nameinput_lineedit = QLineEdit(menu_widget)
        self.nameinput_lineedit.setObjectName(u"nameinput_lineedit")
        self.nameinput_lineedit.setMinimumSize(QSize(300, 0))

        self.verticalLayout.addWidget(self.nameinput_lineedit, 0, Qt.AlignHCenter)

        self.start_button = QPushButton(menu_widget)
        self.start_button.setObjectName(u"start_button")
        self.start_button.setMinimumSize(QSize(180, 0))

        self.verticalLayout.addWidget(self.start_button, 0, Qt.AlignHCenter)

        self.verticalLayout.setStretch(2, 1)

        self.retranslateUi(menu_widget)

        QMetaObject.connectSlotsByName(menu_widget)
    # setupUi

    def retranslateUi(self, menu_widget):
        menu_widget.setWindowTitle(QCoreApplication.translate("menu_widget", u"Form", None))
        self.title_label.setText(QCoreApplication.translate("menu_widget", u"Speed typing test", None))
        self.picture_label.setText("")
        self.entername_label.setText(QCoreApplication.translate("menu_widget", u"Enter your name", None))
        self.nameinput_lineedit.setText("")
        self.start_button.setText(QCoreApplication.translate("menu_widget", u"Start", None))
    # retranslateUi

