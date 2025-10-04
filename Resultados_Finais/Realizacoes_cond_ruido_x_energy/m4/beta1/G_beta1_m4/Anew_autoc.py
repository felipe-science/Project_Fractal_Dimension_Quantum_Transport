import numpy as np
import matplotlib.pyplot as plt

def read_data(filename):
    """
    Lê os dados de condutância e energia do arquivo.
    
    Args:
    filename (str): Nome do arquivo de dados.
    
    Returns:
    tuple: Vetores de energia e condutância.
    """
    data = np.loadtxt(filename)
    energy = data[:, 0]      # Primeira coluna: Energia
    conductance = data[:, 1]  # Segunda coluna: Condutância
    return energy, conductance

def autocorrelation(signal):
    """
    Calcula a autocorrelação de um sinal.
    
    Args:
    signal (numpy array): Vetor de condutância.
    
    Returns:
    numpy array: Vetor de autocorrelação.
    """
    signal_mean = signal - np.mean(signal)
    correlation = np.correlate(signal_mean, signal_mean, mode='full')
    return correlation[correlation.size // 2:]

def main():
    Nfile = 500
    mean_corr = None
    lags = None

    for i in range(Nfile):
        filename = f"G{i}.dat"
        energy, conductance = read_data(filename)
        autocorr = autocorrelation(conductance)
        
        if mean_corr is None:
            NP = len(autocorr)
            mean_corr = np.zeros(NP)
            lags = np.arange(NP) * (energy[1] - energy[0])

        mean_corr[:len(autocorr)] += autocorr[:len(mean_corr)]

    # Calcular a média e normalizar
    mean_corr /= Nfile
    mean_corr /= mean_corr[0]  # Normaliza pelo valor em lag = 0

    # Plotar o gráfico
    plt.figure(figsize=(8, 5))
    plt.plot(lags, mean_corr, label='Autocorrelação da condutância')
    plt.xlabel('Lag de Energia')
    plt.ylabel('Autocorrelação Normalizada')
    plt.title('Autocorrelação da Condutância em Função da Energia')
    plt.grid(True)
    plt.legend()
    plt.show()

    # Salvar em arquivo
    with open("mean_autocorrelation.dat", "w") as f:
        for i in range(len(mean_corr)):
            f.write(f"{lags[i]} {mean_corr[i]}\n")

# Executar o programa
if __name__ == "__main__":
    main()
