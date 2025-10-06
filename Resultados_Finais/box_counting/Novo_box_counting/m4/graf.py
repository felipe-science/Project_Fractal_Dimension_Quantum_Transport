import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("outputG/G0.dat")
plt.plot(data[:,0], data[:,1])
plt.show()