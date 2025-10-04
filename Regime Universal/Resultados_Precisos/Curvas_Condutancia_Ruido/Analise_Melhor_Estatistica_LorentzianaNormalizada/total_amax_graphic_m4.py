import numpy as np
import matplotlib.pyplot as plt


data_gamma_m_beta1 = np.loadtxt("gamma_m_beta1.dat", float)
data_gamma_m_beta2 = np.loadtxt("gamma_m_beta2.dat", float)
data_gamma_m_beta4 = np.loadtxt("gamma_m_beta4.dat", float)

listm = data_gamma_m_beta1[:,0]
list_gamma_beta1 = data_gamma_m_beta1[:,1]
list_gamma_beta2 = data_gamma_m_beta2[:,1]
list_gamma_beta4 = data_gamma_m_beta4[:,1]


#m = 2
G_m4_beta1_curve = np.loadtxt('m4/G_beta1_m4/amax_curve.dat', float)
G_m4_beta2_curve = np.loadtxt('m4/G_beta2_m4/amax_curve.dat', float)
G_m4_beta4_curve = np.loadtxt('m4/G_beta4_m4/amax_curve.dat', float)
G_m4_beta1_point = np.loadtxt('m4/G_beta1_m4/amax_point.dat', float)
G_m4_beta2_point = np.loadtxt('m4/G_beta2_m4/amax_point.dat', float)
G_m4_beta4_point = np.loadtxt('m4/G_beta4_m4/amax_point.dat', float)




fig, axs = plt.subplots(nrows=3, ncols=1, figsize=(12, 6))

# Adicionar o primeiro gráfico
xc = G_m4_beta1_curve[:,0]/list_gamma_beta1[4]
yc = G_m4_beta1_curve[:,1]
xp = G_m4_beta1_point[:,0]/list_gamma_beta1[4]
yp = G_m4_beta1_point[:,1]
mean = np.average(yc)

axs[0].plot(xc, yc, label=r'$g(\epsilon)$', color='red', zorder=1)
axs[0].scatter(xp, yp, color='black', zorder=2)
axs[0].set_title(r'$m = 4$', fontsize=35)
axs[0].set_xlabel(r'$\epsilon / \gamma$', fontsize=30)
axs[0].set_ylabel(r'$g(\epsilon)$', fontsize=30)
axs[0].axhline(mean, linestyle='--', color='dimgray', label= r'$\langle g(\epsilon) \rangle$')
axs[0].tick_params(axis='both',  labelsize=25)
#axs[0].legend(loc = 'best')




# Adicionar o segundo gráfico
xc = G_m4_beta2_curve[:,0]/list_gamma_beta2[4]
yc = G_m4_beta2_curve[:,1]
xp = G_m4_beta2_point[:,0]/list_gamma_beta2[4]
yp = G_m4_beta2_point[:,1]
mean = np.average(yc)

axs[1].plot(xc, yc, label=r'$g(\epsilon)$', color='green', zorder=1)
axs[1].scatter(xp, yp, color='black', zorder=2)
#axs[1].set_title(r'$\beta=2$   $m = 0$')
axs[1].set_xlabel(r'$\epsilon / \gamma$', fontsize=30)
axs[1].set_ylabel(r'$g(\epsilon)$', fontsize=30)
axs[1].axhline(mean, linestyle='--', color='dimgray', label= r'$\langle g(\epsilon) \rangle$')
axs[1].tick_params(axis='both',  labelsize=25)
#axs[1].legend(loc = 'best')

# Adicionar o terceiro gráfico
xc = G_m4_beta4_curve[:,0]/list_gamma_beta4[4]
yc = G_m4_beta4_curve[:,1]
xp = G_m4_beta4_point[:,0]/list_gamma_beta4[4]
yp = G_m4_beta4_point[:,1]
mean = np.average(yc)

axs[2].plot(xc, yc, label=r'$g(\epsilon)$', color='blue', zorder=1)
axs[2].scatter(xp, yp, color='black', zorder=2)
#axs[2].set_title(r'$\beta=2$   $m = 0$')
axs[2].set_xlabel(r'$\epsilon / \gamma$', fontsize=30)
axs[2].set_ylabel(r'$g(\epsilon)$', fontsize=30)
axs[2].axhline(mean, linestyle='--', color='dimgray', label= r'$\langle g(\epsilon) \rangle$')
axs[2].tick_params(axis='both',  labelsize=25)
#axs[2].legend(loc = 'best')

plt.subplots_adjust(hspace=1.0, wspace=0.5, left=0.1, right=0.95, top=0.9, bottom=0.14)
plt.savefig("total_amax_m4.png", dpi=200)
plt.show()