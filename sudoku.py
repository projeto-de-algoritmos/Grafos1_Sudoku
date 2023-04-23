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
# define o fundo da tela como branco
tela.fill((255, 255, 255))

# Definição da dimensão do tabuleiro, necessária para a confecção da interface gráfica
dimensao = 9
# Definição do tamanho em píxeis de cada quadrado do tabuleiro, no caso 50x50
tamanho_quadrado = 75
# Espaçamento entre os retângulos do tabuleiro de sudoku
espacamento = 5
# matriz de elementos que representam os valores dentro do tabuleiro iniciando as 91 posições com 0
tabuleiro = {(i, j): 0 for i in range(dimensao) for j in range(dimensao)}
# iniciando uma célula como selecionado, para não quebrar a função
i_sel, j_sel = 0, 0


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
            # loopings para adicionar quadrados de cores diferentes, formando o tabuleiro
            x = espacamento + j * (tamanho_quadrado + espacamento)
            y = espacamento + i * (tamanho_quadrado + espacamento)
            cor = cinza_escuro if (i + j) % 2 == 0 else cinza_claro
            pygame.draw.rect(tela, cor, (x, y, tamanho_quadrado, tamanho_quadrado))
            # renderizar na tela o número de cada elemento da matriz
            if tabuleiro[(i, j)] != 0:  # verifica se a posição (i, j), do tabuleiro difere de 0
                # gera uma string com o número que o player digitou
                numero = fonte.render(str(tabuleiro[(i, j)]), True, preto)
                # a função caixa_de_numero cria um quadrado que pode renderizar texto, é já define o número a ser
                # exibido no centro do retângulo selecionado
                caixa_de_numero = numero.get_rect(center=(x + (tamanho_quadrado / 2), y + (tamanho_quadrado / 2)))
                # adiciona na tela a caixa_de_numero
                tela.blit(numero, caixa_de_numero)


while True:
    desenhar_tabuleiro()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        elif event.type == KEYDOWN:  # verifica se alguma tecla foi pressionada
            if event.unicode.isdigit():
                # atualiza o valor dentro da célula da matriz de elementos do tabuleiro, conforme o valor digitado
                tabuleiro[(i_sel, j_sel)] = int(event.unicode)
        # verifica em qual quadrado o player clicou
        elif event.type == MOUSEBUTTONDOWN:
            # atualiza as coordenadas da célula selecionada
            posicao_mouse = pygame.mouse.get_pos()
            # [1] representa o eixo y
            i_sel = (posicao_mouse[1] - espacamento) // (tamanho_quadrado + espacamento)
            # [0] representa o eixo x
            j_sel = (posicao_mouse[0] - espacamento) // (tamanho_quadrado + espacamento)
    pygame.display.update()
