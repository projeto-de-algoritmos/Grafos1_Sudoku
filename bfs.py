def verificar_entrada(grafo_tabuleiro):
    fila = []
    for i in range(9):
        for j in range(9):
            if grafo_tabuleiro.nodes[(i, j)]['valor'] == 0:
                fila.append((i, j))

    while fila:
        linha, coluna = fila.pop(0)
        if grafo_tabuleiro.nodes[(linha, coluna)]['valor'] == 0:
            for x in range(1, 10):
                if numero_valido(grafo_tabuleiro, linha, coluna, x):
                    grafo_tabuleiro.nodes[(linha, coluna)]['valor'] = x
                    fila.append((linha, coluna))
                    break
            else:
                # Nenhum valor é válido, volta para o nó anterior
                grafo_tabuleiro.nodes[(linha, coluna)]['valor'] = 0
                if fila:
                    linha, coluna = fila[-1]
                else:
                    # Todos os nós foram preenchidos e verificados
                    break
        else:
            if not numero_valido(grafo_tabuleiro, linha, coluna, grafo_tabuleiro.nodes[(linha, coluna)]['valor']):
                return False
            for i, j in pega_vizinhos(linha, coluna):
                if grafo_tabuleiro.nodes[(i, j)]['valor'] == 0:
                    fila.append((i, j))

    return True


def numero_valido(grafo_tabuleiro, linha, coluna, x):
    if x in [grafo_tabuleiro.nodes[(linha, j)]['valor'] for j in range(9)]:
        return False
    if x in [grafo_tabuleiro.nodes[(i, coluna)]['valor'] for i in range(9)]:
        return False
    linha_bloco, coluna_bloco = linha // 3, coluna // 3
    for i in range(linha_bloco * 3, linha_bloco * 3 + 3):
        for j in range(coluna_bloco * 3, coluna_bloco * 3 + 3):
            if grafo_tabuleiro.nodes[(i, j)]['valor'] == x:
                return False
    return True


def pega_vizinhos(linha, coluna):
    vizinhos = []
    for i in range(9):
        if i != coluna:
            vizinhos.append((linha, i))
        if i != linha:
            vizinhos.append((i, coluna))

    sublinha = linha // 3
    subcoluna = coluna // 3
    for i in range(sublinha * 3, sublinha * 3 + 3):
        for j in range(subcoluna * 3, subcoluna * 3 + 3):
            if i != linha or j != coluna:
                vizinhos.append((i, j))

    return vizinhos
