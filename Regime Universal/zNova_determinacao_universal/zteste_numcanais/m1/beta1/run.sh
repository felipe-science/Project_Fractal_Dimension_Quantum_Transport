#!/bin/bash

# Caminho dos scripts Python
SCRIPT1="A1condutancia_sierpinski_n54_m3_beta1.py"
SCRIPT2="A2condutancia_sierpinski_n54_m3_beta1.py"
SCRIPT3="A3condutancia_sierpinski_n54_m3_beta1.py"
SCRIPT4="A4condutancia_sierpinski_n54_m3_beta1.py"

# Executa cada script em um novo terminal
echo "Executando o primeiro script em um novo terminal..."
gnome-terminal -- bash -c "python3 $SCRIPT1; exec bash"

echo "Executando o segundo script em um novo terminal..."
gnome-terminal -- bash -c "python3 $SCRIPT2; exec bash"

echo "Executando o terceiro script em um novo terminal..."
gnome-terminal -- bash -c "python3 $SCRIPT3; exec bash"

echo "Executando o quarto script em um novo terminal..."
gnome-terminal -- bash -c "python3 $SCRIPT4; exec bash"

echo "Todos os scripts foram iniciados em novos terminais!"

