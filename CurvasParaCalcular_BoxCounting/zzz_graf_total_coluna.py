import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import scienceplots


def func_reta(x,a,b):
    return a*x+b

def ajustar_curva(xd, yd):
    param,pcov = curve_fit(func_reta,xd,yd)

    a = param[0]
    b = param[1]

    pontosx = np.linspace(xd[0],xd[-1],1000)
    pontosy = []
    for x in pontosx:
        pontosy.append(func_reta(x,a,b))

    return pontosx, pontosy

G_m0_beta1 = np.loadtxt("m0/DADOS_BC_Gbeta1.dat", float)
G_m0_beta2 = np.loadtxt("m0/DADOS_BC_Gbeta2.dat", float)
G_m0_beta4 = np.loadtxt("m0/DADOS_BC_Gbeta4.dat", float)
S_m0_beta1 = np.loadtxt("m0/DADOS_BC_Sbeta1.dat", float)
S_m0_beta2 = np.loadtxt("m0/DADOS_BC_Sbeta2.dat", float)
S_m0_beta4 = np.loadtxt("m0/DADOS_BC_Sbeta4.dat", float)

G_m1_beta1 = np.loadtxt("m1/DADOS_BC_Gbeta1.dat", float)
G_m1_beta2 = np.loadtxt("m1/DADOS_BC_Gbeta2.dat", float)
G_m1_beta4 = np.loadtxt("m1/DADOS_BC_Gbeta4.dat", float)
S_m1_beta1 = np.loadtxt("m1/DADOS_BC_Sbeta1.dat", float)
S_m1_beta2 = np.loadtxt("m1/DADOS_BC_Sbeta2.dat", float)
S_m1_beta4 = np.loadtxt("m1/DADOS_BC_Sbeta4.dat", float)

G_m2_beta1 = np.loadtxt("m2/DADOS_BC_Gbeta1.dat", float)
G_m2_beta2 = np.loadtxt("m2/DADOS_BC_Gbeta2.dat", float)
G_m2_beta4 = np.loadtxt("m2/DADOS_BC_Gbeta4.dat", float)
S_m2_beta1 = np.loadtxt("m2/DADOS_BC_Sbeta1.dat", float)
S_m2_beta2 = np.loadtxt("m2/DADOS_BC_Sbeta2.dat", float)
S_m2_beta4 = np.loadtxt("m2/DADOS_BC_Sbeta4.dat", float)

G_m3_beta1 = np.loadtxt("m3/DADOS_BC_Gbeta1.dat", float)
G_m3_beta2 = np.loadtxt("m3/DADOS_BC_Gbeta2.dat", float)
G_m3_beta4 = np.loadtxt("m3/DADOS_BC_Gbeta4.dat", float)
S_m3_beta1 = np.loadtxt("m3/DADOS_BC_Sbeta1.dat", float)
S_m3_beta2 = np.loadtxt("m3/DADOS_BC_Sbeta2.dat", float)
S_m3_beta4 = np.loadtxt("m3/DADOS_BC_Sbeta4.dat", float)

G_m4_beta1 = np.loadtxt("m4/DADOS_BC_Gbeta1.dat", float)
G_m4_beta2 = np.loadtxt("m4/DADOS_BC_Gbeta2.dat", float)
G_m4_beta4 = np.loadtxt("m4/DADOS_BC_Gbeta4.dat", float)
S_m4_beta1 = np.loadtxt("m4/DADOS_BC_Sbeta1.dat", float)
S_m4_beta2 = np.loadtxt("m4/DADOS_BC_Sbeta2.dat", float)
S_m4_beta4 = np.loadtxt("m4/DADOS_BC_Sbeta4.dat", float)




fit_G_m0_beta1 = ajustar_curva(G_m0_beta1[:,0], G_m0_beta1[:,1])
fit_G_m0_beta2 = ajustar_curva(G_m0_beta2[:,0], G_m0_beta2[:,1])
fit_G_m0_beta4 = ajustar_curva(G_m0_beta4[:,0], G_m0_beta4[:,1])
fit_S_m0_beta1 = ajustar_curva(S_m0_beta1[:,0], S_m0_beta1[:,1])
fit_S_m0_beta2 = ajustar_curva(S_m0_beta2[:,0], S_m0_beta2[:,1])
fit_S_m0_beta4 = ajustar_curva(S_m0_beta4[:,0], S_m0_beta4[:,1])

fit_G_m1_beta1 = ajustar_curva(G_m1_beta1[:,0], G_m1_beta1[:,1])
fit_G_m1_beta2 = ajustar_curva(G_m1_beta2[:,0], G_m1_beta2[:,1])
fit_G_m1_beta4 = ajustar_curva(G_m1_beta4[:,0], G_m1_beta4[:,1])
fit_S_m1_beta1 = ajustar_curva(S_m1_beta1[:,0], S_m1_beta1[:,1])
fit_S_m1_beta2 = ajustar_curva(S_m1_beta2[:,0], S_m1_beta2[:,1])
fit_S_m1_beta4 = ajustar_curva(S_m1_beta4[:,0], S_m1_beta4[:,1])

fit_G_m2_beta1 = ajustar_curva(G_m2_beta1[:,0], G_m2_beta1[:,1])
fit_G_m2_beta2 = ajustar_curva(G_m2_beta2[:,0], G_m2_beta2[:,1])
fit_G_m2_beta4 = ajustar_curva(G_m2_beta4[:,0], G_m2_beta4[:,1])
fit_S_m2_beta1 = ajustar_curva(S_m2_beta1[:,0], S_m2_beta1[:,1])
fit_S_m2_beta2 = ajustar_curva(S_m2_beta2[:,0], S_m2_beta2[:,1])
fit_S_m2_beta4 = ajustar_curva(S_m2_beta4[:,0], S_m2_beta4[:,1])

fit_G_m3_beta1 = ajustar_curva(G_m3_beta1[:,0], G_m3_beta1[:,1])
fit_G_m3_beta2 = ajustar_curva(G_m3_beta2[:,0], G_m3_beta2[:,1])
fit_G_m3_beta4 = ajustar_curva(G_m3_beta4[:,0], G_m3_beta4[:,1])
fit_S_m3_beta1 = ajustar_curva(S_m3_beta1[:,0], S_m3_beta1[:,1])
fit_S_m3_beta2 = ajustar_curva(S_m3_beta2[:,0], S_m3_beta2[:,1])
fit_S_m3_beta4 = ajustar_curva(S_m3_beta4[:,0], S_m3_beta4[:,1])

fit_G_m4_beta1 = ajustar_curva(G_m4_beta1[:,0], G_m4_beta1[:,1])
fit_G_m4_beta2 = ajustar_curva(G_m4_beta2[:,0], G_m4_beta2[:,1])
fit_G_m4_beta4 = ajustar_curva(G_m4_beta4[:,0], G_m4_beta4[:,1])
fit_S_m4_beta1 = ajustar_curva(S_m4_beta1[:,0], S_m4_beta1[:,1])
fit_S_m4_beta2 = ajustar_curva(S_m4_beta2[:,0], S_m4_beta2[:,1])
fit_S_m4_beta4 = ajustar_curva(S_m4_beta4[:,0], S_m4_beta4[:,1])



'''

fig, axes = plt.subplots(2, 3, figsize=(15, 8))

#Gbeta1
axes[0,0].scatter(G_m0_beta1[:,0], G_m0_beta1[:,1], label=r'$m=0$')
axes[0,0].scatter(G_m1_beta1[:,0], G_m1_beta1[:,1], label=r'$m=1$')
axes[0,0].scatter(G_m2_beta1[:,0], G_m2_beta1[:,1], label=r'$m=2$')
axes[0,0].scatter(G_m3_beta1[:,0], G_m3_beta1[:,1], label=r'$m=3$')
axes[0,0].scatter(G_m4_beta1[:,0], G_m4_beta1[:,1], label=r'$m=4$')

axes[0,0].plot(fit_G_m0_beta1[0],fit_G_m0_beta1[1])
axes[0,0].plot(fit_G_m1_beta1[0],fit_G_m1_beta1[1])
axes[0,0].plot(fit_G_m2_beta1[0],fit_G_m2_beta1[1])
axes[0,0].plot(fit_G_m3_beta1[0],fit_G_m3_beta1[1])
axes[0,0].plot(fit_G_m4_beta1[0],fit_G_m4_beta1[1])

axes[0,0].set_title(r'$\beta=1$', fontsize=30)
axes[0,0].set_xlabel(r"$log(1/l)$", fontsize=25)
axes[0,0].set_ylabel(r"$log(N)$", fontsize=25)
axes[0,0].tick_params(axis='both', labelsize=20)
#axes[0,0].legend(loc='best', fontsize=20)

#Gbeta2
axes[0,1].scatter(G_m0_beta2[:,0], G_m0_beta2[:,1], label=r'$m=0$')
axes[0,1].scatter(G_m1_beta2[:,0], G_m1_beta2[:,1], label=r'$m=1$')
axes[0,1].scatter(G_m2_beta2[:,0], G_m2_beta2[:,1], label=r'$m=2$')
axes[0,1].scatter(G_m3_beta2[:,0], G_m3_beta2[:,1], label=r'$m=3$')
axes[0,1].scatter(G_m4_beta2[:,0], G_m4_beta2[:,1], label=r'$m=4$')

axes[0,1].plot(fit_G_m0_beta2[0],fit_G_m0_beta2[1])
axes[0,1].plot(fit_G_m1_beta2[0],fit_G_m1_beta2[1])
axes[0,1].plot(fit_G_m2_beta2[0],fit_G_m2_beta2[1])
axes[0,1].plot(fit_G_m3_beta2[0],fit_G_m3_beta2[1])
axes[0,1].plot(fit_G_m4_beta2[0],fit_G_m4_beta2[1])

axes[0,1].set_title(r'$\beta=2$', fontsize=30)
axes[0,1].set_xlabel(r"$log(1/l)$", fontsize=25)
axes[0,1].set_ylabel(r"$log(N)$", fontsize=25)
axes[0,1].tick_params(axis='both', labelsize=20)
#axes[0,1].legend(loc='best', fontsize=20)

#Gbeta4
axes[0,2].scatter(G_m0_beta4[:,0], G_m0_beta4[:,1], label=r'$m=0$')
axes[0,2].scatter(G_m1_beta4[:,0], G_m1_beta4[:,1], label=r'$m=1$')
axes[0,2].scatter(G_m2_beta4[:,0], G_m2_beta4[:,1], label=r'$m=2$')
axes[0,2].scatter(G_m3_beta4[:,0], G_m3_beta4[:,1], label=r'$m=3$')
axes[0,2].scatter(G_m4_beta4[:,0], G_m4_beta4[:,1], label=r'$m=4$')

axes[0,2].plot(fit_G_m0_beta4[0],fit_G_m0_beta4[1])
axes[0,2].plot(fit_G_m1_beta4[0],fit_G_m1_beta4[1])
axes[0,2].plot(fit_G_m2_beta4[0],fit_G_m2_beta4[1])
axes[0,2].plot(fit_G_m3_beta4[0],fit_G_m3_beta4[1])
axes[0,2].plot(fit_G_m4_beta4[0],fit_G_m4_beta4[1])

axes[0,2].set_title(r'$\beta=4$', fontsize=30)
axes[0,2].set_xlabel(r"$log(1/l)$", fontsize=25)
axes[0,2].set_ylabel(r"$log(N)$", fontsize=25)
axes[0,2].tick_params(axis='both', labelsize=20)
#axes[0,2].legend(loc='best', fontsize=20)




#Sbeta1
axes[1,0].scatter(S_m0_beta1[:,0], S_m0_beta1[:,1], label=r'$m=0$')
axes[1,0].scatter(S_m1_beta1[:,0], S_m1_beta1[:,1], label=r'$m=1$')
axes[1,0].scatter(S_m2_beta1[:,0], S_m2_beta1[:,1], label=r'$m=2$')
axes[1,0].scatter(S_m3_beta1[:,0], S_m3_beta1[:,1], label=r'$m=3$')
axes[1,0].scatter(S_m4_beta1[:,0], S_m4_beta1[:,1], label=r'$m=4$')

axes[1,0].plot(fit_S_m0_beta1[0],fit_S_m0_beta1[1])
axes[1,0].plot(fit_S_m1_beta1[0],fit_S_m1_beta1[1])
axes[1,0].plot(fit_S_m2_beta1[0],fit_S_m2_beta1[1])
axes[1,0].plot(fit_S_m3_beta1[0],fit_S_m3_beta1[1])
axes[1,0].plot(fit_S_m4_beta1[0],fit_S_m4_beta1[1])

axes[1,0].set_title(r'$\beta=1$', fontsize=30)
axes[1,0].set_xlabel(r"$log(1/l)$", fontsize=25)
axes[1,0].set_ylabel(r"$log(N)$", fontsize=25)
axes[1,0].tick_params(axis='both', labelsize=20)
#axes[1,0].legend(loc='best', fontsize=20)


#Sbeta2
axes[1,1].scatter(S_m0_beta2[:,0], S_m0_beta2[:,1], label=r'$m=0$')
axes[1,1].scatter(S_m1_beta2[:,0], S_m1_beta2[:,1], label=r'$m=1$')
axes[1,1].scatter(S_m2_beta2[:,0], S_m2_beta2[:,1], label=r'$m=2$')
axes[1,1].scatter(S_m3_beta2[:,0], S_m3_beta2[:,1], label=r'$m=3$')
axes[1,1].scatter(S_m4_beta2[:,0], S_m4_beta2[:,1], label=r'$m=4$')

axes[1,1].plot(fit_S_m0_beta2[0],fit_S_m0_beta2[1])
axes[1,1].plot(fit_S_m1_beta2[0],fit_S_m1_beta2[1])
axes[1,1].plot(fit_S_m2_beta2[0],fit_S_m2_beta2[1])
axes[1,1].plot(fit_S_m3_beta2[0],fit_S_m3_beta2[1])
axes[1,1].plot(fit_S_m4_beta2[0],fit_S_m4_beta2[1])

axes[1,1].set_title(r'$\beta=2$', fontsize=30)
axes[1,1].set_xlabel(r"$log(1/l)$", fontsize=25)
axes[1,1].set_ylabel(r"$log(N)$", fontsize=25)
axes[1,1].tick_params(axis='both', labelsize=20)
#axes[1,1].legend(loc='best', fontsize=20)


#Sbeta4
axes[1,2].scatter(S_m0_beta4[:,0], S_m0_beta4[:,1], label=r'$m=0$')
axes[1,2].scatter(S_m1_beta4[:,0], S_m1_beta4[:,1], label=r'$m=1$')
axes[1,2].scatter(S_m2_beta4[:,0], S_m2_beta4[:,1], label=r'$m=2$')
axes[1,2].scatter(S_m3_beta4[:,0], S_m3_beta4[:,1], label=r'$m=3$')
axes[1,2].scatter(S_m4_beta4[:,0], S_m4_beta4[:,1], label=r'$m=4$')

axes[1,2].plot(fit_S_m0_beta4[0],fit_S_m0_beta4[1])
axes[1,2].plot(fit_S_m1_beta4[0],fit_S_m1_beta4[1])
axes[1,2].plot(fit_S_m2_beta4[0],fit_S_m2_beta4[1])
axes[1,2].plot(fit_S_m3_beta4[0],fit_S_m3_beta4[1])
axes[1,2].plot(fit_S_m4_beta4[0],fit_S_m4_beta4[1])

axes[1,2].set_title(r'$\beta=4$', fontsize=30)
axes[1,2].set_xlabel(r"$log(1/l)$", fontsize=25)
axes[1,2].set_ylabel(r"$log(N)$", fontsize=25)
axes[1,2].tick_params(axis='both', labelsize=20)
#axes[1,2].legend(loc='best', fontsize=20)

axes[1,1].legend(loc='upper center', fontsize=20, bbox_to_anchor=(0.5, -0.4), ncol=5)


plt.subplots_adjust(left=0.05, right=0.99, top=0.9, bottom=0.20, wspace=0.4, hspace=0.6)

plt.savefig("grid_box_counting.png", dpi=250)
plt.show()'
''
''
'''

plt.style.use('science')


plt.figure(figsize=(10, 8))
plt.subplots_adjust(left=0.15, right=0.95, top=0.9, bottom=0.15)

plt.scatter(G_m0_beta1[:,0], G_m0_beta1[:,1], label=r'$m=0$', s = 100, marker='o')
plt.scatter(G_m1_beta1[:,0], G_m1_beta1[:,1], label=r'$m=1$', s = 100, marker='s')
plt.scatter(G_m2_beta1[:,0], G_m2_beta1[:,1], label=r'$m=2$', s = 100, marker='^')
plt.scatter(G_m3_beta1[:,0], G_m3_beta1[:,1], label=r'$m=3$', s = 100, marker='D')
plt.scatter(G_m4_beta1[:,0], G_m4_beta1[:,1], label=r'$m=4$', s = 100, marker='v')

plt.plot(fit_G_m0_beta1[0],fit_G_m0_beta1[1], linewidth=3)
plt.plot(fit_G_m1_beta1[0],fit_G_m1_beta1[1], linewidth=3)
plt.plot(fit_G_m2_beta1[0],fit_G_m2_beta1[1], linewidth=3)
plt.plot(fit_G_m3_beta1[0],fit_G_m3_beta1[1], linewidth=3)
plt.plot(fit_G_m4_beta1[0],fit_G_m4_beta1[1], linewidth=3)

plt.legend(loc='upper left', fontsize=30, frameon=True)

plt.xlabel(r"log$(1/l)$", fontsize=35)
plt.ylabel(r"log$(N)$", fontsize=35)
plt.tick_params(axis='both', labelsize=30)
plt.title(r"Conductance", fontsize=40)
plt.grid(True)
plt.savefig("boxG.png", dpi=250)
plt.show()



plt.figure(figsize=(10, 8))
plt.subplots_adjust(left=0.15, right=0.95, top=0.9, bottom=0.15)

plt.scatter(S_m0_beta1[:,0], S_m0_beta1[:,1], label=r'$m=0$', s = 100, marker='o')
plt.scatter(S_m1_beta1[:,0], S_m1_beta1[:,1], label=r'$m=1$', s = 100, marker='s')
plt.scatter(S_m2_beta1[:,0], S_m2_beta1[:,1], label=r'$m=2$', s = 100, marker='^')
plt.scatter(S_m3_beta1[:,0], S_m3_beta1[:,1], label=r'$m=3$', s = 100, marker='D')
plt.scatter(S_m4_beta1[:,0], S_m4_beta1[:,1], label=r'$m=4$', s = 100, marker='v')

plt.plot(fit_S_m0_beta1[0],fit_S_m0_beta1[1], linewidth=3)
plt.plot(fit_S_m1_beta1[0],fit_S_m1_beta1[1], linewidth=3)
plt.plot(fit_S_m2_beta1[0],fit_S_m2_beta1[1], linewidth=3)
plt.plot(fit_S_m3_beta1[0],fit_S_m3_beta1[1], linewidth=3)
plt.plot(fit_S_m4_beta1[0],fit_S_m4_beta1[1], linewidth=3)

plt.legend(loc='upper left', fontsize=30, frameon=True)

plt.xlabel(r"log$(1/l)$", fontsize=35)
plt.ylabel(r"log$(N)$", fontsize=35)
plt.tick_params(axis='both', labelsize=30)
plt.title(r"Shot Noise Power", fontsize=40)
plt.grid(True)
plt.savefig("boxS.png", dpi=250)
plt.show()