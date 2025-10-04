from numpy import loadtxt
from pylab import scatter, plot, show, title, xlabel, ylabel, tick_params, legend, savefig, grid

data = loadtxt("G.dat",float)

W = []
G = []
desordem = data[:,0]
condutan = data[:,1]

for i in range(len(desordem)-65):
    W.append(desordem[i])
    G.append(condutan[i])


scatter(W, G, color='green')
title("Condutância em função da desordem (E = 0.8 eV)", fontsize='16')
xlabel("W", fontsize='15')
ylabel("<G>", fontsize='15')
tick_params(labelsize=11)
grid(True)
savefig('G_0.8eV.png', format='png')
show()