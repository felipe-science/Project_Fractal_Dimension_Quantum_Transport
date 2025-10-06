import numpy as np
import matplotlib.pyplot as plt
import scienceplots


def func(x, a, b):
    return a*x+b


lista = [1.4983443511023662, 1.6886122407504565, 1.422941897557125, 1.6516918578641293, 1.8569694049077219]
listb = [0.10438459993827345, 0.41007408575033505,0.36635119950537476, 0.5297541999544232, 0.5930423004631632]


plt.style.use(['science'])
fig, ax = plt.subplots(figsize=(6, 4))


for i in range(5):
    data = np.loadtxt(f"m{i}/beta2/outputS/DADOS_BC.dat")
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
plt.savefig('figS.png', dpi=600)
plt.show()