import subprocess
import os

def execute_scripts(script_names):
    """
    Executa uma lista de scripts Python sequencialmente.

    Args:
        script_names (list): Lista com os nomes dos scripts a serem executados.
    """
    for script in script_names:
        try:
            # Construir o caminho absoluto do script
            script_path = os.path.abspath(script)

            # Verificar se o arquivo existe
            if not os.path.exists(script_path):
                print(f"Erro: O arquivo '{script}' não foi encontrado.")
                continue

            print(f"Executando {script}...")

            # Executar o script
            result = subprocess.run(["python", script_path], capture_output=False, text=True)

            # Exibir a saída do script
            if result.returncode == 0:
                print(f"{script} executado com sucesso.")
                print(f"Saída:\n{result.stdout}")
            else:
                print(f"Erro ao executar {script}. Código de saída: {result.returncode}")
                print(f"Erro:\n{result.stderr}")
                break  # Interromper a execução se ocorrer um erro
        except Exception as e:
            print(f"Erro inesperado ao executar {script}: {e}")
            break

# Lista de scripts para executar em sequência
scripts = [
    "m0/cond_ruido_beta1_m0.py",
    "m0/cond_ruido_beta2_m0.py",
    "m0/cond_ruido_beta4_m0.py",
    "m1/cond_ruido_beta1_m1.py",
    "m1/cond_ruido_beta2_m1.py",
    "m1/cond_ruido_beta4_m1.py",
    "m2/cond_ruido_beta1_m2.py",
    "m2/cond_ruido_beta2_m2.py",
    "m2/cond_ruido_beta4_m2.py",
    "m3/cond_ruido_beta1_m3.py",
    "m3/cond_ruido_beta2_m3.py",
    "m3/cond_ruido_beta4_m3.py"

]

# Chamar a função para executar os scripts
execute_scripts(scripts)
