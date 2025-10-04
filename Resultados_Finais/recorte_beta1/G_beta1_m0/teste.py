import numpy as np
import matplotlib.pyplot as plt
import scienceplots

# Carrega dados do arquivo
data = np.loadtxt('density_values.dat', comments='#')

m_list = data[:,0]         # eixo x
dflist = data[:,1]         # método de ajuste
dplist = data[:,2]         # método de contagem de picos
df_err = data[:,3]         # erro do método de ajuste
dp_err = data[:,4]         # erro do método de contagem de picos

plt.style.use('science')

plt.figure(figsize=(10, 8))
plt.subplots_adjust(left=0.12, right=0.95, top=0.9, bottom=0.15)

# Método de ajuste com barras de erro
plt.errorbar(m_list, dflist, yerr=df_err, fmt='o', capsize=5, label='Fit method', markersize=10)

# Método de contagem de picos com barras de erro
plt.errorbar(m_list, dplist, yerr=dp_err, fmt='s', capsize=5, label='Peak counting method', markersize=10)

plt.axhline(y=0.55, color='black', linestyle='--', linewidth=2)
plt.ylim(0,1)
plt.xlabel("m", fontsize=35)
plt.ylabel(r"$\langle \rho \rangle$", fontsize=35)
plt.tick_params(axis='both', labelsize=30)
plt.grid(True)
plt.legend(loc='best', fontsize=30)
plt.savefig("density.png", dpi=300)
plt.show()
