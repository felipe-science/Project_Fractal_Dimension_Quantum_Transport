import os

Nfile = 1000
inicio = 1000

for k in range(Nfile):
     
     old = "G"+str(k)+".dat"
     new = "G"+str(k+inicio)+".dat"

     os.rename(old,new)
