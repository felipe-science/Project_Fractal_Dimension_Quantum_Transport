import os

# Caminho da pasta
pasta = "output_prov"

# Listar arquivos na pasta
k = 0
for arquivo in os.listdir(pasta):
    if arquivo.endswith(".dat"):
        caminho_antigo = os.path.join(pasta, arquivo)
        caminho_novo = os.path.join(pasta, f"G{k+1000}.dat")
        
        # Renomear o arquivo
        os.rename(caminho_antigo, caminho_novo)
        print(f"Renomeado: {arquivo} -> novo_{arquivo}")
        k+=1

# Listar arquivos na pasta
k = 0
for arquivo in os.listdir(pasta):
    if arquivo.endswith(".dat"):
        caminho_antigo = os.path.join(pasta, arquivo)
        caminho_novo = os.path.join(pasta, f"G{k}.dat")
        
        # Renomear o arquivo
        os.rename(caminho_antigo, caminho_novo)
        print(f"Renomeado: {arquivo} -> novo_{arquivo}")
        k+=1