import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("S0.dat")
plt.plot(data[:,0], data[:,1])
plt.show()


x = data[:,0]
y = data[:,1]

y = y/(5.5/2)
x = (x+2)/2

plt.plot(x,y)
plt.show()

f = open("Snew.dat","w")
for i in range(len(x)):
    f.write(f"{x[i]} {y[i]}\n")
f.close()