# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitled.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(570, 406)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(280, 60, 251, 291))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 0, 2, 1, 1)

        self.label_3 = QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 0, 5, 1, 1)

        self.label = QLabel(self.gridLayoutWidget)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(70, 30, 160, 321))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.lat1 = QLineEdit(self.verticalLayoutWidget)
        self.lat1.setObjectName(u"lat1")

        self.verticalLayout.addWidget(self.lat1)

        self.lon1 = QLineEdit(self.verticalLayoutWidget)
        self.lon1.setObjectName(u"lon1")

        self.verticalLayout.addWidget(self.lon1)

        self.lat2 = QLineEdit(self.verticalLayoutWidget)
        self.lat2.setObjectName(u"lat2")

        self.verticalLayout.addWidget(self.lat2)

        self.lon2 = QLineEdit(self.verticalLayoutWidget)
        self.lon2.setObjectName(u"lon2")

        self.verticalLayout.addWidget(self.lon2)

        self.calculate_button = QPushButton(self.verticalLayoutWidget)
        self.calculate_button.setObjectName(u"calculate_button")

        self.verticalLayout.addWidget(self.calculate_button)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 570, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"km", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Distance", None))
        self.lat1.setText("")
        self.lat1.setPlaceholderText(QCoreApplication.translate("MainWindow", u"lattidue_1", None))
        self.lon1.setPlaceholderText(QCoreApplication.translate("MainWindow", u"longitude_1", None))
        self.lat2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"latitude_2", None))
        self.lon2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"longitude2", None))
        self.calculate_button.setText(QCoreApplication.translate("MainWindow", u"Calculate", None))
    # retranslateUi

