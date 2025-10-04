import numpy as np
import matplotlib.pyplot as plt

# Carregar os dados
m0_g_beta1p = np.loadtxt("m0/G_beta1_m0/amax_point.dat", float)
m0_g_beta1c = np.loadtxt("m0/G_beta1_m0/amax_curve.dat", float)

m0_g_beta1px = m0_g_beta1p[:, 0]
m0_g_beta1py = m0_g_beta1p[:, 1]
m0_g_beta1cx = m0_g_beta1c[:, 0]
m0_g_beta1cy = m0_g_beta1c[:, 1]

m1_g_beta1p = np.loadtxt("m1/G_beta1_m1/amax_point.dat", float)
m1_g_beta1c = np.loadtxt("m1/G_beta1_m1/amax_curve.dat", float)

m1_g_beta1px = m1_g_beta1p[:, 0]
m1_g_beta1py = m1_g_beta1p[:, 1]
m1_g_beta1cx = m1_g_beta1c[:, 0]
m1_g_beta1cy = m1_g_beta1c[:, 1]

m2_g_beta1p = np.loadtxt("m2/G_beta1_m0/amax_point.dat", float)
m2_g_beta1c = np.loadtxt("m2/G_beta1_m0/amax_curve.dat", float)

m2_g_beta1px = m2_g_beta1p[:, 0]
m2_g_beta1py = m2_g_beta1p[:, 1]
m2_g_beta1cx = m2_g_beta1c[:, 0]
m2_g_beta1cy = m2_g_beta1c[:, 1]

m3_g_beta1p = np.loadtxt("m3/G_beta1_m3/amax_point.dat", float)
m3_g_beta1c = np.loadtxt("m3/G_beta1_m3/amax_curve.dat", float)

m3_g_beta1px = m3_g_beta1p[:, 0]
m3_g_beta1py = m3_g_beta1p[:, 1]
m3_g_beta1cx = m3_g_beta1c[:, 0]
m3_g_beta1cy = m3_g_beta1c[:, 1]

# Plotando os pontos e curvas
plt.scatter(m0_g_beta1px, m0_g_beta1py, color='blue')
plt.plot(m0_g_beta1cx, m0_g_beta1cy, color='blue', label=r'$m=0$')

plt.scatter(m1_g_beta1px, m1_g_beta1py, color='red')
plt.plot(m1_g_beta1cx, m1_g_beta1cy, color='red', label=r'$m=1$')

plt.scatter(m2_g_beta1px, m2_g_beta1py, color='green')
plt.plot(m2_g_beta1cx, m2_g_beta1cy, color='green', label=r'$m=2$')

plt.scatter(m3_g_beta1px, m3_g_beta1py, color='black')
plt.plot(m3_g_beta1cx, m3_g_beta1cy, color='black', label=r'$m=3$')

# Configurações de eixos, título e ticks
plt.xlabel("Energy", fontsize=18)  # Nome do eixo X
plt.ylabel("Conductance", fontsize=18)  # Nome do eixo Y
plt.legend(loc='best', fontsize=13)  # Tamanho da fonte da legenda
plt.tick_params(axis='both', which='major', labelsize=13)  # Fonte dos ticks
plt.title(r"$\beta = 1$", fontsize=22)  # Título

# Mostrar gráfico
plt.show()
