import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

def autocorr(x):
    n = len(x)
    x = x - np.mean(x)  # centralizar
    result = np.correlate(x, x, mode='full')  # correlaciona com si mesmo
    return result[result.size // 2:] / np.arange(n, 0, -1)

data = np.loadtxt("G_m4_n297.dat")

energy = data[:,0]
conduc = data[:,1]

peaks, _ = find_peaks(conduc, height=0)


#plt.plot(energy, conduc)
#plt.scatter(energy[peaks], conduc[peaks], color='red')
#plt.xlim(0,0.05)
#plt.show()

ac = autocorr(conduc)

#plt.plot(ac)
#plt.show()


Npeaks = len(peaks)
density = Npeaks/(abs(energy[0] - energy[-1]))

print(f"Nº peaks: {Npeaks}")
print(f"density peaks: {density}")