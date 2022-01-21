import matplotlib as plm
import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate
import os
os.chdir('/home/arthur/Documents/Info/IPT/Chaotic-magnetic-pendulum/')

from constante import *
from trajectoire2 import *
from potentiel import *

## Positions des aimants fixes
def aimants_fixes(N,R):
    MM=[]
    for i in range(N):
        MM.append([R*np.cos(2*np.pi*i/(10)),R*np.sin(2*np.pi*i/(10)),-1])
    return MM

n=30000
Nbre_test=10
t = np.arange(0,dt*n,dt)
liste_Naimant=[k for k in range(3,17)]

for R in [2,3,4,5,6,7,8,9,10]:
    print(f"====test R: {R}====")
    liste_t=np.zeros((Nbre_test,len(liste_Naimant)))
    liste_trajectoire=np.zeros((Nbre_test,len(liste_Naimant),3,n))

    for i in range(Nbre_test):
        print (f"===test {i+1}===")
        for j in range(len(liste_Naimant)):
            d0=np.random.uniform(.08,.15,2)
            angle=np.random.uniform(0,2*np.pi)
            v0=np.random.uniform(-0.5,0.5,2)
            MM = aimants_fixes(liste_Naimant[j],R*1e-2)
            r = scipy.integrate.odeint(model, [d0[0]*np.cos(angle),d0[1]*np.sin(angle),v0[0],v0[1]] , t, args=(MM,),tfirst=True)
            r_N=np.sqrt(r[:,0]**2+r[:,1]**2)
            k=len(r)-1
            while r_N[k]<R*1e-2 :
                k-=1
            liste_t[i,j]= k*dt
    np.savetxt(f'liste_t_{R}_b.txt',liste_t)


# liste_mean = [np.mean(liste_t[:,j]) for j in range(len(liste_Naimant))]
# plt.plot(liste_Naimant,liste_mean)
# plt.xlabel("nombre aimant")
# plt.ylabel("temps")
# plt.figure()
# plt.plot( r[:,0],r[:,1],linewidth=.7,color='orange')
# plt.show()

















