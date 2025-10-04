import os
import numpy as np
import matplotlib.pyplot as plt

# Função para extrair o último caractere do nome do diretório e formatar a legenda
def get_custom_label(dirname):
    k = dirname[-1]  # Último caractere do nome do diretório
    return r"$\beta = {}$".format(k)  # Formatação da legenda

# Diretório atual
current_dir = os.getcwd()

# Listar os subdiretórios no diretório atual
subdirs = [d for d in os.listdir(current_dir) if os.path.isdir(d)]

# Função para carregar os dados de autocorrelação
def load_autocorrelation_data(m_value, prefix):
    data_list = []
    labels = []
    beta_values = []

    for subdir in subdirs:
        # Verificar se o nome do diretório começa com o prefixo e contém 'm' seguido do valor
        if subdir.startswith(prefix) and f'm{m_value}' in subdir:
            file_path = os.path.join(subdir, 'mean_autocorrelation.dat')
            if os.path.exists(file_path):
                data = np.loadtxt(file_path)
                beta_value = int(subdir[-1])
                data_list.append(data)
                labels.append(get_custom_label(subdir))
                beta_values.append(beta_value)

    return data_list, labels, beta_values

# Carregar dados para m = 3 e m = 4
data_m3_G, labels_m3_G, beta_values_m3_G = load_autocorrelation_data(3, 'G')
data_m4_G, labels_m4_G, beta_values_m4_G = load_autocorrelation_data(4, 'G')
data_m3_SN, labels_m3_SN, beta_values_m3_SN = load_autocorrelation_data(3, 'SN')
data_m4_SN, labels_m4_SN, beta_values_m4_SN = load_autocorrelation_data(4, 'SN')

# Ordem desejada para plotar: beta1, beta2, beta4
desired_order = [1, 2, 4]

# Filtrar e reordenar os dados com base na ordem desejada para G e SN
def order_data(data_list, labels, beta_values):
    ordered_data = []
    ordered_labels = []
    for beta in desired_order:
        if beta in beta_values:
            idx = beta_values.index(beta)
            ordered_data.append(data_list[idx])
            ordered_labels.append(labels[idx])
    return ordered_data, ordered_labels

ordered_data_m3_G, ordered_labels_m3_G = order_data(data_m3_G, labels_m3_G, beta_values_m3_G)
ordered_data_m4_G, ordered_labels_m4_G = order_data(data_m4_G, labels_m4_G, beta_values_m4_G)
ordered_data_m3_SN, ordered_labels_m3_SN = order_data(data_m3_SN, labels_m3_SN, beta_values_m3_SN)
ordered_data_m4_SN, ordered_labels_m4_SN = order_data(data_m4_SN, labels_m4_SN, beta_values_m4_SN)

# Criar os subplots com um tamanho de figura maior
fig, axs = plt.subplots(2, 2, figsize=(14, 12))  # Aumentar o tamanho da figura

# Gráfico superior esquerdo
for data in ordered_data_m3_G:
    axs[0, 0].plot(np.arange(len(data)), data)

axs[0, 0].set_title("Conductance    m = 3", fontsize='25')
axs[0, 0].set_xlabel('Lag', fontsize="20")
axs[0, 0].set_ylabel('Autocorrelation', fontsize="20")
axs[0, 0].tick_params(axis='both', which='major', labelsize=15, width=2, length=6)
axs[0, 0].tick_params(axis='both', which='minor', labelsize=12, width=1.5, length=4)
axs[0, 0].legend(ordered_labels_m3_G, loc='best', fontsize='15')
axs[0, 0].grid(True)
axs[0, 0].set_xlim(0, 50)
axs[0, 0].set_ylim(0, 1.05)

# Gráfico superior direito
for data in ordered_data_m4_G:
    axs[0, 1].plot(np.arange(len(data)), data)

axs[0, 1].set_title("Conductance    m = 4", fontsize='25')
axs[0, 1].set_xlabel('Lag', fontsize="20")
axs[0, 1].set_ylabel('Autocorrelation', fontsize="20")
axs[0, 1].tick_params(axis='both', which='major', labelsize=15, width=2, length=6)
axs[0, 1].tick_params(axis='both', which='minor', labelsize=12, width=1.5, length=4)
axs[0, 1].legend(ordered_labels_m4_G, loc='best', fontsize='15')
axs[0, 1].grid(True)
axs[0, 1].set_xlim(0, 50)
axs[0, 1].set_ylim(0, 1.05)

# Gráfico inferior esquerdo
for data in ordered_data_m3_SN:
    axs[1, 0].plot(np.arange(len(data)), data)

axs[1, 0].set_title("Shot Noise Power    m = 3", fontsize='25')
axs[1, 0].set_xlabel('Lag', fontsize="20")
axs[1, 0].set_ylabel('Autocorrelation', fontsize="20")
axs[1, 0].tick_params(axis='both', which='major', labelsize=15, width=2, length=6)
axs[1, 0].tick_params(axis='both', which='minor', labelsize=12, width=1.5, length=4)
axs[1, 0].legend(ordered_labels_m3_SN, loc='best', fontsize='15')  # Adicionar a legenda aqui
axs[1, 0].grid(True)
axs[1, 0].set_xlim(0, 50)
axs[1, 0].set_ylim(0, 1.05)

# Gráfico inferior direito
for data in ordered_data_m4_SN:
    axs[1, 1].plot(np.arange(len(data)), data)

axs[1, 1].set_title("Shot Noise Power    m = 4", fontsize='25')
axs[1, 1].set_xlabel('Lag', fontsize="20")
axs[1, 1].set_ylabel('Autocorrelation', fontsize="20")
axs[1, 1].tick_params(axis='both', which='major', labelsize=15, width=2, length=6)
axs[1, 1].tick_params(axis='both', which='minor', labelsize=12, width=1.5, length=4)
axs[1, 1].legend(ordered_labels_m4_SN, loc='best', fontsize='15')  # Adicionar a legenda aqui
axs[1, 1].grid(True)
axs[1, 1].set_xlim(0, 50)
axs[1, 1].set_ylim(0, 1.05)

# Ajustar o espaçamento vertical
plt.subplots_adjust(hspace=0.4)  # Ajuste o valor conforme necessário

# Salvar o gráfico em alta resolução
plt.savefig("autocorrelation_with_legend.png", dpi=500)

# Mostrar o gráfico
plt.show()
