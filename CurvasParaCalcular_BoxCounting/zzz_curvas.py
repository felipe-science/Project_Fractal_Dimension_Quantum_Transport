import numpy as np
import matplotlib.pyplot as plt
import scienceplots

G_m0_beta1 = np.loadtxt("G_m0_beta1.dat", float)
G_m1_beta1 = np.loadtxt("G_m1_beta1.dat", float)
G_m2_beta1 = np.loadtxt("G_m2_beta1.dat", float)
G_m3_beta1 = np.loadtxt("G_m3_beta1.dat", float)
G_m4_beta1 = np.loadtxt("G_m4_beta1.dat", float)

plt.style.use('science')

plt.figure(figsize=(15, 5))
plt.subplots_adjust(left=0.09, right=0.97, top=0.98, bottom=0.24)

plt.plot(G_m0_beta1[:,0], G_m0_beta1[:,1], linewidth=0.5, label=r"$m=0$")
plt.xlabel(r"$E$ $(eV)$", fontsize=40)
plt.ylabel(r"$G$ $(e^2/h)$", fontsize=40)
plt.xlim(-2,+2)
plt.ylim(3,9.4)
plt.tick_params(axis='both', labelsize=35)
#plt.legend(loc='upper left', fontsize=30)
plt.savefig("m0.png", dpi=200)
plt.show()

plt.figure(figsize=(15, 5))
plt.subplots_adjust(left=0.09, right=0.97, top=0.98, bottom=0.24)

plt.plot(G_m1_beta1[:,0], G_m1_beta1[:,1], linewidth=0.5, label=r"$m=1$")
plt.xlabel(r"$E$ $(eV)$", fontsize=40)
plt.ylabel(r"$G$ $(e^2/h)$", fontsize=40)
plt.xlim(-2,+2)
plt.ylim(1.3,7.5)
plt.tick_params(axis='both', labelsize=35)
#plt.legend(loc='upper left', fontsize=30)
plt.savefig("m1.png", dpi=200)
plt.show()

plt.figure(figsize=(15, 5))
plt.subplots_adjust(left=0.09, right=0.97, top=0.98, bottom=0.24)

plt.plot(G_m2_beta1[:,0], G_m2_beta1[:,1], linewidth=0.5, label=r"$m=2$")
plt.xlabel(r"$E$ $(eV)$", fontsize=40)
plt.ylabel(r"$G$ $(e^2/h)$", fontsize=40)
plt.xlim(-2,+2)
plt.ylim(0.5,6)
plt.tick_params(axis='both', labelsize=35)
#plt.legend(loc='upper left', fontsize=30)
plt.savefig("m2.png", dpi=200)
plt.show()

plt.figure(figsize=(15, 5))
plt.subplots_adjust(left=0.09, right=0.97, top=0.98, bottom=0.24)

plt.plot(G_m3_beta1[:,0], G_m3_beta1[:,1], linewidth=0.5, label=r"$m=3$")
plt.xlabel(r"$E$ $(eV)$", fontsize=40)
plt.ylabel(r"$G$ $(e^2/h)$", fontsize=40)
plt.xlim(-2,+2)
plt.ylim(-0.5,4.5)
plt.tick_params(axis='both', labelsize=35)
#plt.legend(loc='upper left', fontsize=30)
plt.savefig("m3.png", dpi=200)
plt.show()

plt.figure(figsize=(15, 5))
plt.subplots_adjust(left=0.09, right=0.97, top=0.98, bottom=0.24)

plt.plot(G_m4_beta1[:,0], G_m4_beta1[:,1], linewidth=0.5, label=r"$m=4$")
plt.xlabel(r"$E$ $(eV)$", fontsize=40)
plt.ylabel(r"$G$ $(e^2/h)$", fontsize=40)
plt.xlim(-2,+2)
plt.ylim(-0.5,4.5)
plt.tick_params(axis='both', labelsize=35)
#plt.legend(loc='upper left', fontsize=30)
plt.savefig("m4.png", dpi=200)
plt.show()




