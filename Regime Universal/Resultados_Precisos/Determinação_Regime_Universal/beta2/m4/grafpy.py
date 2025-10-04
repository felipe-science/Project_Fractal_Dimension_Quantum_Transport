from numpy import loadtxt, linspace
from pylab import scatter, show, plot

data = loadtxt("rmsG.dat")

x = data[:,0]
y = data[:,1]


xline = linspace(x[0],x[-1], 1000)
yline = []
for k in range(1000):
    yline.append(0.52)

plot(xline, yline, color='red')

scatter(x,y)
show()