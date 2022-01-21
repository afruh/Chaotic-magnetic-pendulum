import matplotlib as plm
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as mticker
import scipy.integrate
import os
os.chdir('/home/arthur/Documents/Info/IPT/Chaotic-magnetic-pendulum/')

from constante import *
from trajectoire2 import *
from potentiel import *


# position des aimants fixes en m, (z = 0) et sens de la force (-1 attraction ou +1 répuslsion)

MM=[[0,0,-1]]
MM=[]
N_aimant_c=16
for i in range(N_aimant_c):
    MM.append([8e-2*np.cos(2*np.pi*i/N_aimant_c),8e-2*np.sin(2*np.pi*i/N_aimant_c),1])
# N_aimant_c=8
# for i in range(N_aimant_c):
#     MM.append([3e-2*np.cos(2*np.pi*i/N_aimant_c),3e-2*np.sin(2*np.pi*i/N_aimant_c),1])


n=30000

# initial condition
r0 = [.1,.1,.7,-.7]

# time points
t = np.arange(0,dt*n,dt)

# store solution
x = np.empty_like(t)
y = np.empty_like(t)
# record initial conditions
x[0] = r0[0]
y[0] = r0[1]

# solve ODE
r = scipy.integrate.odeint(model, r0, t, args=(MM,),tfirst=True)
x = r[:,0]
y = r[:,1]


fig,ax=plt.subplots()

Lmax = max(max(np.abs(x[:])),max(np.abs(y[:])))
Lmax += .01
X = np.linspace(-Lmax, Lmax, 1000)
Y = np.linspace(-Lmax, Lmax, 1000)
X, Y = np.meshgrid(X, Y)
Z=V(X,Y,MM)


potentiel = ax.imshow(Z,extent=[-Lmax,Lmax,-Lmax,Lmax],cmap='viridis')
cbar = plt.colorbar(potentiel)
ticks_loc = cbar.ax.get_yticks().tolist()
cbar.ax.yaxis.set_label_coords(-.9,.5)
cbar.ax.yaxis.set_major_locator(mticker.FixedLocator(ticks_loc))
#cbar.ax.set_yticklabels([label_format.format(x) for x in ticks_loc],fontsize=8)
 #cbar.ax.set_yticklabels([f'{i:.1e}' for i in cbar.get_ticks()])
cbar.set_label('énergie potentielle (J)', rotation=90)

ax.plot(x, y,linewidth=.7,color='orange')

for Mk in MM :
    plt.scatter(Mk[0], Mk[1],alpha=.2,color='r',)

plt.legend()

x=np.arange(-.2,.2,.001)
Z=V(x,0,MM)
plt.figure()
plt.plot(x,Z)
x=np.arange(-.2,.2,.001)
y=np.arange(-.2,.2,.001)
Z=V(x,y,MM)
plt.figure()
plt.plot(x,Z)
plt.show()