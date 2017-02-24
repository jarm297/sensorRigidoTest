# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rigidoBotonesConexion.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!


import socket
import sys
import binascii
import threading
import numpy as np
import socket
import scipy.ndimage
import sys, struct
#from pylab import *
import time
import sqlite3
#ion()

maxint = 2 ** (struct.Struct('i').size * 8 - 1) - 1
sys.setrecursionlimit(maxint)

class Ui_MainWindow(object):
    def __init__(self):
        print("init")
        self.vectorDatosDistribucionPresion = []
        self.vectorDesencriptado = []
        self.iniciaTramaDeDatos = False
        self.columnas = 48;
        self.filas = 48;
        matriz = [[0 for x in range(self.columnas)] for x in range(self.filas)] 
        matriz[0][0] = 255
        self.sensorConnectionStatus = False
        self.connectionRequest = False
        
    def socketConnection(self):
        
        self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        #Sensor 2
        self.UDP_IP = "192.168.0.124"
        self.UDP_IP_CLIENT = "192.168.0.151"
        self.UDP_PORT_CLIENT = 2233
        self.UDP_PORT = 10002
        print("escuchando...", self.UDP_IP, self.UDP_PORT)
        self.s.bind((self.UDP_IP, self.UDP_PORT))
        self.campoSensor1Creado = False

        for i in range(3):            
            time.sleep(2)
            self.s.sendto(bytes('*','utf-8'), (self.UDP_IP_CLIENT, self.UDP_PORT_CLIENT))
            #self.sc.send(('*').encode())
            print("conecto")
        self.connectionRequest = False
        self.sensorConnectionStatus = True
        self.sqlDataBase()
        
    def sqlDataBase(self):
        print('sql database')
        self.conn = sqlite3.connect('distribucionPresionSensorRigido.db', timeout=10)
        self.c = self.conn.cursor()
        # Create table
        self.c.execute('''CREATE TABLE IF NOT EXISTS sensorRigido
                     (id text, data real, connectionStatus text)''')
        # Insert a row of data
        for row in self.c.execute("SELECT * FROM sensorRigido WHERE 1"):
            if row[0] == '1':
                self.campoSensor1Creado = True

        if self.campoSensor1Creado == False:
            self.campoSensor1Creado = True
            self.c.execute("INSERT INTO sensorRigido VALUES ('1','initValue sensor 1','True')")
        self.c.execute("UPDATE `sensorRigido` SET `connectionStatus` = '%s' WHERE `id`='1'" % 'True')
        self.conn.commit()
        
    def desencriptarVector(self,vector):
        n = len(vector);
        fil = 0;
        col = 0;
        matriz = [[0 for x in range(self.columnas)] for x in range(self.filas)];
        banderacero = 0;
        for x in range(0, n):
            datos = vector[x];
            if datos == 0:
                banderacero = 1;
            elif datos == 255:
                return matriz;
            else:
                if banderacero == 1:
                    for k in range (0, datos):
                        if col == self.columnas:
                            col = 0;
                            fil = fil + 1;
                            if fil > self.filas:
                                return matriz;
                            matriz[fil][col] = 0;
                        col = col + 1;
                else:
                    if col >= self.columnas:
                        col = 0;
                        fil = fil + 1;
                        if fil >= self.filas:
                            return matriz;
                    matriz[fil][col] = datos;
                    col = col + 1;
                banderacero = 0;
                
    def recibeDatos(self):

        while True:
            for row in self.c.execute("SELECT * FROM sensorRigido WHERE `id`='1'"):
                if row[2] == 'True':
                    self.connectionRequest = True
                else:
                    self.sensorConnectionStatus = False
                    self.connectionRequest = False
                    #self.sc.close()
                    self.s.close()
                    print('cierra conexion')
            if self.sensorConnectionStatus == True:
                        
                buf = self.s.recv(6000)
                print(time.strftime("%H:%M:%S"))
                
                info = [buf[i:i+1] for i in range(0, len(buf), 1)]
                #try:
                for i in info:
                    valorDecimal = int(binascii.hexlify(i),16)
                    
                    if self.iniciaTramaDeDatos == False:
                      self.vectorDatosDistribucionPresion.append(valorDecimal)
                      
                      if valorDecimal == 255:
                        self.primerByte = self.vectorDatosDistribucionPresion[len(self.vectorDatosDistribucionPresion) - 3]
                        self.segundoByte = self.vectorDatosDistribucionPresion[len(self.vectorDatosDistribucionPresion) - 2]
                        self.numeroBytes = self.primerByte*255 + self.segundoByte

                        if(self.numeroBytes == len(self.vectorDatosDistribucionPresion) - 3):

                            self.vectorDatosDistribucionPresion=self.vectorDatosDistribucionPresion[:len(self.vectorDatosDistribucionPresion)-1]
                            self.vectorDatosDistribucionPresion=self.vectorDatosDistribucionPresion[:len(self.vectorDatosDistribucionPresion)-1]
                            self.vectorDatosDistribucionPresion=self.vectorDatosDistribucionPresion[:len(self.vectorDatosDistribucionPresion)-1]
                            self.vectorDatosDistribucionPresion.append(255)
                            self.vectorDesencriptado = self.desencriptarVector(self.vectorDatosDistribucionPresion)
                            self.dibujarDistribucionPresion(self.vectorDesencriptado)
                            self.vectorDatosDistribucionPresion = []
                            info = []
                            self.iniciaTramaDeDatos = False
                            self.s.sendto(bytes('*','utf-8'), (self.UDP_IP_CLIENT, self.UDP_PORT_CLIENT))
                            #self.sc.send(('*').encode())
                            break
                        else:
                            self.vectorDatosDistribucionPresion = []
                            info = []
                            self.iniciaTramaDeDatos = False
                            self.s.sendto(bytes('*','utf-8'), (self.UDP_IP_CLIENT, self.UDP_PORT_CLIENT))
                            #self.sc.send(('*').encode())
                            break

                    if valorDecimal == 255 and self.iniciaTramaDeDatos == False:
                        self.s.sendto(bytes('*','utf-8'), (self.UDP_IP_CLIENT, self.UDP_PORT_CLIENT))
                        #self.sc.send(('*').encode())
                        self.iniciaTramaDeDatos = True
                self.s.sendto(bytes('*','utf-8'), (self.UDP_IP_CLIENT, self.UDP_PORT_CLIENT))
                #self.sc.send(('*').encode())
            else:
                if self.connectionRequest == True:
                    self.socketConnection()
                print("sensor desconectado")
        
    def dibujarDistribucionPresion(self, matrizDistribucion):
##
      maximoValor = 0
      
      for i in range(self.filas):
        for j in range(self.columnas):
            matrizDistribucion[i][j] = matrizDistribucion[i][j]*1.5

            if matrizDistribucion[i][j] > 200:
                #matrizDistribucion[i][j] = 240
                pass
            if matrizDistribucion[i][j] >= maximoValor:
                maximoValor = matrizDistribucion[i][j]

      
      data = scipy.ndimage.zoom(matrizDistribucion, 1)
      print("inserta datos base de datos")
      #self.c.execute("UPDATE `sensorRigido` SET `data`= '%s', `connectionStatus` = '%s' WHERE `id`='1'" % (matrizDistribucion,'True'))
      self.c.execute("UPDATE `sensorRigido` SET `data`= '%s' WHERE `id`='1'" % matrizDistribucion)
      self.conn.commit()

    def conectarSensor(self):
        #try:
            self.socketConnection()
            self.recibeDatos()
            #threading.Timer(0.01, self.recibeDatos()).start()
            print("conecta conecta")
        #except:
            #print("No conecta")

if __name__ == "__main__":
    import sys
    ui = Ui_MainWindow()
    ui.conectarSensor()
    #ui.recibeDatos()

