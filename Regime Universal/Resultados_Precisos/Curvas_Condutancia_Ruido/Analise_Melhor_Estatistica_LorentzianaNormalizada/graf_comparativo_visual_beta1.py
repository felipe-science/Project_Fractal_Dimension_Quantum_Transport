import numpy as np
import matplotlib.pyplot as plt

# Carregar os dados
lorentz0_beta1 = np.loadtxt("m0/G_beta1_m0/aaalorentz.dat", float)
lorentz1_beta1 = np.loadtxt("m1/G_beta1_m1/aaalorentz.dat", float)
lorentz2_beta1 = np.loadtxt("m2/G_beta1_m2/aaalorentz.dat", float)
lorentz3_beta1 = np.loadtxt("m3/G_beta1_m3/aaalorentz.dat", float)
lorentz4_beta1 = np.loadtxt("m4/G_beta1_m4/aaalorentz.dat", float)

points0_beta1 = np.loadtxt("m0/G_beta1_m0/aaapoints.dat", float)
points1_beta1 = np.loadtxt("m1/G_beta1_m1/aaapoints.dat", float)
points2_beta1 = np.loadtxt("m2/G_beta1_m2/aaapoints.dat", float)
points3_beta1 = np.loadtxt("m3/G_beta1_m3/aaapoints.dat", float)
points4_beta1 = np.loadtxt("m4/G_beta1_m4/aaapoints.dat", float)

# Separar os dados em x e y
x_m0_b1, y_m0_b1 = lorentz0_beta1[:, 0], lorentz0_beta1[:, 1]
x_m1_b1, y_m1_b1 = lorentz1_beta1[:, 0], lorentz1_beta1[:, 1]
x_m2_b1, y_m2_b1 = lorentz2_beta1[:, 0], lorentz2_beta1[:, 1]
x_m3_b1, y_m3_b1 = lorentz3_beta1[:, 0], lorentz3_beta1[:, 1]
x_m4_b1, y_m4_b1 = lorentz4_beta1[:, 0], lorentz4_beta1[:, 1]


xp_m0_b1, yp_m0_b1 = points0_beta1[:,0], points0_beta1[:,1]
xp_m1_b1, yp_m1_b1 = points1_beta1[:,0], points1_beta1[:,1]
xp_m2_b1, yp_m2_b1 = points2_beta1[:,0], points2_beta1[:,1]
xp_m3_b1, yp_m3_b1 = points3_beta1[:,0], points3_beta1[:,1]
xp_m4_b1, yp_m4_b1 = points4_beta1[:,0], points4_beta1[:,1]

# Plotar os dados com estilos diferentes
plt.plot(x_m0_b1, y_m0_b1, linestyle='-', color='black', label=r'$m = 0$')
plt.plot(x_m1_b1, y_m1_b1, linestyle='--', color='red', label=r'$m = 1$')
plt.plot(x_m2_b1, y_m2_b1, linestyle='-.', color='blue', label=r'$m = 2$')
plt.plot(x_m3_b1, y_m3_b1, linestyle=':', color='green', label=r'$m = 3$')
plt.plot(x_m4_b1, y_m4_b1, linestyle='-', color='purple', label=r'$m = 4$')

#plt.scatter(xp_m0_b1, yp_m0_b1, color='black')
#plt.scatter(xp_m1_b1, yp_m1_b1, color='red')
#plt.scatter(xp_m2_b1, yp_m2_b1, color='blue')
#plt.scatter(xp_m3_b1, yp_m3_b1, color='green')
#plt.scatter(xp_m4_b1, yp_m4_b1, color='purple')

plt.subplots_adjust(left=0.15, right=0.95, top=0.9, bottom=0.15)

# Ajustar limites dos eixos
plt.xlim(0, 1.5)
plt.ylim(0.1, 1.1)
plt.grid(True)
plt.legend(loc='best', fontsize=16)
plt.tick_params(axis='both', labelsize=16)
plt.xlabel(r'$\epsilon / \gamma$', fontsize='22')
plt.ylabel("Autocorrelation", fontsize='22')
plt.title(r"$\beta=1$", fontsize='24')
plt.savefig("compareGbeta1.png", dpi=200)
plt.show()
