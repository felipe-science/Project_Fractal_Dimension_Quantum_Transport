import numpy as np
import matplotlib.pyplot as plt

NP = 100

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
    
    Nfile = 188

    mean_corr = np.zeros([NP])

    for i in range(Nfile):
        filename = f"S{i}.dat"
        energy, conductance = read_data(filename)
        autocorr = autocorrelation(conductance)
    
        # Gerar eixo x para a autocorrelação (lags em energia)
        lags = np.arange(len(autocorr)) * (energy[1] - energy[0])
    
        for j in range(NP):
            mean_corr[j] += autocorr[j]

    # Calcular a média
    mean_corr /= Nfile
    
    # Normalizar pela autocorrelação em lag = 0
    mean_corr /= mean_corr[0]  # Normaliza pelo primeiro valor (lag = 0)

    # Plotar a autocorrelação
    plt.figure(figsize=(8, 5))
    plt.plot(lags, mean_corr, label='Autocorrelação da condutância')
    plt.xlabel('Lag de Energia')
    plt.ylabel('Autocorrelação Normalizada')
    plt.title('Autocorrelação da Condutância em Função da Energia')
    plt.grid(True)
    plt.legend()
    plt.show()

    # Salvar a média da autocorrelação normalizada
    with open("mean_autocorrelation.dat", "w") as f:
        for i in range(NP):
            f.write(f"{lags[i]} {mean_corr[i]}\n")


# Executar o programa
if __name__ == "__main__":
    main()
