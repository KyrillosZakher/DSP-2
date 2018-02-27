# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled2.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import pyaudio
import numpy as np
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(80, 110, 241, 61))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(80, 210, 261, 91))
        self.label_2.setObjectName("label_2")
        self.Frequency = QtWidgets.QTextEdit(self.centralwidget)
        self.Frequency.setGeometry(QtCore.QRect(400, 110, 291, 61))
        self.Frequency.setObjectName("Frequency")
        self.Duration = QtWidgets.QTextEdit(self.centralwidget)
        self.Duration.setGeometry(QtCore.QRect(400, 230, 291, 61))
        self.Duration.setObjectName("Duration")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(460, 390, 231, 81))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 51))
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
        self.label.setText(_translate("MainWindow", "Frequency (Hz)"))
        self.label_2.setText(_translate("MainWindow", "Duration (Sec)"))
        self.pushButton.setText(_translate("MainWindow", "Play"))

        self.pushButton.clicked.connect(self.play)
    def play(self):
        p = pyaudio.PyAudio()
        volume = .5  # range [0.0, 1.0]
        fs = 44100  # sampling rate, Hz, must be integer : number op points in one second
        duration = float(self.Duration.toPlainText())  # input  # in seconds, may be float
        f = float(self.Frequency.toPlainText())  # input   # sine frequency, Hz, may be float
        # generate samples, note conversion to float32 array
        samples = (np.sin(2 * np.pi * np.arange(fs * duration) * f / fs)).astype(np.float32)
        # for paFloat32 sample values must be in range [-1.0, 1.0]
        stream = p.open(format=pyaudio.paFloat32,
                        channels=1,
                        rate=fs,
                        output=True)
        # play. May repeat with different volume values (if done interactively)
        stream.write(volume * samples)
        stream.stop_stream()
        stream.close()
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

