import numpy as np
import matplotlib.pyplot as plt
import scienceplots

data = np.loadtxt("parameters.dat", float)

mlist = data[:,0]
alpha = data[:,1]
beta = data[:,2]
gamma = data[:,3]
den_for = data[:,4]
den_max = data[:,5]

# Ativar o estilo "science"
plt.style.use(['science'])

# Criar figura
plt.figure(figsize=(6,4))

plt.scatter(mlist, den_for, marker="X", color='C0', s=40, label='fit method', zorder=2)
plt.scatter(mlist, den_max, marker="P", color='C1', s=40, label = 'peak counting method', zorder=3)
plt.axhline(y=0.55, color='black', linestyle='--', linewidth=2, zorder=1)
plt.ylim(0.055,1.055)
plt.xlabel(r"$m$", fontsize = 25)
plt.ylabel(r"$\langle \rho \rangle$", fontsize = 25)
plt.tick_params(axis='both', which='major', labelsize=20)
plt.legend(loc='best', fontsize = 18)
plt.grid('True')
plt.savefig("density_per_gamma.png", dpi=400)
plt.show()