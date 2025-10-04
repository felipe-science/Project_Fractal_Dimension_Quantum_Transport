import os

def rename_dat_files():
    # Listar todos os arquivos no diretório atual que terminam com .dat
    files = [f for f in os.listdir() if f.endswith('.dat')]
    
    # Ordenar os arquivos numericamente com base no número após 'G'
    files.sort(key=lambda x: int(x[1:-4]))  # Assume que os arquivos são no formato G{n}.dat
    
    # Renomear os arquivos sequencialmente de G0.dat até o último
    for i, filename in enumerate(files):
        # Criar novo nome de arquivo sequencialmente (G0.dat, G1.dat, G2.dat, ...)
        new_name = f"G{i}.dat"
        
        # Caminho completo do arquivo original e do novo arquivo
        old_file_path = os.path.join(os.getcwd(), filename)
        new_file_path = os.path.join(os.getcwd(), new_name)
        
        # Renomear o arquivo apenas se o nome novo for diferente do atual
        if old_file_path != new_file_path:
            os.rename(old_file_path, new_file_path)
            print(f"Renomeado: {filename} -> {new_name}")
        else:
            print(f"Nome já correto: {filename}")

# Chamar a função
rename_dat_files()
