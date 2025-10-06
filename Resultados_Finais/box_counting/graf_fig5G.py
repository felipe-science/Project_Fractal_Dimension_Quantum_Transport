import numpy as np
import matplotlib.pyplot as plt
import scienceplots


def func(x, a, b):
    return a*x+b

data0 = np.loadtxt("m0/beta1/DADOS_BC.dat")
data1 = np.loadtxt("m1/beta1/DADOS_BC.dat")
data2 = np.loadtxt("m2/beta1/DADOS_BC.dat")
data3 = np.loadtxt("m3/beta1/DADOS_BC.dat")
data4 = np.loadtxt("m4/beta1/DADOS_BC.dat")

lista = [1.5974181512798582, 1.3323851218716511, 1.855296482241495, 1.855296482241495, 1.8803052378904457]
listb = [-0.30562714523289447, 0.3133927486522131,0.5930422998525282, 0.7261773217781983, 0.7038179997151417]


plt.style.use(['science'])
fig, ax = plt.subplots(figsize=(6, 4))


for i in range(5):
    data = np.loadtxt(f"m{i}/beta1/DADOS_BC.dat")
    datax = data[:,0]
    datay = data[:,1]

    x = np.linspace(datax[0], datax[-1],1000)
    y = func(x, lista[i], listb[i])

    plt.scatter(datax, datay, label=rf'$m={i}$')
    plt.plot(x,y, linewidth=2)


plt.xlabel('$log(1/l)$', fontsize=20)
plt.ylabel('$log(N)$', fontsize=20)
plt.title('Conductance', fontsize=22)
plt.tick_params(labelsize=18)

plt.legend(loc='best', fontsize=15)
plt.grid(True)
plt.savefig('fig.png', dpi=600)
plt.show()