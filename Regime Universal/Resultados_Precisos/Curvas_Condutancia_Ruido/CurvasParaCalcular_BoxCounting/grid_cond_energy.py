import numpy as np
import matplotlib.pyplot as plt
import scienceplots


plt.style.use('science')

fig, axs = plt.subplots(5, 1, figsize=(8, 12))  # 5 linhas, 1 coluna

for i in range(5):
    
    dataG = np.loadtxt(f"m{i}/G_m{i}_beta1.dat", float)

    axs[i].plot(dataG[:,0], dataG[:,1], linewidth=0.4)
    #axs[i].set_title(f'm = {i}', fontsize=20)
     

    axs[i].set_xlabel(rf"$E$ $(eV)$", fontsize=20)
    axs[i].set_ylabel(rf"$G$ $(e^2/h)$", fontsize=20)
    axs[i].tick_params(axis='both', labelsize=20)
   

    axs[i].set_xlim(-1,1)
    match i:
        case 0:
            axs[i].set_ylim(3.0,9.2)
        case 1:
            axs[i].set_ylim(1.0,7.0)
        case 2:
            axs[i].set_ylim(0.7,6.0)
        case 3:
            axs[i].set_ylim(-0.2,4.2)
    



plt.tight_layout()  # Ajusta o layout para não sobrepor os títulos
plt.savefig("grid_cond_energy.png", dpi=500)
plt.show()