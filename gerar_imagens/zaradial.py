import matplotlib.pyplot as plt
import numpy as np

def get_radial_color_matrix(resolution=300):
    """ Gera uma matriz de cores com um degradê radial 
        Azul → Vermelho → Amarelo 
    """
    x = np.linspace(-1, 1, resolution)
    y = np.linspace(-1, 1, resolution)
    X, Y = np.meshgrid(x, y)

    # Cálculo da distância normalizada ao centro (0,0)
    distance = np.sqrt(X**2 + Y**2)  # Distância radial ao centro
    norm_distance = np.clip(distance / np.sqrt(2), 0, 1)  # Normaliza para [0,1]

    # Azul → Vermelho → Amarelo (Radial)
    R = np.minimum(2 * norm_distance, 1.0)  # Aumenta o vermelho progressivamente
    G = np.maximum(2 * (norm_distance - 0.5), 0.0)  # Aumenta o verde na segunda metade
    B = np.maximum(1.0 - 2 * norm_distance, 0.0)  # Diminui o azul radialmente

    return R, G, B

def get_horizontal_color_matrix(resolution=300):
    """ Gera uma matriz de cores com um degradê horizontal 
        Azul (esquerda) → Vermelho (meio) → Amarelo (direita) 
    """
    x = np.linspace(0, 1, resolution)  # Variação apenas no eixo X
    norm_distance = x  # Normalização direta de 0 a 1

    # Azul → Vermelho → Amarelo (Horizontal)
    R = np.minimum(2 * norm_distance, 1.0)  # Aumenta o vermelho progressivamente
    G = np.maximum(2 * (norm_distance - 0.5), 0.0)  # Aumenta o verde na segunda metade
    B = np.maximum(1.0 - 2 * norm_distance, 0.0)  # Diminui o azul progressivamente

    # Expande para toda a altura (Y constante)
    R, G, B = np.tile(R, (resolution, 1)), np.tile(G, (resolution, 1)), np.tile(B, (resolution, 1))

    return R, G, B

def get_diagonal_color_matrix(resolution=300):
    """ Gera uma matriz de cores com um degradê diagonal 
        Azul (canto superior esquerdo) → Vermelho (centro) → Amarelo (canto inferior direito) 
    """
    x = np.linspace(0, 1, resolution)
    y = np.linspace(0, 1, resolution)
    X, Y = np.meshgrid(x, y)

    norm_distance = (X + Y) / 2  # Combina X e Y para criar o efeito diagonal

    # Azul → Vermelho → Amarelo (Diagonal)
    R = np.minimum(2 * norm_distance, 1.0)  # Aumenta o vermelho progressivamente
    G = np.maximum(2 * (norm_distance - 0.5), 0.0)  # Aumenta o verde na segunda metade
    B = np.maximum(1.0 - 2 * norm_distance, 0.0)  # Diminui o azul progressivamente

    return R, G, B

def get_diagonal_cyan_brown(resolution=300):
    """ 
    Gera uma matriz de cores com um degradê diagonal 
    Ciano (0,1,1) → Verde/Acinzentado → Marrom (0.5,0.25,0)
    """
    x = np.linspace(0, 1, resolution)
    y = np.linspace(0, 1, resolution)
    X, Y = np.meshgrid(x, y)

    norm_distance = (X + Y) / 2  # Controla a variação diagonal

    # Ciano (0,1,1) → Verde/Acinzentado → Marrom (0.55,0.27,0.07)
    R = 0.2 + 0.35 * norm_distance  # Aumento gradual do vermelho
    G = 1.0 - 0.8 * norm_distance  # Verde diminui suavemente
    B = 1.0 - 1.2 * norm_distance  # Azul desaparece mais rapidamente

    R = np.clip(R, 0, 0.55)
    G = np.clip(G, 0.27, 1.0)
    B = np.clip(B, 0.07, 1.0)

    return R, G, B


def get_diagonal_blue_red(resolution=300):
    """ Gera uma matriz de cores com um degradê diagonal 
        Azul Médio (31, 119, 180) → Vermelho (255, 0, 0)
    """
    x = np.linspace(0, 1, resolution)
    y = np.linspace(0, 1, resolution)
    X, Y = np.meshgrid(x, y)

    norm_distance = (X + Y) / 2  # Controla a variação diagonal

    # Azul Médio (31, 119, 180) → Vermelho (255, 0, 0)
    R = 31 + norm_distance * (255 - 31)  # Aumenta o vermelho progressivamente
    G = 119 - norm_distance * 119  # Reduz o verde até 0
    B = 180 - norm_distance * 180  # Reduz o azul até 0

    return R / 255, G / 255, B / 255  # Normaliza para intervalo [0,1]

def sierpinski_carpet(x, y, size, level):
    if level == 0:
        return
    else:
        new_size = size / 3
        sierpinski_carpet(x, y, new_size, level - 1)
        sierpinski_carpet(x + new_size, y, new_size, level - 1)
        sierpinski_carpet(x + 2 * new_size, y, new_size, level - 1)
        sierpinski_carpet(x, y + new_size, new_size, level - 1)
        sierpinski_carpet(x + 2 * new_size, y + new_size, new_size, level - 1)
        sierpinski_carpet(x, y + 2 * new_size, new_size, level - 1)
        sierpinski_carpet(x + new_size, y + 2 * new_size, new_size, level - 1)
        sierpinski_carpet(x + 2 * new_size, y + 2 * new_size, new_size, level - 1)

        # Adiciona buraco central (remove cor)
        plt.gca().add_patch(plt.Rectangle((x + new_size, y + new_size), new_size, new_size, color="#1A1A1A"))

def plot_sierpinski(level):
    plt.figure(figsize=(8, 8))
    ax = plt.gca()
    ax.set_facecolor("#1A1A1A")  # Define fundo fixo como preto
    plt.axis('off')

    # Aplicar sempre o degradê inicial
    R, G, B = get_diagonal_blue_red()
    img = np.dstack([R, G, B])  # Combinar canais
    plt.imshow(img, extent=[0, 1, 0, 1], origin="lower")

    sierpinski_carpet(0, 0, 1, level)
    plt.savefig(f"sierpinski_radial_{level}.png", dpi=300, bbox_inches='tight', facecolor="#000000")
    plt.show()

# Gerar o Carpete de Sierpinski com degradê radial e fundo fixo
for m in range(4):
    plot_sierpinski(m)
