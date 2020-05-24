# -*- coding: utf-8 -*-
"""
Created on Sat May 23 16:06:30 2020
https://www.youtube.com/watch?v=V4hbzn-Lh_Y 
metodo trapecio
@author: fonix
"""

import numpy as np  #IMPORTAR LIBRERIA NUMPY  ALMACENANDO EN LA VARIABLE np

def trapecio(x):  #crear una funcio con un parametro x
    y=pow(x,2)  #integral de x cuadrada
    return y  
#pedir datos al usuario desde la consola.
b=float(input("introduce  limite inferior: ")) # limite inderior almacenar en b
a=float(input("introduce limite superio: ")) #limite superior almacenar en a
n=int(input("introducie el numero de trapacios: ")) #numero de trapecio alcaenar en n
x=np.zeros([n+1]) #np.zeros lelna el vector en ceros para que no este en espacio vacio n=numero de trapeciosintroducidos por el usuario
h=(b-a)/n  # se divide entre el numero de trapecios h=altura

x[0]=a #limite superio 
x[n]=b #limite inferior
suma=0 #incializar valor 
for i in np.arange(1,n): #arange se utilizara para usar valores float
    x[i]=x[i-1]+h  #iteracion del valor de x 
    suma=suma+trapecio(x[i]) #llamar la funcino y que calule el valor que tiene la x[i]
    
inte = (h/2)*(trapecio(x[0])+2*suma+trapecio(x[n])) #la formula 
print("El resultado es : " ,inte)
    