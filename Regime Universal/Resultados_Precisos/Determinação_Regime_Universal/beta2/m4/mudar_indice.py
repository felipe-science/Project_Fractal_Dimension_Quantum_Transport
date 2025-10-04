import os

Nfile = 286
inicio = 721

for k in range(Nfile):
     
     old = "G"+str(k)+".dat"
     new = "G"+str(k+inicio)+".dat"

     os.rename(old,new)
