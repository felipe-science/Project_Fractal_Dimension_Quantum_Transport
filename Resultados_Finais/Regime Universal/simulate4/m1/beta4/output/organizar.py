import os

# Diretório atual
diretorio = "."

# Filtrar arquivos que começam com 'G' e terminam com '.dat'
arquivos_filtrados = [
    f for f in os.listdir(diretorio)
    if f.startswith('G') and f.endswith('.dat') and os.path.isfile(f)
]

N = len(arquivos_filtrados)
print(N)

for i in range(N):

    # Nome atual do arquivo e o novo nome
    nome_antigo = arquivos_filtrados[i]
    nome_novo = f"G{i}.dat"

    # Renomear
    os.rename(nome_antigo, nome_novo)


