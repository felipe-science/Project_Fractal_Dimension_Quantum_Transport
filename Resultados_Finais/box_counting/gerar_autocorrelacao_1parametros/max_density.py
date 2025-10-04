import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks



gamma_m0 = 0.0002694
gamma_m1 = 0.00012855
gamma_m2 = 0.00012855
gamma_m3 = 0.0002882132327714495
gamma_m4 = 0.00012855

gamma_m1 = 1
gamma_m2 = 1
gamma_m3 = 1
gamma_m4 = 1

Nfile = 500

Npeaks_m1_sum = 0
Npeaks_m2_sum = 0
Npeaks_m3_sum = 0
Npeaks_m4_sum = 0

densityE_m3 = 0

for i in range(Nfile):

    data_m1 = np.loadtxt(f"m1/outputG/G{i}.dat")
    data_m2 = np.loadtxt(f"m2/outputG/G{i}.dat")
    data_m3 = np.loadtxt(f"m3/outputG/G{i}.dat")
    data_m4 = np.loadtxt(f"m4/outputG/G{i}.dat")
    
    Em1 = data_m1[:,0]
    Gm1 = data_m1[:,1]

    Em2 = data_m2[:,0]
    Gm2 = data_m2[:,1]

    Em3 = data_m3[:,0]
    Gm3 = data_m3[:,1]

    Em4 = data_m4[:,0]
    Gm4 = data_m4[:,1]

    peaksm1, _ = find_peaks(Gm1, height=0)
    peaksm2, _ = find_peaks(Gm2, height=0)
    peaksm3, _ = find_peaks(Gm3, height=0)
    peaksm4, _ = find_peaks(Gm4, height=0)
    
    Npeaks_m1 = len(peaksm1)
    Npeaks_m1_sum+=Npeaks_m1

    Npeaks_m2 = len(peaksm2)
    Npeaks_m2_sum+=Npeaks_m2
    
    Npeaks_m3 = len(peaksm3)
    Npeaks_m3_sum+=Npeaks_m3

    Npeaks_m4 = len(peaksm4)
    Npeaks_m4_sum+=Npeaks_m4

    
    print(Em3[peaksm3[0]])


    if(i == 3 or i == 4):
        

        plt.figure(figsize=(12, 6), dpi=80)
        
        plt.plot(Em3/0.000128551, Gm3, color='red', zorder=1)
        plt.scatter(Em3[peaksm3]/0.000128551, Gm3[peaksm3], color='black', zorder=2)
        plt.xlabel(r'$\epsilon / \gamma$', fontsize=30)
        plt.ylabel(r'$g(\epsilon)$', fontsize=30)
        plt.tick_params(axis='both',  labelsize=25)
        plt.subplots_adjust(left=0.10, right=0.95, top=0.95, bottom=0.15) 
        plt.show()

        
        '''
        plt.figure(figsize=(12, 6), dpi=80)
        
        plt.plot(Em4/0.000128551, Gm4, color='red', zorder=1)
        plt.scatter(Em4[peaksm4]/0.000128551, Gm4[peaksm4], color='black', zorder=2)
        plt.xlabel(r'$\epsilon / \gamma$', fontsize=30)
        plt.ylabel(r'$g(\epsilon)$', fontsize=30)
        plt.tick_params(axis='both',  labelsize=25)
        plt.subplots_adjust(left=0.10, right=0.95, top=0.95, bottom=0.15) 
        plt.show()
        '''

