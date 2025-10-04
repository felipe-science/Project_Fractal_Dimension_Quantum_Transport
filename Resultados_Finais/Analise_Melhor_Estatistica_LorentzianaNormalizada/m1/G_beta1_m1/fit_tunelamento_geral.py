import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Definir a função lorentziana generalizada com tratamento de erro
def f_oficial(delta_epsilon, g, x):
    # Evitar divisão por zero
    g = max(g, 1e-10)  # Define um valor mínimo para Gamma
    return 1 / ((1 + ((delta_epsilon / g) ** 2))) ** x

def f1(delta_epsilon, g):
    g = max(g, 1e-10)  # Define um valor mínimo para Gamma

    term1 = 1/(g**2 - 2*g + 2)
    term2 = (3*g*(2-g)-2)/(1+(delta_epsilon**2))
    term3 = (4*(1+g*(g-2))) / ((1+(delta_epsilon**2))**2)
    total = term1*(term2+term3)
    return total

# Função alvo para ajuste
def f(delta_epsilon, g, x):
    term1 = -g * (g - 1) * (
        1/(1+delta_epsilon**2) +
        (1+4*x**2)/((1+4*x**2)**2 + delta_epsilon**2)
    )

    term2 = 0.5 * (
        1/(1+delta_epsilon**2) +
        1/((1+4*x**2)**2 + delta_epsilon**2)
    )

    term3 = (g-1)**2 * (
        (1+delta_epsilon**2)/((1+delta_epsilon**2)**2) +
        ((1+4*x**2)**2 - delta_epsilon**2)/(((1+4*x**2)**2 + delta_epsilon**2**2)**2)
    )

    return term1 + term2 + term3

def density_ro(g, x):
    # Densidade calculada com os parâmetros ajustados
    return (1 / (2 * np.pi * g)) * np.sqrt((12 * x * (x + 1)) / (2 * x))

cutoff = 47

# Carregar dados
data = np.loadtxt("mean_autocorrelation.dat", float)
datax = data[:, 0]
datay = data[:, 1]

# Cortar os dados
datax = datax[:cutoff]
datay = datay[:cutoff]

# Normalizar eixo x
datax = datax / 0.002777

# Fazer o ajuste (fit) da função f aos dados
initial_guess = [1, 1]  # chute inicial: g e x
bounds = ([1e-10, 1e-10], [np.inf, np.inf])
popt, _ = curve_fit(f, datax, datay, p0=initial_guess, bounds=bounds)
Gamma_fit, x_fit = popt

# Calcular a densidade
# ro = density_ro(Gamma_fit, x_fit)

# Imprimir os parâmetros ajustados
print("\n\n=====================")
print(f"gamma = {Gamma_fit}")
print(f"x     = {x_fit}")
# print(f"density = {ro}")
print("=====================\n\n")

# Calcular a curva ajustada
x_curve = np.linspace(datax[0], datax[-1], 10000)
y_curve = f(x_curve, Gamma_fit, x_fit)

# Plotar os dados e o ajuste
plt.scatter(datax, datay, color='red', label="Dados")
plt.plot(x_curve, y_curve, label="Ajuste", color='blue')
plt.legend()
plt.grid(True)
plt.show()

# Salvar os dados no arquivo
with open("aaapoints.dat", "w") as f1:
    for xval, yval in zip(datax, datay):
        f1.write(f"{xval} {yval}\n")

with open("aaalorentz.dat", "w") as f2:
    for xval, yval in zip(x_curve, y_curve):
        f2.write(f"{xval} {yval}\n")
