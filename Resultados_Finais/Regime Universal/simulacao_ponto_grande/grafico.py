import numpy as np
import matplotlib.pyplot as plt


data_m0_beta1_G = np.loadtxt('m0/beta1/G.dat', float)
data_m0_beta2_G = np.loadtxt('m0/beta2/G.dat', float)
data_m0_beta4_G = np.loadtxt('m0/beta4/G.dat', float)

data_m1_beta1_G = np.loadtxt('m1/beta1/G.dat', float)
data_m1_beta2_G = np.loadtxt('m1/beta2/G.dat', float)
data_m1_beta4_G = np.loadtxt('m1/beta4/G.dat', float)

data_m2_beta1_G = np.loadtxt('m2/beta1/G.dat', float)
data_m2_beta2_G = np.loadtxt('m2/beta2/G.dat', float)
data_m2_beta4_G = np.loadtxt('m2/beta4/G.dat', float)

data_m3_beta1_G = np.loadtxt('m3/beta1/G.dat', float)
data_m3_beta2_G = np.loadtxt('m3/beta2/G.dat', float)
data_m3_beta4_G = np.loadtxt('m3/beta4/G.dat', float)

data_m4_beta1_G = np.loadtxt('m4/beta1/G.dat', float)
data_m4_beta2_G = np.loadtxt('m4/beta2/G.dat', float)
data_m4_beta4_G = np.loadtxt('m4/beta4/G.dat', float)

# ===================================================

data_m0_beta1_S = np.loadtxt('m0/beta1/rmsG.dat', float)
data_m0_beta2_S = np.loadtxt('m0/beta2/rmsG.dat', float)
data_m0_beta4_S = np.loadtxt('m0/beta4/rmsG.dat', float)

data_m1_beta1_S = np.loadtxt('m1/beta1/rmsG.dat', float)
data_m1_beta2_S = np.loadtxt('m1/beta2/rmsG.dat', float)
data_m1_beta4_S = np.loadtxt('m1/beta4/rmsG.dat', float)

data_m2_beta1_S = np.loadtxt('m2/beta1/rmsG.dat', float)
data_m2_beta2_S = np.loadtxt('m2/beta2/rmsG.dat', float)
data_m2_beta4_S = np.loadtxt('m2/beta4/rmsG.dat', float)

data_m3_beta1_S = np.loadtxt('m3/beta1/rmsG.dat', float)
data_m3_beta2_S = np.loadtxt('m3/beta2/rmsG.dat', float)
data_m3_beta4_S = np.loadtxt('m3/beta4/rmsG.dat', float)

data_m4_beta1_S = np.loadtxt('m4/beta1/rmsG.dat', float)
data_m4_beta2_S = np.loadtxt('m4/beta2/rmsG.dat', float)
data_m4_beta4_S = np.loadtxt('m4/beta4/rmsG.dat', float)


'''
plt.plot(data_m0_beta1_G[:,0], data_m0_beta1_G[:,1], label=r'$m = 0$  $\beta=1$')
plt.plot(data_m0_beta2_G[:,0], data_m0_beta2_G[:,1], label=r'$m = 0$  $\beta=2$')
plt.plot(data_m0_beta4_G[:,0], data_m0_beta4_G[:,1], label=r'$m = 0$  $\beta=4$')

plt.plot(data_m1_beta1_G[:,0], data_m1_beta1_G[:,1], label=r'$m = 1$  $\beta=1$')
plt.plot(data_m1_beta2_G[:,0], data_m1_beta2_G[:,1], label=r'$m = 1$  $\beta=2$')
plt.plot(data_m1_beta4_G[:,0], data_m1_beta4_G[:,1], label=r'$m = 1$  $\beta=4$')

plt.plot(data_m2_beta1_G[:,0], data_m2_beta1_G[:,1], label=r'$m = 2$  $\beta=1$')
plt.plot(data_m2_beta2_G[:,0], data_m2_beta2_G[:,1], label=r'$m = 2$  $\beta=2$')
plt.plot(data_m2_beta4_G[:,0], data_m2_beta4_G[:,1], label=r'$m = 2$  $\beta=4$')

plt.plot(data_m3_beta1_G[:,0], data_m3_beta1_G[:,1], label=r'$m = 3$  $\beta=1$')
plt.plot(data_m3_beta2_G[:,0], data_m3_beta2_G[:,1], label=r'$m = 3$  $\beta=2$')
plt.plot(data_m3_beta4_G[:,0], data_m3_beta4_G[:,1], label=r'$m = 3$  $\beta=4$')

plt.plot(data_m4_beta1_G[:,0], data_m4_beta1_G[:,1], label=r'$m = 4$  $\beta=1$')
plt.plot(data_m3_beta2_G[:,0], data_m4_beta2_G[:,1], label=r'$m = 4$  $\beta=2$')
plt.plot(data_m4_beta4_G[:,0], data_m4_beta4_G[:,1], label=r'$m = 4$  $\beta=4$')

plt.legend(loc='best')
plt.savefig("teste.png")
plt.show()
'''

fig, axes = plt.subplots(2, 3, figsize=(15, 10))

#Beta1
axes[0,0].scatter(data_m0_beta1_G[:,0], data_m0_beta1_G[:,1], label=r'$m = 0$')
axes[0,0].scatter(data_m1_beta1_G[:,0], data_m1_beta1_G[:,1], label=r'$m = 1$')
axes[0,0].scatter(data_m2_beta1_G[:,0], data_m2_beta1_G[:,1], label=r'$m = 2$')
axes[0,0].scatter(data_m3_beta1_G[:,0], data_m3_beta1_G[:,1], label=r'$m = 3$')
axes[0,0].scatter(data_m4_beta1_G[:,0], data_m4_beta1_G[:,1], label=r'$m = 4$')
axes[0,0].set_title(r'$\beta = 1$', fontsize='30')
axes[0,0].set_xlabel(r'$W$', fontsize='25')
axes[0,0].set_ylabel(r'$\langle G \rangle$', fontsize='25')
axes[0,0].tick_params(axis='both', labelsize=20)

#Beta1
axes[0,1].scatter(data_m0_beta2_G[:,0], data_m0_beta2_G[:,1], label=r'$m = 0$')
axes[0,1].scatter(data_m1_beta2_G[:,0], data_m1_beta2_G[:,1], label=r'$m = 1$')
axes[0,1].scatter(data_m2_beta2_G[:,0], data_m2_beta2_G[:,1], label=r'$m = 2$')
axes[0,1].scatter(data_m3_beta2_G[:,0], data_m3_beta2_G[:,1], label=r'$m = 3$')
axes[0,1].scatter(data_m4_beta2_G[:,0], data_m4_beta2_G[:,1], label=r'$m = 4$')
axes[0,1].set_title(r'$\beta = 2$', fontsize='30')
axes[0,1].set_xlabel(r'$W$', fontsize='25')
axes[0,1].set_ylabel(r'$\langle G \rangle$', fontsize='25')
axes[0,1].tick_params(axis='both', labelsize=20)

#Beta1
axes[0,2].scatter(data_m0_beta4_G[:,0], data_m0_beta4_G[:,1], label=r'$m = 0$')
axes[0,2].scatter(data_m1_beta4_G[:,0], data_m1_beta4_G[:,1], label=r'$m = 1$')
axes[0,2].scatter(data_m2_beta4_G[:,0], data_m2_beta4_G[:,1], label=r'$m = 2$')
axes[0,2].scatter(data_m3_beta4_G[:,0], data_m3_beta4_G[:,1], label=r'$m = 3$')
axes[0,2].scatter(data_m4_beta4_G[:,0], data_m4_beta4_G[:,1], label=r'$m = 4$')
axes[0,2].set_title(r'$\beta = 4$', fontsize='30')
axes[0,2].set_xlabel(r'$W$', fontsize='25')
axes[0,2].set_ylabel(r'$\langle G \rangle$', fontsize='25')
axes[0,2].tick_params(axis='both', labelsize=20)




#Beta1
axes[1,0].scatter(data_m0_beta1_S[:,0], data_m0_beta1_S[:,1], label=r'$m = 0$')
axes[1,0].scatter(data_m1_beta1_S[:,0], data_m1_beta1_S[:,1], label=r'$m = 1$')
axes[1,0].scatter(data_m2_beta1_S[:,0], data_m2_beta1_S[:,1], label=r'$m = 2$')
axes[1,0].scatter(data_m3_beta1_S[:,0], data_m3_beta1_S[:,1], label=r'$m = 3$')
axes[1,0].scatter(data_m4_beta1_S[:,0], data_m4_beta1_S[:,1], label=r'$m = 4$')
axes[1,0].axhline(y=0.74, color='black', linestyle='--', linewidth=2)
axes[1,0].set_title(r'$\beta = 1$', fontsize='30')
axes[1,0].set_xlabel(r'$W$', fontsize='25')
axes[1,0].set_ylabel(r'$ rms(G)$', fontsize='25')
axes[1,0].tick_params(axis='both', labelsize=20)

#Beta1
axes[1,1].scatter(data_m0_beta2_S[:,0], data_m0_beta2_S[:,1], label=r'$m = 0$')
axes[1,1].scatter(data_m1_beta2_S[:,0], data_m1_beta2_S[:,1], label=r'$m = 1$')
axes[1,1].scatter(data_m2_beta2_S[:,0], data_m2_beta2_S[:,1], label=r'$m = 2$')
axes[1,1].scatter(data_m3_beta2_S[:,0], data_m3_beta2_S[:,1], label=r'$m = 3$')
axes[1,1].scatter(data_m4_beta2_S[:,0], data_m4_beta2_S[:,1], label=r'$m = 4$')
axes[1,1].axhline(y=0.54, color='black', linestyle='--', linewidth=2)
axes[1,1].set_title(r'$\beta = 2$', fontsize='30')
axes[1,1].set_xlabel(r'$W$', fontsize='25')
axes[1,1].set_ylabel(r'$ rms(G)$', fontsize='25')
axes[1,1].tick_params(axis='both', labelsize=20)

#Beta1
axes[1,2].scatter(data_m0_beta4_S[:,0], data_m0_beta4_S[:,1], label=r'$m = 0$')
axes[1,2].scatter(data_m1_beta4_S[:,0], data_m1_beta4_S[:,1], label=r'$m = 1$')
axes[1,2].scatter(data_m2_beta4_S[:,0], data_m2_beta4_S[:,1], label=r'$m = 2$')
axes[1,2].scatter(data_m3_beta4_S[:,0], data_m3_beta4_S[:,1], label=r'$m = 3$')
axes[1,2].scatter(data_m4_beta4_S[:,0], data_m4_beta4_S[:,1], label=r'$m = 4$')
axes[1,2].axhline(y=0.37, color='black', linestyle='--', linewidth=2)
axes[1,2].set_title(r'$\beta = 4$', fontsize='30')
axes[1,2].set_xlabel(r'$W$', fontsize='25')
axes[1,2].set_ylabel(r'$ rms(G)$', fontsize='25')
axes[1,2].tick_params(axis='both', labelsize=20)

axes[1,1].legend(loc='upper center', fontsize=20, bbox_to_anchor=(0.5, -0.3), ncol=5)

plt.subplots_adjust(left=0.08, right=0.99, top=0.9, bottom=0.20, wspace=0.30, hspace=0.6)
plt.savefig("grafico_universal.png", dpi=250)
plt.show()