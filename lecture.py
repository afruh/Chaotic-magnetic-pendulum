import numpy as np
import os
os.chdir('/home/arthur/Documents/Info/IPT/Chaotic-magnetic-pendulum/')
for R in range(2,6):
    A=np.loadtxt(f'liste_t_{R}.txt')
    liste_mean = [np.mean(A[:,j]) for j in range(len(A[0]))]
    #plt.boxplot(A)
    plt.plot(range(1,14),liste_mean,label=f'R = {R}cm')
plt.legend()
plt.xlabel("nombre aimant")
plt.ylabel("temps")
plt.show()