import kwant
from numpy import linspace
import biblioteca as bib
from random import random, randint
from kwant.digest import uniform

##---------------------------------------------------------------------
## Inputs
##---------------------------------------------------------------------
L          =  30
Llead      =  30
W          =  3
Ninteracao = 0

syst = bib.criar_sistema_sierpinski(L, Llead, W, Ninteracao)

kwant.plot(syst)



energias = linspace(-4,4,100)
resultado = bib.condutancia_energia(syst,energias)