import os
import numpy as np
import pylab as plt

# Diretório onde o código está sendo executado (pode ser alterado se necessário)
directories = os.getcwd()

# Lista todos os arquivos que começam com 'G' e terminam com '.dat'
total_files = [f for f in os.listdir(directories) if f.startswith('G') and f.endswith('.dat')]

cont_max = 0
sum_ro = 0.0
N_file = len(total_files)


# Exibe os arquivos encontrados
for name_file in total_files:
    
    data = np.loadtxt(name_file,float)
    datax = data[:,0]
    datay = data[:,1]

    deltaE = datax[-1] - datax[0]

    cont_max = 0
    N = len(datay)
    for i in range(1,N-1,1):
        if(datay[i] > datay[i-1] and datay[i] > datay[i+1]):
            cont_max+=1
    ro = 1.0*cont_max/(datax[-1] - datax[0])
    sum_ro += ro

average_ro = sum_ro/N_file
print("\n\n====================")
print(f"Density: {average_ro}")
print("====================\n\n")


N = len(datay)
for i in range(1,N-1,1):
    if(datay[i] > datay[i-1] and datay[i] > datay[i+1]):
        plt.scatter(datax[i], datay[i], color="red")
plt.plot(datax, datay)
plt.show()