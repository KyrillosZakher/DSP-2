# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication,QMessageBox,QFileDialog
import scipy.io as sio
import numpy as np
import plotly
from plotly import tools
import plotly.graph_objs as go
plotly.offline.init_notebook_mode(connected=True)

class Ui_Show(object):
    def setupUi(self, Show):
        Show.setObjectName("Show")
        Show.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(Show)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(440, 30, 271, 511))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.textEdit = QtWidgets.QTextEdit(self.groupBox)
        self.textEdit.setGeometry(QtCore.QRect(80, 200, 111, 51))
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(self.groupBox)
        self.textEdit_2.setGeometry(QtCore.QRect(80, 70, 111, 51))
        self.textEdit_2.setObjectName("textEdit_2")
        self.textEdit_3 = QtWidgets.QTextEdit(self.groupBox)
        self.textEdit_3.setGeometry(QtCore.QRect(80, 330, 111, 51))
        self.textEdit_3.setObjectName("textEdit_3")
        self.Filter = QtWidgets.QPushButton(self.groupBox)
        self.Filter.setGeometry(QtCore.QRect(60, 440, 161, 51))
        self.Filter.setObjectName("Filter")
        self.Browse = QtWidgets.QPushButton(self.centralwidget)
        self.Browse.setGeometry(QtCore.QRect(10, 30, 401, 511))
        self.error_dialog = QtWidgets.QErrorMessage()
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.Browse.setFont(font)
        self.Browse.setObjectName("Browse")
        Show.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Show)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        Show.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Show)
        self.statusbar.setObjectName("statusbar")
        Show.setStatusBar(self.statusbar)

        self.retranslateUi(Show)
        QtCore.QMetaObject.connectSlotsByName(Show)

    def retranslateUi(self, Show):
        _translate = QtCore.QCoreApplication.translate
        Show.setWindowTitle(_translate("Show", "MainWindow"))
        self.groupBox.setTitle(_translate("Show", "Filter"))
        self.Filter.setText(_translate("Show", "Filter"))
        self.Browse.setText(_translate("Show", "Browse and Display"))
        self.Filter.setEnabled(False)
        self.Browse.clicked.connect(self.openFileNameDialog)
        self.Filter.clicked.connect(self.filter_callBack)

    def openFileNameDialog(self):
        global signal
        fileName, _ = QFileDialog.getOpenFileName(None,"QFileDialog.getOpenFileName()", "","All Files (*);;MatLab Files (*.mat)")
        if fileName:
            signal = sio.loadmat(fileName)
            self.Filter.setEnabled(True)
            signal = signal['val'][0,:]
            trace1 = go.Scatter(y=signal, marker={'color': 'red', 'size': "19"}, mode="lines", name='signal')
            data = go.Data([trace1])
            layout = go.Layout(title="Signal Displaying", xaxis={'title': 'Samples'}, yaxis={'title': 'Amplitude'})
            figure = go.Figure(data=data, layout=layout)
            plotly.offline.plot(figure)


    def filter_callBack(self):
         global signal
         try:
            first_parameter_filter = float(self.textEdit.toPlainText())
            Second_parameter_filter = float(self.textEdit_2.toPlainText())
            Third_parameter_filter = float(self.textEdit_3.toPlainText())
            signal_filtered = np.convolve([first_parameter_filter, Second_parameter_filter, Third_parameter_filter],
                                          signal)
            trace1 = go.Scatter(y=signal, marker={'color': 'red', 'size': "19"},
                                mode="lines", name='signal')
            trace2 = go.Scatter(
                y=signal_filtered, marker={'color': 'black', 'size': "19"},
                mode="lines", name='Filtered_Signal'
            )
            fig = tools.make_subplots(rows=2, cols=1)
            fig.append_trace(trace1, 1, 1)
            fig.append_trace(trace2, 2, 1)
            fig['layout'].update(height=1000, width=1000)
            plotly.offline.plot(fig)
         except ValueError:
             self.error_dialog.showMessage('There is a wrong number or there is an empty field')
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Show = QtWidgets.QMainWindow()
    ui = Ui_Show()
    ui.setupUi(Show)
    Show.show()
    sys.exit(app.exec_())

