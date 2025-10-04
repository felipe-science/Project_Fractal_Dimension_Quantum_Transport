import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("rmsG.dat")

plt.plot(data[:,0], data[:,1])
plt.scatter(data[:,0], data[:,1])
plt.axhline(y=0.74, color='black')
plt.show()