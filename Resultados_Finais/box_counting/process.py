import subprocess

scripts = [
    "/home/felipe-moreira/Documentos/Pesquisa/Project_Fractal_Dimension_Quantum_Transport/Resultados_Finais/box_counting/m0/beta4/code_m0_paralelo.py",
    "/home/felipe-moreira/Documentos/Pesquisa/Project_Fractal_Dimension_Quantum_Transport/Resultados_Finais/box_counting/m1/beta4/code_m1_paralelo.py",
    "/home/felipe-moreira/Documentos/Pesquisa/Project_Fractal_Dimension_Quantum_Transport/Resultados_Finais/box_counting/m2/beta4/code_m2_paralelo.py",
    "/home/felipe-moreira/Documentos/Pesquisa/Project_Fractal_Dimension_Quantum_Transport/Resultados_Finais/box_counting/m3/beta4/code_m3_paralelo.py",
    "/home/felipe-moreira/Documentos/Pesquisa/Project_Fractal_Dimension_Quantum_Transport/Resultados_Finais/box_counting/m4/beta4/code_m4_paralelo.py"
]


# Executa cada um em sequência
for script in scripts:
    print(f"\n➡️ Executando {script}...")
    result = subprocess.run(["python3", script])
    
    if result.returncode == 0:
        print(f"✅ {script} finalizado com sucesso.\n")
    else:
        print(f"❌ Erro ao executar {script} (código {result.returncode}). Interrompendo execução.")
        break
