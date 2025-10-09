import numpy as np
import matplotlib.pyplot as plt
import scienceplots


def func(x, a, b):
    return a*x+b

data0 = np.loadtxt("m0/outputG/DADOS_BC.dat")
data1 = np.loadtxt("m1/outputG/DADOS_BC.dat")
data2 = np.loadtxt("m2/outputG/DADOS_BC.dat")
data3 = np.loadtxt("m3/outputG/DADOS_BC.dat")
data4 = np.loadtxt("m4/outputG/DADOS_BC.dat")

lista = [1.6902240401864572, 1.7892451394257116, 1.8455150412894314, 1.8583650892009613, 1.8820611141335446]
listb = [0.4900155715480123, 0.683435321297555,0.8055342499333561, 0.5069003573854317, 0.5905672855249632]


plt.style.use(['science'])
fig, ax = plt.subplots(figsize=(6, 6))


for i in range(5):
    data = np.loadtxt(f"m{i}/outputG/DADOS_BC.dat")
    datax = data[:,0]
    datay = data[:,1]

    x = np.linspace(datax[0], datax[-1],1000)
    y = func(x, lista[i], listb[i])

    y = y-y[0]
    datay = datay-datay[0]

    plt.scatter(datax, datay, label=rf'$m={i}$; $tan(\theta)={round(lista[i],2)}$')
    plt.plot(x,y, linewidth=2)


plt.xlabel('$log(1/l)$', fontsize=20)
plt.ylabel('$log(N)$', fontsize=20)
plt.title('Conductance', fontsize=22)
plt.tick_params(labelsize=18)

plt.legend(loc='best', fontsize=16)
plt.savefig('figGd.png', dpi=600)
plt.show()