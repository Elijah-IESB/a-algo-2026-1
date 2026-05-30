"""Missao de engenharia de grafos com Dijkstra."""

import heapq
import random


class Grafo:
    """Representa um grafo ponderado nao direcionado."""

    def __init__(self, quantidade_nos):
        self.quantidade_nos = quantidade_nos
        self.adjacencias = {
            no: [] for no in range(1, quantidade_nos + 1)
        }
        self.arestas = set()

    def adicionar_aresta(self, origem, destino, peso):
        """Adiciona uma aresta ao grafo, evitando lacos e duplicatas."""
        aresta = tuple(sorted((origem, destino)))

        if origem == destino or aresta in self.arestas:
            return False

        self.arestas.add(aresta)

        self.adjacencias[origem].append((destino, peso))
        self.adjacencias[destino].append((origem, peso))

        return True

    def gerar_grafo_aleatorio(self, quantidade_arestas):
        """Gera um grafo ponderado aleatorio conectado."""
        quantidade_maxima = self.quantidade_nos * (self.quantidade_nos - 1) // 2

        if quantidade_arestas < self.quantidade_nos - 1:
            raise ValueError("A quantidade de arestas nao conecta todos os nos.")

        if quantidade_arestas > quantidade_maxima:
            raise ValueError("A quantidade de arestas excede o maximo possivel.")

        for no in range(1, self.quantidade_nos):
            peso = random.randint(1, 100)
            self.adicionar_aresta(no, no + 1, peso)

        while len(self.arestas) < quantidade_arestas:
            origem = random.randint(1, self.quantidade_nos)
            destino = random.randint(1, self.quantidade_nos)
            peso = random.randint(1, 100)

            self.adicionar_aresta(origem, destino, peso)

    def dijkstra(self, inicio, fim):
        """Calcula o menor caminho entre dois nos usando Dijkstra."""
        distancias = {
            no: float("inf") for no in range(1, self.quantidade_nos + 1)
        }
        anteriores = {
            no: None for no in range(1, self.quantidade_nos + 1)
        }

        distancias[inicio] = 0
        fila_prioridade = [(0, inicio)]

        while fila_prioridade:
            distancia_atual, no_atual = heapq.heappop(fila_prioridade)

            if no_atual == fim:
                break

            if distancia_atual > distancias[no_atual]:
                continue

            for vizinho, peso in self.adjacencias[no_atual]:
                nova_distancia = distancia_atual + peso

                if nova_distancia < distancias[vizinho]:
                    distancias[vizinho] = nova_distancia
                    anteriores[vizinho] = no_atual
                    heapq.heappush(fila_prioridade, (nova_distancia, vizinho))

        caminho = self.reconstruir_caminho(anteriores, inicio, fim)

        return caminho, distancias[fim]

    def reconstruir_caminho(self, anteriores, inicio, fim):
        """Reconstrui o caminho encontrado pelo algoritmo de Dijkstra."""
        caminho = []
        no_atual = fim

        while no_atual is not None:
            caminho.append(no_atual)
            no_atual = anteriores[no_atual]

        caminho.reverse()

        if caminho[0] == inicio:
            return caminho

        return []

    def imprimir_arestas(self):
        """Imprime todas as arestas do grafo."""
        print("ARESTAS DO GRAFO:")

        for origem, destino in sorted(self.arestas):
            peso = self.buscar_peso(origem, destino)
            print(f"{origem} -- {destino} | peso: {peso}")

    def buscar_peso(self, origem, destino):
        """Busca o peso de uma aresta."""
        for vizinho, peso in self.adjacencias[origem]:
            if vizinho == destino:
                return peso

        return None


def main():
    """Executa a missao de engenharia de grafos."""
    quantidade_nos = 50
    quantidade_arestas = 150
    no_inicio = 1
    no_fim = 50

    grafo = Grafo(quantidade_nos)
    grafo.gerar_grafo_aleatorio(quantidade_arestas)

    caminho, custo_total = grafo.dijkstra(no_inicio, no_fim)

    print("=" * 60)
    print("MISSAO DE ENGENHARIA DE GRAFOS")
    print("=" * 60)
    print(f"Grafo gerado com {quantidade_nos} nos e {len(grafo.arestas)} arestas.")
    print()

    print(f"Menor caminho do No {no_inicio} ate o No {no_fim}:")
    print(" -> ".join(map(str, caminho)))
    print()
    print(f"Custo total calculado: {custo_total}")

    print()
    print("=" * 60)
    print("Resumo da entrega:")
    print("Arquivo .py gerado com grafo aleatorio, Dijkstra e saida no terminal.")
    print("=" * 60)


if __name__ == "__main__":
    main()
