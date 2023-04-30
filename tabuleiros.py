def tabuleiro_fixo(grafo_tabuleiro):
    # Criando board fixo para não ser necessário gerar um aleatório a toda nova interação

    grafo_tabuleiro.nodes[(0, 1)]['valor'] = 3
    grafo_tabuleiro.nodes[(0, 2)]['valor'] = 4
    grafo_tabuleiro.nodes[(0, 3)]['valor'] = 6
    grafo_tabuleiro.nodes[(0, 4)]['valor'] = 7
    grafo_tabuleiro.nodes[(0, 6)]['valor'] = 8
    grafo_tabuleiro.nodes[(0, 7)]['valor'] = 9
    grafo_tabuleiro.nodes[(1, 1)]['valor'] = 9
    grafo_tabuleiro.nodes[(1, 3)]['valor'] = 5
    grafo_tabuleiro.nodes[(1, 4)]['valor'] = 1
    grafo_tabuleiro.nodes[(1, 5)]['valor'] = 8
    grafo_tabuleiro.nodes[(1, 6)]['valor'] = 3
    grafo_tabuleiro.nodes[(1, 7)]['valor'] = 7
    grafo_tabuleiro.nodes[(1, 8)]['valor'] = 4
    grafo_tabuleiro.nodes[(2, 0)]['valor'] = 8
    grafo_tabuleiro.nodes[(2, 2)]['valor'] = 3
    grafo_tabuleiro.nodes[(2, 6)]['valor'] = 2
    grafo_tabuleiro.nodes[(2, 7)]['valor'] = 5
    grafo_tabuleiro.nodes[(2, 8)]['valor'] = 6
    grafo_tabuleiro.nodes[(3, 0)]['valor'] = 4
    grafo_tabuleiro.nodes[(3, 1)]['valor'] = 1
    grafo_tabuleiro.nodes[(3, 2)]['valor'] = 5
    grafo_tabuleiro.nodes[(3, 4)]['valor'] = 8
    grafo_tabuleiro.nodes[(3, 5)]['valor'] = 6
    grafo_tabuleiro.nodes[(3, 7)]['valor'] = 3
    grafo_tabuleiro.nodes[(4, 2)]['valor'] = 9
    grafo_tabuleiro.nodes[(4, 4)]['valor'] = 2
    grafo_tabuleiro.nodes[(4, 6)]['valor'] = 7
    grafo_tabuleiro.nodes[(4, 8)]['valor'] = 5
    grafo_tabuleiro.nodes[(5, 0)]['valor'] = 7
    grafo_tabuleiro.nodes[(5, 1)]['valor'] = 8
    grafo_tabuleiro.nodes[(5, 3)]['valor'] = 9
    grafo_tabuleiro.nodes[(5, 4)]['valor'] = 5
    grafo_tabuleiro.nodes[(5, 5)]['valor'] = 1
    grafo_tabuleiro.nodes[(5, 6)]['valor'] = 4
    grafo_tabuleiro.nodes[(5, 8)]['valor'] = 2
    grafo_tabuleiro.nodes[(6, 0)]['valor'] = 9
    grafo_tabuleiro.nodes[(6, 1)]['valor'] = 4
    grafo_tabuleiro.nodes[(6, 3)]['valor'] = 2
    grafo_tabuleiro.nodes[(6, 3)]['valor'] = 2
    grafo_tabuleiro.nodes[(6, 4)]['valor'] = 5
    grafo_tabuleiro.nodes[(6, 5)]['valor'] = 7
    grafo_tabuleiro.nodes[(6, 7)]['valor'] = 8
    grafo_tabuleiro.nodes[(6, 8)]['valor'] = 1
    grafo_tabuleiro.nodes[(7, 0)]['valor'] = 3
    grafo_tabuleiro.nodes[(7, 1)]['valor'] = 2
    grafo_tabuleiro.nodes[(7, 2)]['valor'] = 5
    grafo_tabuleiro.nodes[(7, 4)]['valor'] = 1
    grafo_tabuleiro.nodes[(7, 6)]['valor'] = 6
    grafo_tabuleiro.nodes[(7, 7)]['valor'] = 7
    grafo_tabuleiro.nodes[(7, 8)]['valor'] = 9
    grafo_tabuleiro.nodes[(8, 1)]['valor'] = 8
    grafo_tabuleiro.nodes[(8, 2)]['valor'] = 7
    grafo_tabuleiro.nodes[(8, 3)]['valor'] = 6
    grafo_tabuleiro.nodes[(8, 4)]['valor'] = 9
    grafo_tabuleiro.nodes[(8, 5)]['valor'] = 2
    grafo_tabuleiro.nodes[(8, 7)]['valor'] = 5
    grafo_tabuleiro.nodes[(8, 8)]['valor'] = 3

    ## apagar daqui pra cima
    grafo_tabuleiro.nodes[(0, 5)]['valor'] = 7
    grafo_tabuleiro.nodes[(0, 8)]['valor'] = 1
    grafo_tabuleiro.nodes[(1, 0)]['valor'] = 6
    grafo_tabuleiro.nodes[(1, 2)]['valor'] = 2
    grafo_tabuleiro.nodes[(2, 1)]['valor'] = 7
    grafo_tabuleiro.nodes[(2, 3)]['valor'] = 3
    grafo_tabuleiro.nodes[(2, 4)]['valor'] = 6
    grafo_tabuleiro.nodes[(2, 5)]['valor'] = 9
    grafo_tabuleiro.nodes[(3, 3)]['valor'] = 4
    grafo_tabuleiro.nodes[(3, 6)]['valor'] = 1
    grafo_tabuleiro.nodes[(3, 8)]['valor'] = 7
    grafo_tabuleiro.nodes[(4, 0)]['valor'] = 9
    grafo_tabuleiro.nodes[(4, 1)]['valor'] = 6
    grafo_tabuleiro.nodes[(4, 3)]['valor'] = 7
    grafo_tabuleiro.nodes[(4, 5)]['valor'] = 3
    grafo_tabuleiro.nodes[(4, 7)]['valor'] = 4
    grafo_tabuleiro.nodes[(5, 2)]['valor'] = 8
    grafo_tabuleiro.nodes[(5, 7)]['valor'] = 9
    grafo_tabuleiro.nodes[(6, 2)]['valor'] = 4
    grafo_tabuleiro.nodes[(6, 6)]['valor'] = 3
    grafo_tabuleiro.nodes[(7, 3)]['valor'] = 8
    grafo_tabuleiro.nodes[(7, 5)]['valor'] = 6
    grafo_tabuleiro.nodes[(8, 0)]['valor'] = 5
    grafo_tabuleiro.nodes[(8, 6)]['valor'] = 9



def verificar_coordenadas(i, j):
    coordenadas = [(0, 5), (0, 8), (1, 0), (1, 2), (2, 1), (2, 3), (2, 4), (2, 5),
                   (3, 3), (3, 6), (3, 8), (4, 0), (4, 1), (4, 3), (4, 5), (4, 7),
                   (5, 2), (5, 7), (6, 2), (6, 6), (7, 3), (7, 5), (8, 0), (8, 6)]
    if (i, j) in coordenadas:
        return True
    else:
        return False
