import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("G_m4_n297.dat")
plt.plot(data[:,0], data[:,1])
plt.show()