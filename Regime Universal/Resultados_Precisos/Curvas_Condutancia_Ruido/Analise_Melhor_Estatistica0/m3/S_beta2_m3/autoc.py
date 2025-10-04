import os
import numpy as np
import matplotlib.pyplot as plt

i_slice = 0
f_slice = 1000

# Função para calcular a autocorrelação de um vetor de dados
def autocorrelation(y):
    n = len(y)
    mean = np.mean(y)
    c0 = np.sum((y - mean) ** 2) / n
    result = np.correlate(y - mean, y - mean, mode='full')
    result = result[result.size // 2:] / (c0 * n)
    return result

# Função para calcular a média das autocorrelações
def mean_autocorrelation(correlations):
    # Ajustar o tamanho das autocorrelações (cortar para o menor tamanho comum)
    min_len = min(len(corr) for corr in correlations)
    truncated_corr = [corr[:min_len] for corr in correlations]
    
    # Converter a lista para uma matriz numpy e calcular a média ao longo do eixo 0
    return np.mean(np.array(truncated_corr), axis=0)

# Obter a lista de arquivos no diretório atual que terminam com '.dat'
files = [f for f in os.listdir() if f.endswith('.dat') and f != 'mean_autocorrelation.dat']

# Inicializar uma lista para armazenar as autocorrelações de cada arquivo
autocorr_list = []

# Processar cada arquivo
for file in files:
    print(f"Processando o arquivo: {file}")
    
    # Carregar os dados do arquivo
    data = np.loadtxt(file)
    
    # Verificar se o arquivo tem mais de uma coluna
    if data.ndim == 1:
        print(f"O arquivo {file} não possui duas colunas, pulando...")
        continue
    
    y_data = data[:, 1]  # Segunda coluna (y)
    
    N = f_slice - i_slice
    y = []
    for i in range(N):
        idx = i + i_slice
        y.append(y_data[idx])

    # Calcular a autocorrelação para o eixo y
    autocorr = autocorrelation(y)
    
    # Adicionar a autocorrelação à lista
    autocorr_list.append(autocorr)

# Calcular a média das autocorrelações
if autocorr_list:
    mean_autocorr = mean_autocorrelation(autocorr_list)

    # Exibir a média da autocorrelação
    plt.plot(mean_autocorr)
    plt.title("Média da Autocorrelação")
    plt.xlabel("Lags")
    plt.ylabel("Autocorrelação")
    plt.show()

    # Salvar a média da autocorrelação em um arquivo
    np.savetxt('mean_autocorrelation.dat', mean_autocorr)

    # Encontrar a posição do valor mais próximo de 0.5
    idx_closest_to_0_5 = np.argmin(np.abs(mean_autocorr - 0.5))
    print(f"O valor mais próximo de 0.5 está na posição: {idx_closest_to_0_5}")
    print(f"Valor correspondente: {mean_autocorr[idx_closest_to_0_5]}")

else:
    print("Nenhuma autocorrelação foi calculada. Verifique os arquivos.")
