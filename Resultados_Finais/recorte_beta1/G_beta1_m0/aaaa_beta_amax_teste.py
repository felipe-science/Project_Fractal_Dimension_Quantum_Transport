import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks


gamma = 0.0033

Nfile = 253

values_density = np.zeros([Nfile])

sum_max = 0
for i in range(Nfile):

    data = np.loadtxt(f"G{i}.dat", float)
    G = data[:,1]

    peaks, _ = find_peaks(G)
    sum_max+=len(peaks)


    values_density[i] = len(peaks)

E = data[:,0]
E = E/gamma

dE = E[-1]-E[0]


density = sum_max/(Nfile*dE)
print(f"density = {density}")

plt.plot(E,G)

for i in range(len(peaks)):
    idx = peaks[i]
    plt.scatter(E[idx], G[idx], color='red')
plt.show()



#Calculo de erro
for i in range(Nfile):
    values_density[i] = values_density[i]/(dE)
error_density = np.std(values_density, ddof=1) #/ np.sqrt(len(values_density))
print(error_density)