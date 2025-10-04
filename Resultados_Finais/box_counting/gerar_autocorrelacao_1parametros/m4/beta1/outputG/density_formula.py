import numpy as np
import matplotlib.pyplot as plt

def rho(alpha, beta, gamma):
    return (1/(2*np.pi*gamma))*np.sqrt(6*beta*(alpha+1))


alpha = 1.4683616980965866
beta = 0.7711334470395808
gamma = 1.0000162713593954

density = rho(alpha, beta, gamma)
print(density)