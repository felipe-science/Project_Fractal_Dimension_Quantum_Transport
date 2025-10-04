import os
import shutil
import time

# Listar apenas arquivos que começam com "G" e terminam com ".dat"
arquivos = sorted([f for f in os.listdir('.') if os.path.isfile(f) and f.startswith("G") and f.endswith(".dat")])

# Etapa 1: renomear para nomes temporários (evita conflito de sobrescrita)
x = 1000000
for i, old in enumerate(arquivos):
    new = f"G{i+x}.dat"
    shutil.move(old, new)

time.sleep(3)  # pausa de 3 segundos

# Etapa 2: renomear para nomes finais ordenados
arquivos = sorted([f for f in os.listdir('.') if os.path.isfile(f) and f.startswith("G") and f.endswith(".dat")])

x = 0
for i, old in enumerate(arquivos):
    new = f"G{i+x}.dat"
    shutil.move(old, new)
