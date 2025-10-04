import os
import time
import shutil

files = os.listdir(".")

files_filter = [f for f in files if f.startswith("G") and f.endswith(".dat")]
# Exemplo: imprimir os nomes dos arquivos encontrados
i = 1000000
for arquivo in files_filter:
    
    name_old = arquivo
    name_new = f"G{i}.dat"
    shutil.move(name_old, name_new)
    i+=1



print(f"Nº arquivos: {i}")


time.sleep(10)  # Pausa de 2 segundos



files = os.listdir(".")

files_filter = [f for f in files if f.startswith("G") and f.endswith(".dat")]
# Exemplo: imprimir os nomes dos arquivos encontrados
i = 0
for arquivo in files_filter:
    
    name_old = arquivo
    name_new = f"G{i}.dat"
    shutil.move(name_old, name_new)
    i+=1



print(f"Nº arquivos: {i}")