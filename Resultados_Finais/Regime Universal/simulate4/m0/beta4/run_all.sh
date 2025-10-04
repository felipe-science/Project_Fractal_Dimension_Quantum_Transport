#!/bin/bash

# Lista dos scripts Python
scripts=(
    zcond_disorder1.py
    zcond_disorder2.py
    zcond_disorder3.py
    zcond_disorder4.py
    zcond_disorder5.py
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
