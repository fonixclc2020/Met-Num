# -*- coding: utf-8 -*-
"""
Created on Sun May 24 00:00:02 2020

@author: fonix
"""

import numpy as np
import matplotlib.pyplot as plt

def trap(n,x,fx,t):
    suma=0
    for i in range(1,n):
        suma=suma+fx[i]
    I=(x[n]-x[0])*(fx[0]+2*suma+fx[n])/(2*t)
    return I
num= int(input("numeor de datos a analizae "))
h = float(input("ancho de los trapecios "))
n=num
x=np.zeros([n])
fx=np.zeros([n])
print("introducr datos")

for i in range(0,n):
    x[i]=input("x["+str(i)+"] ")
    fx[i]=input("fx["+str(i)+"] ")
    
n=num-1
t=(x[n]-x[0])/h
print ("el valor de la integracion es " ,trap(n,x,fx,t))
plt.plot(x,fx)
plt.ylabel("F(x)")
plt.xlabel("X")
plt.show()