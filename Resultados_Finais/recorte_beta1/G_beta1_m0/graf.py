import matplotlib.pyplot as plt
import numpy as np

data = np.loadtxt("G1.dat", float)

plt.plot(data[:,0], data[:,1])
plt.show()
