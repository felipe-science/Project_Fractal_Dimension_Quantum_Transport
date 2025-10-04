from numpy import loadtxt
from pylab import scatter, plot, show, title, xlabel, ylabel, tick_params, legend, savefig, grid

dataG   = loadtxt("G.dat", float)
datarms = loadtxt("rmsG.dat", float)

W = dataG[:,0]
G = dataG[:,1]
rms = datarms[:,1]


scatter(W, G, color='green')
title("Condutância em função da desordem ", fontsize='16')
xlabel("W", fontsize='15')
ylabel("<G>", fontsize='15')
tick_params(labelsize=11)
grid(True)
savefig('G_0.8eV.png', format='png')
show()

scatter(W, rms, color='red')
title("rms(G) ", fontsize='16')
xlabel("W", fontsize='15')
ylabel("rms(G)", fontsize='15')
tick_params(labelsize=11)
grid(True)
savefig('rms_0.8eV.png', format='png')
show()