# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(528, 466)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_omer = QtWidgets.QLabel(self.centralwidget)
        self.label_omer.setGeometry(QtCore.QRect(30, 80, 461, 111))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(30)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_omer.setFont(font)
        self.label_omer.setObjectName("label_omer")
        self.click_button = QtWidgets.QPushButton(self.centralwidget, clicked= lambda:self.sample_function())
        self.click_button.setGeometry(QtCore.QRect(80, 240, 331, 131))
        font = QtGui.QFont()
        font.setFamily("Noto Serif")
        font.setPointSize(36)
        self.click_button.setFont(font)
        self.click_button.setObjectName("click_button")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 528, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_omer.setText(_translate("MainWindow", "omercik"))
        self.click_button.setText(_translate("MainWindow", "PushButton"))


    def sample_function(self):
        self.label_omer.setText("clicked dsf")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
