import kwant
from itertools import chain
from numpy import linspace, exp
from kwant.digest import uniform
from random import random, randint
from pylab import scatter, plot, show, xlabel, ylabel, title


a = 1
t = 1.0
L = 30
W = 5


def criar_sistema(a = a, t = t, L = L, W = W, Ninteracao = 1):


    def onsite(site, params):
        return  params['U0'] * (uniform(repr(site), repr(params['salt'])) - 0.5) + 4 * t

    def hopping(site_i, site_j, params):
        xi, yi = site_i.pos
        xj, yj = site_j.pos
        return -exp(-0.5j * params['phi'] * (xi - xj) * (yi + yj))


    
    def fase_0(coordenadas, syst, lat):

	    xi = coordenadas[0]
	    xf = coordenadas[1]
	    yi = coordenadas[2]
	    yf = coordenadas[3]

	    lado0 = abs(xf-xi)
	    lado1 = lado0/3.0


	    # Excluindo a região central
	    for i in range(int(xi),int(xf)):
		    for j in range(int(yi), int(yf)):
			    if(i >= xi+lado1 and i <= xf-lado1 and j >= yi+lado1 and j <= yf-lado1):
				    del syst[lat(i, j)]


	    #Retornando as coordenadas dos 8 quadrados restantes
	    quadrado1 = [xi,xi+lado1, yi, yi+lado1]
	    quadrado2 = [xi+lado1, xi+2*lado1, yi, yi+lado1]
	    quadrado3 = [xi+2*lado1, xi+3*lado1, yi, yi+lado1]
	    quadrado4 = [xi,xi+lado1, yi+lado1, yi+2*lado1]
	    quadrado5 = [xi+2*lado1, xi+3*lado1, yi+lado1, yi+2*lado1]
	    quadrado6 = [xi,xi+lado1, yi+2*lado1, yi+3*lado1]
	    quadrado7 = [xi+lado1, xi+2*lado1, yi+2*lado1, yi+3*lado1]
	    quadrado8 = [xi+2*lado1, xi+3*lado1, yi+2*lado1, yi+3*lado1]



	    coordenadas_quadrados_restantes = [quadrado1, quadrado2, quadrado3, quadrado4, quadrado5, quadrado6, quadrado7, quadrado8]


	    return syst, coordenadas_quadrados_restantes


    def forma_espalhamento(pos):
            x, y = pos
            return -L/2 <= x <= L/2 and -L/2 <= y <= L/2
    def forma_lead(pos):
        x, y = pos
        return -W/2 <= y <= W/2



    #Gerar uma rede quadrada bidimensional e em seguida gerar o sistema
    lat = kwant.lattice.square(a)
    syst = kwant.Builder()

    #Criando a região de espalhamento e interação entre vizinhos
    syst[lat.shape(forma_espalhamento, (0, 0))] = potential = onsite
    syst[lat.neighbors()] = hopping

    #Gerando o lead do lado esquerdo
    lead = kwant.Builder(kwant.TranslationalSymmetry((-a, 0)))
    lead[lat.shape(forma_lead, (0, 0))] = 4 * t
    lead[lat.neighbors()] = hopping

    #Ativando os lead
    syst.attach_lead(lead)
    syst.attach_lead(lead.reversed())


#    Ninteracao = 2
    Nquadrados = 1
    aux_coord = [[-L/2,L/2,-L/2,L/2]]


    for m in range(Ninteracao):

	    aux = []
	    for k in range(Nquadrados):
		    retorno_da_funcao = fase_0(aux_coord[k],syst,lat)
		    aux.append(retorno_da_funcao[1])

	    syst = retorno_da_funcao[0]
	    aux_coord = list(chain(*aux))
	    Nquadrados = Nquadrados*8

    syst = syst.finalized()
    kwant.plot(syst)

    return syst

#Função retorna a condutancia recebendo (syst, energy, U0, phi)
def condutancia_desordem(sys, energy, U0, phi):

    salt = salt = randint(0, 665768768)    
    params = dict(U0=U0, phi=phi, salt=salt)
    matrizs = kwant.smatrix(sys, energy=energy, args=[params])
    G = matrizs.transmission(1,0)
    return G




sys = criar_sistema()
kwant.plot(sys)


U0 = 0.1
phi = 0
energia = 2.0

Namostras = 1000
Npontos_desordem = 100
image_list = ...
for i in range(Npontos_desordem+1):
	image = open("Desordem"+str(i)+".dat","w")

	
	w = i*0.03
	image.write("# Derodem W = "+str(w)+" (Primeira linha representa a o valor da desordem)\n")
	image.write(str(w)+"\n")
	for n in range(Namostras):
		G = condutancia_desordem(sys, energia, w, phi)
		image.write(str(G)+"\n")
	
	image.close()



