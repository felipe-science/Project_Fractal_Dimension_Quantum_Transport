import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

gamma_m4 = 0.00012855


data = np.loadtxt("G_m4_n297.dat")

energy = data[:,0]
conduc = data[:,1]

plt.plot(energy, conduc)
plt.show()

energy = energy[47000:53000]
conduc = conduc[47000:53000]

peaks, _ = find_peaks(conduc, height=0)




Npeaks = len(peaks)
density = Npeaks/((abs(energy[peaks[0]] - energy[peaks[-1]])/gamma_m4))

print(f"Nº peaks: {Npeaks}")
print(f"density peaks: {density}")

print(f"faixa {energy[0]} ate {energy[-1]}")

plt.plot(energy, conduc)
plt.show()