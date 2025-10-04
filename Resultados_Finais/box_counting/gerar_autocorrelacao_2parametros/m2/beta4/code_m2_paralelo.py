from   __future__   import division
from   kwant.digest import uniform
import tinyarray
import kwant
import numpy as np
import time
from itertools import chain
from pylab import scatter, plot, show, xlabel, ylabel, title, figure, tick_params, savefig
import shutil
from joblib import Parallel, delayed   # <-- paralelização

file_i = 126
file_f = 500

## define Pauli-matrices
sigma_0 = tinyarray.array([[1, 0], [0, 1]])
sigma_x = tinyarray.array([[0, 1], [1, 0]])
sigma_y = tinyarray.array([[0, -1j], [1j, 0]])
sigma_z = tinyarray.array([[1, 0], [0, -1]])


##---------------------------------------------------------------------
## Inputs
##---------------------------------------------------------------------
E0     =  0
Ef     =  0.02
W      =  0.50
a      =  1
L      = 297
Wlead  = 115
Nf     = 2
e_z    = 0.08
alpha  = 0.5

##---------------------------------------------------------------------
## Constantes
##---------------------------------------------------------------------
dE     = (Ef-E0)/100
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
    lat = kwant.lattice.square(a, norbs=1)
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



def calc_smatrix(E, syst, salt, W):
    smatrix = kwant.smatrix(syst, energy=E, params=dict(salt=salt, W=W*sigma_0))
    G_10 = smatrix.transmission(1, 0)
    sn = kwant.physics.two_terminal_shotnoise(smatrix)
    return E, G_10, sn, smatrix.num_propagating(0)

def G_E_desordemfixa(syst, l):
    energies = np.arange(E0, Ef, dE)
    salt = np.random.randint(2000000)  # Seed

    t0 = time.time()

    # Paralelizar cálculos em energias
    results = Parallel(n_jobs=-1)(
        delayed(calc_smatrix)(E, syst, salt, W) for E in energies
    )

    # Separar resultados
    energies, conductance, shotnoise, n_modes = zip(*results)

    # Salvar arquivos
    np.savetxt(f"G{l}.dat", np.column_stack((energies, conductance)))
    np.savetxt(f"S{l}.dat", np.column_stack((energies, shotnoise)))

    
    if l == file_i:
        print(f"\nNúmero de modos para E = {Ef} eV: {n_modes[-1]}")

    deltat = time.time() - t0
    print(f"run = {l}  Time = {round(deltat/60,2)} min")

##---------------------------------------------------------------------
## Main
##---------------------------------------------------------------------
def main():
    syst = criar_sistema_sierpinski()
    kwant.plot(syst)

    for l in range(file_i, file_f, 1):
        G_E_desordemfixa(syst, l)
        shutil.move(f"G{l}.dat", f"outputG/G{l}.dat")
        shutil.move(f"S{l}.dat", f"outputS/S{l}.dat")

if __name__ == '__main__':
    main()
