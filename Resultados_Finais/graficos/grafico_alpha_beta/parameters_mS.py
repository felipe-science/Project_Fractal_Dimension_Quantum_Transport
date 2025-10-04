import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
import scienceplots

# Carregando os dados
data_S_beta1 = np.loadtxt("S_beta1_alphavsm.dat", float)
data_S_beta2 = np.loadtxt("S_beta2_alphavsm.dat", float)
data_S_beta4 = np.loadtxt("S_beta4_alphavsm.dat", float)

data_b_beta1 = np.loadtxt("Sbeta_data_b1.dat", float)
data_b_beta2 = np.loadtxt("Sbeta_data_b2.dat", float)
data_b_beta4 = np.loadtxt("Sbeta_data_b4.dat", float)

Sbeta1x = data_S_beta1[:, 0]
Sbeta1y = data_S_beta1[:, 1]

Sbeta2x = data_S_beta2[:, 0]
Sbeta2y = data_S_beta2[:, 1]

Sbeta4x = data_S_beta4[:, 0]
Sbeta4y = data_S_beta4[:, 1]



plt.style.use('science')

plt.figure(figsize=(10, 8))
plt.subplots_adjust(left=0.12, right=0.98, top=0.92, bottom=0.12)  # Volta ao ajuste original

# Criando o gráfico
plt.plot(Sbeta1x, Sbeta1y, linewidth=3)
plt.scatter(Sbeta1x, Sbeta1y, label=r'$l$; $\beta = 1$', marker='<', s=150)
plt.plot(Sbeta2x, Sbeta2y, linewidth=3)
plt.scatter(Sbeta2x, Sbeta2y, label=r'$l$; $\beta = 2$', marker='*', s=150)
plt.plot(Sbeta4x, Sbeta4y, linewidth=3)
plt.scatter(Sbeta4x, Sbeta4y, label=r'$l$; $\beta=4$', marker='s', s=150)

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

plt.title("Shot Noise Power", fontsize=40)
plt.xlabel(r"$m$", fontsize=40)
plt.ylabel(r'Fit parameters ($l$,$n$)', fontsize=40)

plt.gca().xaxis.set_major_locator(MaxNLocator(integer=True))
plt.tick_params(axis='both', labelsize=30)
plt.ylim(0.20, 1.6)
plt.grid(True)

# Salvar (sem bbox_inches='tight', pois a legenda está dentro)
plt.savefig("alpha_mS.png", dpi=250)
plt.show()