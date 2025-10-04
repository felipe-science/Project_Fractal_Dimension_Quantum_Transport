import numpy as np
import matplotlib.pyplot as plt
import scienceplots

data = np.loadtxt('density_values.dat', comments='#')

m_list = data[:,0]
dflist = data[:,1]
dplist = data[:,2]

plt.style.use('science')

plt.figure(figsize=(10, 8))
plt.subplots_adjust(left=0.12, right=0.95, top=0.9, bottom=0.15)

plt.scatter(m_list, dflist, label='fit method', s=100)
plt.scatter(m_list, dplist, label='Peak counting method', s = 100)
plt.axhline(y=0.55, color='black', linestyle='--', linewidth=2)  # Exemplo com cor e estilo de linha
plt.ylim(0,1)
plt.xlabel("m", fontsize=35)
plt.ylabel(r"$\langle \rho \rangle$", fontsize=35)
plt.tick_params(axis='both', labelsize=30)
plt.grid(True)
plt.legend(loc='best', fontsize=30)
plt.savefig("density.png", dpi=300)
plt.show()