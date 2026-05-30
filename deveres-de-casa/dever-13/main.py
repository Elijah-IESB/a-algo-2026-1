"""Desafio da arvore geradora maxima com Kruskal."""

import time


class Grafo:
    """Representa um grafo ponderado para executar Kruskal maximo."""

    def __init__(self, vertices):
        self.vertices = vertices
        self.grafo = []

    def adicionar_aresta(self, origem, destino, peso):
        """Adiciona uma aresta ponderada ao grafo."""
        self.grafo.append([origem, destino, peso])

    def buscar_raiz(self, pai, indice):
        """Busca a raiz de um conjunto usando compressao de caminho."""
        if pai[indice] == indice:
            return indice

        pai[indice] = self.buscar_raiz(pai, pai[indice])
        return pai[indice]

    def unir_redes(self, pai, rank, raiz_x, raiz_y):
        """Une dois conjuntos usando o rank para balancear a arvore."""
        if rank[raiz_x] < rank[raiz_y]:
            pai[raiz_x] = raiz_y
        elif rank[raiz_x] > rank[raiz_y]:
            pai[raiz_y] = raiz_x
        else:
            pai[raiz_y] = raiz_x
            rank[raiz_x] += 1

    def executar_kruskal_maximo(self):
        """Retorna a arvore geradora maxima e seu custo total."""
        resultado = []
        custo_total = 0
        arestas_ordenadas = sorted(
            self.grafo,
            key=lambda item: item[2],
            reverse=True,
        )

        pai = list(range(self.vertices))
        rank = [0] * self.vertices

        indice_aresta = 0
        quantidade_arestas = 0

        while (
            quantidade_arestas < self.vertices - 1
            and indice_aresta < len(arestas_ordenadas)
        ):
            origem, destino, peso = arestas_ordenadas[indice_aresta]
            indice_aresta += 1

            raiz_origem = self.buscar_raiz(pai, origem)
            raiz_destino = self.buscar_raiz(pai, destino)

            if raiz_origem != raiz_destino:
                resultado.append([origem, destino, peso])
                custo_total += peso
                quantidade_arestas += 1
                self.unir_redes(pai, rank, raiz_origem, raiz_destino)

        return resultado, custo_total


def montar_grafo():
    """Monta o grafo usado na atividade."""
    grafo = Grafo(8)

    grafo.adicionar_aresta(4, 7, 1)
    grafo.adicionar_aresta(5, 6, 2)
    grafo.adicionar_aresta(4, 5, 3)
    grafo.adicionar_aresta(6, 7, 4)
    grafo.adicionar_aresta(0, 1, 5)
    grafo.adicionar_aresta(3, 7, 6)
    grafo.adicionar_aresta(2, 5, 7)
    grafo.adicionar_aresta(2, 6, 8)
    grafo.adicionar_aresta(1, 2, 9)
    grafo.adicionar_aresta(1, 6, 10)
    grafo.adicionar_aresta(1, 5, 11)
    grafo.adicionar_aresta(1, 7, 13)
    grafo.adicionar_aresta(1, 4, 14)
    grafo.adicionar_aresta(0, 4, 15)
    grafo.adicionar_aresta(0, 3, 16)
    grafo.adicionar_aresta(3, 6, 17)
    grafo.adicionar_aresta(0, 7, 18)

    return grafo


def main():
    """Executa o desafio da arvore geradora maxima."""
    grafo = montar_grafo()

    inicio = time.perf_counter()
    caminho_final, custo_final = grafo.executar_kruskal_maximo()
    fim = time.perf_counter()

    tempo_execucao = (fim - inicio) * 1000

    print("--- RESULTADO DA ARVORE GERADORA MAXIMA ---")
    print("Rotas escolhidas para o caminho mais caro sem ciclos:")

    for origem, destino, peso in caminho_final:
        print(f"Rota da cidade {origem} para a cidade {destino} | Custo: {peso}")

    print(f"\nCusto Total Maximo: {custo_final}")
    print(f"Tempo de execucao: {tempo_execucao:.4f} milissegundos")


if __name__ == "__main__":
    main()
