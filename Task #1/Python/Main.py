# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from sound_GUI import Ui_Listen
from project import Ui_Show
from Sample import Ui_Sample



class Ui_MainWindow(object):

    def ListenWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Listen()
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(840, 810)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Sampling = QtWidgets.QPushButton(self.centralwidget)
        self.Sampling.setGeometry(QtCore.QRect(160, 240, 531, 181))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.Sampling.setFont(font)
        self.Sampling.setObjectName("Sampling")
        self.show = QtWidgets.QPushButton(self.centralwidget)
        self.show.setGeometry(QtCore.QRect(160, 30, 531, 181))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.show.setFont(font)
        self.show.setObjectName("show")
        self.listen = QtWidgets.QPushButton(self.centralwidget)
        self.listen.setGeometry(QtCore.QRect(160, 450, 531, 181))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.listen.setFont(font)
        self.listen.setObjectName("listen")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 840, 47))
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
        self.Sampling.setText(_translate("MainWindow", "Sampling..."))
        self.show.setText(_translate("MainWindow", "Show Signal..."))
        self.listen.setText(_translate("MainWindow", "Listen..."))

        self.listen.clicked.connect(self.ListenWindow)
        self.show.clicked.connect(self.ShowWindow)
        self.Sampling.clicked.connect(self.SampleWindow)

    def ListenWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Listen()
        self.ui.setupUi(self.window)
        self.window.show()

    def ShowWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Show()
        self.ui.setupUi(self.window)
        self.window.show()

    def SampleWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Sample()
        self.ui.setupUi(self.window)
        self.window.show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

