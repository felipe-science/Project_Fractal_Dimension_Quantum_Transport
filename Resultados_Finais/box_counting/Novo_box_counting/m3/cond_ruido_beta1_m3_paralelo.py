from __future__ import division
from kwant.digest import uniform
import tinyarray
import kwant
import numpy as np
import time
import os
from itertools import chain
from pylab import show
import shutil
from joblib import Parallel, delayed   # <-- paralelização

file_i = 0
file_f = 1


## define Pauli-matrices
sigma_0 = tinyarray.array([[1, 0], [0, 1]])
sigma_x = tinyarray.array([[0, 1], [1, 0]])
sigma_y = tinyarray.array([[0, -1j], [1j, 0]])
sigma_z = tinyarray.array([[1, 0], [0, -1]])

##---------------------------------------------------------------------
## Inputs
##---------------------------------------------------------------------
E0     =  -0.5
Ef     =  +0.5
W      =  0.703
a      =  1
L      = 297
Wlead  = 25
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

# Anderson disorder (função dependente de salt e W)
def disorder(site, salt, W):
    return onsite + W*(uniform(repr(site), repr(salt)) - 0.5)

def criar_sistema_sierpinski():
    def fase_0(coordenadas, syst, lat):
        xi, xf, yi, yf = coordenadas
        lado0 = abs(xf - xi)
        lado1 = lado0 / 3.0

        # Excluindo a região central
        for i in range(int(xi), int(xf)):
            for j in range(int(yi), int(yf)):
                if (i >= xi + lado1 and i <= xf - lado1 and
                    j >= yi + lado1 and j <= yf - lado1):
                    del syst[lat(i, j)]

        # Retornando coordenadas dos 8 quadrados restantes
        quadrados = [
            [xi, xi+lado1, yi, yi+lado1],
            [xi+lado1, xi+2*lado1, yi, yi+lado1],
            [xi+2*lado1, xi+3*lado1, yi, yi+lado1],
            [xi, xi+lado1, yi+lado1, yi+2*lado1],
            [xi+2*lado1, xi+3*lado1, yi+lado1, yi+2*lado1],
            [xi, xi+lado1, yi+2*lado1, yi+3*lado1],
            [xi+lado1, xi+2*lado1, yi+2*lado1, yi+3*lado1],
            [xi+2*lado1, xi+3*lado1, yi+2*lado1, yi+3*lado1],
        ]
        return syst, quadrados

    def forma_espalhamento(pos):
        x, y = pos
        return -L/2 <= x <= L/2 and -L/2 <= y <= L/2

    def forma_lead(pos):
        x, y = pos
        return -Wlead/2 <= y <= Wlead/2

    lat = kwant.lattice.square(a, norbs=2)
    syst = kwant.Builder()

    # Região de espalhamento com desordem
    syst[lat.shape(forma_espalhamento, (0, 0))] = disorder
    syst[lat.neighbors()] = -t

    # Lead esquerdo
    lead = kwant.Builder(kwant.TranslationalSymmetry((-a, 0)))
    lead[lat.shape(forma_lead, (0, 0))] = onsite
    lead[lat.neighbors()] = -t

    # Ativando leads
    syst.attach_lead(lead)
    syst.attach_lead(lead.reversed())

    Nquadrados = 1
    aux_coord = [[-L/2, L/2, -L/2, L/2]]

    for m in range(Nf):
        aux = []
        for k in range(Nquadrados):
            retorno_da_funcao = fase_0(aux_coord[k], syst, lat)
            aux.append(retorno_da_funcao[1])
        syst = retorno_da_funcao[0]
        aux_coord = list(chain(*aux))
        Nquadrados *= 8

    return syst.finalized()

##---------------------------------------------------------------------
## Funções auxiliares
##---------------------------------------------------------------------

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

