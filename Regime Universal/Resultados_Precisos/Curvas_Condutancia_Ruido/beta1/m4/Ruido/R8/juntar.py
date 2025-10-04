from numpy import loadtxt

Nfile = 10

total_data = []

f = open("SN_m4_n161.dat", "a")
for i in range(Nfile):
    data = loadtxt("SN_m4_n161R"+str(i+1)+".dat",float)
    datax = data[:,0]
    datay = data[:,1]
    
    for j in range(len(datax)):
        f.write(str(datax[j])+"    "+str(datay[j])+"\n")

f.close()    