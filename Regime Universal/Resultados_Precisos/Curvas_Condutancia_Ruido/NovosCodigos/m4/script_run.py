import subprocess

# Lista dos três scripts Python que você deseja executar em sequência
scripts = ["cond_ruido_beta1_m4.py", "cond_ruido_beta2_m4.py", "cond_ruido_beta4_m4.py"]

for script in scripts:
    try:
        # Executa cada script
        result = subprocess.run(['python3', script], check=True)
        print(f"{script} terminou com sucesso.")
    except subprocess.CalledProcessError as e:
        print(f"Ocorreu um erro ao executar {script}: {e}")
        break  # Interrompe a execução se algum script falhar

