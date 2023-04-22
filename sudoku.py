import pygame
from pygame.locals import *
from sys import exit

pygame.init()

tela = pygame.display.set_mode((725, 725))
pygame.display.set_caption('Sudoku')

# Definição de algumas cores necessárias na confecção da interface gráfica
branco = (255, 255, 255)
cinza_claro = (220, 220, 220)
cinza_escuro = (170, 170, 170)
vermelho = (255, 0, 0)
preto = (0, 0, 0)

fonte = pygame.font.SysFont('Arial', 40)
tela.fill((255, 255, 255))

# Definição da dimensão do tabuleiro, necessária para a confecção da interface gráfica
dimensao = 9
# Definição do tamanho em pixels de cada quadrado do tabuleiro, no caso 50x50
tamanho_quadrado = 75
# Espaçamento entre os retângulos do tabuleiro de sudoku
espacamento = 5

# Função para desenhar o tabuleiro
def desenhar_tabuleiro():
    # bordas que separam cada quadrado 3x3
    pygame.draw.line(tela, preto, (242, 0), (242, 725), 5)
    pygame.draw.line(tela, preto, (482, 0), (482, 725), 5)
    pygame.draw.line(tela, preto, (0, 242), (725, 242), 5)
    pygame.draw.line(tela, preto, (0, 482), (725, 482), 5)
    # Bordas laterais
    pygame.draw.line(tela, preto, (2, 2), (2, 723), 5)  # borda esquerda
    pygame.draw.line(tela, preto, (2, 2), (723, 2), 5)  # borda superior
    pygame.draw.line(tela, preto, (0, 723), (725, 723), 6)  # borda inferior
    pygame.draw.line(tela, preto, (723, 0), (723, 723), 5)  # borda direita

    for i in range(dimensao):
        for j in range(dimensao):
            x = espacamento + j * (tamanho_quadrado + espacamento)
            y = espacamento + i * (tamanho_quadrado + espacamento)
            cor = cinza_escuro if (i + j) % 2 == 0 else cinza_claro
            pygame.draw.rect(tela, cor, (x, y, tamanho_quadrado, tamanho_quadrado))


while True:
    desenhar_tabuleiro()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    pygame.display.update()