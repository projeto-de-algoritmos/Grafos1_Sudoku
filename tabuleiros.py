def tabuleiro_fixo(grafo_tabuleiro):
    # Criando board fixo para não ser necessário gerar um aleatório a toda nova interação
    grafo_tabuleiro.nodes[(0, 5)][repr(int)] = 7
    grafo_tabuleiro.nodes[(0, 8)][repr(int)] = 1
    grafo_tabuleiro.nodes[(1, 0)][repr(int)] = 6
    grafo_tabuleiro.nodes[(1, 2)][repr(int)] = 2
    grafo_tabuleiro.nodes[(2, 1)][repr(int)] = 7
    grafo_tabuleiro.nodes[(2, 3)][repr(int)] = 3
    grafo_tabuleiro.nodes[(2, 4)][repr(int)] = 6
    grafo_tabuleiro.nodes[(2, 5)][repr(int)] = 9
    grafo_tabuleiro.nodes[(3, 3)][repr(int)] = 4
    grafo_tabuleiro.nodes[(3, 6)][repr(int)] = 1
    grafo_tabuleiro.nodes[(3, 8)][repr(int)] = 7
    grafo_tabuleiro.nodes[(4, 0)][repr(int)] = 9
    grafo_tabuleiro.nodes[(4, 1)][repr(int)] = 6
    grafo_tabuleiro.nodes[(4, 3)][repr(int)] = 7
    grafo_tabuleiro.nodes[(4, 5)][repr(int)] = 3
    grafo_tabuleiro.nodes[(4, 7)][repr(int)] = 4
    grafo_tabuleiro.nodes[(5, 2)][repr(int)] = 8
    grafo_tabuleiro.nodes[(5, 7)][repr(int)] = 9
    grafo_tabuleiro.nodes[(6, 2)][repr(int)] = 4
    grafo_tabuleiro.nodes[(6, 6)][repr(int)] = 3
    grafo_tabuleiro.nodes[(7, 3)][repr(int)] = 8
    grafo_tabuleiro.nodes[(7, 5)][repr(int)] = 6
    grafo_tabuleiro.nodes[(8, 0)][repr(int)] = 5
    grafo_tabuleiro.nodes[(8, 6)][repr(int)] = 9