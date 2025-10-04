from numpy import loadtxt
import os

inicio = 2928
Nfile = 1000

for i in range(Nfile):
    os.rename('G'+str(i)+'.dat', 'G'+str(i+inicio)+'.dat')
