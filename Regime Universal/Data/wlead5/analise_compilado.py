from numpy import loadtxt, sqrt
from statistics import mean, variance
from pylab import scatter, plot, show, title, xlabel, ylabel, tick_params, legend, savefig


Nfile = 101
dados_brutos = loadtxt('Dados_Compilados_E2.0eV_m3_n54_wlead5.txt')
dados = []

# Separação de dados
for i in range(Nfile):
    dados.append(dados_brutos[:,i])


# Separar em duas listas
def tratamento_dados(dados):

	W = []
	G = []
	aux = []

	N = len(dados)
	for i in range(N):
		valores = dados[i]
		W.append(valores[0])
		
		aux = []
		Ndados = len(valores)
		for n in range(Ndados):
			if(n!=0):
				aux.append(valores[n])
		G.append(aux)
			
	return W,G


def calcular_media(dados):

	W = dados[0]
	valores = dados[1]
	G = []

	Nvalores = len(valores)
	for i in range(Nvalores):
		G.append(mean(valores[i]))

	return W, G

def calcular_variancia(dados):

	W = dados[0]
	valores = dados[1]
	varG = []

	Nvalores = len(valores)
	for i in range(Nvalores):
		varG.append(variance(valores[i]))

	return W, varG

def calcular_rms(dados):

	W = dados[0]
	valores = dados[1]
	rms = []

	Nvalores = len(valores)
	for i in range(Nvalores):

		ndados = len(valores[i])
		dados = valores[i]
		soma = 0
		for j in range(ndados):
			soma = soma+(dados[i]*dados[i])
		rms.append(sqrt(soma/ndados))

	return W, rms

dados_tratados = tratamento_dados(dados)
desordemXmedia = calcular_media(dados_tratados)
desordemXvaria = calcular_variancia(dados_tratados)

W = desordemXmedia[0]
mediaG = desordemXmedia[1]
variaG = desordemXvaria[1]

scatter(W,mediaG, color='green')
title("Condutância em função da desordem (E = 2.0 eV)", fontsize='16')
xlabel("W", fontsize='15')
ylabel("<G>", fontsize='15')
tick_params(labelsize=11)
savefig('media_condutancia_2.0eV.png', format='png')
show()

scatter(W,variaG, color='red')
title("Variância de G em função da desordem (E = 2.0 eV)", fontsize='16')
xlabel("W", fontsize='15')
ylabel("Variancia de G", fontsize='15')
tick_params(labelsize=11)
savefig('desvio_padrao_2.0eV.png', format='png')
show()

print(len(mediaG))

# Imprimir arquivo com as médias
arquivo_mediaG = open('mediaG_N3.dat','w')
arquivo_varian = open('varian_N3.dat', 'w')
for k in range(len(mediaG)):
	arquivo_mediaG.write(str(W[k])+"   "+str(mediaG[k])+"\n")
	arquivo_varian.write(str(W[k])+"   "+str(variaG[k])+"\n")
arquivo_mediaG.close()
arquivo_varian.close()

calcular_rms(dados_tratados)