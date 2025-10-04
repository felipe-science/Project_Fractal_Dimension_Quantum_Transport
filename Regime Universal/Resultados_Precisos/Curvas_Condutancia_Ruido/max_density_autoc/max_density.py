import h5py
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

# Função para suavização usando interpolação cúbica (semelhante ao filtro Bézier)
def smooth_bezier(x, y, num_points=1000):
    # Criar uma spline cúbica
    cs = CubicSpline(x, y)
    
    # Gerar pontos interpolados
    x_new = np.linspace(x.min(), x.max(), num_points)
    y_smooth = cs(x_new)
    
    return x_new, y_smooth

# Carregar dados do arquivo
filename = 'G_m3_n53w08_R1.dat'
data = np.loadtxt(filename)

# Extrair a segunda coluna (eixo y)
x_data = data[:, 0]
y_data = data[:, 1]


listx_max = []
listy_max = []







x = []
y = []
i_slice = 48000
f_slice = 52000
N = f_slice - i_slice
for i in range(N):
    
    idx = i+i_slice
    
    x.append(x_data[idx])
    y.append(y_data[idx])

    if(y_data[idx] > y_data[idx-1] and y_data[idx] > y_data[idx+1]):
        listx_max.append(x_data[idx])
        listy_max.append(y_data[idx])

plt.plot(x,y, color='blue')
plt.scatter(listx_max,listy_max, color='red')
plt.xlabel(r"Energy $(eV)$", fontsize='15')
plt.ylabel("Conductance", fontsize='15')
plt.savefig("graf.png")
plt.show()