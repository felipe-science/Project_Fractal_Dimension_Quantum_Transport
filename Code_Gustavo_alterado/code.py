from   __future__   import division
from   kwant.digest import uniform
import tinyarray
import kwant
import numpy as np
import time
import os


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
N      =  12
Ly     =  50
dy     =  15
E      =  1.5
W0     =  0
Wf     =  1.5
way    = "/content/drive/MyDrive/DADOS/research/research_2021/fibonacci/square/model_1/disorder/find_W/Ly50_dy15_00_11/N12/"

##---------------------------------------------------------------------
## Constantes
##---------------------------------------------------------------------
dW     = (Wf-W0)/40
t      = 1.0 * sigma_0
onsite = 4 * sigma_0


##---------------------------------------------------------------------
## Fibonacci
##---------------------------------------------------------------------

def fibonacci():
    m0 = "0"
    m1 = "1"
    M  = m0 + m1
    for i in range(N):
        m  = m0+m1
        M += m
        m0 = m1
        m1 = m
    return M


##---------------------------------------------------------------------
## System
##---------------------------------------------------------------------


# Anderson disorder
def disorder(site,salt,W):
    return onsite + W*(uniform(repr(site),repr(salt))-0.5)


def make_system():
    syst = kwant.Builder()

    
    #### Define the scattering region. ####
    for i in range(1+len(fibonacci())):
        for j in range(Ly):
            syst[square(i,j)] = disorder
    syst[square.neighbors()] = -t


    ### Define the leads. ####
    
    ## left and rigth
    sym  = kwant.TranslationalSymmetry((-1,0))
    lead = kwant.Builder(sym)
    for i in range(3):
        for j in range(Ly):
            lead[square(i,j)] = onsite
    lead[square.neighbors()] = -t
    syst.attach_lead(lead)
    syst.attach_lead(lead.reversed())
    

    return syst


##---------------------------------------------------------------------
## Remove atoms
##---------------------------------------------------------------------
def removeAtoms(syst):

    F = fibonacci()
    n = 0
    for i in range(len(F)):
        n += 1
        if F[i] == "0":
            for j in np.arange(dy,Ly-dy):
                del syst[square(n,j)]

    return syst
    

##---------------------------------------------------------------------
## Number of propagation modes
##---------------------------------------------------------------------

def num_propagating(syst):
    smatrix = kwant.smatrix(syst, energy=E, params=dict(salt=0, W=0*sigma_0))
    print(smatrix.num_propagating(0))


##---------------------------------------------------------------------
## Conductance vs disorder strength, with fixed Fermi energy
##---------------------------------------------------------------------

def run(syst,i):

    salt = np.random.randint(2000000) # Seed
    t    = time.time()
    f    = open(("G%i.dat")%(i),"w")
    for W in np.arange(W0,Wf,dW):
         smatrix = kwant.smatrix(syst, energy=E, params=dict(salt=salt,W=W*sigma_0))
         G_10    = smatrix.transmission(1,0)
         f.write(("%e %e\n")%(W,G_10))
    f.close()
    os.system(("mv G%i.dat    "+way+"output/")%(i))
    t = time.time()-t
    print(("Simulation = %i, Time = %i s = %f min")%(i,t,t/60))



def G_E(syst):
    for i in range(2000):
        try:
            f = open(("G%i.dat")%(i),"r")
            f.close()
        except Exception:
            try:
                f = open((way+"output/G%i.dat")%(i),"r")
                f.close()
            except Exception:
                run(syst,i)
    

##---------------------------------------------------------------------
## Main
##---------------------------------------------------------------------

def main():
    os.system("mkdir "+way+"output")
    syst = make_system()
    syst = removeAtoms(syst).finalized()
    #kwant.plot(syst)
    #num_propagating(syst)
    G_E(syst)

    
if __name__ == '__main__':
    main()
