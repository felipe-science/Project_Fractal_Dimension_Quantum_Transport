import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
from scipy.ndimage import gaussian_filter1d

# Definir intervalo
i_slice = 49500
f_slice = 50500
N = f_slice - i_slice

# Listar arquivos no diretório atual que contêm "m4" no nome
files = [f for f in os.listdir() if 'm4' in f and f.endswith('.dat')]

# Preparar o grid de gráficos (3 linhas e 2 colunas) com nova dimensão quadrada
fig, axs = plt.subplots(3, 2, figsize=(12, 12))  # Dimensões quadradas

# Função de autocorrelação (se necessário)
def autocorrelation(data):
    n = len(data)
    mean = np.mean(data)
    c0 = np.sum((data - mean) ** 2) / n
    result = np.correlate(data - mean, data - mean, mode='full')
    result = result[result.size // 2:] / (c0 * n)
    return result

# Função para formatar ticks como números reais
def format_ticks(x, _):
    return f'{x:.2f}'  # Formato: 2 casas decimais

# Lista para armazenar os resultados
results = []

# Função para processar e plotar dados
def process_and_plot(ax, filename, beta_value, m_value):
    # Carregar dados do arquivo
    data = np.loadtxt(filename)

    # Extrair a segunda coluna (eixo y)
    x_data = data[:, 0]
    y_data = data[:, 1]

    # Suavizar os dados usando um filtro gaussiano
    y_data_smoothed = gaussian_filter1d(y_data, sigma=2)  # Ajuste o sigma conforme necessário

    listx_max = []
    listy_max = []

    x = []
    y = []

    for i in range(N):
        idx = i + i_slice

        x.append(x_data[idx])
        y.append(y_data[idx])

        # Verificar se é um máximo local considerando vizinhos diretos
        if (y_data_smoothed[idx] > y_data_smoothed[idx - 1] and
            y_data_smoothed[idx] > y_data_smoothed[idx + 1]):
            listx_max.append(x_data[idx])
            listy_max.append(y_data[idx])

    # Calcular a densidade de máximos
    ro = len(listx_max) / len(x)
    tau_ro = 0.5513288954217921 / ro

    # Formatar e imprimir a saída como solicitado
    result_line = f"beta{beta_value}  m{m_value}  condutancia      tau_ro = {tau_ro}    rho = {ro}\n"
    results.append(result_line)  # Adicionar à lista de resultados
    print(result_line.strip())  # Print para visualizar no console

    # Plotar os dados no subplot específico
    ax.plot(x, y, color='blue')
    ax.scatter(listx_max, listy_max, color='red')
    ax.set_xlabel(r"Energy $(eV)$", fontsize=24)
    ax.set_ylabel(r"Conductance ($\frac{e^2}{h}$)", fontsize=24)

    # Ajustar tamanho da fonte dos ticks
    ax.tick_params(axis='both', labelsize=20)  # Aumenta o tamanho da fonte dos ticks

    # Formatar os ticks como números reais
    ax.xaxis.set_major_formatter(FuncFormatter(format_ticks))
    ax.yaxis.set_major_formatter(FuncFormatter(format_ticks))

    # Adicionar o texto dentro do gráfico com a informação do beta e m
    ax.text(0.05, 0.84, f'beta{beta_value}\nm = {m_value}', transform=ax.transAxes, fontsize=14, color='black',
            bbox=dict(facecolor='white', alpha=0.8))

# Processar e plotar gráficos para os arquivos
for filename in files:
    if 'beta1' in filename:
        process_and_plot(axs[0, 0], filename, '1', '4')
    elif 'beta2' in filename:
        process_and_plot(axs[1, 0], filename, '2', '4')
    elif 'beta4' in filename:
        process_and_plot(axs[2, 0], filename, '4', '4')

# Ajustar layout
plt.tight_layout()

# Salvar o gráfico com os subplots posicionados verticalmente
plt.savefig('conductance_m4.png', dpi=500)
plt.show()

# Salvar os resultados em um arquivo
with open('results_conductance_m4.txt', 'w') as f:
    f.writelines(results)
