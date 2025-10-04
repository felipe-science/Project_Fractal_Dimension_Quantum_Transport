
import os

# Obtém o diretório do script atual
current_directory = os.getcwd()

# Lista todos os arquivos no diretório atual
files_in_directory = os.listdir(current_directory)

# Filtra os arquivos que começam com 'G' e terminam com '.dat'
filtered_files = [file for file in files_in_directory if file.startswith('S') and file.endswith('.dat')]

# Exibe os nomes dos arquivos encontrados
print("Arquivos .dat que começam com 'S' encontrados:")
i = 0
for file in filtered_files:
    
    current_name = file
    new_name = f"G{i}.dat"
    os.rename(current_name, new_name)
    i+=1
