import time
import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate
import os
os.chdir('/home/arthur/Documents/Info/IPT/Chaotic-magnetic-pendulum/')

from constante import *
from trajectoire2 import *
from trajectoire import *
from potentiel import *



# position des aimants fixes en m, (z = 0) et sens de la force (-1 attraction ou +1 répuslsion)

MM=[[0,0,-1]]
MM=[]
for i in range(8):
    MM.append([5e-2*np.cos(2*np.pi*i/(10)),5e-2*np.sin(2*np.pi*i/(10)),1])
for i in range(5):
    MM.append([3.5e-2*np.cos(2*np.pi*i/(6)),3.5e-2*np.sin(2*np.pi*i/(6)),1])


n=20000

# initial condition
r0 = [.3,.3,-1,2]

# time points
dt=.01
t = np.arange(0,dt*n,dt)

# store solution
x = np.empty_like(t)
y = np.empty_like(t)
# record initial conditions
x[0] = r0[0]
y[0] = r0[1]


T1=time.time()
# solve ODE
# sol = scipy.integrate.solve_ivp(model,[0,dt*n],r0,method='BDF', args=(MM,),dense_output=True)
# r=sol.sol(t)
r = scipy.integrate.odeint(model, r0, t, args=(MM,),tfirst=True)
T2=time.time()
print(f"{n} etapes / odeint : {T2-T1}s ")

x1,y1 = r[:,0], r[:,1]


T1=time.time()
p,_,_,_,_,_=trajectoire1([r0[0],r0[1]],[r0[2],r0[3]],n,MM)
T2=time.time()
print(f"{n} etapes / main : {T2-T1}s ")

d=np.sqrt((x1-p[0,:])**2+(y1-p[1,:])**2)

d1=[]
d2=[]
for k in range(len(x1)-1):
    d1.append((x1[k+1]-x1[k])**2+(y1[k+1]-y1[k])**2)
    d2.append((p[0,k+1]-p[0,k])**2+(p[1,k+1]-p[1,k])**2)
plt.figure()
plt.plot(x1[:10000],y1[:10000],label='odeint')
#plt.plot(p[0,:10000],p[1,:10000],label='à la main')
plt.legend()
plt.figure()
plt.plot(d[10000:17500])
plt.figure()
plt.plot(d1[10000:17500])
plt.plot(d2[10000:17500])
plt.show()

