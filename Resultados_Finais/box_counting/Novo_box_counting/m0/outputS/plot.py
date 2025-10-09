import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("S0.dat")
plt.plot(data[:,0], data[:,1])
plt.show()

ener = data[:,0]
newG = data[:,1]-6

plt.plot(data[:,0], newG)
plt.show()


f = open("newG.dat", "w")
for i in range(len(ener)):
    f.write(f"{ener[i]} {newG[i]}\n")
f.close()