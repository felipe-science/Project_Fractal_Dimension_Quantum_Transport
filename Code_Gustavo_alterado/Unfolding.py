import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks
import glob
import os


# Configurações Iniciais
# ---------------------------------------

beta = 1  
diretorio_dados = f'beta1/outputG'
padrao_arquivos = '*.dat'
grau_polinomio = 12
num_bins = 70


# Estilo de Plotagem
# ---------------------------------------

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

# -------------------------------------
# Funções
# ---------------------------------------

def extrair_maximos(posicoes, condutancias):
    indices_picos, _ = find_peaks(condutancias, prominence=0.1)
    return posicoes[indices_picos]

def realizar_unfolding(posicoes, grau):
    posicoes_ordenadas = np.sort(posicoes)
    contagem_acumulada = np.arange(1, len(posicoes_ordenadas) + 1)
    coef = np.polyfit(posicoes_ordenadas, contagem_acumulada, grau)
    polinomio = np.poly1d(coef)
    unfolded = polinomio(posicoes_ordenadas)
    espacamentos = np.diff(unfolded)
    espacamentos = espacamentos[espacamentos > 0]
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

def wigner_cdf(s, beta):
    pdf = distribuicao_wigner(s, beta)
    ds = s[1] - s[0]
    cdf = np.cumsum(pdf) * ds
    return cdf / cdf[-1]  # normaliza para 1


# ---------------------------------------------
# Cria o Vetor Contendo os Espaçamentos Entre Máximos
# ---------------------------------------

todos_espacamentos = []

lista_arquivos = glob.glob(os.path.join(diretorio_dados, padrao_arquivos))
print(f"Total de arquivos encontrados: {len(lista_arquivos)}")

for arquivo in lista_arquivos:
    try:
        dados = np.loadtxt(arquivo)
        posicoes, condutancias = dados[:, 0], dados[:, 1]
        picos = extrair_maximos(posicoes, condutancias)

        if len(picos) < grau_polinomio + 1:
            continue

        espacamentos = realizar_unfolding(picos, grau=grau_polinomio)
        todos_espacamentos.extend(espacamentos)

    except Exception as e:
        print(f"Erro no arquivo {arquivo}: {e}")
        continue

todos_espacamentos = np.array(todos_espacamentos)


# Testes Para Verificar a Média e a Área Normalizada
# ---------------------------------------

media_s = np.mean(todos_espacamentos)
print(f"Média dos espaçamentos normalizados: ⟨s⟩ = {media_s:.4f}")

# Área
conteudo_hist, bin_edges = np.histogram(todos_espacamentos, bins=num_bins, density=True)
area_hist = np.sum(conteudo_hist * np.diff(bin_edges))
print(f"Área total sob o histograma (deve ser ≈1): {area_hist:.4f}")

# -----------------------------------------
# Plotagem do Histograma
# ---------------------------------------

s_vals = np.linspace(0, 4, 1000)
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

# Salvar o Gráfico 
#plt.savefig(f"C:/Users/Amakusa/Desktop/Graficos/Hist_beta{beta}.pdf", format="pdf", bbox_inches="tight", dpi=1000)
plt.show()
