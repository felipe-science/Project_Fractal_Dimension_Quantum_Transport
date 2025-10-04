import os
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

# Definir a função lorentziana generalizada
def lorentziana_generalizada(delta_epsilon, Gamma, alpha):
    return 1 / (1 + (delta_epsilon / Gamma)**2)**alpha

# Função para extrair as informações do nome da pasta e realizar o ajuste
def process_directory(directory):
    filepath = os.path.join(directory, "mean_autocorrelation.dat")
    
    if not os.path.exists(filepath):
        print(f"Arquivo {filepath} não encontrado.")
        return None, None, None, None
    
    # Carregar os dados do arquivo
    data0 = np.loadtxt(filepath)
    data = data0[:30]
    
    # Supondo que o eixo x seja simplesmente o índice dos dados (caso não haja valores x)
    x_data = np.arange(len(data))
    
    # Fazer o ajuste (fit) da função lorentziana aos dados
    initial_guess = [1, 1]
    try:
        popt, _ = curve_fit(lorentziana_generalizada, x_data, data, p0=initial_guess)
        Gamma_fit, alpha_fit = popt
        return x_data, data, popt, Gamma_fit, alpha_fit
    except RuntimeError:
        print(f"Ajuste falhou para o diretório: {os.path.basename(directory)}")
        return None, None, None, None

# Caminho do diretório principal que contém os diretórios
main_directory = "."

# Listar todos os subdiretórios
all_directories = [os.path.join(main_directory, d) for d in os.listdir(main_directory) if os.path.isdir(os.path.join(main_directory, d))]

# Inicializar a lista para armazenar resultados
results = []

# Criar uma figura para plotagem
plt.figure(figsize=(15, 10))

# Número total de diretórios
n_directories = len(all_directories)

# Processar cada diretório
for idx, directory in enumerate(all_directories):
    x_data, data, popt, Gamma_fit, alpha_fit = process_directory(directory)
    
    # Verificar se o ajuste foi bem-sucedido
    if x_data is not None and data is not None and popt is not None:
        # Definir subplot
        plt.subplot((n_directories + 2) // 3, 3, idx + 1)  # Ajusta automaticamente a grade
        plt.scatter(x_data, data, label='Dados', color='blue')
        
        # Criar um vetor x com mais pontos para o ajuste
        x_fit = np.linspace(0, 30, 1000)  # 1000 pontos entre 0 e 30
        fitted_curve = lorentziana_generalizada(x_fit, *popt)
        plt.plot(x_fit, fitted_curve, color='red', label='Ajuste')
        
        # Configurações do gráfico
        plt.xlim(0, 30)
        plt.title(f"{os.path.basename(directory)}: α = {alpha_fit:.4f}, Γ = {Gamma_fit:.4f}")
        plt.xlabel("Delta Epsilon")
        plt.ylabel("Autocorrelação")
        plt.legend()
        
        # Calcular o valor de ρ
        rho = (1 / (2 * np.pi * Gamma_fit)) * np.sqrt(12 * alpha_fit * (alpha_fit + 1) / (2 * alpha_fit))
        
        # Printar os resultados
        print(f"{os.path.basename(directory)} {alpha_fit:.4f} {Gamma_fit:.4f} {rho:.4f}")
    
    else:
        print(f"Não foi possível plotar o diretório: {os.path.basename(directory)}")

# Ajustar layout e salvar a figura
plt.tight_layout()
plt.savefig("todos_os_graficos.png")
plt.show()
