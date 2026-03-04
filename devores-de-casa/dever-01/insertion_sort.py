def insertion_sort(arr):
    """
    Implementa o algoritmo Insertion Sort com complexidade O(n²).
    
    Args:
        arr (list): Lista de números a ser ordenada
    
    Returns:
        list: Lista ordenada em ordem crescente
    """
    # Percorre a lista a partir do segundo elemento
    for i in range(1, len(arr)):
        key = arr[i]  # Elemento a ser inserido
        j = i - 1
        
        # Compara e desloca elementos maiores que key
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        
        # Insere o elemento na posição correta
        arr[j + 1] = key
    
    return arr


# Exemplos de uso
if __name__ == "__main__":
    # Exemplo 1: Lista desordenada
    lista1 = [64, 34, 25, 12, 22, 11, 90]
    print("Lista original:", lista1)
    print("Lista ordenada:", insertion_sort(lista1.copy()))
    print()
    
    # Exemplo 2: Lista já ordenada
    lista2 = [1, 2, 3, 4, 5]
    print("Lista já ordenada:", lista2)
    print("Resultado:", insertion_sort(lista2.copy()))
    print()
    
    # Exemplo 3: Lista com números negativos
    lista3 = [-5, 10, -3, 0, 8, -1]
    print("Lista com negativos:", lista3)
    print("Lista ordenada:", insertion_sort(lista3.copy()))
    print()
    
    # Exemplo 4: Lista em ordem inversa
    lista4 = [9, 7, 5, 3, 1]
    print("Lista em ordem inversa:", lista4)
    print("Lista ordenada:", insertion_sort(lista4.copy()))
    print()