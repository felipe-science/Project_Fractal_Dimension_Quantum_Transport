import numpy as np
import pylab as plt


beta1G = np.loadtxt("beta1/G.dat")
beta1rmsG = np.loadtxt("beta1/rmsG.dat")

beta2G = np.loadtxt("beta2/G.dat")
beta2rmsG = np.loadtxt("beta2/rmsG.dat")

beta4G = np.loadtxt("beta4/G.dat")
beta4rmsG = np.loadtxt("beta4/rmsG.dat")


xG1 = beta1G[:,0]
yG1 = beta1G[:,1]
xG2 = beta2G[:,0]
yG2 = beta2G[:,1]
xG4 = beta4G[:,0]
yG4 = beta4G[:,1]

xrms1 = beta1rmsG[:,0]
yrms1 = beta1rmsG[:,1]

xrms2 = beta2rmsG[:,0]
yrms2 = beta2rmsG[:,1]

xrms4 = beta4rmsG[:,0]
yrms4 = beta4rmsG[:,1]


fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

# Plotar o primeiro gráfico no subplot à esquerda
ax1.scatter(xG1, yG1, label='beta1')
ax1.scatter(xG2, yG2, label='beta2')
ax1.scatter(xG4, yG4, label='beta4')
ax1.set_title("Gráfico G")
ax1.set_xlabel("W")
ax1.set_ylabel("G")
ax1.legend(loc='best')

# Plotar o segundo gráfico no subplot à direita
ax2.scatter(xrms1, yrms1, label='beta1')
ax2.scatter(xrms2, yrms2, label='beta2')
ax2.scatter(xrms4, yrms4, label='beta4')
ax2.set_title("Gráfico RMS")
ax2.set_xlabel("W")
ax2.set_ylabel("rms(G)")
ax2.legend(loc='best')

ax2.axhline(y=0.74, color='black', linestyle='--', linewidth=2)
ax2.axhline(y=0.52, color='black', linestyle='--', linewidth=2)
ax2.axhline(y=0.37, color='black', linestyle='--', linewidth=2)

# Ajustar o layout para evitar sobreposição
plt.tight_layout()

# Mostrar os gráficos
plt.show()