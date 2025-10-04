from numpy import loadtxt
import matplotlib.pyplot as plt

# Carregar os dados
dataG   = loadtxt("G.dat", float)
datarms = loadtxt("rmsG.dat", float)

W   = dataG[:,0]
G   = dataG[:,1]
rms = datarms[:,1]

# Criar figura e eixos (1 linha, 2 colunas)
fig, axs = plt.subplots(1, 2, figsize=(12, 5))  # Tamanho opcional

# --- Primeiro subplot: <G> vs W ---
axs[0].scatter(W, G, color='green')
axs[0].set_title("Condutância em função da desordem", fontsize=16)
axs[0].set_xlabel("W", fontsize=14)
axs[0].set_ylabel("<G>", fontsize=14)
axs[0].tick_params(labelsize=11)
axs[0].grid(True)

# --- Segundo subplot: rms(G) vs W ---
axs[1].scatter(W, rms, color='red')
axs[1].axhline(y=0.52, color='black', linestyle='--')  # Linha horizontal
axs[1].set_title("rms(G)", fontsize=16)
axs[1].set_xlabel("W", fontsize=14)
axs[1].set_ylabel("rms(G)", fontsize=14)
axs[1].tick_params(labelsize=11)
axs[1].grid(True)

# Ajuste de layout
plt.tight_layout()

# Salvar figura única com os dois gráficos
plt.savefig("G_and_rms_0.8eV.png", format='png')

# Mostrar o gráfico
plt.show()
