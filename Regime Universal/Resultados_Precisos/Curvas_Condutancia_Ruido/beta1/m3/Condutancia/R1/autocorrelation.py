import numpy as np
import matplotlib.pyplot as plt

# Função para calcular a autocorrelação
def autocorrelation(data):
    n = len(data)
    mean = np.mean(data)
    c0 = np.sum((data - mean) ** 2) / n
    result = np.correlate(data - mean, data - mean, mode='full')
    result = result[result.size // 2:] / (c0 * n)
    return result

# Carregar dados do arquivo
filename = 'G_m3_n53w08_R1.dat'
data = np.loadtxt(filename)

# Extrair a segunda coluna (eixo y)
y_data0 = data[:, 1]

y_data = []
for i in range(len(y_data0)):
    if(i > 10000):
        y_data.append(y_data0[i])

# Calcular a autocorrelação
autocorr_result = autocorrelation(y_data)

# Plotar o gráfico da autocorrelação
plt.figure(figsize=(10, 5))
plt.plot(autocorr_result, label='Autocorrelação')
plt.axhline(y=0.5, color='r', linestyle='--', label='Autocorrelação = 0.5')
plt.title('Autocorrelação')
plt.xlabel('Lag')
plt.ylabel('Autocorrelação')
plt.grid()
plt.legend()
plt.show()

# Encontrar o lag onde a autocorrelação atinge 0.5
lag_05 = np.where(autocorr_result >= 0.5)[0]

if lag_05.size > 0:
    print(f'O comprimento de correlação (lag) onde a autocorrelação atinge 0.5 é: {lag_05[0]}')
else:
    # Se não encontrar, imprimir os valores de autocorrelação
    for lag, value in enumerate(autocorr_result):
        print(f'Lag: {lag}, Autocorrelação: {value}')
    print('A autocorrelação não atinge 0.5.')
