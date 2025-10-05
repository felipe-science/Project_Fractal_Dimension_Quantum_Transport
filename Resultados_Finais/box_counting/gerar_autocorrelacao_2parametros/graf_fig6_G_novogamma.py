import numpy as np
import matplotlib.pyplot as plt
import scienceplots
from scipy.signal import find_peaks

data = np.loadtxt("parametersG_beta1.dat", float)

listm = data[:,0]
gamma = data[:,3]

gamma = [0.00015178029667030186, 0.0001740, 0.000186361, 0.00014704, 0.00012854]


plt.style.use(['science'])
fig, axes = plt.subplots(5, 1, figsize=(6, 10), sharey=False)

plt.rcParams.update({'axes.labelsize': 20})  # x e y labels
plt.rcParams.update({'axes.titlesize': 20})  # títulos

data0 = np.loadtxt("m0/beta1/outputGn/G8.dat")
data1 = np.loadtxt("m1/beta1/outputG/G20.dat")
data2 = np.loadtxt("m2/beta1/outputG/G11.dat")
data3 = np.loadtxt("m3/beta1/outputG/G28.dat")
data4 = np.loadtxt("m4/beta1/outputG/G1.dat")

E0, G0 = data0[:,0], data0[:,1]
E1, G1 = data1[:,0], data1[:,1]
E2, G2 = data2[:,0], data2[:,1]
E3, G3 = data3[:,0], data3[:,1]
E4, G4 = data4[:,0], data4[:,1]

peaks0, _ = find_peaks(G0)
peaks1, _ = find_peaks(G1)
peaks2, _ = find_peaks(G2)
peaks3, _ = find_peaks(G3)
peaks4, _ = find_peaks(G4)

axes[0].plot(E0/gamma[0], G0, zorder=0)
axes[0].scatter(E0[peaks0]/gamma[0], G0[peaks0], color='red', zorder=1)
axes[0].set_title(rf"$m = 0$; $\Gamma = {round(gamma[0],6)}$")
axes[0].set_xlabel(r"$E$/$\Gamma$", fontsize=16)
axes[0].set_ylabel(r"$G(e/h)$", fontsize=16)

axes[1].plot(E1/gamma[1], G1, zorder=0)
axes[1].scatter(E1[peaks1]/gamma[1], G1[peaks1], color='red', zorder=1)
axes[1].set_title(rf"$m = 1$ $\Gamma = {round(gamma[1],6)}$")
axes[1].set_xlabel(r"$E$/$\Gamma$", fontsize=16)
axes[1].set_ylabel(r"$G(e/h)$", fontsize=16)

axes[2].plot(E2/gamma[2], G2, zorder=0)
axes[2].scatter(E2[peaks2]/gamma[2], G2[peaks2], color='red', zorder=1)
axes[2].set_title(rf"$m = 2$; $\Gamma = {round(gamma[2],6)}$")
axes[2].set_xlabel(r"$E$/$\Gamma$", fontsize=16)
axes[2].set_ylabel(r"$G(e/h)$", fontsize=16)

axes[3].plot(E3/gamma[3], G3, zorder=0)
axes[3].scatter(E3[peaks3]/gamma[3], G3[peaks3], color='red', zorder=1)
axes[3].set_title(rf"$m = 3$; $\Gamma = {round(gamma[3],6)}$")
axes[3].set_xlabel(r"$E$/$\Gamma$", fontsize=16)
axes[3].set_ylabel(r"$G(e/h)$", fontsize=16)

axes[4].plot(E4/gamma[4], G4, zorder=0)
axes[4].scatter(E4[peaks4]/gamma[4], G4[peaks4], color='red', zorder=1)
axes[4].set_title(rf"$m = 4$; $\Gamma = {round(gamma[4],6)}$")
axes[4].set_xlabel(r"$E$/$\Gamma$", fontsize=16)
axes[4].set_ylabel(r"$G(e/h)$", fontsize=16)

fig.subplots_adjust(hspace=1.0)  # aumenta o espaçamento entre os subplots

plt.savefig("fig_grid.png", dpi=600)
plt.show()

density0 = len(peaks0)/(abs(E0[0]-E0[-1])/gamma[0])
density1 = len(peaks1)/(abs(E1[0]-E1[-1])/gamma[1])
density2 = len(peaks2)/(abs(E2[0]-E2[-1])/gamma[2])
density3 = len(peaks3)/(abs(E3[0]-E3[-1])/gamma[3])
density4 = len(peaks4)/(abs(E4[0]-E4[-1])/gamma[4])

print(f"d0 = {density0}")
print(f"d1 = {density1}")
print(f"d2 = {density2}")
print(f"d3 = {density3}")
print(f"d4 = {density4}")