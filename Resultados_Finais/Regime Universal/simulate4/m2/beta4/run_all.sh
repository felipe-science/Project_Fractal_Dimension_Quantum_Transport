#!/bin/bash

# Lista dos scripts Python
scripts=(
    run1.py
    run2.py
    run3.py
    run4.py
    run5.py
)

# Executar todos os scripts em paralelo
for script in "${scripts[@]}"
do
    echo "Executando $script..."
    python "$script" &
done

# Esperar todos os processos terminarem
wait
echo "Todos os scripts foram concluídos."
