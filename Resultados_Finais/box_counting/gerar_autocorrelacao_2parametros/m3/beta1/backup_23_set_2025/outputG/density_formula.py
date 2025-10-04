import numpy as np
import matplotlib.pyplot as plt

def rho(alpha, beta, gamma):
    return (1/(2*np.pi*gamma))*np.sqrt(6*beta*(alpha+1))


alpha = 0.3790999493265258
beta = 0.7624749629714177
gamma = 1.0000002009395756

density = rho(alpha, beta, gamma)
print(density)