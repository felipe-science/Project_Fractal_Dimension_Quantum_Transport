from numpy import loadtxt

Nfile = 101
dados_brutos = loadtxt('Dados_Compilados_E2.0eV_m3_n54_wlead5.txt')
dados = []




image_list = ...
for i in range(Nfile):
    image = open("Desordem"+str(i)+".dat","w")
    dados = dados_brutos[:,i]
    ndados = len(dados)
    
    image.write("# Derodem W = "+str(i)+" (Primeira linha representa a o valor da desordem)\n")
    for n in range(ndados):
	    image.write(str(dados[n])+"\n")
	
    image.close()