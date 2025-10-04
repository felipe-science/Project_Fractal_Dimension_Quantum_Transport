import numpy as np
import matplotlib.pyplot as plt
import scienceplots


plt.style.use('science')

fig, axs = plt.subplots(5, 1, figsize=(6, 12))  # 5 linhas, 1 coluna

for i in range(5):
    
    dataG = np.loadtxt(f"m{i}/G_beta1_m{i}/G1.dat", float)

    axs[i].plot(dataG[:,0], dataG[:,1], label=f'Gráfico {i+1}')
    axs[i].set_title(f'Gráfico {i+1}')
    axs[i].legend()
    axs[i].grid(True)

plt.tight_layout()  # Ajusta o layout para não sobrepor os títulos
plt.show()