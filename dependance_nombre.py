import matplotlib as plm
import matplotlib.pyplot as plt
import numpy as np
import os
os.chdir('/home/arthur/Documents/Info/IPT/Chaotic-magnetic-pendulum/')

from constante import *
from trajectoire import *
from potentiel import *

## Positions des aimants fixes
def aimants_fixes(N,R):
    MM=[]
    for i in range(N):
        MM.append([R*np.cos(2*np.pi*i/(10)),R*np.sin(2*np.pi*i/(10)),-1])
    return MM

n=30000
R=6e-2
Nbre_test=10
liste_Naimant=[k for k in range(3,10)]
#print(liste_N)

plt.figure()
liste_t=np.zeros((Nbre_test,len(liste_Naimant)))

for i in range(Nbre_test):
    for j in range(len(liste_Naimant)):
        (x,y)=np.random.uniform(7,10,2)
        (vx,vy)=np.random.uniform(-0.3,0.3,2)
        MM = aimants_fixes(liste_Naimant[j],R)
        p_N,V_N,A_N = trajectoire1([x,y], [vx,vy], n,MM)
        r_N=np.sqrt(p_N[0,:]**2+p_N[1,:]**2)
        k=n-1
        while r_N[k]<R :
            k-=1
        liste_t[i,j]= k
        #print (N,liste_t)

    plt.scatter(liste_Naimant,liste_t[i])
plt.show()















