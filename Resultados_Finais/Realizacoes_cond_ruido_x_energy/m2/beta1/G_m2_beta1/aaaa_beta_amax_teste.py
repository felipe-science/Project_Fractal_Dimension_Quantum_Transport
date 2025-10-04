import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks


gamma = 0.00366502
Nfile = 668

sum_max = 0
for i in range(Nfile):

    data = np.loadtxt(f"G{i}.dat", float)
    G = data[:,1]

    peaks, _ = find_peaks(G)
    sum_max+=len(peaks)


E = data[:,0]

E = E/gamma
dE = E[peaks[-1]]-E[peaks[0]]
dE = E[-1]-E[0]



density = sum_max/(Nfile*dE)
print(f"density = {density}")

plt.plot(E,G)

for i in range(len(peaks)):
    idx = peaks[i]
    plt.scatter(E[idx], G[idx], color='red')
plt.show()
