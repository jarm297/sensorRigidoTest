# -*- coding: utf-8 -*-
"""
Created on Fri May 19 18:16:38 2017

@author: User
"""

def calcularCOP(matriz):
    filas = 48
    columnas = 48
    ppres = 0 
    #ceros = [0,0]
    px = 0
    py = 0
    threshold_min = 40 # debajo de este valor, el dato se considera ruido
    num_pres = 0
    """Se calculan los valores de x y y del COP"""
    for i in range(0,filas):
        for j in range(0,columnas):
            if matriz[i][j] > threshold_min:
                px = px + matriz[i][j]*i
                py = py + matriz[i][j]*j
                ppres = ppres + matriz[i][j]
                num_pres = num_pres+1
    if ppres>0:
        px = px/ppres
        py = py/ppres
        max_pres = num_pres*255*1.5#Valor máximo de salida de todos 
        #Sensores presionados
        ppres = ppres/max_pres
    #ceros = [px,py]
    print(ppres)
    return (px,py,ppres)

def calcularVector(old,matriz):
    (px,py) = calcularCOP(matriz)
    cx = px - old[0]
    cy = py - old[1]
    print (cx,cy)   
    return (cx,cy) 