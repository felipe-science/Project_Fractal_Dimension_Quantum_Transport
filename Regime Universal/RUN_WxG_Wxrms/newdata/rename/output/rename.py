from numpy import loadtxt
import os

inicio = 317
Nfile = 19

for i in range(Nfile):
    os.rename('G'+str(i)+'.dat', 'G'+str(i+inicio)+'.dat')
