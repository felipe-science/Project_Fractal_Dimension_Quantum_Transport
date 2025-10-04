import kwant
import tinyarray
from itertools import chain
from numpy import linspace, exp
from kwant.digest import uniform
from random import random, randint
from pylab import scatter, plot, show, xlabel, ylabel, title, figure, tick_params, savefig


## define Pauli-matrices
sigma_0 = tinyarray.array([[1, 0], [0, 1]])
sigma_x = tinyarray.array([[0, 1], [1, 0]])
sigma_y = tinyarray.array([[0, -1j], [1j, 0]])
sigma_z = tinyarray.array([[1, 0], [0, -1]])


##---------------------------------------------------------------------
## Constantes
##---------------------------------------------------------------------
t      = 1.0 * sigma_0
a      = 1
onsite = 4.0 * sigma_0


def condutancia_energia(syst, energies):
    # Compute transmission as a function of energy
    data = []
    for energy in energies:
        smatrix = kwant.smatrix(syst, energy)
        data.append(smatrix.transmission(0, 1))

    return energias, data


def criar_sistema_sierpinski(L, Llead, W, Ninteracao):

    def onsite(site, salt, W):
        return onsite + (W*sigma_0)*(uniform(repr(site),repr(salt))-0.5)
                                

    def hopping(site_i, site_j, params):
        xi, yi = site_i.pos
        xj, yj = site_j.pos
        return -exp(-0.5j * params['phi'] * (xi - xj) * (yi + yj))*t

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
        return -Llead/2 <= y <= Llead/2


    #Gerar uma rede quadrada bidimensional e em seguida gerar o sistema
    lat = kwant.lattice.square(a)
    syst = kwant.Builder()

    #Criando a região de espalhamento e interação entre vizinhos
    syst[lat.shape(forma_espalhamento, (0, 0))] = onsite
    syst[lat.neighbors()] = hopping

    #Gerando o lead do lado esquerdo
    lead = kwant.Builder(kwant.TranslationalSymmetry((-a, 0)))
    lead[lat.shape(forma_lead, (0, 0))] = 4 * t
    lead[lat.neighbors()] = hopping

    #Ativando os lead
    syst.attach_lead(lead)
    syst.attach_lead(lead.reversed())


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
    
    return syst

