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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLayout,
    QLineEdit, QMainWindow, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QSpinBox, QStatusBar,
    QVBoxLayout, QWidget)
import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(400, 450)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamilies([u"Segoe MDL2 Assets"])
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"* {\n"
"	color: white;\n"
"}\n"
"\n"
"#title_label {\n"
"  text-align: center;\n"
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
"	width: 200px;\n"
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
        self.main_layout = QWidget(MainWindow)
        self.main_layout.setObjectName(u"main_layout")
        sizePolicy.setHeightForWidth(self.main_layout.sizePolicy().hasHeightForWidth())
        self.main_layout.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setFamilies([u"Segoe Script"])
        self.main_layout.setFont(font1)
        self.verticalLayout = QVBoxLayout(self.main_layout)
        self.verticalLayout.setSpacing(1)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetNoConstraint)
        self.verticalLayout.setContentsMargins(25, 5, 25, 5)
        self.title_label = QLabel(self.main_layout)
        self.title_label.setObjectName(u"title_label")
        font2 = QFont()
        font2.setFamilies([u"MS Shell Dlg 2"])
        font2.setPointSize(24)
        font2.setBold(False)
        self.title_label.setFont(font2)
        self.title_label.setLayoutDirection(Qt.LeftToRight)
        self.title_label.setStyleSheet(u"")
        self.title_label.setScaledContents(False)

        self.verticalLayout.addWidget(self.title_label, 0, Qt.AlignHCenter)

        self.graphic_window = QLabel(self.main_layout)
        self.graphic_window.setObjectName(u"graphic_window")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.graphic_window.sizePolicy().hasHeightForWidth())
        self.graphic_window.setSizePolicy(sizePolicy1)
        self.graphic_window.setScaledContents(True)

        self.verticalLayout.addWidget(self.graphic_window)

        self.options_layout = QHBoxLayout()
        self.options_layout.setSpacing(15)
        self.options_layout.setObjectName(u"options_layout")
        self.options_layout.setContentsMargins(50, 10, 50, 10)
        self.watermark_input_text = QLineEdit(self.main_layout)
        self.watermark_input_text.setObjectName(u"watermark_input_text")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.watermark_input_text.sizePolicy().hasHeightForWidth())
        self.watermark_input_text.setSizePolicy(sizePolicy2)
        font3 = QFont()
        font3.setFamilies([u"calibri 53"])
        self.watermark_input_text.setFont(font3)
        self.watermark_input_text.setStyleSheet(u"")
        self.watermark_input_text.setDragEnabled(False)

        self.options_layout.addWidget(self.watermark_input_text)

        self.font_size_label = QLabel(self.main_layout)
        self.font_size_label.setObjectName(u"font_size_label")
        self.font_size_label.setFont(font3)

        self.options_layout.addWidget(self.font_size_label)

        self.spin_box = QSpinBox(self.main_layout)
        self.spin_box.setObjectName(u"spin_box")
        self.spin_box.setFont(font3)

        self.options_layout.addWidget(self.spin_box)


        self.verticalLayout.addLayout(self.options_layout)

        self.save_button = QPushButton(self.main_layout)
        self.save_button.setObjectName(u"save_button")
        self.save_button.setEnabled(True)
        font4 = QFont()
        font4.setFamilies([u"calibri 53"])
        font4.setBold(True)
        self.save_button.setFont(font4)
        self.save_button.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.save_button, 0, Qt.AlignHCenter)

        self.verticalLayout.setStretch(1, 5)
        self.verticalLayout.setStretch(2, 2)
        self.verticalLayout.setStretch(3, 2)
        MainWindow.setCentralWidget(self.main_layout)
        self.graphic_window.raise_()
        self.save_button.raise_()
        self.title_label.raise_()
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 400, 21))
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
        self.graphic_window.setText("")
        self.watermark_input_text.setText("")
        self.watermark_input_text.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter watermark text", None))
        self.font_size_label.setText(QCoreApplication.translate("MainWindow", u"Font Size", None))
        self.save_button.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuAbout.setTitle(QCoreApplication.translate("MainWindow", u"About", None))
    # retranslateUi

