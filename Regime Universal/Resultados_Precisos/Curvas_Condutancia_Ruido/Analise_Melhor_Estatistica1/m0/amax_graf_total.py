import numpy as np
import matplotlib.pyplot as plt

# =============================POINTS===============================
g_beta1_point = np.loadtxt("G_beta1_m0/amax_point.dat", float)
g_beta2_point = np.loadtxt("G_beta2_m0/amax_point.dat", float)
g_beta4_point = np.loadtxt("G_beta4_m0/amax_point.dat", float)
s_beta1_point = np.loadtxt("S_beta1_m0/amax_point.dat", float)
s_beta2_point = np.loadtxt("S_beta2_m0/amax_point.dat", float)
s_beta4_point = np.loadtxt("S_beta4_m0/amax_point.dat", float)

g_beta1_pointx = g_beta1_point[:, 0]
g_beta1_pointy = g_beta1_point[:, 1]

g_beta2_pointx = g_beta2_point[:, 0]
g_beta2_pointy = g_beta2_point[:, 1]

g_beta4_pointx = g_beta4_point[:, 0]
g_beta4_pointy = g_beta4_point[:, 1]

s_beta1_pointx = s_beta1_point[:, 0]
s_beta1_pointy = s_beta1_point[:, 1]

s_beta2_pointx = s_beta2_point[:, 0]
s_beta2_pointy = s_beta2_point[:, 1]

s_beta4_pointx = s_beta4_point[:, 0]
s_beta4_pointy = s_beta4_point[:, 1]

# =======================================================================
plt.scatter(g_beta1_pointx, g_beta1_pointy, color='blue')
plt.scatter(g_beta2_pointx, g_beta2_pointy, color='green')
plt.scatter(g_beta4_pointx, g_beta4_pointy, color='orange')
plt.scatter(s_beta1_pointx, s_beta1_pointy, color='purple')
plt.scatter(s_beta2_pointx, s_beta2_pointy, color='black')
plt.scatter(s_beta4_pointx, s_beta4_pointy, color='red')

# =============================CURVE===============================
g_beta1_point = np.loadtxt("G_beta1_m0/amax_curve.dat", float)
g_beta2_point = np.loadtxt("G_beta2_m0/amax_curve.dat", float)
g_beta4_point = np.loadtxt("G_beta4_m0/amax_curve.dat", float)
s_beta1_point = np.loadtxt("S_beta1_m0/amax_curve.dat", float)
s_beta2_point = np.loadtxt("S_beta2_m0/amax_curve.dat", float)
s_beta4_point = np.loadtxt("S_beta4_m0/amax_curve.dat", float)

g_beta1_pointx = g_beta1_point[:, 0]
g_beta1_pointy = g_beta1_point[:, 1]

g_beta2_pointx = g_beta2_point[:, 0]
g_beta2_pointy = g_beta2_point[:, 1]

g_beta4_pointx = g_beta4_point[:, 0]
g_beta4_pointy = g_beta4_point[:, 1]

s_beta1_pointx = s_beta1_point[:, 0]
s_beta1_pointy = s_beta1_point[:, 1]

s_beta2_pointx = s_beta2_point[:, 0]
s_beta2_pointy = s_beta2_point[:, 1]

s_beta4_pointx = s_beta4_point[:, 0]
s_beta4_pointy = s_beta4_point[:, 1]

plt.plot(g_beta1_pointx, g_beta1_pointy, color='blue', label=r'$G - \beta=1$')
plt.plot(g_beta2_pointx, g_beta2_pointy, color='green', label=r'G - $\beta=2$')
plt.plot(g_beta4_pointx, g_beta4_pointy, color='orange', label=r'G - $\beta=4$')
plt.plot(s_beta1_pointx, s_beta1_pointy, color='purple', label=r'S - $\beta=1$')
plt.plot(s_beta2_pointx, s_beta2_pointy, color='black', label=r'S - $\beta=2$')
plt.plot(s_beta4_pointx, s_beta4_pointy, color='red', label=r'S - $\beta=4$')

plt.xlim(0, 0.0034)

# Configurações de legenda, título, eixos e ticks
plt.legend(loc='best', fontsize=15)  # Fonte da legenda
plt.ylabel('Autocorrelation', fontsize=18)  # Nome do eixo X
plt.xlabel('Energy', fontsize=18)  # Nome do eixo Y
plt.title(r"$m = 0$", fontsize=22)  # Título
plt.tick_params(axis='both', which='major', labelsize=13)  # Fonte dos ticks
plt.savefig("m0_lorentziana.png", dpi=300)
plt.show()
