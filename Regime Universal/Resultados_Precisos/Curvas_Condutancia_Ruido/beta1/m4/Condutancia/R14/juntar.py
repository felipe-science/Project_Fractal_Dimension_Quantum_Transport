from numpy import loadtxt

Nfile = 10

total_data = []

f = open("G_m4_n161.dat", "a")
for i in range(Nfile):
    data = loadtxt("G_m4_n161w036_R"+str(i+1)+".dat",float)
    datax = data[:,0]
    datay = data[:,1]
    
    for j in range(len(datax)):
        f.write(str(datax[j])+"    "+str(datay[j])+"\n")

f.close()    