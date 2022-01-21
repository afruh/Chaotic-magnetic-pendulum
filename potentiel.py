import numpy as np
from constante import *

## Calcul du Potentiel
def h(x,y):
    return d+H*(1-np.sqrt(1-(x**2+y**2)/H**2))

def Vmag(x,y,MM):
    S=0
    for k in range(len(MM)):
        S += MM[k][2]/((MM[k][0]-x)**2+(MM[k][1]-y)**2+h(x,y)**2)**(3/2)
    return +mu0*(moment_magn**2)*S/2/np.pi

def V(x,y,MM):
    return  Vmag(x,y,MM)+h(x,y)*m*g

