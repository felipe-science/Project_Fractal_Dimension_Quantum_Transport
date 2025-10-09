import numpy as np
import matplotlib.pyplot as plt
import scienceplots


def func(x, a, b):
    return a*x+b


lista = [1.69299998314867, 1.7337284850345407, 1.7822593616403086, 1.8071963635975052, 1.883863022956228]
listb = [0.04038178916560176, 0.552396999428106, 0.4797051074879479, 0.45435203609839553, 0.3072748567545786]


plt.style.use(['science'])
fig, ax = plt.subplots(figsize=(6, 6))


for i in range(5):
    data = np.loadtxt(f"m{i}/outputS/DADOS_BC.dat")
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
plt.title('Shot Noise Power', fontsize=22)
plt.tick_params(labelsize=18)

plt.legend(loc='best', fontsize=16)
plt.savefig('figSd.png', dpi=600)
plt.show()