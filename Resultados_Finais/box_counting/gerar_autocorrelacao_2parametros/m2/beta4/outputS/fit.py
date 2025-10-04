import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Definir a função lorentziana generalizada com tratamento de erro
def f(delta_epsilon, g, a, b):
    #a=1
    #b=1
    #g = 0.00018330959338887157
    # Evitar divisão por zero
    g = max(g, 1e-10)  # Define um valor mínimo para Gamma
    return 1 / (1 + (delta_epsilon / g)**(2 * b))**a


def density_ro(g, a, b):
    ro = (1/(2*np.pi))*np.sqrt((6*b*(a+1))/(g**2))
    return ro

cutoff = 20


data = np.loadtxt("mean_autocorrelation.dat",float)
datax = data[:,0]
datay = data[:,1]

datax = datax[:cutoff]
datay = datay[:cutoff]

NN = len(datax)
for k in range(NN):
    datax[k] = datax[k]/1
    #datax[k] = datax[k]/0.0007662792136859497

# Fazer o ajuste (fit) da função lorentziana aos dados
initial_guess = [1, 1, 1]  # Gama, alpha, beta iniciais

# Definir limites para evitar valores inválidos
popt, _ = curve_fit(f, datax, datay, p0=initial_guess, bounds=([1e-10, 0, 0], [np.inf, np.inf, np.inf]))
Gamma_fit, alpha_fit, beta_fit = popt



# Ajuste dos dados
#initial_guess = [1.29, 0.8, 0.0023]  # Chute inicial para os parâmetros: amp, mean, stddev
#params, covariance = curve_fit(f, datax, datay, p0=initial_guess)

#g, a, b = params
ro = density_ro(Gamma_fit, alpha_fit, beta_fit)

print("\n\n=====================")
print(f"alpha = {alpha_fit}")
print(f"beta = {beta_fit}")
print(f"gamma = {Gamma_fit}")
print(f"density = {ro}")
print("=====================\n\n")


x_curve = np.linspace(datax[0], datax[-1], 10000)
y_curve = []
for x in x_curve:
    y = f(x, Gamma_fit, alpha_fit, beta_fit)
    y_curve.append(y)

plt.scatter(datax, datay, color='red')
plt.plot(x_curve, y_curve)
plt.grid(True)
plt.title("m=3")
plt.xlabel(r"$\delta \epsilon / \gamma$")
plt.ylabel(r"$C(\epsilon)$")
plt.savefig("m4.png", dpi=300)
plt.show()


#imprimir resultado final
f1 = open("aaapoints.dat", "w")
for k in range(len(datax)):
    f1.write(f"{datax[k]} {datay[k]}\n")
f1.close()

f2 = open("aaalorentz.dat", "w")
for k in range(len(x_curve)):
    f2.write(f"{x_curve[k]} {y_curve[k]}\n")
f2.close()