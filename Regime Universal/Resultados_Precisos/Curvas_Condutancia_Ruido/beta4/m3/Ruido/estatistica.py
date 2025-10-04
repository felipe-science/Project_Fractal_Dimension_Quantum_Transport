from numpy import mean, std, loadtxt


data = loadtxt("fractal_dimension.dat",float)

media = mean(data)
desvi = std(data)

print("Média: ",media)
print("Desvio padrão: ",desvi)