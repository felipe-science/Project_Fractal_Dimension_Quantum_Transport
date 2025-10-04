from numpy import loadtxt
import os

inicio = 449
Nfile = 261

for i in range(Nfile):
    os.rename('G'+str(i)+'.dat', 'G'+str(i+inicio)+'.dat')
