# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                          QMetaObject, QObject, QPoint, QRect,
                          QSize, QTime, QUrl, Qt)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
                         QFont, QFontDatabase, QGradient, QIcon,
                         QImage, QKeySequence, QLinearGradient, QPainter,
                         QPalette, QPixmap, QRadialGradient, QTransform)
from PyQt5.QtWidgets import (QApplication, QComboBox, QLineEdit, QMainWindow,
                             QMenuBar, QPushButton, QSizePolicy, QStatusBar,
                             QWidget, QTextBrowser)


class Ui_MainWindow(object):
    def __init__(self, memo):
        self.memo = memo

    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(540, 420)
        font = QFont()
        font.setPointSize(14)
        MainWindow.setFont(font)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)

        self.input = QLineEdit(self.centralwidget)
        self.input.setObjectName(u"input")
        self.input.setGeometry(QRect(30, 90, 480, 30))
        self.input2 = QLineEdit(self.centralwidget)
        self.input2.setObjectName(u"input2")
        self.input2.setGeometry(QRect(30, 140, 60, 30))
        self.input3 = QLineEdit(self.centralwidget)
        self.input3.setObjectName(u"input3")
        self.input3.setGeometry(QRect(120, 140, 60, 30))
        self.input4 = QLineEdit(self.centralwidget)
        self.input4.setObjectName(u"input4")
        self.input4.setGeometry(QRect(210, 140, 60, 30))
        self.input5 = QLineEdit(self.centralwidget)
        self.input5.setObjectName(u"input5")
        self.input5.setGeometry(QRect(300, 140, 60, 30))
        self.btn = QPushButton(self.centralwidget)
        self.btn.setObjectName(u"btn")
        self.btn.setGeometry(QRect(390, 140, 120, 30))
        self.option1 = QComboBox(self.centralwidget)
        self.option1.setObjectName(u"option1")
        self.option1.setGeometry(QRect(30, 40, 200, 30))
        self.option2 = QComboBox(self.centralwidget)
        self.option2.setObjectName(u"option2")
        self.option2.setGeometry(QRect(310, 40, 200, 30))

        self.label1 = QTextBrowser(self.centralwidget)
        self.label1.setObjectName(u"label1")
        self.label1.setGeometry(QRect(30, 190, 480, 300))

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 600, 31))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.input.setText(self.memo['topToken'])
        timing = self.memo['timing']
        self.input2.setText(timing[0])
        self.input3.setText(timing[1])
        self.input4.setText(timing[2])
        self.input5.setText(timing[3])

        self.btn.setText(QCoreApplication.translate("MainWindow", u"SURPRISE ME", None))
    # retranslateUi
