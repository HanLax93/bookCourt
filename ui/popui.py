# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pop.ui'
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
from PyQt5.QtWidgets import (QApplication, QMainWindow, QMenuBar, QSizePolicy,
    QStatusBar, QTextBrowser, QVBoxLayout, QWidget)

class Ui_PopWindow(object):
    def setupUi(self, PopWindow):
        if not PopWindow.objectName():
            PopWindow.setObjectName(u"PopWindow")
        PopWindow.resize(600, 270)
        self.centralwidget = QWidget(PopWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(0, 0, 601, 241))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.text2 = QTextBrowser(self.verticalLayoutWidget)
        self.text2.setObjectName(u"text2")

        self.verticalLayout.addWidget(self.text2)

        self.text1 = QTextBrowser(self.verticalLayoutWidget)
        self.text1.setObjectName(u"text1")

        self.verticalLayout.addWidget(self.text1)

        PopWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(PopWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 600, 22))
        PopWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(PopWindow)
        self.statusbar.setObjectName(u"statusbar")
        PopWindow.setStatusBar(self.statusbar)

        self.retranslateUi(PopWindow)

        QMetaObject.connectSlotsByName(PopWindow)
    # setupUi

    def retranslateUi(self, PopWindow):
        PopWindow.setWindowTitle(QCoreApplication.translate("PopWindow", u"MainWindow", None))
    # retranslateUi

