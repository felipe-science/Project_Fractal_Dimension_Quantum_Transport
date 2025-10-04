import kwant
import time
import tinyarray
from itertools import chain
from numpy import linspace, exp, arange, transpose, conjugate, dot, zeros, trace
from kwant.digest import uniform
from random import random, randint
from pylab import scatter, plot, show, xlabel, ylabel, title, figure, tick_params, savefig

## define Pauli-matrices
sigma_0 = tinyarray.array([[1, 0], [0, 1]])
sigma_x = tinyarray.array([[0, 1], [1, 0]])
sigma_y = tinyarray.array([[0, -1j], [1j, 0]])
sigma_z = tinyarray.array([[1, 0], [0, -1]])

##---------------------------------------------------------------------
## Inputs
##---------------------------------------------------------------------
L      =  53
Wlead  =  10
E0     =  -0.5
Ef     =  +0.5
W      =  0
Nf     =  3

##---------------------------------------------------------------------
## Constantes
##---------------------------------------------------------------------
dE     = (Ef-E0)/100000
W      = W * sigma_0
t      = 1.0
a      = 1
onsite = 0


def criar_sistema_sierpinski():

 
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
        return -Wlead/2 <= y <= Wlead/2


    #Gerar uma rede quadrada bidimensional e em seguida gerar o sistema
    lat = kwant.lattice.square(a)
    syst = kwant.Builder()

    #Criando a região de espalhamento e interação entre vizinhos
    syst[lat.shape(forma_espalhamento, (0, 0))] = potential = onsite
    syst[lat.neighbors()] = -t

    #Gerando o lead do lado esquerdo
    lead = kwant.Builder(kwant.TranslationalSymmetry((-a, 0)))
    lead[lat.shape(forma_lead, (0, 0))] = onsite
    lead[lat.neighbors()] = -t

    #Ativando os lead
    syst.attach_lead(lead)
    syst.attach_lead(lead.reversed())


    Nquadrados = 1
    aux_coord = [[-L/2,L/2,-L/2,L/2]]


    for m in range(Nf):

	    aux = []
	    for k in range(Nquadrados):
		    retorno_da_funcao = fase_0(aux_coord[k],syst,lat)
		    aux.append(retorno_da_funcao[1])

	    syst = retorno_da_funcao[0]
	    aux_coord = list(chain(*aux))
	    Nquadrados = Nquadrados*8

    syst = syst.finalized()
    
    return syst


def G_E(syst):
    
    condutan = []
    energies = arange(E0,Ef,dE)

    t = time.time()
    f = open("G_m"+str(Nf)+"_n"+str(L)+".dat","w")
    for E in energies:
         smatrix = kwant.smatrix(syst, energy=E)
         G_10    = smatrix.transmission(1,0)
         condutan.append(G_10)
         f.write(("%e %e\n")%(E,G_10))
    f.close()
    t = time.time()-t
    print(("Time = %i s = %f min")%(t,t/60))
    print("\nNúmero de modos para E =",Ef,"eV:",smatrix.num_propagating(0))
    

    figure()
    plot(energies, condutan)
    title("Condutância", fontsize='14')
    xlabel("Energia [t]", fontsize='13')
    ylabel("Condutância [e^2/h]", fontsize='13')
    tick_params(labelsize = 13)
    savefig(("condutancia_sierpins_m%i_n%i.png")%(Nf,L))
    show()


syst = criar_sistema_sierpinski()
kwant.plot(syst)


G_E(syst)