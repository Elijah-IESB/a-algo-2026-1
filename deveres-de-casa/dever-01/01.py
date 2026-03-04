import time
import random

def insertion_sort(lista):
    for i in range(1, len(lista)):
        chave = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > chave:
            lista[j + 1] = lista[j]
            j = j - 1
        lista[j + 1] = chave

while True:
    print("\nTeste do Insertion Sort")
    print("Digite 0 para encerrar o programa")

    n = int(input("Digite o tamanho da lista (n): "))

    if n == 0:
        print("Encerrando programa...")
        break

    lista = []
    for i in range(n):
        numero = random.randint(0, n * 10)
        lista.append(numero)

    print("Ordenando lista...")

    inicio = time.time()
    insertion_sort(lista)
    fim = time.time()

    tempo = fim - inicio

    print("Tempo de execução:", tempo, "segundos")