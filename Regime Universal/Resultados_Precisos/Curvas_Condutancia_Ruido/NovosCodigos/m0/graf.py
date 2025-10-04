import numpy as np
import matplotlib.pyplot as plt

G_m0_beta1 = np.loadtxt("G_m0_beta1/G_m3_n53w08_R0.dat", float)
G_m0_beta2 = np.loadtxt("G_m0_beta2/G_m3_n53w213_R0.dat")
G_m0_beta4 = np.loadtxt("G_m0_beta4/G_m3_n53w370_R0.dat", float)

plt.plot(G_m0_beta1[:,0], G_m0_beta1[:,1])
plt.show()

plt.plot(G_m0_beta1[:,0], G_m0_beta2[:,1])
plt.show()

plt.plot(G_m0_beta2[:,0], G_m0_beta2[:,1])
plt.show()