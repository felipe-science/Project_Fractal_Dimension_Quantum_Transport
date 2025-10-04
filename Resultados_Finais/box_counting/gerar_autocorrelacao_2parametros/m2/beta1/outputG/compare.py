import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

data_n = np.loadtxt("G9.dat", float)
#data_p = np.loadtxt("G9_para.dat", float)

plt.plot(data_n[:,0], data_n[:,1])
plt.show()

#plt.plot(data_p[:,0], data_p[:,1])
#plt.show()


peaksn, _ = find_peaks(data_n[:,1], height=0)  # height=0 means only values > 0
#peaksp, _ = find_peaks(data_p[:,1], height=0)  # height=0 means only values > 0

print(len(peaksn))
#print(len(peaksp))