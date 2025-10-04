import numpy as np
import matplotlib.pyplot as plt


data_beta1 = np.loadtxt("gamma_m_beta1S.dat", float)
data_beta2 = np.loadtxt("gamma_m_beta2S.dat", float)
data_beta4 = np.loadtxt("gamma_m_beta4S.dat", float)

xbeta1 = data_beta1[:,0]
ybeta1 = data_beta1[:,1]*1000.0

xbeta2 = data_beta2[:,0]
ybeta2 = data_beta2[:,1]*1000.0

xbeta4 = data_beta4[:,0]
ybeta4 = data_beta4[:,1]*1000.0


plt.scatter(xbeta1,ybeta1, color='red')
plt.plot(xbeta1, ybeta1, color='red', label=r'$\beta=1$')
plt.scatter(xbeta2,ybeta2, color='green')
plt.plot(xbeta2, ybeta2, color='green', label=r'$\beta=2$')
plt.scatter(xbeta4,ybeta4, color='blue')
plt.plot(xbeta4, ybeta4, color='blue', label=r'$\beta=4$')
plt.legend(loc='best', fontsize='15')
plt.xlabel(r'$m$', fontsize='15')
plt.ylabel(r'$\Gamma$ $(x 10^{-3})$', fontsize='15')
plt.tick_params(axis='both', which='major', labelsize=14)
plt.tick_params(axis='both', which='minor', labelsize=14)
plt.grid(True)
plt.savefig("gamma_mS.png", dpi=200)
plt.show()