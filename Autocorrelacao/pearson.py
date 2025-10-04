from numpy import loadtxt, cov, var

data = loadtxt("G_m3_n53.dat",float)

energia = data[:,0]
conduta = data[:,1]

covariancia = cov(energia,conduta)

print(covariancia)