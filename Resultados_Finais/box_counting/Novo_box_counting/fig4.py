import numpy as np
import matplotlib.pyplot as plt
import scienceplots

data0 = np.loadtxt("m0/outputG/G0.dat", float)
data1 = np.loadtxt("m1/outputG/G0.dat", float)
data2 = np.loadtxt("m2/outputG/G0.dat", float)
data3 = np.loadtxt("m3/outputG/G0.dat", float)
data4 = np.loadtxt("m4/outputG/G0.dat", float)

plt.style.use(['science'])
fig, axes = plt.subplots(5, 1, figsize=(6, 10), sharey=False)

axes[0].plot(data0[:,0], data0[:,1], linewidth=0.5)
axes[0].set_xlim(-0.05, 0.05)
axes[0].set_ylim(10, 15.5)
axes[0].set_xlabel(r"$E(eV)$", fontsize=16)
axes[0].set_ylabel(r"$G(e²/h)$", fontsize=16)

axes[1].plot(data1[:,0], data1[:,1], linewidth=0.5)
axes[1].set_xlim(-0.05, 0.05)
axes[1].set_ylim(7, 13)
axes[1].set_xlabel(r"$E(eV)$", fontsize=16)
axes[1].set_ylabel(r"$G(e²/h)$", fontsize=16)

axes[2].plot(data2[:,0], data2[:,1], linewidth=0.5)
axes[2].set_xlim(-0.05, 0.05)
axes[2].set_ylim(7, 12)
axes[2].set_xlabel(r"$E(eV)$", fontsize=16)
axes[2].set_ylabel(r"$G(e²/h)$", fontsize=16)

axes[3].plot(data3[:,0], data3[:,1], linewidth=0.5)
axes[3].set_xlim(-0.05, 0.05)
axes[3].set_ylim(3.5, 9.5)
axes[3].set_xlabel(r"$E(eV)$", fontsize=16)
axes[3].set_ylabel(r"$G(e²/h)$", fontsize=16)

axes[4].plot(data4[:,0], data4[:,1], linewidth=0.5)
axes[4].set_xlim(-0.05, 0.05)
#axes[4].set_ylim(10, 15.5)
axes[4].set_xlabel(r"$E(eV)$", fontsize=16)
axes[4].set_ylabel(r"$G(e²/h)$", fontsize=16)

plt.subplots_adjust(hspace=0.5)

for ax in axes:
    ax.tick_params(axis='both', which='major', labelsize=15)



plt.savefig("figfig.png", dpi=600)
plt.show()