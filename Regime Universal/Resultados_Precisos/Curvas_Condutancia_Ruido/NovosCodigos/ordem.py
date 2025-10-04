import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("buracos.dat")

x = data[:,0]
y = data[:,1]

plt.scatter(x,y)
plt.show()