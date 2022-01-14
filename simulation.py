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


n=28000

#p,V,A = trajectoire1([7.01,8.01], [0,0], n)
p2,V2,A2 = trajectoire1([6.5,6.5], [-.3,.3], n, MM)


fig,ax=plt.subplots()

saut=50
p2_b=np.zeros((2,len(p2[0])//saut))
for i in range(2):
    p2_b[i,:]=[p2[0,saut*k] for k in range(len(p2[0])//saut)]

Lmax = max(max(np.abs(p2_b[0,:])),max(np.abs(p2_b[1,:])))
Lmax += .01
x = np.linspace(-Lmax, Lmax, 1000)
y = np.linspace(-Lmax, Lmax, 1000)
X, Y = np.meshgrid(x, y)
Z=V(X,Y,MM)


potentiel = ax.imshow(Z,extent=[-Lmax,Lmax,-Lmax,Lmax],cmap='viridis')
cbar = plt.colorbar(potentiel)
ticks_loc = cbar.ax.get_yticks().tolist()
cbar.ax.yaxis.set_label_coords(-.9,.5)
cbar.ax.yaxis.set_major_locator(mticker.FixedLocator(ticks_loc))
#cbar.ax.set_yticklabels([label_format.format(x) for x in ticks_loc],fontsize=8)
 #cbar.ax.set_yticklabels([f'{i:.1e}' for i in cbar.get_ticks()])
cbar.set_label('énergie potentielle (J)', rotation=90)

ax.plot(p2[0,:], p2[1,:],label='Les 20 premières secondes',linewidth=.5,color='red')
# ax.plot(p2[0,:2000], p2[1,:2000],label='Les 20 premières secondes',linewidth=.5,color='red')
# ax.plot(p2[0,10000:12000], p2[1,10000:12000],label='entre 100 et 120 secondes',linewidth=.5,color='orange')
# ax.plot(p2[0,25000:], p2[1,25000:],label='Après 280 secondes',linewidth=.5,color='grey')
# ax.set_aspect('equal', adjustable='box')
#plt.plot(p[0,:], p[1,:])
for Mk in MM :
    plt.scatter(Mk[0], Mk[1],zorder=3,color='r')

plt.legend()
plt.show()
