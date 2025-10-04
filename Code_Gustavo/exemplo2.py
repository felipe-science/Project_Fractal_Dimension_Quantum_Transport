from   __future__   import division
from   kwant.digest import uniform
import kwant
import numpy as np
import time


## Define the graphene lattice
square = kwant.lattice.square()


##---------------------------------------------------------------------
## Inputs
##---------------------------------------------------------------------
Lx     =  5
Ly     =  20
E0     = -5
Ef     =  5
W      =  5


##---------------------------------------------------------------------
## Constantes
##---------------------------------------------------------------------
dE     = (Ef-E0)/100
t      = 1.0
onsite = 4


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
## Conductance vs Fermi energy
##---------------------------------------------------------------------

def G_E(syst):

    salt = np.random.randint(2000000) # Seed
    t    = time.time()
    f    = open("G.dat","w")
    for E in np.arange(E0,Ef,dE):
         smatrix = kwant.smatrix(syst, energy=E, params=dict(salt=salt))
         G_10    = smatrix.transmission(1,0)
         f.write(("%e %e\n")%(E,G_10))
    f.close()
    t = time.time()-t
    print(("Time = %i s = %f min")%(t,t/60))
    

##---------------------------------------------------------------------
## Main
##---------------------------------------------------------------------

def main():
    syst = make_system().finalized()
    #kwant.plot(syst)
    G_E(syst)

    
if __name__ == '__main__':
    main()
