import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import os

# Definir a função lorentziana generalizada com tratamento de erro
def lorentziana_generalizada(delta_epsilon, Gamma, alpha, beta):
    # Evitar divisão por zero
    Gamma = max(Gamma, 1e-10)  # Define um valor mínimo para Gamma
    return 1 / (1 + (delta_epsilon / Gamma)**(2 * beta))**alpha

# Função para realizar o ajuste de curva
def process_file(filename):
    if not os.path.exists(filename):
        print(f"Arquivo {filename} não encontrado.")
        return None, None, None, None
    
    # Carregar os dados do arquivo
    data0 = np.loadtxt(filename)
    data = data0[:4000]  # Se você deseja ajustar apenas os primeiros 30 pontos

    # Eixo x a partir da primeira coluna (delta_epsilon) e y a partir da segunda (autocorrelação)
    #x_data = data[:, 0]
    #x_data = np.linspace(0,0.2,len(y_data))
    y_data = data
    x_data = np.linspace(0,0.06,len(y_data))

    # Fazer o ajuste (fit) da função lorentziana aos dados
    initial_guess = [1, 1, 1]  # Gama, alpha, beta iniciais
    try:
        # Definir limites para evitar valores inválidos
        popt, _ = curve_fit(
            lorentziana_generalizada, x_data, y_data, p0=initial_guess, 
            bounds=([1e-10, 0, 0], [np.inf, np.inf, np.inf])
        )
        Gamma_fit, alpha_fit, beta_fit = popt
        return x_data, y_data, popt, Gamma_fit, alpha_fit, beta_fit
    except (RuntimeError, ValueError) as e:
        print(f"Ajuste falhou. Erro: {str(e)}")
        return None, None, None, None

# Nome do arquivo
filename = "mean_autocorrelation.dat"

# Processar o arquivo e realizar o ajuste
x_data, y_data, popt, Gamma_fit, alpha_fit, beta_fit = process_file(filename)

# Verificar se o ajuste foi bem-sucedido
if x_data is not None and y_data is not None and popt is not None:
    # Criar um vetor x com mais pontos para o ajuste
    x_fit = np.linspace(min(x_data), max(x_data), 1000)  # 1000 pontos no intervalo de x_data
    fitted_curve = lorentziana_generalizada(x_fit, *popt)

    # Plotar os dados e o ajuste
    plt.figure(figsize=(10, 6))
    plt.scatter(x_data, y_data, label='Dados', color='blue')
    plt.plot(x_fit, fitted_curve, color='red', label='Ajuste')

    # Configurações do gráfico
    plt.title(f"Ajuste de Curva: α = {alpha_fit:.4f}, Γ = {Gamma_fit:.4f}, β = {beta_fit:.4f}")
    plt.xlabel("Delta Epsilon")
    plt.ylabel("Autocorrelação")
    plt.legend()
    
    # Mostrar o gráfico
    plt.show()

    # Calcular o valor de ρ
    rho = (1 / (2 * np.pi)) * np.sqrt(6 * beta_fit * (alpha_fit + 1) / (Gamma_fit**2))
    
    # Exibir os parâmetros ajustados
    print(f"Parâmetros Ajustados:\nGamma = {Gamma_fit:.4f}\nAlpha = {alpha_fit:.4f}\nBeta = {beta_fit:.4f}\nRho = {rho:.4f}")
    
    # Salvar os parâmetros ajustados em um arquivo
    with open("fit_results.dat", "w") as f:
        f.write(f"Gamma: {Gamma_fit:.4f}\n")
        f.write(f"Alpha: {alpha_fit:.4f}\n")
        f.write(f"Beta: {beta_fit:.4f}\n")
        f.write(f"Rho: {rho:.4f}\n")

    fl1 = open("data_curve.dat","w")
    fl2 = open("data_scate.dat","w")
    for i in range(len(x_data)):
        fl1.write(f"{x_data[i]} {y_data[i]}\n")
    for i in range(len(x_fit)):
        fl2.write(f"{x_fit[i]} {fitted_curve[i]}\n")
    fl1.close()
    fl2.close()

else:
    print("O ajuste falhou.")
