from   __future__   import division
from   kwant.digest import uniform
import tinyarray
import kwant
import numpy as np
import time
import os


file_i = 4000
file_f = 4500

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
W0     =  0
Wf     =  5
E      =  1.2


##---------------------------------------------------------------------
## Constantes
##---------------------------------------------------------------------
dW     = (Wf-W0)/100
t      = 1.0 * sigma_0
onsite = 4 * sigma_0


##---------------------------------------------------------------------
## System
##---------------------------------------------------------------------


def area(pos):
    x, y = pos
    return 0<=x<=Lx and 0<=y<=Ly


# Anderson disorder
def disorder(site,salt,W):
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
    for i in range(file_i, file_f,1):
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
    os.system("mkdir output")
    syst = make_system().finalized()
    #kwant.plot(syst)
    G_E(syst)

    
if __name__ == '__main__':
    main()
