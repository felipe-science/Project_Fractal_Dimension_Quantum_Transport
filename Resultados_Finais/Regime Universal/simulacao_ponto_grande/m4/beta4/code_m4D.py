from   __future__   import division
from   kwant.digest import uniform
import tinyarray
import kwant
import numpy as np
import time
from itertools import chain
import shutil

file_i = 3
file_f = 5000

## Define the graphene lattice
square = kwant.lattice.square(norbs=1)

## define Pauli-matrices
sigma_0 = tinyarray.array([[1, 0], [0, 1]])
sigma_x = tinyarray.array([[0, 1], [1, 0]])
sigma_y = tinyarray.array([[0, -1j], [1j, 0]])
sigma_z = tinyarray.array([[1, 0], [0, -1]])


##---------------------------------------------------------------------
## Inputs
##---------------------------------------------------------------------
W0     =  0
Wf     =  1.0
E      =  1.0
a      =  1
L      = 297
Wlead  = 130
Nf     = 4
e_z    = 0.08
alpha  = 0.5

##---------------------------------------------------------------------
## Constantes
##---------------------------------------------------------------------
dW     = (Wf-W0)/10
t      = 1.0 * sigma_0
onsite = 4 * sigma_0*0 + e_z * sigma_z


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
    lat = kwant.lattice.square(a=1, norbs=1)
    syst = kwant.Builder()

    #Criando a região de espalhamento e interação entre vizinhos
    syst[lat.shape(forma_espalhamento, (0, 0))] = disorder
    #syst[lat.neighbors()] = -t
    
    # hoppings in x-direction
    syst[kwant.builder.HoppingKind((1, 0), lat, lat)] = -t * sigma_0 + 1j * alpha * sigma_y / 2
    # hoppings in y-directions
    syst[kwant.builder.HoppingKind((0, 1), lat, lat)] = -t * sigma_0 - 1j * alpha * sigma_x / 2



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

    Ws = np.arange(W0, Wf, dW)
    results = []

    for W in Ws:
        smatrix = kwant.smatrix(syst, energy=E, params=dict(salt=salt, W=W*sigma_0))
        G_10    = smatrix.transmission(1,0)
        results.append([W, G_10])

    results = np.array(results)
    np.savetxt(f"G{i}.dat", results, fmt="%.6e")

    shutil.move(f"G{i}.dat", f"output/G{i}.dat")

    t = time.time()-t
    print(("Simulation = %i, Time = %i s = %f min")%(i,t,t/60))


def G_E(syst):
    for i in range(file_i,file_f,5):
        try:
            f = open(("G0_%i.dat")%(i),"r")
            f.close()
        except Exception:
            try:
                f = open(("output/G0_%i.dat")%(i),"r")
                f.close()
            except Exception:
                run(syst,i)
    

##---------------------------------------------------------------------
## Main
##---------------------------------------------------------------------

def main():
    #os.system("mkdir output")
    syst = criar_sistema_sierpinski()
    kwant.plot(syst)
    G_E(syst)

    
if __name__ == '__main__':
    main()
