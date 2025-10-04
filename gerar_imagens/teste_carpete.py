import matplotlib.pyplot as plt
import numpy as np

def sierpinski_carpet(x, y, size, level):
    if level == 0:
        # Desenha um quadrado preenchido
        plt.gca().add_patch(plt.Rectangle((x, y), size, size, color=(1, 0.1, 0.7))) #magenta claro
        plt.gca().add_patch(plt.Rectangle((x, y), size, size, color=(0.6, 0.4, 0.8))) #Lavanda
        plt.gca().add_patch(plt.Rectangle((x, y), size, size, color=(0.6, 0.4, 0.8))) #Lavanda
        plt.gca().add_patch(plt.Rectangle((x, y), size, size, color=(0.9, 0.5, 0.2))) #Laranja queimado
        plt.gca().add_patch(plt.Rectangle((x, y), size, size, color=(0.2, 0.8, 0.2))) #Turquesa
        plt.gca().add_patch(plt.Rectangle((x, y), size, size, color=(0.5, 0.25, 0.0))) #Marrom escuro
        plt.gca().add_patch(plt.Rectangle((x, y), size, size, color=(1.0, 0.8, 0.6))) #Pessego
        plt.gca().add_patch(plt.Rectangle((x, y), size, size, color=(0.31, 0.78, 0.47))) #Esmeralda
        plt.gca().add_patch(plt.Rectangle((x, y), size, size, color=(1.0, 0.84, 0.0))) #Ouro
        plt.gca().add_patch(plt.Rectangle((x, y), size, size, color=(0.4, 0.7, 1.0))) #Azul celeste
        plt.gca().add_patch(plt.Rectangle((x, y), size, size, color=(0.2, 0.2, 0.2))) #Azul celeste
        plt.gca().add_patch(plt.Rectangle((x, y), size, size, color=(1.0, 0.2, 0.2))) #Vermelho intenso

    else:
        # Recursivamente desenha 8 quadrados
        new_size = size / 3
        sierpinski_carpet(x, y, new_size, level - 1)
        sierpinski_carpet(x + new_size, y, new_size, level - 1)
        sierpinski_carpet(x + 2 * new_size, y, new_size, level - 1)
        sierpinski_carpet(x, y + new_size, new_size, level - 1)
        sierpinski_carpet(x + 2 * new_size, y + new_size, new_size, level - 1)
        sierpinski_carpet(x, y + 2 * new_size, new_size, level - 1)
        sierpinski_carpet(x + new_size, y + 2 * new_size, new_size, level - 1)
        sierpinski_carpet(x + 2 * new_size, y + 2 * new_size, new_size, level - 1)

def plot_sierpinski(level):
    plt.figure(figsize=(8, 8))
    plt.axis('off')
    sierpinski_carpet(0, 0, 1, level)
    plt.savefig(f"m{level}.png")
    plt.show()

# Exemplo de uso: Gerar o carpete de Sierpinski de nível 4
for m in range(4):
    plot_sierpinski(m)

