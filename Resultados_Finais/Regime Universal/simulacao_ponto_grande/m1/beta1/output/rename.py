import os
import shutil
import time

diretorio = "."
arquivos = [f for f in os.listdir('.') if os.path.isfile(f) and f.endswith('.dat')]

x = 1000000
for i in range(len(arquivos)):

    old = arquivos[i]
    new = f"G{i+x}.dat"

    shutil.move(old, new)


time.sleep(3)  # pausa de 3 segundos

diretorio = "."
arquivos = [f for f in os.listdir('.') if os.path.isfile(f) and f.endswith('.dat')]

x = 0
for i in range(len(arquivos)):

    old = arquivos[i]
    new = f"G{i+x}.dat"

    shutil.move(old, new)


