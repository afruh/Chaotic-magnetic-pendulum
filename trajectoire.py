import numpy as np
from constante import *
from potentiel import *

def trajectoire1(pos, vit, n, MM):
    """pos et vit deux vecteurs de dimension 2 représentant la position initiale en cm, et la vitesse initale en m/s, n le nombre de points de la simulation"""

    p = np.zeros((3,n)) # vecteur contenant les positions successives
    p[0,0]=pos[0] *1e-2# x
    p[1,0]=pos[1] *1e-2# y
    p[2,0]= h(p[0,0],p[1,0])# z


    v= vit # on négliga la vitesse verticale, par rapport aux vitesses selon x et y
    V=np.zeros((2,n))
    V[0,0]=vit[0]
    V[1,0]=vit[1]

    A=np.zeros((2,n))
    Af=np.zeros(n-1)
    Am=np.zeros(n-1)
    Ag=np.zeros(n-1)

    for k in range (n-1):

        # calcul de l'accélération
        ag = [-g/H * p[0,k], -g/H * p[1,k]]
        af = [-kf1 * v[0], -kf1*v[1]]
        am=[0,0]
        a=[0,0]
        for Mk in MM :
            rk = np.sqrt((Mk[0]-p[0,k])**2 + (Mk[1]-p[1,k])**2 + p[2,k]**2)
            am[0]+=Mk[2]*km*(p[0,k]-Mk[0])/rk**4
            am[1]+=Mk[2]*km*(p[1,k]-Mk[1])/rk**4
            #print(am)
            #TODO revérifier les signes des forces

        #print(ag, af, am)

        a[0] = ag[0] + af[0] + am[0]
        a[1] = ag[1] + af[1] + am[1]
        A[0,k+1]=a[0]

        Am[k]=np.sqrt(am[0]**2+am[1]**2)
        Af[k]=np.sqrt(af[0]**2+af[1]**2)
        Ag[k]=np.sqrt(ag[0]**2+ag[1]**2)
        # a[2] = ag[1] + af[1] + am[1]

        # calcul de la vitesse
        #TODO changer la méthode d'intégration
        v[0]+= a[0]*dt
        v[1]+= a[1]*dt
        V[0,k+1] = v[0]
        V[1,k+1] = v[1]

        # calcul de la position
        p[0, k+1] = p[0, k] + v[0]*dt
        p[1, k+1] = p[1, k] + v[1]*dt
        #print(p[0,k+1], p[1,k+1])
        p[2, k+1] = h(p[0, k+1],p[1, k+1])

    return p,V, A ,Am,Af,Ag