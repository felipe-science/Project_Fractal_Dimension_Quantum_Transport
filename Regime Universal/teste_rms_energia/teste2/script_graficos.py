from numpy import loadtxt
from pylab import scatter, plot, show, title, xlabel, ylabel, tick_params, legend, savefig, grid

dataG   = loadtxt("G.dat", float)
datarms = loadtxt("rmsG.dat", float)

W = dataG[:,0]
G = dataG[:,1]
rms = datarms[:,1]


scatter(W, G, color='green')
title("Condutância em função da desordem (W = 0.72)", fontsize='16')
xlabel("E", fontsize='15')
ylabel("<G>", fontsize='15')
tick_params(labelsize=11)
grid(True)
savefig('G_W0.72.png', format='png')
show()

scatter(W, rms, color='red')
title("rms(G) (W = 0.72)", fontsize='16')
xlabel("E", fontsize='15')
ylabel("rms(G)", fontsize='15')
tick_params(labelsize=11)
grid(True)
savefig('rms_W0.72.png', format='png')
show()