from numpy import loadtxt, linspace
from pylab import scatter, plot, show, title, xlabel, ylabel, tick_params, legend, savefig, grid
from scipy.optimize import curve_fit

def func_reta(x,a,b):
    return a*x+b

# Ajuste de curvas
def ajuste_curva(xd, yd):
    
    param,pcov = curve_fit(func_reta,xd,yd)

    a = param[0]
    b = param[1]

    pontosx = linspace(xd[0],xd[-1],1000)
    pontosy = []
    for x in pontosx:
        pontosy.append(func_reta(x,a,b))

    scatter(xd,yd, color='green')
    plot(pontosx,pontosy, color = 'black', linestyle = 'dashed')
    title("Dimensão Fractal - Curva de Condutância", fontsize='16')
    xlabel("log(1/l)", fontsize='15')
    ylabel("log(N)", fontsize='15')
    tick_params(labelsize='12')
    savefig('condutancia_D'+str(round(a,2))+'.png', format='png')
    show()

    print("\nDimensao Fractal = ",a)

data = loadtxt("DADOS_BC_Sbeta4.dat",float)

pontosx = data[:,0]
pontosy = data[:,1]

ajuste_curva(pontosx, pontosy)
show()
