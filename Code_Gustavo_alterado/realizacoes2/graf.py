import numpy as np
import matplotlib.pyplot as plt


data = np.loadtxt("outputG/G2.dat")

plt.plot(data[:,0], data[:,1])
plt.xlabel("Energy")
plt.ylabel("Conductance")
plt.show()

x = data[:,0]
y = data[:,1]

var = np.var(y)

print(f"variancia: {var}")