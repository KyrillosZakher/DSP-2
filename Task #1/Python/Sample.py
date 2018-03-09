
# coding: utf-8

# In[2]:


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled3.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

import matplotlib.pyplot as plt
import numpy as np



from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication,QMessageBox,QFileDialog
import scipy.io as sio
import numpy as np
import plotly
import numpy
from numpy import sin,cos,pi
from plotly import tools
import plotly.graph_objs as go
plotly.offline.init_notebook_mode(connected=True)

class Ui_Sample(object):
    def setupUi(self, Sample):
        Sample.setObjectName("Sample")
        Sample.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(Sample)
        self.centralwidget.setObjectName("centralwidget")
        self.choose = QtWidgets.QLabel(self.centralwidget)
        self.choose.setGeometry(QtCore.QRect(40, 30, 337, 21))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.choose.setFont(font)
        self.choose.setObjectName("choose")
        self.Frequency = QtWidgets.QTextEdit(self.centralwidget)
        self.Frequency.setGeometry(QtCore.QRect(580, 70, 91, 31))
        self.Frequency.setObjectName("Frequency")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(480, 70, 91, 20))
        self.label.setObjectName("label")
        self.Amplitude = QtWidgets.QTextEdit(self.centralwidget)
        self.Amplitude.setGeometry(QtCore.QRect(580, 120, 91, 31))
        self.Amplitude.setObjectName("Amplitude")
        self.SR = QtWidgets.QTextEdit(self.centralwidget)
        self.SR.setGeometry(QtCore.QRect(580, 170, 91, 31))
        self.SR.setObjectName("SR")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(480, 120, 81, 20))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(480, 170, 81, 21))
        self.label_3.setObjectName("label_3")
        self.choose_2 = QtWidgets.QLabel(self.centralwidget)
        self.choose_2.setGeometry(QtCore.QRect(550, 30, 174, 21))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.choose_2.setFont(font)
        self.choose_2.setObjectName("choose_2")
        self.sample = QtWidgets.QPushButton(self.centralwidget)
        self.sample.setGeometry(QtCore.QRect(580, 210, 91, 31))
        self.sample.setObjectName("sample")
        self.close = QtWidgets.QPushButton(self.centralwidget)
        self.close.setGeometry(QtCore.QRect(630, 510, 111, 41))
        self.close.setObjectName("close")
        self.Clear = QtWidgets.QPushButton(self.centralwidget)
        self.Clear.setGeometry(QtCore.QRect(690, 150, 91, 31))
        self.Clear.setObjectName("Clear")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(60, 80, 121, 121))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.exp = QtWidgets.QPushButton(self.widget)
        self.exp.setObjectName("exp")
        self.verticalLayout.addWidget(self.exp)
        self.sine = QtWidgets.QPushButton(self.widget)
        self.sine.setObjectName("sine")
        self.verticalLayout.addWidget(self.sine)
        self.cosine = QtWidgets.QPushButton(self.widget)
        self.cosine.setObjectName("cosine")
        self.verticalLayout.addWidget(self.cosine)
        self.exp.raise_()
        self.sine.raise_()
        self.cosine.raise_()
        self.choose.raise_()
        self.Frequency.raise_()
        self.label.raise_()
        self.Amplitude.raise_()
        self.SR.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.exp.raise_()
        self.choose_2.raise_()
        self.choose_2.raise_()
        self.sample.raise_()
        self.choose.raise_()
        self.close.raise_()
        self.Clear.raise_()
        Sample.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Sample)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        Sample.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Sample)
        self.statusbar.setObjectName("statusbar")
        Sample.setStatusBar(self.statusbar)

        self.retranslateUi(Sample)
        self.close.clicked.connect(Sample.close)
        self.Clear.clicked.connect(self.Frequency.clear)
        self.Clear.clicked.connect(self.Amplitude.clear)
        self.Clear.clicked.connect(self.SR.clear)
        QtCore.QMetaObject.connectSlotsByName(Sample)

    def retranslateUi(self, Sample):
        global signal
        signal =0
        _translate = QtCore.QCoreApplication.translate
        Sample.setWindowTitle(_translate("Sample", "MainWindow"))
        self.choose.setText(_translate("Sample", "Choose what to plot"))
        self.label.setText(_translate("Sample", "Frequency (Hz)"))
        self.label_2.setText(_translate("Sample", "Amplitude"))
        self.label_3.setText(_translate("Sample", "Sampling Rate"))
        self.choose_2.setText(_translate("Sample", "if you want to Sample"))
        self.sample.setText(_translate("Sample", "Sample"))
        self.close.setText(_translate("Sample", "Close"))
        self.Clear.setText(_translate("Sample", "Clear Values"))
        self.exp.setText(_translate("Sample", "Exp"))
        self.sine.setText(_translate("Sample", "Sine"))
        self.cosine.setText(_translate("Sample", "Cosine"))
        self.exp.clicked.connect(self.Exp)
        self.sine.clicked.connect(self.Sin)
        self.cosine.clicked.connect(self.Cos)
        self.sample.clicked.connect(self.Samp)


    def Exp(self):
        global signal
        signal = 'Exp'
        Fs = 8000
        f = 5
        sample = 8000
        x = np.arange(sample)
        y = np.exp(2 * np.pi * f * x / Fs)
        plt.plot(x, y)
        plt.xlabel('sample(n)')
        plt.ylabel('voltage(V)')
        plt.show()


    def Sin(self):
        global signal
        signal = 'Sin'
        Fs = 8000
        f = 5
        sample = 8000
        x = np.arange(sample)
        y = np.sin(2 * np.pi * f * x / Fs)
        plt.plot(x, y)
        plt.xlabel('sample(n)')
        plt.ylabel('voltage(V)')
        plt.show()


    def Cos(self):
        global signal
        signal = 'Cos'
        Fs = 8000
        f = 5
        sample = 8000
        x = np.arange(sample)
        y = np.sin(2 * np.pi * f * x / Fs)
        plt.plot(x, y)
        plt.xlabel('sample(n)')
        plt.ylabel('voltage(V)')
        plt.show()

    
    def Samp(self):
        global signal
        
        
        
        

        if(signal == 'Exp'):

            time_of_view = 1.;  # s.
            analog_time = np.linspace(0, time_of_view, 10e5);  # s.

            sampling_rate = S_Sampling_Rate = float(self.SR.toPlainText());  # Hz
            sampling_period = 1. / sampling_rate;  # s
            sample_number = time_of_view / sampling_period;
            sampling_time = np.linspace(0, time_of_view, sample_number);

            carrier_frequency = S_Frequency = float(self.Frequency.toPlainText());
            amplitude = S_Amplitude = float(self.Amplitude.toPlainText());
            phase = 0;

            quantizing_bits = 4;
            quantizing_levels = 2 ** quantizing_bits / 2;
            quantizing_step = 1. / quantizing_levels;

            def analog_signal(time_point):
                return amplitude * np.exp(2 * np.pi * carrier_frequency * time_point + phase);

            sampling_signal = analog_signal(sampling_time);
            quantizing_signal = np.round(sampling_signal / quantizing_step) * quantizing_step;

            fig = plt.figure()
            plt.plot(analog_time, analog_signal(analog_time));
            # plt.stem (sampling_time, sampling_signal);
            plt.stem(sampling_time, quantizing_signal, linefmt='r-', markerfmt='rs', basefmt='r-');
            plt.title("Sampling")
            plt.xlabel("Time")
            plt.ylabel("Amplitude")

            plt.show()
            signal =0

        elif(signal == 'Sin'):

            time_of_view = 1.;  # s.
            analog_time = np.linspace(0, time_of_view, 10e5);  # s.

            sampling_rate = S_Sampling_Rate = float(self.SR.toPlainText());  # Hz
            sampling_period = 1. / sampling_rate;  # s

            carrier_frequency = S_Frequency = float(self.Frequency.toPlainText());
            amplitude = S_Amplitude = float(self.Amplitude.toPlainText());
            amplitude = 1;
            phase = 0;

            quantizing_bits = 4;
            quantizing_levels = 2 ** quantizing_bits / 2;
            quantizing_step = 1. / quantizing_levels;

            def analog_signal(time_point):
                return amplitude * np.sin(2 * np.pi * carrier_frequency * time_point + phase);

            sampling_signal = analog_signal(sampling_time);
            quantizing_signal = np.round(sampling_signal / quantizing_step) * quantizing_step;

            fig = plt.figure()
            plt.plot(analog_time, analog_signal(analog_time));
            # plt.stem (sampling_time, sampling_signal);
            plt.stem(sampling_time, quantizing_signal, linefmt='r-', markerfmt='rs', basefmt='r-');
            plt.title("Sampling")
            plt.xlabel("Time")
            plt.ylabel("Amplitude")

            plt.show()
            signal =0

        elif(signal == 'Cos'):

            time_of_view = 1.;  # s.
            analog_time = np.linspace(0, time_of_view, 10e5);  # s.

            sampling_rate = S_Sampling_Rate = float(self.SR.toPlainText());  # Hz
            sampling_period = 1. / sampling_rate;  # s
            sample_number = time_of_view / sampling_period;
            sampling_time = np.linspace(0, time_of_view, sample_number);


            carrier_frequency = S_Frequency = float(self.Frequency.toPlainText());
            amplitude = S_Amplitude = float(self.Amplitude.toPlainText());
            phase = 0;

            quantizing_bits = 4;
            quantizing_levels = 2 ** quantizing_bits / 2;
            quantizing_step = 1. / quantizing_levels;

            def analog_signal(time_point):
                return amplitude * np.cos(2 * np.pi * carrier_frequency * time_point + phase);

            sampling_signal = analog_signal(sampling_time);
            quantizing_signal = np.round(sampling_signal / quantizing_step) * quantizing_step;

            fig = plt.figure()
            plt.plot(analog_time, analog_signal(analog_time));
            # plt.stem (sampling_time, sampling_signal);
            plt.stem(sampling_time, quantizing_signal, linefmt='r-', markerfmt='rs', basefmt='r-');
            plt.title("Sampling")
            plt.xlabel("Time")
            plt.ylabel("Amplitude")

            plt.show()
            signal = 0
        elif(signal == 0):
            print('No signal')


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Sample = QtWidgets.QMainWindow()
    ui = Ui_Sample()
    ui.setupUi(Sample)
    Sample.show()
    sys.exit(app.exec_())


