import numpy as np
import matplotlib.pyplot as plt
import scienceplots


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






plt.style.use('science')
plt.figure(figsize=(10, 8))
plt.subplots_adjust(left=0.15, right=0.95, top=0.9, bottom=0.15)

plt.gca().set_aspect('auto')  # Ou 'equal' se quiser manter proporções idênticas


#plt.scatter(data_m0_beta1_G[:,0], data_m0_beta1_G[:,1], label=r'$m = 0$')
plt.scatter(data_m0_beta1_G[:,0], data_m0_beta1_G[:,1]/28, label=r'$m = 0$', s=100, marker='o')  
plt.scatter(data_m1_beta1_G[:,0], data_m1_beta1_G[:,1]/28, label=r'$m = 1$', s=100, marker='s')  
plt.scatter(data_m2_beta1_G[:,0], data_m2_beta1_G[:,1]/22, label=r'$m = 2$', s=100, marker='^')  
plt.scatter(data_m3_beta1_G[:,0], data_m3_beta1_G[:,1]/10, label=r'$m = 3$', s=100, marker='D')  
plt.scatter(data_m4_beta1_G[:,0], data_m4_beta1_G[:,1]/10, label=r'$m = 4$', s=100, marker='v')  


plt.plot(data_m0_beta1_G[:,0], data_m0_beta1_G[:,1]/28, linewidth=2)
plt.plot(data_m1_beta1_G[:,0], data_m1_beta1_G[:,1]/28, linewidth=2)
plt.plot(data_m2_beta1_G[:,0], data_m2_beta1_G[:,1]/22, linewidth=2)
plt.plot(data_m3_beta1_G[:,0], data_m3_beta1_G[:,1]/10, linewidth=2)
plt.plot(data_m4_beta1_G[:,0], data_m4_beta1_G[:,1]/10, linewidth=2)

plt.legend(loc='upper right', fontsize=30, frameon=True)

plt.xlabel(r"$W$ (Disorder strength)", fontsize=35)
plt.ylabel(r"$\langle G \rangle$ $(e²/h)$", fontsize=35)
plt.tick_params(axis='both', labelsize=30)
plt.xlim(0,4)
plt.grid(True)
plt.savefig("mediaG.png", dpi=250)
plt.show()



plt.figure(figsize=(10, 8))
plt.subplots_adjust(left=0.15, right=0.95, top=0.9, bottom=0.15)



#plt.scatter(data_m0_beta1_G[:,0], data_m0_beta1_G[:,1], label=r'$m = 0$')
plt.scatter(data_m0_beta1_S[:,0], data_m0_beta1_S[:,1], label=r'$m = 0$', s=100, marker='o')
plt.scatter(data_m1_beta1_S[:,0], data_m1_beta1_S[:,1], label=r'$m = 1$', s=100, marker='s')
plt.scatter(data_m2_beta1_S[:,0], data_m2_beta1_S[:,1], label=r'$m = 2$', s=100, marker='^')
plt.scatter(data_m3_beta1_S[:,0], data_m3_beta1_S[:,1], label=r'$m = 3$', s=100, marker='D')
plt.scatter(data_m4_beta1_S[:,0], data_m4_beta1_S[:,1], label=r'$m = 4$', s=100, marker='v')

plt.plot(data_m0_beta1_S[:,0], data_m0_beta1_S[:,1], linewidth=2)
plt.plot(data_m1_beta1_S[:,0], data_m1_beta1_S[:,1], linewidth=2)
plt.plot(data_m2_beta1_S[:,0], data_m2_beta1_S[:,1], linewidth=2)
plt.plot(data_m3_beta1_S[:,0], data_m3_beta1_S[:,1], linewidth=2)
plt.plot(data_m4_beta1_S[:,0], data_m4_beta1_S[:,1], linewidth=2)

plt.axhline(y=0.74, color='black', linestyle='--', linewidth=2)  # Linha horizontal em y=5

plt.legend(loc='lower left', fontsize=30, frameon=True, bbox_to_anchor=(+0.04, 0))

plt.xlabel(r"$W$ (Disorder strength)", fontsize=35)
plt.ylabel(r"rms($G$) $(e^2/h)$", fontsize=35)
plt.tick_params(axis='both', labelsize=30)
plt.xlim(0,4)
plt.grid(True)
plt.savefig("rmsG.png", dpi=250)
plt.show()


