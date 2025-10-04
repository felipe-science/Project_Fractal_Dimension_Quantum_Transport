import numpy as np
import pylab as plt

# Carregar os dados
rmsG_m0_b1 = np.loadtxt("G_m0_b1.dat", float)
rmsG_m1_b1 = np.loadtxt("G_m1_b1.dat", float)
rmsG_m2_b1 = np.loadtxt("G_m2_b1.dat", float)
rmsG_m3_b1 = np.loadtxt("G_m3_b1.dat", float)
rmsG_m4_b1 = np.loadtxt("G_m4_b1.dat", float)

rmsG_m0_b2 = np.loadtxt("G_m0_b2.dat", float)
rmsG_m1_b2 = np.loadtxt("G_m1_b2.dat", float)
rmsG_m2_b2 = np.loadtxt("G_m2_b2.dat", float)
rmsG_m3_b2 = np.loadtxt("G_m3_b2.dat", float)
rmsG_m4_b2 = np.loadtxt("G_m4_b2.dat", float)

rmsG_m0_b4 = np.loadtxt("G_m0_b4.dat", float)
rmsG_m1_b4 = np.loadtxt("G_m1_b4.dat", float)
rmsG_m2_b4 = np.loadtxt("G_m2_b4.dat", float)
rmsG_m3_b4 = np.loadtxt("G_m3_b4.dat", float)
rmsG_m4_b4 = np.loadtxt("G_m4_b4.dat", float)

# Criar subplots (uma linha com três colunas)
fig, axs = plt.subplots(1, 3, figsize=(15, 5))  # 1 linha, 3 colunas

# Gráfico para beta=1
axs[0].plot(rmsG_m0_b1[:,0], rmsG_m0_b1[:,1], label='m=0')
axs[0].plot(rmsG_m1_b1[:,0], rmsG_m1_b1[:,1], label='m=1')
axs[0].plot(rmsG_m2_b1[:,0], rmsG_m2_b1[:,1], label='m=2')
axs[0].plot(rmsG_m3_b1[:,0], rmsG_m3_b1[:,1], label='m=3')
axs[0].plot(rmsG_m4_b1[:,0], rmsG_m4_b1[:,1], label='m=4')
axs[0].grid(True)
axs[0].set_xlim(0, 3)
axs[0].set_xlabel(r"$W$", fontsize=20)
axs[0].set_ylabel(r"$\langle G \rangle$", fontsize=20)
axs[0].set_title(r"$\beta=1$", fontsize=20)
axs[0].tick_params(axis='both', which='major', labelsize=15)
axs[0].legend(loc='best', fontsize='15')

# Gráfico para beta=2
axs[1].plot(rmsG_m0_b2[:,0], rmsG_m0_b2[:,1], label='m=0')
axs[1].plot(rmsG_m1_b2[:,0], rmsG_m1_b2[:,1], label='m=1')
axs[1].plot(rmsG_m2_b2[:,0], rmsG_m2_b2[:,1], label='m=2')
axs[1].plot(rmsG_m3_b2[:,0], rmsG_m3_b2[:,1], label='m=3')
axs[1].plot(rmsG_m4_b2[:,0], rmsG_m4_b2[:,1], label='m=4')
axs[1].grid(True)
axs[1].set_xlim(0, 3)
axs[1].set_xlabel(r"$W$", fontsize=20)
axs[1].set_ylabel(r"$\langle G \rangle$", fontsize=20)
axs[1].set_title(r"$\beta=2$", fontsize=20)
axs[1].tick_params(axis='both', which='major', labelsize=15)
axs[1].legend(loc='best', fontsize='15')

# Gráfico para beta=4
axs[2].plot(rmsG_m0_b4[:,0], rmsG_m0_b4[:,1], label='m=0')
axs[2].plot(rmsG_m1_b4[:,0], rmsG_m1_b4[:,1], label='m=1')
axs[2].plot(rmsG_m2_b4[:,0], rmsG_m2_b4[:,1], label='m=2')
axs[2].plot(rmsG_m3_b4[:,0], rmsG_m3_b4[:,1], label='m=3')
axs[2].plot(rmsG_m4_b4[:,0], rmsG_m4_b4[:,1], label='m=4')
axs[2].grid(True)
axs[2].set_xlim(0, 3)
axs[2].set_xlabel(r"$W$", fontsize=20)
axs[2].set_ylabel(r"$\langle G \rangle$", fontsize=20)
axs[2].set_title(r"$\beta=4$", fontsize=20)
axs[2].tick_params(axis='both', which='major', labelsize=15)
axs[2].legend(loc='best', fontsize='15')

# Ajustar o layout
plt.tight_layout()
plt.savefig("img_G.png", dpi=300)
plt.show()
