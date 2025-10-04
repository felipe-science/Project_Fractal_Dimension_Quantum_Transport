from   __future__   import division
from   kwant.digest import uniform
import kwant
import numpy as np
import tinyarray
import time
import os
import shutil

file_i = 3000
file_f = 4000

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
Lx     =  45
Ly     =  20
E0     =  0.0
Ef     =  1.2
W      =  2.25


##---------------------------------------------------------------------
## Constantes
##---------------------------------------------------------------------
dE     = (Ef-E0)/2000
W      = W * sigma_0
t      = 1.0 * sigma_0
onsite = 4.0 * sigma_0


##---------------------------------------------------------------------
## System
##---------------------------------------------------------------------


def area(pos):
    x, y = pos
    return 0<=x<=Lx and 0<=y<=Ly


# Anderson disorder
def disorder(site,salt):
    return onsite + W*(uniform(repr(site),repr(salt))-0.5)


def make_system():
    syst = kwant.Builder()
    
    #### Define the scattering region. ####
    syst[square.shape(area, (0, 0))] = disorder
    syst[square.neighbors()] = -t

    ### Define the leads. ####
    
    ## left and rigth
    sym  = kwant.TranslationalSymmetry((-1,0))
    lead = kwant.Builder(sym)
    lead[square.shape(area, (0, 0))] = onsite
    lead[square.neighbors()] = -t
    syst.attach_lead(lead)
    syst.attach_lead(lead.reversed())
    

    return syst


##---------------------------------------------------------------------
## Short noise vs Fermi energy, with fixed W
##---------------------------------------------------------------------

def run(syst,i):

    salt = np.random.randint(2000000) # Seed
    t    = time.time()
    g    = open(f"G{i}.dat", "w")
    f    = open(("sn%s.dat")%(i),"w")
    for E in np.arange(E0,Ef,dE):
        smatrix = kwant.smatrix(syst, energy=E, params=dict(salt=salt))
        sn      = kwant.physics.two_terminal_shotnoise( smatrix )
        G = smatrix.transmission(0,1)
        f.write(("%e %e\n")%(E,sn))
        g.write(("%e %e\n")%(E,G))
    f.close()
    g.close()
    shutil.move(f"sn{i}.dat", f"outputS/sn{i}.dat")
    shutil.move(f"G{i}.dat", f"outputG/G{i}.dat")
    t = time.time()-t
    print(("Simulation = %i, Time = %i s = %f min")%(i,t,t/60))


def sn_E(syst):
    for i in range(file_i, file_f, 1):
        try:
            f = open(("sn0_%i.dat")%(i),"r")
            f.close()
        except Exception:
            try:
                f = open(("output/sn0_%i.dat")%(i),"r")
                f.close()
            except Exception:
                run(syst,i)
    

##---------------------------------------------------------------------
## Main
##---------------------------------------------------------------------

def main():
    syst = make_system().finalized()
    #kwant.plot(syst)
    sn_E(syst)

    
if __name__ == '__main__':
    main()
