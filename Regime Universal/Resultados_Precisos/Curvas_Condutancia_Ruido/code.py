import numpy as np

# Função para ler e processar os dados de condutância
def read_conductance_file(file_path):
    try:
        with open(file_path, 'r') as f:
            data = f.readlines()
        
        results = []
        for line in data:
            # Ignorar linhas vazias
            line = line.strip()
            if not line:
                continue
            
            # Extrair informações relevantes
            parts = line.split()
            if len(parts) >= 6:  # Verifica se a linha contém o número esperado de partes
                try:
                    beta = parts[0]
                    m_value = parts[1]
                    noise_type = parts[2]
                    tau_ro = float(parts[4].split('=')[1])
                    rho = float(parts[5].split('=')[1])
                    results.append({
                        'beta': beta,
                        'm': m_value,
                        'noise_type': noise_type,
                        'tau_ro': tau_ro,
                        'rho': rho
                    })
                except ValueError as e:
                    print(f"Erro ao converter dados em {file_path}: {e}")
        
        print(f"Dados de {file_path}:")
        for result in results:
            print(result)
        return results
    except Exception as e:
        print(f"Erro ao ler {file_path}: {e}")

# Função para ler o arquivo de saída (output.dat)
def read_output(file_path):
    try:
        output_data = []
        with open(file_path, 'r') as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith('#'):  # Ignorar linhas vazias ou comentários
                    continue
                # Ignorar linhas que não podem ser convertidas em floats
                try:
                    output_data.append([float(x) for x in line.split() if x.replace('.', '', 1).isdigit()])
                except ValueError as e:
                    print(f"Erro ao processar linha em {file_path}: {e}")
        
        output_data = np.array(output_data)
        print(f"Dados de {file_path}:")
        print(output_data)
        return output_data
    except Exception as e:
        print(f"Erro ao ler {file_path}: {e}")

# Caminhos dos arquivos
conductance_shot_file = 'conductance_shot.txt'
results_conductance_file = 'results_conductance.txt'
output_file = 'output.dat'

# Ler os arquivos
conductance_shot_data = read_conductance_file(conductance_shot_file)
results_conductance_data = read_conductance_file(results_conductance_file)
output_data = read_output(output_file)
