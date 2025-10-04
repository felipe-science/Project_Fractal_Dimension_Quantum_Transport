import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


def ro_function(g,a):
    return (1/(2*np.pi))*np.sqrt((12*a*(a+1))/(2*a))

# Carregar os dados
data = np.loadtxt('mean_autocorrelation.dat')
x = data[:, 0]
y = data[:, 1]

#x = x/0.00280365

x = x[:100]
y = y[:100]

# Definir a função modelo
def func(x, a, g):
    return 1 / (1 + (x/g)**(2))**a


# Estimativas iniciais para os parâmetros (ajuste conforme necessário)
initial_guess = [1.0, 1.0]  # [a, b, g]

# Realizar o ajuste
bounds = ([0, 0], [np.inf, np.inf])  # a > 0, g > 0
params, covariance = curve_fit(func, x, y, p0=initial_guess, bounds=bounds)
#params, covariance = curve_fit(func, x, y, p0=initial_guess)

# Extrair os parâmetros ajustados
a_fit, g_fit = params
print(f"Parâmetros ajustados:")
print(f"a = {a_fit:.8f}")
#print(f"b = {b_fit:.4f}")
print(f"g = {g_fit:.8f}")

# Calcular o y ajustado
y_fit = func(x, a_fit, g_fit)

# Plotar os dados e o ajuste
plt.figure(figsize=(10, 6))
plt.scatter(x, y, label='Dados experimentais', color='blue')
plt.plot(x, y_fit, label='Ajuste', color='red')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Ajuste não-linear')
plt.legend()
plt.grid(True)

# Salvar a figura (opcional)
plt.savefig('ajuste.png')
plt.show()



ro = ro_function(g_fit, a_fit)
print(f"density = {ro}")