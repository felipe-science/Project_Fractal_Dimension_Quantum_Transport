from numpy import loadtxt
from pylab import scatter, plot, show, title, xlabel, ylabel, tick_params, legend, savefig, grid

dataG   = loadtxt("G.dat", float)
datarms = loadtxt("rmsG.dat", float)

W = dataG[:,0]
G = dataG[:,1]
rms = datarms[:,1]


scatter(W, G, color='green')
title("Condutância em função da desordem (E = 2.0 eV)", fontsize='16')
xlabel("W", fontsize='15')
ylabel("<G>", fontsize='15')
tick_params(labelsize=11)
savefig('G_2.0eV.png', format='png')
grid(True)
show()

scatter(W, rms, color='red')
title("rms(G) (E = 2.0 eV)", fontsize='16')
xlabel("W", fontsize='15')
ylabel("rms(G)", fontsize='15')
tick_params(labelsize=11)
grid(True)
savefig('rms_2.0eV.png', format='png')
show()