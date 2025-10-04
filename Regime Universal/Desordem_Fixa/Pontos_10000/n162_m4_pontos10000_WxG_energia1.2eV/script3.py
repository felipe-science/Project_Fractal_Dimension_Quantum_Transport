import os
import numpy as np


## --------------------------------------------------------------------------
## Number of files
## --------------------------------------------------------------------------


def numberOfFiles():
    for i in range(20000):
        try:
            f = open(("output/G%i.dat")%(i),"r")
            f.close()
        except Exception:
            return i


## --------------------------------------------------------------------------
## Number of files
## --------------------------------------------------------------------------


def Number_of_steps():
    f = open("output/G0.dat","r")
    i = f.readline().split()
    N = 0
    while True:
        if len(i) == 0:
            break
        N += 1
        i  = f.readline().split()
    f.close()
    return N


## --------------------------------------------------------------------------
## Average and variance
## --------------------------------------------------------------------------


def vec_x(FILE):
    f = open(FILE,"r")
    i = f.readline().split()
    x = []
    while True:
        if len(i) == 0:
            break
        x += [float(i[0])]
        i  = f.readline().split()
    f.close()
    return x


def averageAndVariance(Nf,N):

    x    = vec_x("output/G0.dat")
    y_0  = np.zeros(N)
    y2_0 = np.zeros(N)


    ## Get data
    for i in range(Nf):
        f = open(("output/G%i.dat")%(i),"r")
        for j in range(N):
            k = f.readline().split()
            G = float(k[1])

            y_0[j]  += G
            y2_0[j] += G*G

        f.close()

    y_0  /= Nf
    y2_0 /= Nf


    ## Averege
    f = open("G.dat","w")
    for i in range(N):
        f.write(("%e %e \n")%(x[i],y_0[i]))
    f.close()


    ## Variance
    f = open("rmsG.dat","w")
    for i in range(N):
        rmsG = np.sqrt(y2_0[i]-y_0[i]**2)
        f.write(("%e %e \n")%(x[i],rmsG))
    f.close()


## --------------------------------------------------------------------------
## Main
## --------------------------------------------------------------------------


def main():
    Nf = numberOfFiles()
    print("Number of files = ",Nf)
    
    N  = Number_of_steps()
    averageAndVariance(Nf,N)
    
    

if __name__ == '__main__':
    main()
