import os
import numpy as np
from scipy.signal import find_peaks
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def f_goe(s):
    return (np.pi / 2) * s * np.exp(- (np.pi / 4) * s**2)

def unfolding(x, ordem=3):
    # Ajusta um polinômio à contagem acumulada dos níveis
    x = np.sort(x)
    n = np.arange(1, len(x) + 1)  # contagem acumulada
    coef = np.polyfit(x, n, ordem)
    p = np.poly1d(coef)
    x_unfolded = p(x)  # aplica o unfolding
    return x_unfolded

path_directory = "realizacoes2/outputG"
all_files = os.listdir(path_directory)

files_name = [
    f for f in all_files
    if f.startswith("G") and f.endswith(".dat") and os.path.isfile(os.path.join(path_directory, f))
]

list_s = []
for fn in files_name:
    data = np.loadtxt(f"{path_directory}/{fn}", float)
    x = data[:, 0]
    y = data[:, 1]

    # Encontra picos
    index_peaks, _ = find_peaks(y, prominence=0.01)
    if len(index_peaks) < 2:
        continue  # ignora arquivos com menos de 2 picos

    # Níveis de energia nos picos
    energy_levels = x[index_peaks]
    
    # Unfolding
    unfolded_levels = unfolding(energy_levels, ordem=1)

    # Espaçamentos normalizados
    s = np.diff(unfolded_levels)
    list_s.extend(s)

# Plot
curvex = np.linspace(0, 5, 1000)
curvey = f_goe(curvex)

plt.hist(list_s, bins=70, density=True, color='skyblue', edgecolor='black', label='Dados')
plt.plot(curvex, curvey, 'r-', lw=2, label='GOE (β=1)')
plt.xlabel("s (espaçamento normalizado)")
plt.ylabel("Densidade de Probabilidade")
plt.title("Distribuição de espaçamentos com Unfolding")
plt.legend()
plt.grid(True)
plt.show()
