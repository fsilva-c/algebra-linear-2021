import numpy as np
from matplotlib import pyplot as plt
from datetime import datetime

circle = [
    [0, 3],
    [1.5, 2.5],
    [2.5, 1.5],
    [3, 0],
    [2.5, -1.5],
    [1.5, -2.5],
    [0, -3],
    [-1.5, -2.5],
    [-2.5, -1.5],
    [-3, 0],
    [-2.5, 1.5],
    [-1.5, 2.5],
    [0, 3]
]

p_hours = [
    [0, 1.5],
    [0, 1],
    [0, 0.5],
    [0, 0]
]

p_minutes = [
    [0, 2],
    [0, 1.5],
    [0, 1],
    [0, 0.5],
    [0, 0]
]

p_seconds = [
    [0, 2.5],
    [0, 2],
    [0, 1.5],
    [0, 1],
    [0, 0.5],
    [0, 0]
]

def rotate_matrix(_vetor, _ang_rotation):
    '''
        Este método recebe um vetor em R2 e um angulo, e rotaciona
        este vetor utilizando a matriz de rotação.
    '''
    m_rot = np.array([
        [np.cos(np.deg2rad(_ang_rotation)), -np.sin(np.deg2rad(_ang_rotation))],
        [np.sin(np.deg2rad(_ang_rotation)),  np.cos(np.deg2rad(_ang_rotation))]
    ])

    new_vetor = np.matmul(m_rot, _vetor)

    return new_vetor

def connect_points(p_0, p_1):
    ''' 
        Este metodo recebe dois pontos e os conecta atraves
        de uma linha, plotando este segmento de reta no grafico.
    '''
    ax.plot([p_0[0], p_1[0]], [p_0[1], p_1[1]], 'k-')

def draw_lines_points(_list_x_y):
    '''
        Este metodo recebe uma lista de pontos em R2 (x, y)
        e desenha uma linha entre cada ponto da lista.
    '''
    for i in range(len(_list_x_y) - 1):
        connect_points(_list_x_y[i], _list_x_y[i + 1])

def plot_ponteiro(_ponteiro, _color, _ang_rotation):
    '''
        Este metodo recebe uma lista de pontos, uma cor e um angulo, 
        e realiza a rotação de todos os pontos contidos na lista.
    '''
    for i in range(len(_ponteiro)):
        vetor = rotate_matrix(_ponteiro[i], _ang_rotation)
        ax.plot(vetor[0], vetor[1], _color)
        _ponteiro[i] = vetor

''' configuração inicial do gráfico '''
fig, ax = plt.subplots()

draw_lines_points(circle) # desenha o circulo de fora do grafico

ax.set_title('Relógio Alinhamento Limiar')
ax.figure.set_size_inches(8, 8)
plt.xticks([])
plt.yticks([])
ax.text(-0.2, 2.5, '12', fontsize=25)
ax.text(2.5, -0.2, '3',  fontsize=25)
ax.text(-0.1, -2.8, '6', fontsize=25)
ax.text(-2.8, -0.1, '9', fontsize=25)

''' primeiro plot... '''
A = -1 * 360
now = datetime.now()
# ajuste dos ponteiros do relogio, seguindo a hora atual...
plot_ponteiro(p_hours,   'co', (((A / 60) * now.minute) / 12) + ((A / 12) * now.hour))
plot_ponteiro(p_minutes, 'bo', (A / 60) * now.minute)
plot_ponteiro(p_seconds, 'go', (A / 60) * now.second)

''' plot dinâmico dos ponteiros... '''
ang_seconds = A / 60
ang_minutes = ang_seconds / 60
ang_hours = ang_minutes / 60

wait = 1

while True:
    plot_ponteiro(p_seconds, 'go', ang_seconds)
    plot_ponteiro(p_minutes, 'bo', ang_minutes)
    plot_ponteiro(p_hours,   'co', ang_hours)

    plt.draw()

    for i in range(26, 11, -1):
        ax.lines.remove(ax.lines[i])

    plt.pause(wait)
