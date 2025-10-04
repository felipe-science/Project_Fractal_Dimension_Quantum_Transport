from numpy import loadtxt, linspace
from pylab import scatter, plot, show, title, xlabel, ylabel, tick_params, legend, savefig, grid

dataG   = loadtxt("G.dat", float)
datarms = loadtxt("rmsG.dat", float)

W = dataG[:,0]
G = dataG[:,1]
rms = datarms[:,1]


linex_beta1 = linspace(W[0], datarms[-1], 10000)
liney_beta1 = []
for i in range(len(linex_beta1)):
    liney_beta1.append(0.74)



scatter(W, G, color='green')
title("Condutância em função da desordem ", fontsize='16')
xlabel("W", fontsize='15')
ylabel("<G>", fontsize='15')
tick_params(labelsize=11)
grid(True)
savefig('G_0.8eV.png', format='png')
show()

plot(linex_beta1, liney_beta1, linestyle='--')
scatter(W, rms, color='red')
title("rms(G)", fontsize='16')
xlabel("W", fontsize='15')
ylabel("rms(G)", fontsize='15')
tick_params(labelsize=11)
grid(True)
savefig('rms_0.8eV.png', format='png')
show()