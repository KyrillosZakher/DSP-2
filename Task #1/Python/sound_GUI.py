# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sound_gui.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import pyaudio
import numpy as np

class Ui_Listen(object):
    def setupUi(self, Listen):
        Listen.setObjectName("Listen")
        Listen.resize(1551, 740)
        self.centralwidget = QtWidgets.QWidget(Listen)
        self.centralwidget.setObjectName("centralwidget")
        self.PlaySins = QtWidgets.QPushButton(self.centralwidget)
        self.PlaySins.setGeometry(QtCore.QRect(120, 416, 531, 121))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.PlaySins.setFont(font)
        self.PlaySins.setObjectName("PlaySins")
        self.PlaySinExp = QtWidgets.QPushButton(self.centralwidget)
        self.PlaySinExp.setGeometry(QtCore.QRect(730, 420, 801, 111))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.PlaySinExp.setFont(font)
        self.PlaySinExp.setObjectName("PlaySinExp")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(130, 40, 501, 131))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(130, 190, 481, 131))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.freq = QtWidgets.QTextEdit(self.centralwidget)
        self.freq.setGeometry(QtCore.QRect(700, 70, 571, 71))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.freq.setFont(font)
        self.freq.setObjectName("freq")
        self.dura = QtWidgets.QTextEdit(self.centralwidget)
        self.dura.setGeometry(QtCore.QRect(700, 230, 581, 71))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.dura.setFont(font)
        self.dura.setObjectName("dura")
        Listen.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Listen)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1551, 47))
        self.menubar.setObjectName("menubar")
        Listen.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Listen)
        self.statusbar.setObjectName("statusbar")
        Listen.setStatusBar(self.statusbar)

        self.retranslateUi(Listen)
        QtCore.QMetaObject.connectSlotsByName(Listen)

    def retranslateUi(self, Listen):
        _translate = QtCore.QCoreApplication.translate
        Listen.setWindowTitle(_translate("Listen", "MainWindow"))
        self.PlaySins.setText(_translate("Listen", "Play Sinusoids..."))
        self.PlaySinExp.setText(_translate("Listen", "Play Sinusoids and Exponentials..."))
        self.label.setText(_translate("Listen", "Frequenzy in (Hz) :"))
        self.label_2.setText(_translate("Listen", "Duration in (Sec) :"))

        self.PlaySins.clicked.connect(self.play1)
        self.PlaySinExp.clicked.connect(self.play2)


    def play1(self):
        p = pyaudio.PyAudio()
        volume = .5  # range [0.0, 1.0]
        fs = 44100  # sampling rate, Hz, must be integer : number op points in one second
        duration = float(self.dura.toPlainText())  # input  # in seconds, may be float
        f = float(self.freq.toPlainText())  # input   # sine frequency, Hz, may be float
        # generate samples, note conversion to float32 array
        samples = (np.sin(2 * np.pi * np.arange(fs * duration) * f / fs) + np.sin(
            2 * np.pi * np.arange(fs * duration) * f / fs)).astype(np.float32)
        # for paFloat32 sample values must be in range [-1.0, 1.0]
        stream = p.open(format=pyaudio.paFloat32,
                        channels=1,
                        rate=fs,
                        output=True)
        # play. May repeat with different volume values (if done interactively)
        stream.write(volume * samples)
        stream.stop_stream()
        stream.close()

    def play2(self):
        p = pyaudio.PyAudio()
        volume = .5  # range [0.0, 1.0]
        fs = 44100  # sampling rate, Hz, must be integer : number op points in one second
        duration = float(self.dura.toPlainText())  # input  # in seconds, may be float
        f = float(self.freq.toPlainText())  # input   # sine frequency, Hz, may be float
        # generate samples, note conversion to float32 array
        samples = (np.sin(2 * np.pi * np.arange(fs * duration) * f / fs) + np.exp(
            (-1j) * 2 * np.pi * np.arange(fs * duration) * f / fs)).astype(np.float32)
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
    Listen = QtWidgets.QMainWindow()
    ui = Ui_Listen()
    ui.setupUi(Listen)
    Listen.show()
    sys.exit(app.exec_())

