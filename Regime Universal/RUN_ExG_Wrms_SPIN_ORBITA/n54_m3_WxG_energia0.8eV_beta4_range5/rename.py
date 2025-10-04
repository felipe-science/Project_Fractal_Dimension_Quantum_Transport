from numpy import loadtxt
import os

inicio = 752
Nfile = 54

for i in range(Nfile):
    os.rename('G'+str(i)+'.dat', 'G'+str(i+inicio)+'.dat')
