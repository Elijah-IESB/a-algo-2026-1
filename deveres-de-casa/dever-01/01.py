import time
import random

def insertion_sort(lista):
    for i in range(1, len(lista)):
        chave = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > chave:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = chave

# 1. Solicita o tamanho da lista
n = int(input("Digite o tamanho da lista (n): "))

# 2. Gera uma lista aleatória para testar (pior cenário seria uma lista decrescente)
lista_teste = [random.randint(0, n * 10) for _ in range(n)]

print(f"\nOrdenando {n} elementos...")

# 3. Medição do tempo
inicio = time.time()  # Marca o tempo inicial
insertion_sort(lista_teste)
fim = time.time()     # Marca o tempo final

tempo_total = fim - inicio

# 4. Exibe o resultado
print("-" * 30)
print(f"Ordenação concluída!")
print(f"Tempo de execução: {tempo_total:.6f} segundos")
print("-" * 30)