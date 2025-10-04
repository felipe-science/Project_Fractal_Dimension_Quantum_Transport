import numpy as np
import matplotlib.pyplot as plt
import scienceplots

plt.style.use(['science'])
plt.figure(figsize=(6,4))

beta_list = [1,2,4]
for i in range(3):

    beta=beta_list[i]

    data = np.loadtxt(f"parametersG_beta{beta}.dat")

    listmf = data[:,0]
    listal = data[:,1]
    listbt = data[:,2]
    listgm = data[:,3]
    listdf = data[:,4]
    listdm = data[:,5]

    plt.scatter(listmf, listal, label=rf'$l$; $\beta={beta}$', zorder=i+1)
    plt.plot(listmf, listal)
    plt.scatter(listmf, listbt, label=rf'$n$; $\beta={beta}$', zorder=i+4)
    plt.plot(listmf, listbt)
    plt.xlabel(r'$m$', fontsize=25)
    plt.ylabel(r'Fit parameters $(l,n)$', fontsize=25)
    plt.title("Conductance", fontsize=25)
    plt.tick_params(axis='both', which='major', labelsize=20)
    plt.legend(loc='upper left', fontsize=12, ncol=3)
    plt.grid(True)
    plt.ylim(0,3)
plt.savefig("parametersG.png", dpi=300)
plt.show()