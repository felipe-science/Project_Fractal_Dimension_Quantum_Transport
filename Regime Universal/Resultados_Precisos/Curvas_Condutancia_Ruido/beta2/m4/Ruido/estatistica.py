from numpy import mean, std, loadtxt


data = loadtxt("data_fractal_dimension.dat",float)

media = mean(data)
desvi = std(data)

print("Média: ",media)
print("Desvio padrão: ",desvi)