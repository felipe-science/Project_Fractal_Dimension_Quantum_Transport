import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

# Carregando os dados
data_G_beta1 = np.loadtxt("G_beta1_alphavsm.dat", float)
data_G_beta2 = np.loadtxt("G_beta2_alphavsm.dat", float)
data_G_beta4 = np.loadtxt("G_beta4_alphavsm.dat", float)


Gbeta1x = data_G_beta1[:, 0]
Gbeta1y = data_G_beta1[:, 1]

Gbeta2x = data_G_beta2[:, 0]
Gbeta2y = data_G_beta2[:, 1]

Gbeta4x = data_G_beta4[:, 0]
Gbeta4y = data_G_beta4[:, 1]

# Criando o gráfico
plt.plot(Gbeta1x, Gbeta1y, color='red', label=r'$\beta = 1$')
plt.scatter(Gbeta1x, Gbeta1y, color='red', marker='<')
plt.plot(Gbeta2x, Gbeta2y, color='green', label=r'$\beta = 2$')
plt.scatter(Gbeta2x, Gbeta2y, color='green', marker='*')
plt.plot(Gbeta4x, Gbeta4y, color='blue', label=r'$\beta=4$')
plt.scatter(Gbeta4x, Gbeta4y, color='blue', marker='+')

# Adicionando legendas e rótulos
plt.legend(loc='best', fontsize='13')
plt.xlabel(r"$m$", fontsize=20)
plt.ylabel(r'$\alpha$', fontsize=20)

# Ajustando os ticks para números inteiros no eixo x
plt.gca().xaxis.set_major_locator(MaxNLocator(integer=True))

# Ajustando os tickparams
plt.tick_params(axis='both', which='major', labelsize=14)
plt.tick_params(axis='both', which='minor', labelsize=14)

# Exibindo o gráfico
plt.savefig("novo.png", dpi=200)
plt.grid(True)
plt.show()
