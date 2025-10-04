import subprocess

def run_script(script_name):
    try:
        # Executa o script usando o Python 3
        subprocess.run(['python3', script_name], check=True)
        print(f"{script_name} executado com sucesso.")
    except subprocess.CalledProcessError as e:
        # Captura qualquer erro na execução do script
        print(f"Erro ao executar {script_name}: {e}")
        raise

if __name__ == "__main__":
    # Lista de scripts a serem executados
    scripts = ['cond_ruido_beta1_m0.py', 'cond_ruido_beta2_m0.py', 'cond_ruido_beta4_m0.py', 'cond_ruido_beta1_m1.py', 'cond_ruido_beta2_m1.py', 'cond_ruido_beta4_m1.py', 'cond_ruido_beta1_m2.py', 'cond_ruido_beta2_m2.py', 'cond_ruido_beta4_m2.py']

    # Executa cada script em sequência
    for script in scripts:
        run_script(script)

