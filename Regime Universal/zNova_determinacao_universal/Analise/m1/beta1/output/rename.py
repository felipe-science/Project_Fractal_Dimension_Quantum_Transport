import os

def rename_dat_files():
    # Diretório atual (onde o código está rodando)
    directory = os.getcwd()
    
    # Listar todos os arquivos no diretório
    files = os.listdir(directory)
    
    # Filtrar apenas os arquivos com extensão .dat
    dat_files = [file for file in files if file.endswith('.dat')]
    
    # Renomear os arquivos
    for i, file in enumerate(dat_files):
        # Novo nome no formato G%.dat
        new_name = f"G{i}.dat"
        
        # Caminho completo do arquivo original e do novo nome
        original_path = os.path.join(directory, file)
        new_path = os.path.join(directory, new_name)
        
        # Renomear o arquivo
        os.rename(original_path, new_path)
        print(f"Arquivo {file} renomeado para {new_name}")

# Executar a função
rename_dat_files()
