import numpy as np
## Initilisation et constantes

m = 4.73e-3/2 # masse de l'aimant en kg
g = 9.81 # m/s^2
dt = 0.01 # pas de temps
H = 0.85 # la longueur du fil en m
d = 0.01 # hauteur entre aimants fixes et point le plsu bas de l'aimant mobile en m
N = 17

kf1=0.01400026111242504 # force frottement

##Calcul force dipole dipole

B=60e-3 #norme du champ B à la surface de l'aimant
R=5.59E-3 #rayon aimant
l=4.81E-3 #hauteur aimant
V=np.pi*R**2*l
mu0=4*np.pi*1E-7

M=2*B/mu0*np.sqrt(R**2+l**2)/l
moment_magn=M*V

km=3*mu0*moment_magn**2/np.pi/m # force magnétique
