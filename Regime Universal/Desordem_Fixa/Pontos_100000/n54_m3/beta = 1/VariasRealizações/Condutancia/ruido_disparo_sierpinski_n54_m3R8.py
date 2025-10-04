from   __future__   import division
from   kwant.digest import uniform
import tinyarray
import kwant
import numpy as np
import time
import os
from itertools import chain
from pylab import scatter, plot, show, xlabel, ylabel, title, figure, tick_params, savefig


## Define the graphene lattice
square = kwant.lattice.square()


## define Pauli-matrices
sigma_0 = tinyarray.array([[1, 0], [0, 1]])
sigma_x = tinyarray.array([[0, 1], [1, 0]])
sigma_y = tinyarray.array([[0, -1j], [1j, 0]])
sigma_z = tinyarray.array([[1, 0], [0, -1]])


##---------------------------------------------------------------------
## Inputs
##---------------------------------------------------------------------
E0     =  -5
Ef     =  +5
W      =  0.80
a      =  1
L      = 53
Wlead  = 5
Nf     = 3

##---------------------------------------------------------------------
## Constantes
##---------------------------------------------------------------------
dE     = (Ef-E0)/100000
t      = 1.0 * sigma_0
onsite = 4 * sigma_0*0


##---------------------------------------------------------------------
## System
##---------------------------------------------------------------------

# Anderson disorder
def disorder(site,salt,W):
    return onsite + W*(uniform(repr(site),repr(salt))-0.5)

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
    syst[lat.shape(forma_espalhamento, (0, 0))] = disorder
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





##---------------------------------------------------------------------
## Conductance vs disorder strength, with fixed Fermi energy
##---------------------------------------------------------------------

def run(syst,i):

    salt = np.random.randint(2000000) # Seed
    t    = time.time()
    f    = open(("G%s.dat")%(i),"w")
    for W in np.arange(W0,Wf,dW):
         smatrix = kwant.smatrix(syst, energy=E, params=dict(salt=salt, W=W*sigma_0))
         G_10    = smatrix.transmission(1,0)
         f.write(("%e %e\n")%(W,G_10))
    f.close()
    os.system(("mv G%i.dat    output/")%(i))
    t = time.time()-t
    print(("Simulation = %i, Time = %i s = %f min")%(i,t,t/60))


def G_E(syst):
    for i in range(1000):
        try:
            f = open(("G0_%i.dat")%(i),"r")
            f.close()
        except Exception:
            try:
                f = open(("output/G0_%i.dat")%(i),"r")
                f.close()
            except Exception:
                run(syst,i)
    



def ShootNoise_E_desordemfixa(syst):
    
    shootnoi = []
    energies = np.arange(E0,Ef,dE)

    salt = np.random.randint(2000000) # Seed
    t = time.time()
    f = open("SN_m"+str(Nf)+"_n"+str(L)+"R8.dat","w")
    for E in energies:
        smatrix = kwant.smatrix(syst, energy=E, params=dict(salt=salt, W=W*sigma_0))
        sn      = kwant.physics.two_terminal_shotnoise(smatrix)
        shootnoi.append(sn)
        f.write(("%e %e\n")%(E,sn))
        porc = (E+5)*10
        print(round(porc,2),"%")
         
    f.close()
    t = time.time()-t
    print(("Time = %i s = %f min")%(t,t/60))
    print("\nNúmero de modos para E =",Ef,"eV:",smatrix.num_propagating(0))
    

    figure()
    plot(energies, shootnoi)
    title("Ruido de disparo", fontsize='14')
    xlabel("Energia [t]", fontsize='13')
    ylabel("Ruído de disparo", fontsize='13')
    tick_params(labelsize = 13)
    savefig(("shootnoise_sierpins_m%i_n%i.png")%(Nf,L))
    show()


##---------------------------------------------------------------------
## Main
##---------------------------------------------------------------------

def main():
    #os.system("mkdir output")
    syst = criar_sistema_sierpinski()
    #kwant.plot(syst)
    ShootNoise_E_desordemfixa(syst)

    
if __name__ == '__main__':
    main()
