import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Load data
data = np.loadtxt('mean_autocorrelation.dat')
x = data[:, 0]
y = data[:, 1]

# Use only first 35 points
x = x[:35]
y = y[:35]

# Define the model function with numerical stability
def func(x, a, b, g):
    """Modified function with numerical safeguards"""
    with np.errstate(divide='ignore', invalid='ignore'):
        exponent = np.where(x == 0, 0, (x/g)**(2*b))  # Handle x=0 case
        exponent = np.nan_to_num(exponent, nan=np.inf, posinf=np.inf, neginf=np.inf)
        return 1 / (1 + exponent)**a

def density_fit(g, a, b):
    """Calculate density from fit parameters"""
    g=1
    return (1/(2*np.pi))*np.sqrt((6*b*(a+1))/(g**2))

# Improved initial guesses based on your previous results
initial_guess = [1.2, 0.9, 0.004]

# Set parameter bounds [a, b, g]
lower_bounds = [0.1, 0.1, 1e-10]  # Minimum reasonable values
upper_bounds = [10, 10, 10]       # Maximum reasonable values

# Perform the fit with bounds
try:
    params, covariance = curve_fit(func, x, y, 
                                 p0=initial_guess,
                                 bounds=(lower_bounds, upper_bounds),
                                 maxfev=10000)  # Increase max iterations
    
    # Extract fitted parameters
    a_fit, b_fit, g_fit = params
    print("Fit successful!")
    print(f"Fitted parameters:")
    print(f"a = {a_fit:.8f}")
    print(f"b = {b_fit:.8f}")
    print(f"g = {g_fit:.8f}")
    
    # Calculate fitted curve and density
    y_fit = func(x, a_fit, b_fit, g_fit)
    density = density_fit(g_fit, a_fit, b_fit)
    print(f"Density from fit: {density:.8f}")
    
    # Calculate parameter uncertainties from covariance matrix
    if covariance is not None:
        perr = np.sqrt(np.diag(covariance))
        print("\nParameter uncertainties:")
        print(f"Δa = {perr[0]:.8f}")
        print(f"Δb = {perr[1]:.8f}")
        print(f"Δg = {perr[2]:.8f}")
    
except Exception as e:
    print(f"Fit failed: {str(e)}")
    # Fallback to initial guesses if fit fails
    a_fit, b_fit, g_fit = initial_guess
    y_fit = func(x, *initial_guess)



# Plot results
plt.figure(figsize=(12, 6))

# Linear scale plot
plt.subplot(1, 2, 1)
plt.scatter(x, y, label='Experimental data', color='blue')
plt.plot(x, y_fit, label=f'Fit: a={a_fit:.2f}, b={b_fit:.2f}, g={g_fit:.4f}', color='red')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Autocorrelation Fit (Linear Scale)')
plt.legend()
plt.grid(True)

# Log-log scale plot
plt.subplot(1, 2, 2)
plt.scatter(x, y, label='Experimental data', color='blue')
plt.plot(x, y_fit, label='Fit', color='red')
plt.xscale('log')
plt.yscale('log')
plt.xlabel('x (log)')
plt.ylabel('y (log)')
plt.title('Autocorrelation Fit (Log Scale)')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.savefig('autocorrelation_fit.png', dpi=300)
plt.show()


