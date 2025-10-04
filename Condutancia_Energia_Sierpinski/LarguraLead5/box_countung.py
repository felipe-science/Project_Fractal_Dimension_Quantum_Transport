from numpy import loadtxt, linspace, log
from pylab import plot, xlabel, ylabel, title, scatter, imshow, show, tick_params
from scipy.optimize import curve_fit

def func_reta(x,a,b):
    return a*x+b

def varredura(x, y, l, valoresx, valoresy):

    ocupacao = False
    N = len(valoresx)
    for i in range(N):

        valx = valoresx[i]
        valy = valoresy[i]

        if(valx > x and valx < x+l and valy > y and valy < y+l):
            ocupacao = True
            return ocupacao
    
    return ocupacao


# Refazer o Box-Counting
def box_counting(dadosx, dadosy):
  
    l = 0.2
    L = 1


    comprl = []
    numecx = []
    comprl_log = []
    numecx_log = []

    
    while(l >= 0.003125):

        n = int(L/(l*L))
        comprl.append(l)

        contagem = 0
        for i in range(n):
            for j in range(n):
                
                x = j*(L/n)
                y = i*(L/n)

                ocupacao = varredura(x,y,l, dadosx, dadosy)
                if(ocupacao):
                    contagem+=1
        
                
        numecx.append(contagem) 
        print("l = ",l,"     n = ",n,"    Nºcx = ",contagem,"    L",l*L,"    D = ",(log(contagem)/log(1/l)))
        l = l/2

    # Calculando os logarítmos
    for k in range(len(comprl)):
        l_log = log(1/comprl[k])
        n_log = log(numecx[k])
    
        comprl_log.append(l_log)
        numecx_log.append(n_log)

    return comprl_log, numecx_log



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
    title("Dimensão Fractal - Carpete Sierpinski", fontsize='16')
    xlabel("log(1/l)", fontsize='15')
    ylabel("log(N)", fontsize='15')
    tick_params(labelsize='12')
    show()

    print("\nDimensao Fractal = ",a)




#Testar com a função afim
data = loadtxt("G_m3_n53.dat",float)
datax = data[:,0]
datay = data[:,1]



dados = box_counting(datax, datay)
ajuste_curva(dados[0],dados[1])