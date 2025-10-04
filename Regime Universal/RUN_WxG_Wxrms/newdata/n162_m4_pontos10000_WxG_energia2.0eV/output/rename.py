from numpy import loadtxt
import os

inicio = 869
Nfile = 135

for i in range(Nfile):
    os.rename('G'+str(i)+'.dat', 'G'+str(i+inicio)+'.dat')
