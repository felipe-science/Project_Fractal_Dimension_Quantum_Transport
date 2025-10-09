import numpy as np
import matplotlib.pyplot as plt
import scienceplots

data0 = np.loadtxt("m0/outputG/G0.dat", float)
data1 = np.loadtxt("m1/outputG/G0.dat", float)
data2 = np.loadtxt("m2/outputG/G0.dat", float)
data3 = np.loadtxt("m3/outputG/G0.dat", float)
data3 = np.loadtxt("m4/outputG/G0.dat", float)

plt.style.use(['science'])
fig, axes = plt.subplots(5, 1, figsize=(6, 10), sharey=False)

axes[0].plot(data0[:,0], data0[:,1], linewidth=0.5)
axes[0].set_xlim(-0.05, 0.05)
#axes[0].set_ylim(7, 12.5)

axes[1].plot(data1[:,0], data1[:,1], linewidth=0.5)
axes[1].set_xlim(-0.05, 0.05)
#axes[1].set_ylim(5.5, 13)

axes[2].plot(data2[:,0], data2[:,1], linewidth=0.5)
axes[2].set_xlim(-0.05, 0.05)
#axes[2].set_ylim(12.5, 18)

axes[3].plot(data2[:,0], data2[:,1], linewidth=0.5)
axes[3].set_xlim(-0.05, 0.05)
#axes[2].set_ylim(5.5, 13)

axes[4].plot(data2[:,0], data2[:,1], linewidth=0.5)
axes[4].set_xlim(-0.05, 0.05)
#axes[2].set_ylim(5.5, 13)

plt.show()