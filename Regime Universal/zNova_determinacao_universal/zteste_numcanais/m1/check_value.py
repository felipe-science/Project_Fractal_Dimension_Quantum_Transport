import numpy as np
import matplotlib.pyplot as plt

data_rms_beta1 = np.loadtxt("beta1/rmsG.dat", float)
data_rms_beta2 = np.loadtxt("beta2/rmsG.dat", float)
data_rms_beta4 = np.loadtxt("beta4/rmsG.dat", float)


x_beta1 = data_rms_beta1[:,0]
x_beta2 = data_rms_beta2[:,0]
x_beta4 = data_rms_beta4[:,0]
y_beta1 = data_rms_beta1[:,1]
y_beta2 = data_rms_beta2[:,1]
y_beta4 = data_rms_beta4[:,1]

linex_beta1 = np.linspace(x_beta1[0], x_beta1[-1], 10000)
linex_beta2 = np.linspace(x_beta2[0], x_beta2[-1], 10000)
linex_beta4 = np.linspace(x_beta4[0], x_beta4[-1], 10000)
liney_beta1 = []
liney_beta2 = []
liney_beta4 = []

for i in range(len(linex_beta1)):
    liney_beta1.append(0.74)
    liney_beta2.append(0.52)
    liney_beta4.append(0.37)

plt.scatter(x_beta1, y_beta1, color='blue', label=r'$\beta = 1$')
plt.scatter(x_beta2, y_beta2, color='red', label=r'$\beta = 2$')
plt.scatter(x_beta4, y_beta4, color='green', label=r'$\beta = 4$')

plt.plot(linex_beta1, liney_beta1, color='blue', linestyle='--')
plt.plot(linex_beta2, liney_beta2, color='red', linestyle='--')
plt.plot(linex_beta4, liney_beta4, color='green', linestyle='--')

plt.xlabel(r"$W$", fontsize='20')
plt.ylabel(r"$rms(G)$", fontsize='20')
plt.tick_params(axis='both', which='major', labelsize=14)
plt.title(r"m = 1", fontsize='22')
plt.legend(loc='best', fontsize='15')
plt.xlim(0,3)
plt.savefig("ordem0.png", dpi=200)
plt.show()