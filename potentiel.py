import numpy as np
from constante import *

## Calcul du Potentiel
def h(x,y):
    return H+d-(np.sqrt(H**2-x**2-y**2))

def Vmag(x,y,MM):
    S=0
    for k in range(len(MM)):
        S += km*MM[k][2]/((MM[k][0]-x)**2+(MM[k][1]-y)**2+h(x,y)**2)**(3/2)
    return +S/3

def V(x,y,MM):
    return Vmag(x,y,MM)+h(x,y)*m*g
