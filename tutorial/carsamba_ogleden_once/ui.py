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
        MainWindow.resize(764, 629)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(40, 10, 651, 591))
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayoutWidget = QWidget(self.tab)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(90, 20, 111, 171))
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

        self.verticalLayoutWidget_2 = QWidget(self.tab)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(230, 10, 341, 291))
        self.verticalLayout_3 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_3 = QLabel(self.verticalLayoutWidget_2)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 0, 5, 1, 1)

        self.label_2 = QLabel(self.verticalLayoutWidget_2)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 0, 2, 1, 1)

        self.label = QLabel(self.verticalLayoutWidget_2)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)


        self.verticalLayout_3.addLayout(self.gridLayout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_4 = QLabel(self.verticalLayoutWidget_2)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout.addWidget(self.label_4)

        self.label_value_azamith = QLabel(self.verticalLayoutWidget_2)
        self.label_value_azamith.setObjectName(u"label_value_azamith")

        self.horizontalLayout.addWidget(self.label_value_azamith)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_5 = QLabel(self.verticalLayoutWidget_2)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_2.addWidget(self.label_5)

        self.final_bearing_label = QLabel(self.verticalLayoutWidget_2)
        self.final_bearing_label.setObjectName(u"final_bearing_label")

        self.horizontalLayout_2.addWidget(self.final_bearing_label)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.midpoint_label = QLabel(self.verticalLayoutWidget_2)
        self.midpoint_label.setObjectName(u"midpoint_label")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.midpoint_label.sizePolicy().hasHeightForWidth())
        self.midpoint_label.setSizePolicy(sizePolicy)

        self.horizontalLayout_4.addWidget(self.midpoint_label)

        self.midpoint_value_label = QLabel(self.verticalLayoutWidget_2)
        self.midpoint_value_label.setObjectName(u"midpoint_value_label")

        self.horizontalLayout_4.addWidget(self.midpoint_value_label)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)

        self.verticalLayoutWidget_3 = QWidget(self.tab)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(70, 330, 111, 211))
        self.verticalLayout_4 = QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.start_lat_lineedit = QLineEdit(self.verticalLayoutWidget_3)
        self.start_lat_lineedit.setObjectName(u"start_lat_lineedit")

        self.verticalLayout_4.addWidget(self.start_lat_lineedit)

        self.start_longitude_lineedit = QLineEdit(self.verticalLayoutWidget_3)
        self.start_longitude_lineedit.setObjectName(u"start_longitude_lineedit")

        self.verticalLayout_4.addWidget(self.start_longitude_lineedit)

        self.bearing_lineEdit = QLineEdit(self.verticalLayoutWidget_3)
        self.bearing_lineEdit.setObjectName(u"bearing_lineEdit")

        self.verticalLayout_4.addWidget(self.bearing_lineEdit)

        self.distance_lineEdit = QLineEdit(self.verticalLayoutWidget_3)
        self.distance_lineEdit.setObjectName(u"distance_lineEdit")

        self.verticalLayout_4.addWidget(self.distance_lineEdit)

        self.calculate_dest_bearing_button = QPushButton(self.verticalLayoutWidget_3)
        self.calculate_dest_bearing_button.setObjectName(u"calculate_dest_bearing_button")

        self.verticalLayout_4.addWidget(self.calculate_dest_bearing_button)

        self.verticalLayoutWidget_4 = QWidget(self.tab)
        self.verticalLayoutWidget_4.setObjectName(u"verticalLayoutWidget_4")
        self.verticalLayoutWidget_4.setGeometry(QRect(230, 330, 351, 211))
        self.verticalLayout_5 = QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.destination_point_label = QLabel(self.verticalLayoutWidget_4)
        self.destination_point_label.setObjectName(u"destination_point_label")

        self.horizontalLayout_5.addWidget(self.destination_point_label)

        self.destination_point_value_label = QLabel(self.verticalLayoutWidget_4)
        self.destination_point_value_label.setObjectName(u"destination_point_value_label")

        self.horizontalLayout_5.addWidget(self.destination_point_value_label)


        self.verticalLayout_5.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.final_bearing_label_2 = QLabel(self.verticalLayoutWidget_4)
        self.final_bearing_label_2.setObjectName(u"final_bearing_label_2")

        self.horizontalLayout_3.addWidget(self.final_bearing_label_2)

        self.final_bearing_value_label = QLabel(self.verticalLayoutWidget_4)
        self.final_bearing_value_label.setObjectName(u"final_bearing_value_label")

        self.horizontalLayout_3.addWidget(self.final_bearing_value_label)


        self.verticalLayout_5.addLayout(self.horizontalLayout_3)

        self.line = QFrame(self.tab)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(10, 300, 661, 21))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 764, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.lat1.setText("")
        self.lat1.setPlaceholderText(QCoreApplication.translate("MainWindow", u"lattidue_1", None))
        self.lon1.setPlaceholderText(QCoreApplication.translate("MainWindow", u"longitude_1", None))
        self.lat2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"latitude_2", None))
        self.lon2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"longitude2", None))
        self.calculate_button.setText(QCoreApplication.translate("MainWindow", u"Calculate", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"km", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Distance", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Azamith", None))
        self.label_value_azamith.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Final bearing", None))
        self.final_bearing_label.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.midpoint_label.setText(QCoreApplication.translate("MainWindow", u"Midpoint ", None))
        self.midpoint_value_label.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.start_lat_lineedit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"start latitude", None))
        self.start_longitude_lineedit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"start longitude", None))
        self.bearing_lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"bearing", None))
        self.distance_lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"distance", None))
        self.calculate_dest_bearing_button.setText(QCoreApplication.translate("MainWindow", u"Caltulate", None))
        self.destination_point_label.setText(QCoreApplication.translate("MainWindow", u"Destination point", None))
        self.destination_point_value_label.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.final_bearing_label_2.setText(QCoreApplication.translate("MainWindow", u"Final bearing", None))
        self.final_bearing_value_label.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Tab 1", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Tab 2", None))
    # retranslateUi

