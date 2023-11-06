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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QSizePolicy, QSpinBox, QStatusBar, QWidget)
import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(681, 562)
        font = QFont()
        font.setFamilies([u"Segoe MDL2 Assets"])
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"* {\n"
"	color: white;\n"
"}\n"
"\n"
"#MainWindow {	\n"
"	background-color: qradialgradient(spread:pad, cx:0.511, cy:0.505682, radius:0.79, fx:0.284091, fy:0.25, stop:0 rgba(95, 95, 95, 255), stop:1 rgba(0, 0, 0, 255))\n"
"}\n"
"\n"
"QMenuBar, QMenu {\n"
"	background-color: rgb(49,49,49);\n"
"	border-bottom: 0.5px solid white;\n"
"}\n"
"\n"
"#graphic_window {\n"
"	background-color: rgba(255, 255, 255, 100);\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"#instruction_label {\n"
"	color: rgba(200, 200, 200, 100);\n"
"}\n"
"\n"
"#watermark_input_text, #spin_box {\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"	border: 0px;\n"
"	border-bottom: 0.5px solid white;\n"
"}\n"
"\n"
"#watermark_input_text::hover, #spin_box::hover {\n"
"	border-bottom: 1.5px solid white;\n"
"}\n"
"\n"
"#save_button {\n"
"	border-radius: 10px;\n"
"	background: grey;\n"
"}\n"
"\n"
"#save_button::hover {\n"
"	border: 1px solid white;\n"
"}")
        self.actionLoad = QAction(MainWindow)
        self.actionLoad.setObjectName(u"actionLoad")
        self.actionSave = QAction(MainWindow)
        self.actionSave.setObjectName(u"actionSave")
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.actionAboutQt = QAction(MainWindow)
        self.actionAboutQt.setObjectName(u"actionAboutQt")
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        font1 = QFont()
        font1.setFamilies([u"Segoe Script"])
        self.centralwidget.setFont(font1)
        self.title_label = QLabel(self.centralwidget)
        self.title_label.setObjectName(u"title_label")
        self.title_label.setGeometry(QRect(240, 10, 187, 39))
        font2 = QFont()
        font2.setFamilies([u"MS Shell Dlg 2"])
        font2.setPointSize(24)
        font2.setBold(False)
        self.title_label.setFont(font2)
        self.title_label.setStyleSheet(u"")
        self.save_button = QPushButton(self.centralwidget)
        self.save_button.setObjectName(u"save_button")
        self.save_button.setGeometry(QRect(240, 490, 186, 27))
        font3 = QFont()
        font3.setFamilies([u"calibri 53"])
        font3.setBold(True)
        self.save_button.setFont(font3)
        self.save_button.setStyleSheet(u"")
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(110, 450, 441, 29))
        self.options_layout = QHBoxLayout(self.layoutWidget)
        self.options_layout.setObjectName(u"options_layout")
        self.options_layout.setContentsMargins(0, 0, 0, 0)
        self.watermark_input_text = QLineEdit(self.layoutWidget)
        self.watermark_input_text.setObjectName(u"watermark_input_text")
        font4 = QFont()
        font4.setFamilies([u"calibri 53"])
        self.watermark_input_text.setFont(font4)
        self.watermark_input_text.setStyleSheet(u"QLabel {\n"
"qproperty-alignment: AlignCenter;\n"
"}")
        self.watermark_input_text.setDragEnabled(False)

        self.options_layout.addWidget(self.watermark_input_text)

        self.font_size_label = QLabel(self.layoutWidget)
        self.font_size_label.setObjectName(u"font_size_label")
        self.font_size_label.setFont(font4)

        self.options_layout.addWidget(self.font_size_label)

        self.spin_box = QSpinBox(self.layoutWidget)
        self.spin_box.setObjectName(u"spin_box")
        self.spin_box.setFont(font4)

        self.options_layout.addWidget(self.spin_box)

        self.instruction_label = QLabel(self.centralwidget)
        self.instruction_label.setObjectName(u"instruction_label")
        self.instruction_label.setGeometry(QRect(100, 180, 481, 131))
        font5 = QFont()
        font5.setPointSize(36)
        self.instruction_label.setFont(font5)
        self.graphic_window = QLabel(self.centralwidget)
        self.graphic_window.setObjectName(u"graphic_window")
        self.graphic_window.setGeometry(QRect(30, 50, 621, 381))
        self.graphic_window.setScaledContents(False)
        MainWindow.setCentralWidget(self.centralwidget)
        self.instruction_label.raise_()
        self.title_label.raise_()
        self.save_button.raise_()
        self.layoutWidget.raise_()
        self.graphic_window.raise_()
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 681, 21))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuAbout = QMenu(self.menubar)
        self.menuAbout.setObjectName(u"menuAbout")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())
        self.menuFile.addAction(self.actionLoad)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuAbout.addAction(self.actionAbout)
        self.menuAbout.addAction(self.actionAboutQt)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionLoad.setText(QCoreApplication.translate("MainWindow", u"Load", None))
        self.actionSave.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.actionAboutQt.setText(QCoreApplication.translate("MainWindow", u"AboutQt", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.title_label.setText(QCoreApplication.translate("MainWindow", u"Watermarker", None))
        self.save_button.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.watermark_input_text.setText("")
        self.watermark_input_text.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter watermark text", None))
        self.font_size_label.setText(QCoreApplication.translate("MainWindow", u"Font Size", None))
        self.instruction_label.setText(QCoreApplication.translate("MainWindow", u"Drag your image here", None))
        self.graphic_window.setText("")
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuAbout.setTitle(QCoreApplication.translate("MainWindow", u"About", None))
    # retranslateUi

