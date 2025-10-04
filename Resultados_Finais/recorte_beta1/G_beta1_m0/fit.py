import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Carregar os dados
data = np.loadtxt('mean_autocorrelation.dat')
x = data[:, 0]
y = data[:, 1]

x = x[:50]
y = y[:50]

# Fixar o valor de gamma (g)
g_fixed = 2.0  # Altere esse valor conforme necessário

# Definir a função modelo com g fixo
def func_fixed_g(x, a, b):
    return 1 / (1 + (x / g_fixed)**(2 * b))**a

# Estimativas iniciais para os parâmetros restantes (a, b)
initial_guess = [1.0, 1.0]  # [a, b]

# Realizar o ajuste
params, covariance = curve_fit(func_fixed_g, x, y, p0=initial_guess)

# Extrair os parâmetros ajustados
a_fit, b_fit = params
print(f"Parâmetros ajustados (com g fixo = {g_fixed}):")
print(f"a = {a_fit:.4f}")
print(f"b = {b_fit:.4f}")

# Calcular o y ajustado
y_fit = func_fixed_g(x, a_fit, b_fit)

# Plotar os dados e o ajuste
plt.figure(figsize=(10, 6))
plt.scatter(x, y, label='Dados experimentais', color='blue')
plt.plot(x, y_fit, label=f'Ajuste (g = {g_fixed})', color='red')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Ajuste não-linear com gamma fixo')
plt.legend()
plt.grid(True)
plt.savefig('ajuste_g_fixo.png')
plt.show()
