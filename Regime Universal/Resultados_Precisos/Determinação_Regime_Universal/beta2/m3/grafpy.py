from numpy import loadtxt
from pylab import scatter, show

data = loadtxt("rmsG.dat")

x = data[:,0]
y = data[:,1]

scatter(x,y)
show()