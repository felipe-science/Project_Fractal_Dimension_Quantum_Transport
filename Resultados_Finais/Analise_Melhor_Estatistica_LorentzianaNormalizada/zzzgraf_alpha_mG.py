import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
import scienceplots

# Carregando os dados
data_G_beta1 = np.loadtxt("G_beta1_alphavsm.dat", float)
data_G_beta2 = np.loadtxt("G_beta2_alphavsm.dat", float)
data_G_beta4 = np.loadtxt("G_beta4_alphavsm.dat", float)

data_b = np.loadtxt("zzzzznovos_betas.dat", float)

Gbeta1x = data_G_beta1[:, 0]
Gbeta1y = data_G_beta1[:, 1]

Gbeta2x = data_G_beta2[:, 0]
Gbeta2y = data_G_beta2[:, 1]

Gbeta4x = data_G_beta4[:, 0]
Gbeta4y = data_G_beta4[:, 1]



plt.style.use('science')

plt.figure(figsize=(10, 8))
plt.subplots_adjust(left=0.12, right=0.98, top=0.92, bottom=0.12)

# Criando o gráfico
plt.plot(Gbeta1x, Gbeta1y, label=r'$\beta = 1$', linewidth=3)
plt.scatter(Gbeta1x, Gbeta1y,  marker='<', s=150)
plt.plot(Gbeta2x, Gbeta2y,  label=r'$\beta = 2$', linewidth=3)
plt.scatter(Gbeta2x, Gbeta2y, marker='*', s=150)
plt.plot(Gbeta4x, Gbeta4y,  label=r'$\beta=4$', linewidth=3)
plt.scatter(Gbeta4x, Gbeta4y,  marker='s', s=150)

plt.scatter(data_b[:,0], data_b[:,1], marker='<', s=150)
plt.plot(data_b[:,0], data_b[:,1], linewidth=3)

# Adicionando legendas e rótulos
plt.legend(loc='best', fontsize=30)
plt.title("Conductance", fontsize=40)
plt.xlabel(r"$m$", fontsize=40)
plt.ylabel(r'$\alpha$', fontsize=40)

# Ajustando os ticks para números inteiros no eixo x
plt.gca().xaxis.set_major_locator(MaxNLocator(integer=True))

# Ajustando os tickparams
plt.tick_params(axis='both', labelsize=30)


# Exibindo o gráfico
plt.grid(True)
plt.savefig("alpha_mG.png", dpi=250)
plt.show()
