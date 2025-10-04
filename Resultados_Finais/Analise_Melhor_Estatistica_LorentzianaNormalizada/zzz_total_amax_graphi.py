import numpy as np
import matplotlib.pyplot as plt
import scienceplots

plt.style.use('science')

data_gamma_m_beta1 = np.loadtxt("gamma_m_beta1.dat", float)
data_gamma_m_beta2 = np.loadtxt("gamma_m_beta2.dat", float)
data_gamma_m_beta4 = np.loadtxt("gamma_m_beta4.dat", float)

listm = data_gamma_m_beta1[:,0]
list_gamma_beta1 = data_gamma_m_beta1[:,1]
list_gamma_beta2 = data_gamma_m_beta2[:,1]
list_gamma_beta4 = data_gamma_m_beta4[:,1]


#m = 0
G_m0_beta1_curve = np.loadtxt('m0/G_beta1_m0/amax_curve.dat', float)
G_m0_beta2_curve = np.loadtxt('m0/G_beta2_m0/amax_curve.dat', float)
G_m0_beta4_curve = np.loadtxt('m0/G_beta4_m0/amax_curve.dat', float)
G_m0_beta1_point = np.loadtxt('m0/G_beta1_m0/amax_point.dat', float)
G_m0_beta2_point = np.loadtxt('m0/G_beta2_m0/amax_point.dat', float)
G_m0_beta4_point = np.loadtxt('m0/G_beta4_m0/amax_point.dat', float)

#m = 1
G_m1_beta1_curve = np.loadtxt('m1/G_beta1_m1/amax_curve.dat', float)
G_m1_beta2_curve = np.loadtxt('m1/G_beta2_m1/amax_curve.dat', float)
G_m1_beta4_curve = np.loadtxt('m1/G_beta4_m1/amax_curve.dat', float)
G_m1_beta1_point = np.loadtxt('m1/G_beta1_m1/amax_point.dat', float)
G_m1_beta2_point = np.loadtxt('m1/G_beta2_m1/amax_point.dat', float)
G_m1_beta4_point = np.loadtxt('m1/G_beta4_m1/amax_point.dat', float)

#m = 2
G_m2_beta1_curve = np.loadtxt('m2/G_beta1_m2/amax_curve.dat', float)
G_m2_beta2_curve = np.loadtxt('m2/G_beta2_m2/amax_curve.dat', float)
G_m2_beta4_curve = np.loadtxt('m2/G_beta4_m2/amax_curve.dat', float)
G_m2_beta1_point = np.loadtxt('m2/G_beta1_m2/amax_point.dat', float)
G_m2_beta2_point = np.loadtxt('m2/G_beta2_m2/amax_point.dat', float)
G_m2_beta4_point = np.loadtxt('m2/G_beta4_m2/amax_point.dat', float)

#m = 3
G_m3_beta1_curve = np.loadtxt('m3/G_beta1_m3/amax_curve.dat', float)
G_m3_beta2_curve = np.loadtxt('m3/G_beta2_m3/amax_curve.dat', float)
G_m3_beta4_curve = np.loadtxt('m3/G_beta4_m3/amax_curve.dat', float)
G_m3_beta1_point = np.loadtxt('m3/G_beta1_m3/amax_point.dat', float)
G_m3_beta2_point = np.loadtxt('m3/G_beta2_m3/amax_point.dat', float)
G_m3_beta4_point = np.loadtxt('m3/G_beta4_m3/amax_point.dat', float)

#m = 4
G_m4_beta1_curve = np.loadtxt('m4/G_beta1_m4/amax_curve.dat', float)
G_m4_beta2_curve = np.loadtxt('m4/G_beta2_m4/amax_curve.dat', float)
G_m4_beta4_curve = np.loadtxt('m4/G_beta4_m4/amax_curve.dat', float)
G_m4_beta1_point = np.loadtxt('m4/G_beta1_m4/amax_point.dat', float)
G_m4_beta2_point = np.loadtxt('m4/G_beta2_m4/amax_point.dat', float)
G_m4_beta4_point = np.loadtxt('m4/G_beta4_m4/amax_point.dat', float)



#m=0
plt.figure(figsize=(15,5))
plt.subplots_adjust(left=0.07, right=0.98, top=0.92, bottom=0.25)

plt.plot(G_m0_beta1_curve[:,0], G_m0_beta1_curve[:,1], linewidth=4, zorder=1, label=r"$m=0$")
plt.scatter(G_m0_beta1_point[:,0], G_m0_beta1_point[:,1], color='red', s=150, zorder=1)

plt.xlabel(r"$E$ $(eV)$", fontsize=40)
plt.ylabel(r"$G$ $(e^2/h)$", fontsize=40)
plt.tick_params(axis='both', labelsize=35)
plt.grid(True)
plt.legend(loc='upper left', fontsize=30)
plt.savefig("maxdensity_m0.png", dpi=250)
plt.show()


#m=1
plt.figure(figsize=(15,5))
plt.subplots_adjust(left=0.07, right=0.98, top=0.92, bottom=0.25)

plt.plot(G_m1_beta1_curve[:,0], G_m1_beta1_curve[:,1], linewidth=4, zorder=1, label=r"$m=1$")
plt.scatter(G_m1_beta1_point[:,0], G_m1_beta1_point[:,1], color='red', s=150, zorder=1)

plt.xlabel(r"$E$ $(eV)$", fontsize=40)
plt.ylabel(r"$G$ $(e^2/h)$", fontsize=40)
plt.tick_params(axis='both', labelsize=35)
plt.grid(True)
plt.legend(loc='upper left', fontsize=30)
plt.savefig("maxdensity_m1.png", dpi=250)
plt.show()

#m=2
plt.figure(figsize=(15,5))
plt.subplots_adjust(left=0.07, right=0.98, top=0.92, bottom=0.25)

plt.plot(G_m2_beta1_curve[:,0], G_m2_beta1_curve[:,1], linewidth=4, zorder=1, label=r"$m=2$")
plt.scatter(G_m2_beta1_point[:,0], G_m2_beta1_point[:,1], color='red', s=150, zorder=1)

plt.xlabel(r"$E$ $(eV)$", fontsize=40)
plt.ylabel(r"$G$ $(e^2/h)$", fontsize=40)
plt.tick_params(axis='both', labelsize=35)
plt.grid(True)
plt.legend(loc='upper left', fontsize=30)
plt.savefig("maxdensity_m2.png", dpi=250)
plt.show()


#m=3
plt.figure(figsize=(15,5))
plt.subplots_adjust(left=0.07, right=0.98, top=0.92, bottom=0.25)

plt.plot(G_m3_beta1_curve[:,0], G_m3_beta1_curve[:,1], linewidth=4, zorder=1, label=r"$m=3$")
plt.scatter(G_m3_beta1_point[:,0], G_m3_beta1_point[:,1], color='red', s=150, zorder=1)

plt.xlabel(r"$E$ $(eV)$", fontsize=40)
plt.ylabel(r"$G$ $(e^2/h)$", fontsize=40)
plt.tick_params(axis='both', labelsize=35)
plt.grid(True)
plt.legend(loc='upper left', fontsize=30)
plt.savefig("maxdensity_m3.png", dpi=250)
plt.show()


#m=4
plt.figure(figsize=(15,5))
plt.subplots_adjust(left=0.07, right=0.98, top=0.92, bottom=0.25)

plt.plot(G_m4_beta1_curve[:,0], G_m4_beta1_curve[:,1], linewidth=4, zorder=1, label=r"$m=4$")
plt.scatter(G_m4_beta1_point[:,0], G_m4_beta1_point[:,1], color='red', s=150, zorder=1)

plt.xlabel(r"$E$ $(eV)$", fontsize=40)
plt.ylabel(r"$G$ $(e^2/h)$", fontsize=40)
plt.tick_params(axis='both', labelsize=35)
plt.grid(True)
plt.legend(loc='upper left', fontsize=30)
plt.savefig("maxdensity_m4.png", dpi=250)
plt.show()