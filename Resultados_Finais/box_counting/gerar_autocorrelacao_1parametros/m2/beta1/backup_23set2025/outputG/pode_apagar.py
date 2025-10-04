import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("mean_autocorrelation.dat", float)

plt.plot(data[:,0], data[:,1])
plt.xlim(0, 0.002)
plt.ylim(0.4,1)
plt.show()