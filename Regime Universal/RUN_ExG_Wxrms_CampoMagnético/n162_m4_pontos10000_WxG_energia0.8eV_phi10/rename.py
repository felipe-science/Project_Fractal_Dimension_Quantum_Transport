from numpy import loadtxt
import os

inicio = 494
Nfile = 250

for i in range(Nfile):
    os.rename('G'+str(i)+'.dat', 'G'+str(i+inicio)+'.dat')
