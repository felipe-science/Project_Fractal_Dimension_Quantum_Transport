import numpy as np
import matplotlib.pyplot as plt

# Carregar os dados
data_G_beta1 = np.loadtxt("beta1/G.dat", float)
data_G_beta2 = np.loadtxt("beta2/G.dat", float)
data_G_beta4 = np.loadtxt("beta4/G.dat", float)

data_rms_beta1 = np.loadtxt("beta1/rmsG.dat", float)
data_rms_beta2 = np.loadtxt("beta2/rmsG.dat", float)
data_rms_beta4 = np.loadtxt("beta4/rmsG.dat", float)

# Extrair colunas
G_xbeta1, G_ybeta1 = data_G_beta1[:, 0], data_G_beta1[:, 1]
G_xbeta2, G_ybeta2 = data_G_beta2[:, 0], data_G_beta2[:, 1]
G_xbeta4, G_ybeta4 = data_G_beta4[:, 0], data_G_beta4[:, 1]

x_beta1, y_beta1 = data_rms_beta1[:, 0], data_rms_beta1[:, 1]
x_beta2, y_beta2 = data_rms_beta2[:, 0], data_rms_beta2[:, 1]
x_beta4, y_beta4 = data_rms_beta4[:, 0], data_rms_beta4[:, 1]

# Linhas de referência
linex_beta1 = np.linspace(x_beta1[0], x_beta1[-1], 10000)
linex_beta2 = np.linspace(x_beta2[0], x_beta2[-1], 10000)
linex_beta4 = np.linspace(x_beta4[0], x_beta4[-1], 10000)
liney_beta1 = np.full_like(linex_beta1, 0.74)
liney_beta2 = np.full_like(linex_beta2, 0.52)
liney_beta4 = np.full_like(linex_beta4, 0.37)

# Criar os subplots
fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# Gráfico 1
axes[1].scatter(x_beta1, y_beta1, color='blue', label=r'$\beta = 1$')
axes[1].scatter(x_beta2, y_beta2, color='red', label=r'$\beta = 2$')
axes[1].scatter(x_beta4, y_beta4, color='green', label=r'$\beta = 4$')

axes[1].plot(linex_beta1, liney_beta1, color='blue', linestyle='--')
axes[1].plot(linex_beta2, liney_beta2, color='red', linestyle='--')
axes[1].plot(linex_beta4, liney_beta4, color='green', linestyle='--')

axes[1].set_xlabel(r"$W$", fontsize=22)
axes[1].set_ylabel(r"$rms(G)$", fontsize=22)
axes[1].tick_params(axis='both', which='major', labelsize=18)
axes[1].set_title(r"$m=4$", fontsize=22)
axes[1].legend(loc='best', fontsize=18)
axes[1].set_xlim(0, 4)

# Gráfico 2
axes[0].scatter(G_xbeta1, G_ybeta1, color='blue', label=r'$\beta = 1$')
axes[0].scatter(G_xbeta2, G_ybeta2, color='red', label=r'$\beta = 2$')
axes[0].scatter(G_xbeta4, G_ybeta4, color='green', label=r'$\beta = 4$')

axes[0].set_xlabel(r"$W$", fontsize=22)
axes[0].set_ylabel(r"$\langle G \rangle$", fontsize=22)
axes[0].tick_params(axis='both', which='major', labelsize=18)
axes[0].set_title(r"$m=4$", fontsize=22)
axes[0].legend(loc='best', fontsize=18)
axes[0].set_xlim(0, 4)

# Ajustar layout e salvar a figura
plt.tight_layout()
plt.savefig("grid_graficos.png", dpi=300)
plt.show()
