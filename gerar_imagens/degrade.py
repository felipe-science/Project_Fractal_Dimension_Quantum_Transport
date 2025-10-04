import matplotlib.pyplot as plt
import numpy as np

def get_radial_color(x, y):
    """ Gera uma cor com um degradê radial que passa de azul para roxo e depois vermelho """
    cx, cy = 0.5, 0.5  # Centro do padrão
    distance = np.sqrt((x + 0.5 - cx) ** 2 + (y + 0.5 - cy) ** 2)  # Distância ao centro
    norm_distance = distance / np.sqrt(2)  # Normaliza para intervalo [0,1]

    # Degradê com transição azul -> roxo -> vermelho
    r = np.sin(norm_distance * np.pi / 2)  # Suaviza o aumento do vermelho
    g = 0.2 * (1 - norm_distance)  # Reduz o verde para tons mais puros
    b = np.cos(norm_distance * np.pi / 2)  # Azul decai suavemente

    return (r, g, b)

    

def get_radial_color_mat(x, y):
    """Gera uma cor com degradê radial passando por azul, laranja, verde, vermelho e roxo"""
    
    # Definindo as cores como tuplas RGB normalizadas
    colors = [
        (31/255, 119/255, 180/255),  # Azul
        (255/255, 127/255, 14/255),  # Laranja
        (44/255, 160/255, 44/255),   # Verde
        (214/255, 39/255, 40/255),   # Vermelho
        (148/255, 103/255, 189/255)  # Roxo
    ]
    
    cx, cy = 0.5, 0.5  # Centro do padrão
    distance = np.sqrt((x + 0.5 - cx) ** 2 + (y + 0.5 - cy) ** 2)
    norm_distance = distance / np.sqrt(2)  # Normalizado para [0,1]
    
    # Mapear norm_distance em 4 intervalos entre as 5 cores
    n_segments = len(colors) - 1
    segment_length = 1.0 / n_segments
    index = min(int(norm_distance / segment_length), n_segments - 1)
    
    t = (norm_distance - index * segment_length) / segment_length
    c1 = colors[index]
    c2 = colors[index + 1]
    
    # Interpolação linear entre c1 e c2
    r = (1 - t) * c1[0] + t * c2[0]
    g = (1 - t) * c1[1] + t * c2[1]
    b = (1 - t) * c1[2] + t * c2[2]
    
    return (r, g, b)



def sierpinski_carpet(x, y, size, level):
    if level == 0:
        color = get_radial_color_mat(x, y)  # Cor baseada na posição radial
        plt.gca().add_patch(plt.Rectangle((x, y), size, size, color=color))
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

def plot_sierpinski(level):
    plt.figure(figsize=(8, 8))
    ax = plt.gca()
    ax.set_facecolor("#1A1A1A")  # Define fundo fixo como preto
    plt.axis('off')
    sierpinski_carpet(0, 0, 1, level)
    plt.savefig(f"sierpinski_radial_{level}.png", dpi=300, bbox_inches='tight', facecolor="#000000")
    plt.show()

# Gerar o Carpete de Sierpinski com degradê radial e fundo fixo
for m in range(5):
    plot_sierpinski(m)
