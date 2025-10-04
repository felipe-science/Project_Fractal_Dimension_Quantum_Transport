import numpy as np
import matplotlib.pyplot as plt
import scienceplots
from scipy.signal import find_peaks

#Parameters
parameters = np.loadtxt("gamma_alpha_beta.dat")
m_lis = parameters[:,0]
a_lis = parameters[:,1]
b_lis = parameters
gamma = parameters[:,3]

#beta1
data_m0_beta1_G = np.loadtxt("m0/beta1/G_m0_beta1/G18.dat", float)
data_m1_beta1_G = np.loadtxt("m1/beta1/G_beta1_m1/G2.dat", float)
data_m2_beta1_G = np.loadtxt("m2/beta1/G_m2_beta1/G1.dat", float)
data_m3_beta1_G = np.loadtxt("m3/beta1/G_m3_beta1/G5.dat", float)
data_m4_beta1_G = np.loadtxt("m4/beta1/G_beta1_m4/G26.dat", float)


E_m0_beta1 = data_m0_beta1_G[:,0]/gamma[0]
E_m1_beta1 = data_m1_beta1_G[:,0]/gamma[1]
E_m2_beta1 = data_m2_beta1_G[:,0]/gamma[2]
E_m3_beta1 = data_m3_beta1_G[:,0]/gamma[3]
E_m4_beta1 = data_m4_beta1_G[:,0]/gamma[4]

G_m0_beta1 = data_m0_beta1_G[:,1]
G_m1_beta1 = data_m1_beta1_G[:,1]
G_m2_beta1 = data_m2_beta1_G[:,1]
G_m3_beta1 = data_m3_beta1_G[:,1]
G_m4_beta1 = data_m4_beta1_G[:,1]


#Finds peaks
peaks0, _ = find_peaks(G_m0_beta1)
peaks1, _ = find_peaks(G_m1_beta1)
peaks2, _ = find_peaks(G_m2_beta1)
peaks3, _ = find_peaks(G_m3_beta1)
peaks4, _ = find_peaks(G_m4_beta1)


plt.style.use('science')
fig, axs = plt.subplots(5, 1, figsize=(6, 15))  # Ajuste o figsize conforme necessário

axs[0].plot(E_m0_beta1, G_m0_beta1)
axs[1].plot(E_m1_beta1, G_m1_beta1)
axs[2].plot(E_m2_beta1, G_m2_beta1)
axs[3].plot(E_m3_beta1, G_m3_beta1)
axs[4].plot(E_m4_beta1, G_m4_beta1)

axs[0].scatter(E_m0_beta1[peaks0], G_m0_beta1[peaks0], color='red', zorder=6)
axs[1].scatter(E_m1_beta1[peaks1], G_m1_beta1[peaks1], color='red', zorder=7)
axs[2].scatter(E_m2_beta1[peaks2], G_m2_beta1[peaks2], color='red', zorder=8)
axs[3].scatter(E_m3_beta1[peaks3], G_m3_beta1[peaks3], color='red', zorder=9)
axs[4].scatter(E_m4_beta1[peaks4], G_m4_beta1[peaks4], color='red', zorder=10)


for i in range(5):
    axs[i].set_xlim(-13,13)
    axs[i].set_xlabel(r"$E/\Gamma$", fontsize='18')
    axs[i].set_ylabel(r"$G(e²/h)$", fontsize='18')
    axs[i].tick_params(labelsize=15)
    axs[i].set_title(rf"m = {i}; $\Gamma = {round(gamma[i],5)}$", fontsize=30)
    axs[i].grid(True)

plt.tight_layout(h_pad=3.0)  # h_pad controla o espaçamento vertical entre os subplots
plt.savefig("fig_G_vs_E.png", dpi=200)
plt.show()


density = len(peaks4)/(abs(E_m4_beta1[0]-E_m4_beta1[-1]))
print(f"Density m0 = {density}")