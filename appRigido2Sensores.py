# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rigidoBotonesConexion.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from mpl_toolkits.axes_grid1 import make_axes_locatable, axes_size
import socket
import sys
import binascii
import threading
import numpy as np
import socket
import scipy.ndimage
import sys, struct
from pylab import *
import time
import sqlite3
import ast
import time
ion()

maxint = 2 ** (struct.Struct('i').size * 8 - 1) - 1
sys.setrecursionlimit(maxint)

class Ui_MainWindow(object):
    def __init__(self):
        print("init")
        self.fig = plt.figure(facecolor='#222222',figsize=(18,9))
        self.fig.set_size_inches(18,9)
        ax = plt.Axes(self.fig, [0., 0., 1., 1.])
        ax.set_axis_off()
        self.fig.add_axes(ax)
        self.fig.canvas.draw()
        #self.fig.canvas.toolbar.pack_forget()
        #plt.show(block=False)
        self.vectorDatosDistribucionPresion = []
        self.vectorDesencriptado = []
        self.iniciaTramaDeDatos = False
        self.columnas = 48;
        self.filas = 48;
        axis = plt.gca()
        axis.get_xaxis().set_visible(False)
        axis.get_yaxis().set_visible(False)
        matriz = [[0 for x in range(self.columnas)] for x in range(self.filas)] 
        matriz[0][0] = 255
        matrizSensor2 = [[0 for x in range(self.columnas)] for x in range(self.filas)] 
        #matrizSensor2[0][0] = 255
        matrizCompleta = np.concatenate((matriz,matrizSensor2),axis=1)
        matrizCompleta[0][0] = 255
        plt.set_cmap('jet')

        self.cbar = self.fig.colorbar(plt.imshow(matrizCompleta), ticks=[5,125,250], fraction=0.024, pad=0.02)
        self.cbar.ax.set_yticklabels(['Baja','Medio','Alto'])
        #divider = make_axes_locatable(plt.gca())
        #cax = divider.append_axes("right","5%",pad="3%")
        #plt.colorbar(plt.imshow(matrizCompleta),cax=cax)
        
        self.initData = scipy.ndimage.zoom(matrizCompleta, 3)
        #self.contour = plt.contour(data)
        
        self.imagen = plt.imshow(self.initData, interpolation = 'nearest')
        self.contador = 0
        self.contour_axis = plt.gca()
        self.sensorConectado = False
        self.defaultNumberOfPlatforms = 2
        self.numberOfPlatforms = 2
        self.intensityAdjustment = 250
        #plt.gca().invert_yaxis()
            
    def sqlDataBase(self):
        
        self.conn = sqlite3.connect('distribucionPresionSensorRigido.db', check_same_thread=False, timeout=10)
        self.c = self.conn.cursor()
        
    def setupUi(self, MainWindow):
        
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1522, 953)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(1520, 853))
        MainWindow.setMaximumSize(QtCore.QSize(1522, 853))
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.graphicsView_2 = QtWidgets.QGraphicsView(self.centralWidget)
        self.graphicsView_2.setGeometry(QtCore.QRect(-20, 0, 2041, 91))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graphicsView_2.sizePolicy().hasHeightForWidth())
        self.graphicsView_2.setSizePolicy(sizePolicy)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        self.graphicsView_2.setPalette(palette)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
        self.graphicsView_2.setBackgroundBrush(brush)
        self.graphicsView_2.setObjectName("graphicsView_2")

        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(1260, 18, 270, 61))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("/Applications/XAMPP/xamppfiles/htdocs/sensorRigido_UDP_Protocol/img/logoGIBIC.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")

        self.label_1 = QtWidgets.QLabel(self.centralWidget)
        self.label_1.setGeometry(QtCore.QRect(675, 10, 311, 71))
        self.label_1.setText("Sensor de presión")
        self.label_1.setStyleSheet("background-color: black; color:white; font size: 28pt; font-size: 22pt;")
        self.label_1.setScaledContents(True)
        self.label_1.setObjectName("label_1")

        self.gridLayoutWidget = QtWidgets.QWidget(self.centralWidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(30, 100, 1451, 751))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        
        canvas = FigureCanvas(self.fig)
        self.gridLayout.addWidget(canvas)
            
        self.gridLayout.setContentsMargins(5, 5, 5, 5)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")

        self.msg = QtWidgets.QMessageBox()
        self.msg.setIcon(QtWidgets.QMessageBox.Information)
        self.msg.setText("Conectando sensor")
        self.msg.setStandardButtons(QtWidgets.QMessageBox.Ok) 

        self.msg1 = QtWidgets.QMessageBox()
        self.msg1.setIcon(QtWidgets.QMessageBox.Information)
        self.msg1.setText("Sensor desconectado")
        self.msg1.setStandardButtons(QtWidgets.QMessageBox.Ok) 

        self.sl = QtWidgets.QSlider(Qt.Horizontal, self.centralWidget)
        self.sl.setMinimum(150)
        self.sl.setMaximum(250)
        self.sl.setValue(20)
        self.sl.setGeometry(QtCore.QRect(1300, 93, 200, 31))
        self.sl.setTickPosition(QtWidgets.QSlider.TicksBelow)

        # Radio button
        #self.radioButton = QtWidgets.QRadioButton(self.centralWidget)
        #self.radioButton.setStyleSheet("background-color: black")
        #self.radioButton.setChecked(True)
        #self.radioButton.setGeometry(QtCore.QRect(175, 55, 20, 20))
        #self.radioButton.setObjectName("radioButton1")

        #self.radioButton_1 = QtWidgets.QRadioButton(self.centralWidget)
        #self.radioButton_1.setStyleSheet("background-color: black")
        #self.radioButton_1.setChecked(True)
        #self.radioButton_1.setGeometry(QtCore.QRect(205, 55, 20, 20))
        #self.radioButton_1.setObjectName("radioButton2")

        #self.radioButton_2 = QtWidgets.QRadioButton(self.centralWidget)
        #self.radioButton_2.setStyleSheet("background-color: black")
        #self.radioButton_2.setChecked(True)
        #self.radioButton_2.setGeometry(QtCore.QRect(235, 55, 20, 20))
        #self.radioButton_2.setObjectName("radioButton3")

        # Radio button group
        #self.groupRadioButton = QtWidgets.QButtonGroup()
        #self.groupRadioButton.addButton(self.radioButton)
        #self.groupRadioButton.addButton(self.radioButton_1)
        #self.groupRadioButton.addButton(self.radioButton_2)  
        #self.groupRadioButton.setExclusive(False)    

        # Push button
        self.pushButton = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton.setStyleSheet("background-color: red; border-style: outset; border-width: 1px; border-radius: 10px; border-color: beige; padding: 6px;")
        self.pushButton.setGeometry(QtCore.QRect(175, 35, 20, 20))
        self.pushButton.setObjectName("pushButton")

        self.pushButton_1 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_1.setStyleSheet("background-color: red; border-style: outset; border-width: 1px; border-radius: 10px; border-color: beige; padding: 6px;")
        self.pushButton_1.setGeometry(QtCore.QRect(205, 35, 20, 20))
        self.pushButton_1.setObjectName("pushButton1")

        self.pushButton_3 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_3.setStyleSheet("background-color: red; border-style: outset; border-width: 1px; border-radius: 10px; border-color: beige; padding: 6px;")
        self.pushButton_3.setGeometry(QtCore.QRect(235, 35, 20, 20))
        self.pushButton_3.setObjectName("pushButton1")

        self.pushButton_2 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_2.setStyleSheet("background-color: gainsboro; color: black; color:black;border-radius: 10px;")
        self.pushButton_2.setGeometry(QtCore.QRect(10, 30, 140, 32))
        self.pushButton_2.setObjectName("pushButton_2")

        self.spinBox = QtWidgets.QSpinBox(self.centralWidget)
        self.spinBox.setGeometry(QtCore.QRect(195, 93, 48, 31))
        self.spinBox.setMinimum(1)
        self.spinBox.setMaximum(3)
        self.spinBox.setValue(3)
        self.spinBox.setObjectName("spinBox")
        self.spinBox.setStyleSheet("border-radius: 2px;")

        self.label_2 = QtWidgets.QLabel(self.centralWidget)
        self.label_2.setGeometry(QtCore.QRect(35, 100, 151, 16))
        self.label_2.setObjectName("label_2")
        self.label_2.setStyleSheet("color:white;")

        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "GIBIC group"))
        self.pushButton.setText(_translate("MainWindow", ""))
        self.pushButton_2.clicked.connect(self.conectarSensor)
        
        self.pushButton_2.setText(_translate("MainWindow", "Conectar sensor"))
        self.label_2.setText(_translate("MainWindow", "Número de plataformas:"))
        self.spinBox.valueChanged.connect(self.valueChangedSpinBox)
        self.sl.valueChanged.connect(self.valuechangeSlider)
        #self.groupRadioButton.buttonClicked[int].connect(self.ButtonGroupClicked)

    #def ButtonGroupClicked(self,clicked):
        #print("radio button clicked",clicked*(-1))

    def valueChangedSpinBox(self):

        self.numberOfPlatforms = self.spinBox.value()
        if self.numberOfPlatforms == 1:

            #self.radioButton.setVisible(True)
            #self.radioButton_1.setVisible(False)
            #self.radioButton_2.setVisible(False)

            self.pushButton.setVisible(True)
            self.pushButton_1.setVisible(False)
            self.pushButton_3.setVisible(False)

            self.pushButton.setStyleSheet("background-color: red; border-radius: 10px;")
            self.pushButton_1.setStyleSheet("background-color: green; border-radius: 10px;")

            matriz = [[0 for x in range(self.columnas)] for x in range(self.filas)] 
            matriz[0][0] = 255
            data = scipy.ndimage.zoom(matriz, 3)
            self.imagen = plt.imshow(data, interpolation = 'nearest')
            self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 100, 951, 751))

            MainWindow.resize(1022, 953)
            MainWindow.setMinimumSize(QtCore.QSize(1020, 853))
            MainWindow.setMaximumSize(QtCore.QSize(1022, 853))

        elif (self.numberOfPlatforms == 2):
            #self.radioButton.setVisible(True)
            #self.radioButton_1.setVisible(True)
            #self.radioButton_2.setVisible(False)

            self.pushButton.setVisible(True)
            self.pushButton_1.setVisible(True)
            self.pushButton_3.setVisible(False)

            #self.radioButton_2.setVisible(False)
            self.pushButton.setStyleSheet("background-color: green; border-radius: 10px;")
            self.pushButton_1.setStyleSheet("background-color: green; border-radius: 10px;")

            matriz = [[0 for x in range(self.columnas)] for x in range(self.filas)] 
            matriz[0][0] = 255
            matrizSensor2 = [[0 for x in range(self.columnas)] for x in range(self.filas)] 
            matrizCompleta = np.concatenate((matriz,matrizSensor2),axis=1)
            matrizCompleta[0][0] = 255
            data = scipy.ndimage.zoom(matrizCompleta, 3)
            self.imagen = plt.imshow(data, interpolation = 'nearest')
            self.imagen.set_data(data)
            self.gridLayoutWidget.setGeometry(QtCore.QRect(30, 100, 1451, 751))

            MainWindow.resize(1522, 953)
            MainWindow.setMinimumSize(QtCore.QSize(1520, 853))
            MainWindow.setMaximumSize(QtCore.QSize(1522, 853))
        elif (self.numberOfPlatforms == 3):

            #self.radioButton.setVisible(True)
            #self.radioButton_1.setVisible(True)
            #self.radioButton_2.setVisible(True)

            self.pushButton.setVisible(True)
            self.pushButton_1.setVisible(True)
            self.pushButton_3.setVisible(True)

            self.pushButton.setStyleSheet("background-color: green; border-radius: 10px;")
            self.pushButton_1.setStyleSheet("background-color: green; border-radius: 10px;")

            matriz = [[0 for x in range(self.columnas)] for x in range(self.filas)] 
            matriz[0][0] = 255
            matrizSensor2 = [[0 for x in range(self.columnas)] for x in range(self.filas)] 
            matrizCompleta = np.concatenate((matriz,matrizSensor2),axis=1)
            matrizCompleta[0][0] = 255
            data = scipy.ndimage.zoom(matrizCompleta, 3)
            self.imagen = plt.imshow(data, interpolation = 'nearest')
            self.imagen.set_data(data)
            self.gridLayoutWidget.setGeometry(QtCore.QRect(30, 100, 1451, 751))

            MainWindow.resize(1022, 953)
            MainWindow.setMinimumSize(QtCore.QSize(1520, 853))
            MainWindow.setMaximumSize(QtCore.QSize(1522, 853))

    def valuechangeSlider(self):
        print("value change slider")
        print(self.sl.value())
        self.intensityAdjustment = self.sl.value()

    def recibeDatos(self):

        self.dibujarDistribucionPresion(self.vectorDesencriptado)
        #print(time.strftime("%H:%M:%S"))
        threading.Timer(0.01, self.recibeDatos).start()

        
    def dibujarDistribucionPresion(self, matrizDistribucion):
        figure(1)
        
        plt.set_cmap('jet')
        #for row in self.c.execute("SELECT * FROM sensorRigido WHERE `id`='1'"):
        for row in self.c.execute("SELECT * FROM sensorRigido WHERE 1"):
          if row[0] == '1':
              datosSensor1 = row[1]
          if row[0] == '2':
              datosSensor2 = row[1]
##        try:
        matrizSensor1 = ast.literal_eval(datosSensor1)
        
        matrizSensor2 = ast.literal_eval(datosSensor2)

        rotate_imgMatriz1 = scipy.ndimage.rotate(matrizSensor1, 0)
        
        rotate_imgMatriz2 = scipy.ndimage.rotate(matrizSensor2, 180)

        matriz2espejo = np.array(rotate_imgMatriz2)
        matriz2espejo = matriz2espejo[::-1,:]
        matriz2espejo = matriz2espejo.tolist()

        matriz1espejo = np.array(rotate_imgMatriz1)
        matriz1espejo = matriz1espejo[:,::-1]
        matriz1espejo = matriz1espejo.tolist()

        matrizCompleta = np.concatenate((matriz1espejo, matriz2espejo), axis=1)
        for i in range(48):
            for j in range(96):
                if matrizCompleta[i][j] > 200:
                    matrizCompleta[i][j] = self.intensityAdjustment

        if self.numberOfPlatforms == 1:
            data = scipy.ndimage.zoom(matriz2espejo, 5)
            self.imagen.set_data(data)
        elif self.numberOfPlatforms == 2:
            print('plot 1')
            dataDatosCompletos = scipy.ndimage.zoom(matrizCompleta, 5)
            self.imagen.set_data(dataDatosCompletos)
        elif self.numberOfPlatforms == 3:
            dataDatosCompletos = scipy.ndimage.zoom(matrizCompleta, 5)
            self.imagen.set_data(dataDatosCompletos)

        
    def conectarSensor(self):
##        try:
        if(self.sensorConectado == False):
            self.sensorConectado = True
            self.sqlDataBase()
            threading.Timer(0.01, self.recibeDatos).start()

            try:
                self.c.execute("UPDATE `sensorRigido` SET `connectionStatus` = '%s' WHERE `id`='1'" % 'True')
                self.c.execute("UPDATE `sensorRigido` SET `connectionStatus` = '%s' WHERE `id`='2'" % 'True')

                self.pushButton.setStyleSheet("background-color: blue; border-style: outset; border-width: 1px; border-radius: 10px; border-color: beige; padding: 6px;")
                self.pushButton_1.setStyleSheet("background-color: blue; border-style: outset; border-width: 1px; border-radius: 10px; border-color: beige; padding: 6px;")
                self.pushButton_3.setStyleSheet("background-color: blue; border-style: outset; border-width: 1px; border-radius: 10px; border-color: beige; padding: 6px;")

                self.pushButton.setStyleSheet("background-color: green; border-style: outset; border-width: 1px; border-radius: 10px; border-color: beige; padding: 6px;")
                self.pushButton_1.setStyleSheet("background-color: green; border-style: outset; border-width: 1px; border-radius: 10px; border-color: beige; padding: 6px;")
                self.pushButton_3.setStyleSheet("background-color: green; border-style: outset; border-width: 1px; border-radius: 10px; border-color: beige; padding: 6px;")
                #self.pushButton.setText("Sensor conectado")
                self.pushButton_2.setText("Desconectar sensor")
            except:
                pass
            print("Sensor conectado")
            self.conn.commit()

            self.msg.exec_()
            print("continua !!!")

        else:
            try:
                self.c.execute("UPDATE `sensorRigido` SET `connectionStatus` = '%s' WHERE `id`='1'" % 'False')
                self.c.execute("UPDATE `sensorRigido` SET `connectionStatus` = '%s' WHERE `id`='2'" % 'False')

                self.sensorConectado = False
                self.pushButton.setStyleSheet("background-color: red; border-style: outset; border-width: 1px; border-radius: 10px; border-color: beige; padding: 6px;")
                self.pushButton_1.setStyleSheet("background-color: red; border-style: outset; border-width: 1px; border-radius: 10px; border-color: beige; padding: 6px;")
                self.pushButton_3.setStyleSheet("background-color: red; border-style: outset; border-width: 1px; border-radius: 10px; border-color: beige; padding: 6px;")
                #self.pushButton.setText("Conectar")
                self.pushButton_2.setText("Conectar sensor")
            except:
                pass
                
            self.conn.commit()
            print("desconecta sensor")
                      

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setStyleSheet('QMainWindow{background-color: #222222; border:2px solid black;}')
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

