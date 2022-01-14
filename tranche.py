import matplotlib as plm
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as mticker
import os
os.chdir('/home/arthur/Documents/Info/IPT/Chaotic-magnetic-pendulum/')

from constante import *
from trajectoire import *
from potentiel import *


# position des aimants fixes en m, (z = 0) et sens de la force (-1 attraction ou +1 répuslsion)

MM=[[0,0,-1]]
MM=[]
for i in range(10):
    MM.append([6e-2*np.cos(2*np.pi*i/(10)),6e-2*np.sin(2*np.pi*i/(10)),1])
for i in range(6):
    MM.append([3.5e-2*np.cos(2*np.pi*i/(6)),3.5e-2*np.sin(2*np.pi*i/(6)),1])


x=np.arange(-.2,.2,.001)
Z=V(x,0,MM)
plt.figure()
plt.plot(x,Z)
plt.show()