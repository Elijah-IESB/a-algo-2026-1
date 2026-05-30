"""Implementacao do algoritmo de Prim para arvore geradora minima."""

import heapq


def algoritmo_prim(grafo, inicio):
    """Retorna a arvore geradora minima e seu custo total."""
    visitados = set()
    fila_prioridade = []
    arvore_minima = []
    custo_total = 0

    visitados.add(inicio)

    for vizinho, custo in grafo[inicio]:
        heapq.heappush(fila_prioridade, (custo, inicio, vizinho))

    while fila_prioridade and len(visitados) < len(grafo):
        custo, origem, destino = heapq.heappop(fila_prioridade)

        if destino not in visitados:
            visitados.add(destino)
            arvore_minima.append((origem, destino, custo))
            custo_total += custo

            for proximo, novo_custo in grafo[destino]:
                if proximo not in visitados:
                    heapq.heappush(
                        fila_prioridade,
                        (novo_custo, destino, proximo),
                    )

    return arvore_minima, custo_total


grafo = {
    "A": [("B", 4), ("C", 4)],
    "B": [("A", 4), ("C", 2), ("D", 5)],
    "C": [("A", 4), ("B", 2), ("D", 5), ("E", 6)],
    "D": [("B", 5), ("C", 5), ("E", 3), ("F", 4)],
    "E": [("C", 6), ("D", 3), ("F", 2)],
    "F": [("D", 4), ("E", 2)],
}

rota, custo_total = algoritmo_prim(grafo, "A")

print("Cabos a serem instalados:")

for origem, destino, custo in rota:
    print(f"{origem} -> {destino}: {custo} km")

print(f"\nQuantidade total minima de cabos: {custo_total} km")
