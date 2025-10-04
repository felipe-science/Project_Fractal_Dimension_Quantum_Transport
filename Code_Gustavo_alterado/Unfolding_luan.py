import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks
import glob
import os
import warnings

warnings.simplefilter('ignore', np.RankWarning)  # Ignora avisos do polyfit

# ---------------------------------------
# Configurações
# ---------------------------------------
beta = 1  
diretorio_dados = f'realizacoes4/outputG'
padrao_arquivos = '*.dat'
grau_polinomio = 1.0
num_bins = 60
plotar_unfolding = True  # True para depurar o ajuste
limite_picos_min = grau_polinomio + 2  # Número mínimo de picos para aplicar o ajuste

# Estilo dos gráficos
plt.style.use('seaborn-v0_8-bright')
plt.rcParams.update({
    "text.usetex": True,
    "font.family": "serif",
    "font.serif": ["Times New Roman"],
    "axes.labelsize": 12,
    "font.size": 12,
    "legend.fontsize": 10,
    "xtick.labelsize": 10,
    "ytick.labelsize": 10,
    "figure.autolayout": True
})

# ---------------------------------------
# Funções
# ---------------------------------------
def extrair_maximos(posicoes, condutancias):
    indices_picos, _ = find_peaks(condutancias, prominence=0.0)
    return posicoes[indices_picos]

def realizar_unfolding(posicoes, grau, plot=False, nome_arquivo=None):
    posicoes_ordenadas = np.sort(posicoes)
    contagem_acumulada = np.arange(1, len(posicoes_ordenadas) + 1)
    coef = np.polyfit(posicoes_ordenadas, contagem_acumulada, grau)
    polinomio = np.poly1d(coef)
    unfolded = polinomio(posicoes_ordenadas)
    espacamentos = np.diff(unfolded)
    espacamentos = espacamentos[espacamentos > 0]

    if plot and nome_arquivo:
        plt.figure(figsize=(6, 4))
        plt.plot(posicoes_ordenadas, contagem_acumulada, label="Original $N(x)$")
        plt.plot(posicoes_ordenadas, polinomio(posicoes_ordenadas), '--', label="Ajuste polinomial")
        plt.xlabel("Energia / Posição dos Máximos")
        plt.ylabel("Contagem acumulada")
        plt.title("Diagnóstico do Unfolding")
        plt.legend()
        plt.grid(True, linestyle=':', alpha=0.6)
        plt.tight_layout()
        plt.savefig(f"{nome_arquivo}_unfolding_check.png", dpi=300)
        plt.close()

    return espacamentos / np.mean(espacamentos)

def distribuicao_wigner(s, beta):
    if beta == 1:
        return (np.pi / 2) * s * np.exp(- (np.pi / 4) * s**2)
    elif beta == 2:
        return (32 / np.pi**2) * s**2 * np.exp(- (4 / np.pi) * s**2)
    elif beta == 4:
        return (2**18 / (3**6 * np.pi**3)) * s**4 * np.exp(- (64 / (9 * np.pi)) * s**2)
    else:
        raise ValueError("Beta inválido. Escolha 1, 2 ou 4.")

# ---------------------------------------
# Loop pelos Arquivos
# ---------------------------------------
todos_espacamentos = []
arquivos_processados = 0
arquivos_poucos_picos = 0

lista_arquivos = glob.glob(os.path.join(diretorio_dados, padrao_arquivos))
print(f"Total de arquivos encontrados: {len(lista_arquivos)}")

for i, arquivo in enumerate(lista_arquivos):
    try:
        dados = np.loadtxt(arquivo)
        posicoes, condutancias = dados[:, 0], dados[:, 1]
        picos = extrair_maximos(posicoes, condutancias)

        if len(picos) < limite_picos_min:
            arquivos_poucos_picos += 1
            continue

        espacamentos = realizar_unfolding(
            picos,
            grau=grau_polinomio,
            plot=plotar_unfolding and i < 3,  # Plota unfolding de até 3 arquivos
            nome_arquivo=f"unfolding_check_{i}"
        )

        todos_espacamentos.extend(espacamentos)
        arquivos_processados += 1

    except Exception as e:
        print(f"Erro no arquivo {arquivo}: {e}")
        continue

todos_espacamentos = np.array(todos_espacamentos)

print(f"Arquivos processados com sucesso: {arquivos_processados}")
print(f"Arquivos com poucos picos: {arquivos_poucos_picos}")
print(f"N total de espaçamentos acumulados: {len(todos_espacamentos)}")

# ---------------------------------------
# Análise Estatística
# ---------------------------------------
media_s = np.mean(todos_espacamentos)
print(f"Média dos espaçamentos normalizados: ⟨s⟩ = {media_s:.4f}")

conteudo_hist, bin_edges = np.histogram(todos_espacamentos, bins=num_bins, density=True)
area_hist = np.sum(conteudo_hist * np.diff(bin_edges))
print(f"Área total sob o histograma (deve ser ≈1): {area_hist:.4f}")

# ---------------------------------------
# Plotagem do Histograma
# ---------------------------------------
s_vals = np.linspace(0, 5, 1000)
wigner_vals = distribuicao_wigner(s_vals, beta)

plt.figure(figsize=(10, 6))
plt.hist(todos_espacamentos, bins=num_bins, density=True,
         alpha=0.5, color='skyblue', edgecolor='black', label='Dados')
plt.plot(s_vals, wigner_vals, 'r--', label=f'Distribuição de Wigner ($\\beta={beta}$)')

plt.xlabel('Espaçamento Normalizado $s$')
plt.ylabel('Densidade de Probabilidade $P(s)$')
plt.title(f'Distribuição dos Espaçamentos entre Máximos — Ensemble $\\beta={beta}$')
plt.legend(frameon=True, facecolor="white", edgecolor="gray", framealpha=0.5)
plt.tick_params(direction='in', right=True, top=True, color='black')
plt.grid(True, linestyle=':', linewidth=0.5, alpha=0.7)
plt.tight_layout()
plt.savefig(f"histograma_espacamentos_beta{beta}.png", dpi=300)
plt.show()
