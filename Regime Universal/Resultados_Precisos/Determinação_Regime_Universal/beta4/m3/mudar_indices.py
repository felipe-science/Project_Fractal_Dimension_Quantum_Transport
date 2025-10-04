import os

Nfile = 10000
inicio = 314

for k in range(Nfile):
     
     old = "G"+str(k)+".dat"
     new = "G"+str(k+inicio)+".dat"

     os.rename(old,new)
