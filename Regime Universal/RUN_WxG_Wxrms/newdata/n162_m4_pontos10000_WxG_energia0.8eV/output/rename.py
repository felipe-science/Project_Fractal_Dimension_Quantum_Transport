from numpy import loadtxt
import os

inicio = 850
Nfile = 161

for i in range(Nfile):
    os.rename('G'+str(i)+'.dat', 'G'+str(i+inicio)+'.dat')
