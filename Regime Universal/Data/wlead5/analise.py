import os
from numpy import loadtxt, sqrt
from statistics import mean, variance
from pylab import scatter, plot, show, title, xlabel, ylabel, tick_params, legend, savefig


mediaG = []
variaG = []
disord = []
rms = []

Nfile = 101
for i in range(Nfile):
    dados = loadtxt('Desordem'+str(i)+'.dat')

    disord.append(dados[0])
    mediaG.append(mean(dados))
    variaG.append(variance(dados))
    rms.append(sqrt(variance(dados)))


scatter(disord, mediaG, color='green')
title("Condutância em função da desordem (E = 2.0 eV)", fontsize='16')
xlabel("W", fontsize='15')
ylabel("<G>", fontsize='15')
tick_params(labelsize=11)
savefig('media_condutancia_2.0eV.png', format='png')
show()

scatter(disord, variaG, color='red')
title("Variância de G em função da desordem (E = 2.0 eV)", fontsize='16')
xlabel("W", fontsize='15')
ylabel("Variancia de G", fontsize='15')
tick_params(labelsize=11)
savefig('variancia_2.0eV.png', format='png')
show()

scatter(disord, rms, color='red')
title("rms(G) em função da desordem (E = 2.0 eV)", fontsize='16')
xlabel("W", fontsize='15')
ylabel("rms(G)", fontsize='15')
tick_params(labelsize=11)
savefig('rms_2.0eV.png', format='png')
show()

print(len(mediaG))

# Imprimir arquivo com as médias
arquivo_mediaG = open('mediaG_N3.dat','w')
arquivo_varian = open('varian_N3.dat', 'w')
arquivo_rms    = open('rms_N3','w')
for k in range(len(mediaG)):
    arquivo_mediaG.write(str(disord[k])+"   "+str(mediaG[k])+"\n")
    arquivo_varian.write(str(disord[k])+"   "+str(variaG[k])+"\n")
    arquivo_rms.write(str(disord[k])+"   "+str(rms[k])+"\n")
arquivo_mediaG.close()
arquivo_varian.close()
arquivo_rms.close()


os.system("mkdir Resultados")
os.system("mv mediaG_N3.dat    Resultados/")
os.system("mv varian_N3.dat    Resultados/")
os.system("mv rms_N3    Resultados/")
os.system("mv rms_2.0eV.png    Resultados/")
os.system("mv variancia_2.0eV.png    Resultados/")
os.system("mv media_condutancia_2.0eV.png    Resultados/")
