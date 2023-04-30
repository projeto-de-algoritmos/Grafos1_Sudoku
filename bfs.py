
def verificar_entrada(grafo_tabuleiro):
    # Cria uma fila para armazenar os nós a serem visitados
    fila = []
    # Cria um conjunto para armazenar os nós já visitados
    visitados = set()
    # Adiciona o primeiro nó na fila
    fila.append((0, 0))
    # Enquanto a fila não estiver vazia, repete o seguinte:
    while fila:
        # Remove o primeiro nó da fila e o marca como visitado
        i, j = fila.pop(0)
        visitados.add((i, j))
        # Obtém o valor do nó atual
        valor = grafo_tabuleiro.nodes[(i, j)]['valor']
        # Verifica se o valor é distinto dos valores dos vizinhos na mesma linha, coluna ou bloco 3x3
        for k, l in pega_vizinhos(i, j):
            if grafo_tabuleiro.nodes[(k, l)]['valor'] == valor:
                return False
            # Se o vizinho ainda não foi visitado, adiciona ele na fila
            if (k, l) not in visitados:
                fila.append((k, l))
    # Se todas as verificações passaram, o sudoku é válido
    return True


def pega_vizinhos(i, j):
    # Retorna uma lista com os índices dos vizinhos de um nó na mesma linha, coluna ou bloco 3x3
    vizinhos = []
    for k in range(9):
        if k != j:
            vizinhos.append((i, k))
        if k != i:
            vizinhos.append((k, j))

    sublinha = i // 3
    subcoluna = j // 3
    for k in range(sublinha * 3, sublinha * 3 + 3):
        for l in range(subcoluna * 3, subcoluna * 3 + 3):
            if k != i or l != j:
                vizinhos.append((k, l))
    return vizinhos
