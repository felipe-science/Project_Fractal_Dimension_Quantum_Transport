import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Carregar os dados
data = np.loadtxt('mean_autocorrelation.dat')
x = data[:, 0]
y = data[:, 1]

x = x[:50]
y = y[:50]

# Definir a função modelo
def func(x, a, b, g):
    return 1 / (1 + (x/g)**(2*b))**a


def density_fit(g,a,b):
    return (1/(2*np.pi))*np.sqrt((6*b*(a+1))/(g**2))

# Estimativas iniciais para os parâmetros (ajuste conforme necessário)
initial_guess = [1.0, 1.0, 1.0]  # [a, b, g]

# Realizar o ajuste
params, covariance = curve_fit(func, x, y, p0=initial_guess)

# Extrair os parâmetros ajustados
a_fit, b_fit, g_fit = params
print(f"Parâmetros ajustados:")
print(f"a = {a_fit:.8f}")
print(f"b = {b_fit:.8f}")
print(f"g = {g_fit:.8f}")

# Calcular o y ajustado
y_fit = func(x, a_fit, b_fit, g_fit)

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

g_fit = 1
print(f"Density fit: {density_fit(g_fit,a_fit,b_fit)}")