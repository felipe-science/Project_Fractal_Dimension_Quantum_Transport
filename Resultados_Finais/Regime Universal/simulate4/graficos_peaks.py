import numpy as np
import matplotlib.pyplot as plt
import scienceplots

data_m0_beta1_G = np.loadtxt('m0/beta1/G.dat', float)
data_m0_beta2_G = np.loadtxt('m0/beta2/G.dat', float)
data_m0_beta4_G = np.loadtxt('m0/beta4/G.dat', float)

data_m1_beta1_G = np.loadtxt('m1/beta1/G.dat', float)
data_m1_beta2_G = np.loadtxt('m1/beta2/G.dat', float)
data_m1_beta4_G = np.loadtxt('m1/beta4/G.dat', float)

data_m2_beta1_G = np.loadtxt('m2/beta1/G.dat', float)
data_m2_beta2_G = np.loadtxt('m2/beta2/G.dat', float)
data_m2_beta4_G = np.loadtxt('m2/beta4/G.dat', float)

data_m3_beta1_G = np.loadtxt('m3/beta1/G.dat', float)
data_m3_beta2_G = np.loadtxt('m3/beta2/G.dat', float)
data_m3_beta4_G = np.loadtxt('m3/beta4/G.dat', float)

data_m4_beta1_G = np.loadtxt('m4/beta1/G.dat', float)
data_m4_beta2_G = np.loadtxt('m4/beta2/G.dat', float)
data_m4_beta4_G = np.loadtxt('m4/beta4/G.dat', float)

# ===================================================

data_m0_beta1_S = np.loadtxt('m0/beta1/rmsG.dat', float)
data_m0_beta2_S = np.loadtxt('m0/beta2/rmsG.dat', float)
data_m0_beta4_S = np.loadtxt('m0/beta4/rmsG.dat', float)

data_m1_beta1_S = np.loadtxt('m1/beta1/rmsG.dat', float)
data_m1_beta2_S = np.loadtxt('m1/beta2/rmsG.dat', float)
data_m1_beta4_S = np.loadtxt('m1/beta4/rmsG.dat', float)

data_m2_beta1_S = np.loadtxt('m2/beta1/rmsG.dat', float)
data_m2_beta2_S = np.loadtxt('m2/beta2/rmsG.dat', float)
data_m2_beta4_S = np.loadtxt('m2/beta4/rmsG.dat', float)

data_m3_beta1_S = np.loadtxt('m3/beta1/rmsG.dat', float)
data_m3_beta2_S = np.loadtxt('m3/beta2/rmsG.dat', float)
data_m3_beta4_S = np.loadtxt('m3/beta4/rmsG.dat', float)

data_m4_beta1_S = np.loadtxt('m4/beta1/rmsG.dat', float)
data_m4_beta2_S = np.loadtxt('m4/beta2/rmsG.dat', float)
data_m4_beta4_S = np.loadtxt('m4/beta4/rmsG.dat', float)



fig, axs = plt.subplots(5, 1, figsize=(6, 15))  # Ajuste o figsize conforme necessário

axs[0].plot(data_m0_beta1_G[:,0], data_m0_beta1_G[:,1])



plt.show()