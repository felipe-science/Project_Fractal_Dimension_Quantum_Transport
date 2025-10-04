
import os
import numpy as np
import matplotlib.pyplot as plt

# Diretório base onde estão os 12 diretórios
base_dir = os.getcwd()  # Diretório atual (onde o código está)

# Inicializar a figura e os subplots
fig, axes = plt.subplots(4, 3, figsize=(15, 10))  # 4 linhas x 3 colunas

# Função para ler os dados de um arquivo com duas colunas
def load_data(file_path):
    try:
        data = np.loadtxt(file_path)
        if data.ndim == 2 and data.shape[1] == 2:
            return data[:, 0], data[:, 1]  # Retorna as duas colunas
        else:
            raise ValueError("Arquivo com formato incorreto.")
    except Exception as e:
        print(f"Erro ao carregar {file_path}: {e}")
        return None, None

# Função para ler os parâmetros do arquivo fit_results.dat
def load_parameters(file_path):
    try:
        with open(file_path, 'r') as f:
            params = f.read().strip()  # Lê os parâmetros e remove espaços em branco
        return params
    except Exception as e:
        print(f"Erro ao carregar {file_path}: {e}")
        return "Parâmetros não disponíveis"

# Lista de diretórios (subpastas) no diretório base
subdirs = [d for d in os.listdir(base_dir) if os.path.isdir(os.path.join(base_dir, d))]

# Garantir que só vamos considerar os primeiros 12 diretórios
subdirs = subdirs[:12]

# Loop através de cada diretório para gerar os gráficos
for i, subdir in enumerate(subdirs):
    # Obter o eixo correspondente no grid (4x3)
    ax = axes[i // 3, i % 3]
    
    # Caminho completo para o diretório
    dir_path = os.path.join(base_dir, subdir)
    
    # Caminhos completos dos arquivos
    curve_file = os.path.join(dir_path, "data_curve.dat")
    scate_file = os.path.join(dir_path, "data_scate.dat")
    fit_file = os.path.join(dir_path, "fit_results.dat")
    
    # Carregar os dados de data_curve.dat
    x_curve, y_curve = load_data(curve_file)
    if x_curve is not None and y_curve is not None:
        ax.plot(x_curve, y_curve, label='Curve Data', color='blue')
    
    # Carregar os dados de data_scate.dat
    x_scate, y_scate = load_data(scate_file)
    if x_scate is not None and y_scate is not None:
        ax.scatter(x_scate, y_scate, label='Scate Data', color='red')
    
    # Carregar os parâmetros de fit_results.dat
    params = load_parameters(fit_file)
    
    # Definir o título do gráfico com os parâmetros
    ax.set_title(f'Diretório: {subdir}\n{params}', fontsize=8)
    
    # Definir rótulos dos eixos
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    
    # Adicionar legenda
    ax.legend(loc='best', fontsize=8)

# Ajustar layout para não sobrepor os gráficos
plt.tight_layout()

# Exibir os gráficos
plt.show()
