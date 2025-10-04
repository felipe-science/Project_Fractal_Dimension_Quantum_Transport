import numpy as np
import matplotlib.pyplot as plt
import scienceplots

plt.style.use('science')

data = np.loadtxt("data_gamma.dat")
x = data[:,0]
y = data[:,1]
y = y*1000

plt.figure(figsize=(8, 6))  # largura = 10, altura = 6 (em polegadas)
plt.scatter(x, y, s=70)

# Legenda e rótulos
plt.tick_params(axis='both', labelsize=25)
plt.xlabel(r'$m$', fontsize=30)
plt.ylabel(r"$\Gamma\ ( \times 10^{-3} )$", fontsize=30)
#plt.title(r"Conductance", fontsize=35)

# Salvar e exibir
plt.subplots_adjust(left=0.14, right=0.95, top=0.9, bottom=0.13)
plt.grid("True")
plt.savefig("autoC_G.png", dpi=250, bbox_inches='tight')
plt.show()

