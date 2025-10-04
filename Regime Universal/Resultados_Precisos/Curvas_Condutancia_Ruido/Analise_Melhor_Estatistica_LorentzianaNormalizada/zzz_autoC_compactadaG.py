import numpy as np
import matplotlib.pyplot as plt
import scienceplots


# Carregar os dados beta1
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


# Carregar os dados beta2
lorentz0_beta2 = np.loadtxt("m0/G_beta2_m0/aaalorentz.dat", float)
lorentz1_beta2 = np.loadtxt("m1/G_beta2_m1/aaalorentz.dat", float)
lorentz2_beta2 = np.loadtxt("m2/G_beta2_m2/aaalorentz.dat", float)
lorentz3_beta2 = np.loadtxt("m3/G_beta2_m3/aaalorentz.dat", float)
lorentz4_beta2 = np.loadtxt("m4/G_beta2_m4/aaalorentz.dat", float)

points0_beta2 = np.loadtxt("m0/G_beta2_m0/aaapoints.dat", float)
points1_beta2 = np.loadtxt("m1/G_beta2_m1/aaapoints.dat", float)
points2_beta2 = np.loadtxt("m2/G_beta2_m2/aaapoints.dat", float)
points3_beta2 = np.loadtxt("m3/G_beta2_m3/aaapoints.dat", float)
points4_beta2 = np.loadtxt("m4/G_beta2_m4/aaapoints.dat", float)


# Carregar os dados beta2
lorentz0_beta4 = np.loadtxt("m0/G_beta4_m0/aaalorentz.dat", float)
lorentz1_beta4 = np.loadtxt("m1/G_beta4_m1/aaalorentz.dat", float)
lorentz2_beta4 = np.loadtxt("m2/G_beta4_m2/aaalorentz.dat", float)
lorentz3_beta4 = np.loadtxt("m3/G_beta4_m3/aaalorentz.dat", float)
lorentz4_beta4 = np.loadtxt("m4/G_beta4_m4/aaalorentz.dat", float)

points0_beta4 = np.loadtxt("m0/G_beta4_m0/aaapoints.dat", float)
points1_beta4 = np.loadtxt("m1/G_beta4_m1/aaapoints.dat", float)
points2_beta4 = np.loadtxt("m2/G_beta4_m2/aaapoints.dat", float)
points3_beta4 = np.loadtxt("m3/G_beta4_m3/aaapoints.dat", float)
points4_beta4 = np.loadtxt("m4/G_beta4_m4/aaapoints.dat", float)





# Separar os dados em x e y - beta1
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


# Separar os dados em x e y - beta2
x_m0_b2, y_m0_b2 = lorentz0_beta2[:, 0], lorentz0_beta2[:, 1]
x_m1_b2, y_m1_b2 = lorentz1_beta2[:, 0], lorentz1_beta2[:, 1]
x_m2_b2, y_m2_b2 = lorentz2_beta2[:, 0], lorentz2_beta2[:, 1]
x_m3_b2, y_m3_b2 = lorentz3_beta2[:, 0], lorentz3_beta2[:, 1]
x_m4_b2, y_m4_b2 = lorentz4_beta2[:, 0], lorentz4_beta2[:, 1]


xp_m0_b2, yp_m0_b2 = points0_beta2[:,0], points0_beta2[:,1]
xp_m1_b2, yp_m1_b2 = points1_beta2[:,0], points1_beta2[:,1]
xp_m2_b2, yp_m2_b2 = points2_beta2[:,0], points2_beta2[:,1]
xp_m3_b2, yp_m3_b2 = points3_beta2[:,0], points3_beta2[:,1]
xp_m4_b2, yp_m4_b2 = points4_beta2[:,0], points4_beta2[:,1]



# Separar os dados em x e y - beta4
x_m0_b4, y_m0_b4 = lorentz0_beta2[:, 0], lorentz0_beta2[:, 1]
x_m1_b4, y_m1_b4 = lorentz1_beta2[:, 0], lorentz1_beta2[:, 1]
x_m2_b4, y_m2_b4 = lorentz2_beta2[:, 0], lorentz2_beta2[:, 1]
x_m3_b4, y_m3_b4 = lorentz3_beta2[:, 0], lorentz3_beta2[:, 1]
x_m4_b4, y_m4_b4 = lorentz4_beta2[:, 0], lorentz4_beta2[:, 1]


xp_m0_b4, yp_m0_b4 = points0_beta4[:,0], points0_beta4[:,1]
xp_m1_b4, yp_m1_b4 = points1_beta4[:,0], points1_beta4[:,1]
xp_m2_b4, yp_m2_b4 = points2_beta4[:,0], points2_beta4[:,1]
xp_m3_b4, yp_m3_b4 = points3_beta4[:,0], points3_beta4[:,1]
xp_m4_b4, yp_m4_b4 = points4_beta4[:,0], points4_beta4[:,1]



'''
#plt.figure(figsize=(20, 6))
plt.figure(figsize=(10, 10))

# Plotar os dados com estilos diferentes - beta1
plt.plot(x_m0_b1, y_m0_b1, linestyle='-', color='orange', label=r'$m = 0$')
plt.plot(x_m1_b1, y_m1_b1, linestyle='--', color='blue', label=r'$m = 1$')
plt.plot(x_m2_b1, y_m2_b1, linestyle='-.', color='green', label=r'$m = 2$')
plt.plot(x_m3_b1, y_m3_b1, linestyle=':', color='purple', label=r'$m = 3$')
plt.plot(x_m4_b1, y_m4_b1, linestyle='-', color='brown', label=r'$m = 4$')

# Plotar os dados com estilos diferentes - beta2
#plt.plot(x_m0_b2, y_m0_b2, linestyle='-', color='cyan', label=r'$m = 0$, $\beta = 2$')
#plt.plot(x_m1_b2, y_m1_b2, linestyle='--', color='magenta', label=r'$m = 1$, $\beta = 2$')
#plt.plot(x_m2_b2, y_m2_b2, linestyle='-.', color='yellow', label=r'$m = 2$, $\beta = 2$')
#plt.plot(x_m3_b2, y_m3_b2, linestyle=':', color='pink', label=r'$m = 3$, $\beta = 2$')
#plt.plot(x_m4_b2, y_m4_b2, linestyle='-', color='gray', label=r'$m = 4$, $\beta = 2$')

# Plotar os dados com estilos diferentes - beta4
#plt.plot(x_m0_b4, y_m0_b4, linestyle='-', color='red', label=r'$m = 0$, $\beta = 4$')
#plt.plot(x_m1_b4, y_m1_b4, linestyle='--', color='darkgreen', label=r'$m = 1$, $\beta = 4$')
#plt.plot(x_m2_b4, y_m2_b4, linestyle='-.', color='darkblue', label=r'$m = 2$, $\beta = 4$')
#plt.plot(x_m3_b4, y_m3_b4, linestyle=':', color='brown', label=r'$m = 3$, $\beta = 4$')
#plt.plot(x_m4_b4, y_m4_b4, linestyle='-', color='olive', label=r'$m = 4$, $\beta = 4$')


plt.subplots_adjust(left=0.15, right=0.95, top=0.9, bottom=0.25)

# Ajustar limites dos eixos
plt.xlim(0, 1.5)
plt.ylim(0.1, 1.1)
plt.grid(True)

plt.legend(loc='lower left', bbox_to_anchor=(0, 0), fontsize=16)

plt.tick_params(axis='both', labelsize=35)
plt.xlabel(r'$\epsilon / \gamma$', fontsize=40)
plt.ylabel("Autocorrelation", fontsize=40)
plt.title(r"Conductance", fontsize=45)
plt.savefig("autoC_G.png", dpi=250)
plt.show()
'''

alpha = 0.9981545143527559
gamma = 0.9993698636873497


def f(delta_epsilon, g, a):
    # Evitar divisão por zero
    g = max(g, 1e-10)  # Define um valor mínimo para Gamma
    return 1 / ((1 + ((delta_epsilon / g) ** 2))) ** a

xlorentziana = np.linspace(0,2,1000)
ylorentziana = f(xlorentziana, gamma, alpha)


# Configurar estilo SciencePlots
plt.style.use('science')

# Criar figura
plt.figure(figsize=(8, 8))

# Plotar os dados com estilos diferentes - beta1
plt.plot(xlorentziana,ylorentziana,color='black', label='lorentzian', linewidth=3, )
plt.plot(x_m0_b1, y_m0_b1, linestyle=':', label=r'$m = 0$', linewidth=3)
plt.plot(x_m1_b1, y_m1_b1, linestyle=':', label=r'$m = 1$', linewidth=3)
plt.plot(x_m2_b1, y_m2_b1, linestyle=':', label=r'$m = 2$', linewidth=3)
plt.plot(x_m3_b1, y_m3_b1, linestyle='-.',  label=r'$m = 3$', linewidth=3)
plt.plot(x_m4_b1, y_m4_b1, linestyle='--',  label=r'$m = 4$', linewidth=3)


# Ajustes do layout
plt.subplots_adjust(left=0.15, right=0.95, top=0.9, bottom=0.15)

# Ajustar limites dos eixos
plt.xlim(0, 1.1)
plt.ylim(0.45, 1.1)
plt.grid(True, linestyle='--', linewidth=0.5)

# Legenda e rótulos
plt.legend(loc='upper right', fontsize=25, frameon=True)
plt.tick_params(axis='both', labelsize=25)
plt.xlabel(r'$\delta E / \Gamma$', fontsize=30)
plt.ylabel("Autocorrelation", fontsize=30)
plt.title(r"Conductance", fontsize=35)

# Salvar e exibir
plt.savefig("autoC_G.png", dpi=250, bbox_inches='tight')
plt.show()