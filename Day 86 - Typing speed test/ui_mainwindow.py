# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QVBoxLayout, QWidget)
import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(500, 536)
        MainWindow.setStyleSheet(u"#MainWindow {	\n"
"	background-color:qradialgradient(spread:pad, cx:0.483682, cy:0.307, radius:0.5, fx:0.478, fy:0, stop:0 rgba(173, 185, 207, 255), stop:1 rgba(255, 255, 255, 255))\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        self.actionHighscores = QAction(MainWindow)
        self.actionHighscores.setObjectName(u"actionHighscores")
        self.actionAboutQt = QAction(MainWindow)
        self.actionAboutQt.setObjectName(u"actionAboutQt")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setEnabled(True)
        self.centralwidget.setAutoFillBackground(False)
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(20, 30, 20, 30)
        self.title_label = QLabel(self.centralwidget)
        self.title_label.setObjectName(u"title_label")
        font = QFont()
        font.setPointSize(20)
        self.title_label.setFont(font)

        self.verticalLayout.addWidget(self.title_label, 0, Qt.AlignHCenter)

        self.picture_label = QLabel(self.centralwidget)
        self.picture_label.setObjectName(u"picture_label")
        self.picture_label.setMaximumSize(QSize(380, 300))
        self.picture_label.setPixmap(QPixmap(u":/resources/Day 86 - Typing speed test/img/icon.png"))
        self.picture_label.setScaledContents(True)
        self.picture_label.setMargin(0)

        self.verticalLayout.addWidget(self.picture_label, 0, Qt.AlignHCenter)

        self.entername_label = QLabel(self.centralwidget)
        self.entername_label.setObjectName(u"entername_label")
        font1 = QFont()
        font1.setPointSize(12)
        self.entername_label.setFont(font1)

        self.verticalLayout.addWidget(self.entername_label, 0, Qt.AlignHCenter)

        self.nameinput_lineedit = QLineEdit(self.centralwidget)
        self.nameinput_lineedit.setObjectName(u"nameinput_lineedit")

        self.verticalLayout.addWidget(self.nameinput_lineedit)

        self.start_button = QPushButton(self.centralwidget)
        self.start_button.setObjectName(u"start_button")

        self.verticalLayout.addWidget(self.start_button)

        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 500, 21))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuInfo = QMenu(self.menubar)
        self.menuInfo.setObjectName(u"menuInfo")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuInfo.menuAction())
        self.menuFile.addAction(self.actionHighscores)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuInfo.addAction(self.actionAbout)
        self.menuInfo.addAction(self.actionAboutQt)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.actionHighscores.setText(QCoreApplication.translate("MainWindow", u"View highscores", None))
        self.actionAboutQt.setText(QCoreApplication.translate("MainWindow", u"AboutQt", None))
        self.title_label.setText(QCoreApplication.translate("MainWindow", u"Typing speed test", None))
        self.picture_label.setText("")
        self.entername_label.setText(QCoreApplication.translate("MainWindow", u"Enter your name", None))
        self.nameinput_lineedit.setText("")
        self.start_button.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"Start", None))
        self.menuInfo.setTitle(QCoreApplication.translate("MainWindow", u"Info", None))
    # retranslateUi

