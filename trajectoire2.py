import numpy as np
from constante import *
from potentiel import *
from scipy.integrate import odeint


def model(t,r,MM):
    x = r[0]
    y = r[1]
    dxdt = r[2]
    dydt = r[3]
    x_m,y_m=0,0
    for Mk in MM :
        rk = np.sqrt((Mk[0]-x)**2 + (Mk[1]-y)**2 + h(x,y)**2)
        x_m+=Mk[2]*(x-Mk[0])/rk**4
        y_m+=Mk[2]*(y-Mk[1])/rk**4
    dxdt_2 = -g/H*x - kf1*dxdt + km*x_m
    dydt_2 = -g/H*y-kf1*dydt + km*y_m
    drdt = [dxdt,dydt,dxdt_2,dydt_2]
    return drdt


