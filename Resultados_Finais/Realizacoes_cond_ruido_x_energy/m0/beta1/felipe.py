import numpy as np
from scipy.signal import find_peaks
import matplotlib.pyplot as plt
from scipy.stats import norm

cont = 0

Nfile = 10000

list_dx = []
for i in range(Nfile):

    try:
        data = np.loadtxt(f"G_m0_beta1/G{i}.dat", float)
        x = data[:, 0]
        y = data[:, 1]

        peaks, _ = find_peaks(y)
        Npeaks = len(peaks)

        for j in range(1, Npeaks):
            dx = x[peaks[j]] - x[peaks[j-1]]
            list_dx.append(dx)

        cont+=1

    except:
        continue  # Pula arquivos com erro

list_dx = np.array(list_dx)

# Normalizar os espaçamentos para média 1 (unfolding básico)
list_dx /= np.mean(list_dx)

# Criar histograma normalizado
counts, bins, _ = plt.hist(list_dx, bins=30, density=True, color='lightgray', edgecolor='black', alpha=0.7, label='Dados')

# Curva teórica GOE (β = 1)
s = np.linspace(0, 5, 200)
P_s = (np.pi / 2) * s * np.exp(- (np.pi / 4) * s**2)
plt.plot(s, P_s, 'r-', lw=2, label='GOE (β = 1)')

plt.xlabel('s (dx normalizado)')
plt.ylabel('Densidade')
plt.title('Distribuição de espaçamentos normalizada (Unfolding)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("grap.png", dpi=300)
plt.show()



print(cont)