from numpy import loadtxt, cov, var, sqrt
from pylab import plot, scatter, show
from random import random

N_row = 7
N_col = 7

autocorrelation_matrix = loadtxt("teste.dat", float)
print(autocorrelation_matrix)

N_row = len(autocorrelation_matrix[:,0])
N_col = len(autocorrelation_matrix[0,:])

coeficientes = []

v0 = autocorrelation_matrix[:,0]
for k in range(N_col):

    vi = autocorrelation_matrix[:,k]
    covariance = cov(v0,vi)
    
    print(covariance)

    pearson = covariance[0,1]/sqrt(covariance[0,0]*covariance[1,1])
    coeficientes.append(pearson)
    
#plot(coeficientes)
#show()
    