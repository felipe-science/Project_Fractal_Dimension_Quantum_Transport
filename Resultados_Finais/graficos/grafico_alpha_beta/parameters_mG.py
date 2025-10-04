import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
import scienceplots

# Carregando os dados
data_G_beta1 = np.loadtxt("G_beta1_alphavsm.dat", float)
data_G_beta2 = np.loadtxt("G_beta2_alphavsm.dat", float)
data_G_beta4 = np.loadtxt("G_beta4_alphavsm.dat", float)

data_b_beta1 = np.loadtxt("Gbeta_data_b1.dat", float)
data_b_beta2 = np.loadtxt("Gbeta_data_b2.dat", float)
data_b_beta4 = np.loadtxt("Gbeta_data_b4.dat", float)

Gbeta1x = data_G_beta1[:, 0]
Gbeta1y = data_G_beta1[:, 1]

Gbeta2x = data_G_beta2[:, 0]
Gbeta2y = data_G_beta2[:, 1]

Gbeta4x = data_G_beta4[:, 0]
Gbeta4y = data_G_beta4[:, 1]



plt.style.use('science')

plt.figure(figsize=(10, 8))
plt.subplots_adjust(left=0.12, right=0.98, top=0.92, bottom=0.12)  # Volta ao ajuste original

# Criando o gráfico
plt.plot(Gbeta1x, Gbeta1y, linewidth=3)
plt.scatter(Gbeta1x, Gbeta1y, label=r'$l$; $\beta = 1$', marker='<', s=150)
plt.plot(Gbeta2x, Gbeta2y, linewidth=3)
plt.scatter(Gbeta2x, Gbeta2y, label=r'$l$; $\beta = 2$', marker='*', s=150)
plt.plot(Gbeta4x, Gbeta4y, linewidth=3)
plt.scatter(Gbeta4x, Gbeta4y, label=r'$l$; $\beta=4$', marker='s', s=150)

plt.plot(data_b_beta1[:,0], data_b_beta1[:,1], linewidth=3)
plt.scatter(data_b_beta1[:,0], data_b_beta1[:,1], label=r'$n$, $\beta = 1$', marker='>', s=150)  # Marcador diferente

plt.plot(data_b_beta2[:,0], data_b_beta2[:,1], linewidth=3)
plt.scatter(data_b_beta2[:,0], data_b_beta2[:,1], label=r'$n$, $\beta = 2$', marker='^', s=150)  # Marcador diferente

plt.plot(data_b_beta4[:,0], data_b_beta4[:,1], linewidth=3)
plt.scatter(data_b_beta4[:,0], data_b_beta4[:,1], label=r'$n$, $\beta = 4$', marker='v', s=150)  # Marcador diferente

# --- Configuração da Legenda (DENTRO do gráfico) ---
legend = plt.legend(
    loc='lower center',                  # Posição automática (evita sobreposição)
    ncol=3,                     # 2 colunas (ajuste conforme espaço)
    fontsize=26,                # Tamanho menor para caber melhor
    frameon=True,               # Moldura visível
    handlelength=1.5,           # Tamanho dos símbolos
    handletextpad=0.5,          # Espaço entre símbolo e texto
    borderaxespad=0.5,          # Espaço entre legenda e eixos
)

plt.title("Conductance", fontsize=40)
plt.xlabel(r"$m$", fontsize=40)
plt.ylabel(r'Fit parameters ($l$,$n$)', fontsize=40)

plt.gca().xaxis.set_major_locator(MaxNLocator(integer=True))
plt.tick_params(axis='both', labelsize=30)
plt.ylim(0.45, 1.2)
plt.grid(True)

# Salvar (sem bbox_inches='tight', pois a legenda está dentro)
plt.savefig("alpha_mG.png", dpi=250)
plt.show()