import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

Nfile = 500

gamma = 0.0005196750668530931


rho = 0
for i in range(Nfile):

    data = np.loadtxt(f"S{i}.dat", float)
    E = data[:,0]/gamma
    G = data[:,1]

    peaks, _ = find_peaks(G, height=1)

    deltaE = abs(E[peaks[0]] - E[peaks[-1]])
    #deltaE = abs(E[0] - E[-1])
    #print(deltaE)
    
    rho += len(peaks)/deltaE

rho = rho/(Nfile)
print(rho)

plt.plot(E/gamma,G, color = 'blue')
plt.scatter(E[peaks]/gamma, G[peaks], color='black', zorder=2)
plt.show()