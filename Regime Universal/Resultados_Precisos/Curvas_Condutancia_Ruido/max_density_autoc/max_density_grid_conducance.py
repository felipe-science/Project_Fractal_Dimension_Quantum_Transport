import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

# Definir intervalo
i_slice = 49000
f_slice = 51000
N = f_slice - i_slice

# Listar arquivos no diretório atual que começam com "G"
files = [f for f in os.listdir() if f.startswith('G') and f.endswith('.dat')]

# Arquivos que correspondem aos betas específicos
files_beta1_m3 = [f for f in files if 'm3' in f and 'beta1' in f]
files_beta2_m3 = [f for f in files if 'm3' in f and 'beta2' in f]
files_beta4_m3 = [f for f in files if 'm3' in f and 'beta4' in f]

files_beta1_m4 = [f for f in files if 'm4' in f and 'beta1' in f]
files_beta2_m4 = [f for f in files if 'm4' in f and 'beta2' in f]
files_beta4_m4 = [f for f in files if 'm4' in f and 'beta4' in f]

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

    listx_max = []
    listy_max = []

    x = []
    y = []

    for i in range(N):
        idx = i + i_slice

        x.append(x_data[idx])
        y.append(y_data[idx])

        # Verificar se é um máximo local
        if y_data[idx] > y_data[idx - 1] and y_data[idx] > y_data[idx + 1]:
            listx_max.append(x_data[idx])
            listy_max.append(y_data[idx])


    ro = len(listx_max) / 0.2
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

# Processar e plotar gráficos para os arquivos m3
if files_beta1_m3:
    process_and_plot(axs[0, 0], files_beta1_m3[0], '1', '3')
if files_beta2_m3:
    process_and_plot(axs[1, 0], files_beta2_m3[0], '2', '3')
if files_beta4_m3:
    process_and_plot(axs[2, 0], files_beta4_m3[0], '4', '3')

# Processar e plotar gráficos para os arquivos m4
if files_beta1_m4:
    process_and_plot(axs[0, 1], files_beta1_m4[0], '1', '4')
if files_beta2_m4:
    process_and_plot(axs[1, 1], files_beta2_m4[0], '2', '4')
if files_beta4_m4:
    process_and_plot(axs[2, 1], files_beta4_m4[0], '4', '4')

# Ajustar layout
plt.tight_layout()

# Salvar o gráfico com os subplots posicionados verticalmente
plt.savefig('conductance.png', dpi=500)
plt.show()

# Salvar os resultados em um arquivo
with open('results_conductance.txt', 'w') as f:
    f.writelines(results)
