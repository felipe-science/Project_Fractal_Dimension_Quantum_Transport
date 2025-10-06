import numpy as np
import matplotlib.pyplot as plt
import scienceplots
from mpl_toolkits.axes_grid1.inset_locator import inset_axes, mark_inset


parameters = np.loadtxt("parametersG_beta1.dat", float)
gamma = parameters[:,3]

data0G = np.loadtxt("m0/beta1/outputG/aaalorentz.dat", float)
data1G = np.loadtxt("m1/beta1/outputG/aaalorentz.dat", float)
data2G = np.loadtxt("m2/beta1/outputG/aaalorentz.dat", float)
data3G = np.loadtxt("m3/beta1/outputG/aaalorentz.dat", float)
data4G = np.loadtxt("m4/beta1/outputG/aaalorentz.dat", float)

E0, cor0 = data0G[:,0], data0G[:,1]
E1, cor1 = data1G[:,0], data1G[:,1]
E2, cor2 = data2G[:,0], data2G[:,1]
E3, cor3 = data3G[:,0], data3G[:,1]
E4, cor4 = data4G[:,0], data4G[:,1]


plt.style.use(['science'])
fig, ax = plt.subplots(figsize=(6, 6))

ax.plot(E0, cor0, label='lorentzian', color='black', linewidth=2)
ax.plot(E0, cor0,':', label=r'$m=0$', color='C0', linewidth=2)
ax.plot(E1, cor1,'--', label=r'$m=1$', color='C1', linewidth=2)
ax.plot(E2, cor2,'-.', label=r'$m=2$', color='C2', linewidth=2)
ax.plot(E3, cor3,':', label=r'$m=3$', color='C3', linewidth=2)
ax.plot(E4, cor4,'--', label=r'$m=4$', color='C4', linewidth=2)

ax.legend(loc='lower left', fontsize='20')

ax.set_ylim(0.4,1.2)
ax.set_xlim(0,1.1)
plt.grid(True)


# Cria o zoom (eixo dentro do eixo principal)
axins = inset_axes(ax, width="50%", height="40%", loc='upper right')

# Plota a mesma curva no inset
axins.plot(E0, cor0, label='lorentzian', color='black', linewidth=5)
axins.plot(E0, cor0,':', label=r'$m=0$', color='C0', linewidth=2)
axins.plot(E1, cor1,'--', label=r'$m=1$', color='C1', linewidth=2)
axins.plot(E2, cor2,'-.', label=r'$m=2$', color='C2', linewidth=2)
axins.plot(E3, cor3,':', label=r'$m=3$', color='C3', linewidth=2)
axins.plot(E4, cor4,'--', label=r'$m=4$', color='C4', linewidth=2)

# Define os limites (zoom)
x1, x2 = 0.35, 0.44   # limites do eixo X
y1, y2 = 0.82, 0.87   # limites do eixo Y
axins.set_xlim(x1, x2)
axins.set_ylim(y1, y2)

# Ligações visuais entre o zoom e o gráfico principal
mark_inset(ax, axins, loc1=2, loc2=4, fc="none", ec="0.5")

plt.tight_layout()

ax.set_xlabel(r'$\epsilon$/$\gamma$', fontsize=30)
ax.set_ylabel('Autocorrelation', fontsize=30)
ax.set_title('Conductance', fontsize=30)

ax.tick_params(axis='both', labelsize=20)

plt.savefig('figG.png', dpi=600)
plt.show()




#Preciso pegar os gamma que tornam a correlação 1