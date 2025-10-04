import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt(f"G{0}.dat", float)

plt.plot(data[:,0], data[:,1])
plt.show()