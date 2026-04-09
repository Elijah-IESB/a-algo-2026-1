def merge_sort(arr):
    """Ordena uma lista usando Merge Sort."""
    if len(arr) <= 1:
        return arr

    meio = len(arr) // 2
    esquerda = merge_sort(arr[:meio])
    direita = merge_sort(arr[meio:])

    return merge(esquerda, direita)


def merge(esquerda, direita):
    """Combina duas listas ordenadas."""
    resultado = []
    i = j = 0

    while i < len(esquerda) and j < len(direita):
        if esquerda[i] < direita[j]:
            resultado.append(esquerda[i])
            i += 1
        else:
            resultado.append(direita[j])
            j += 1

    resultado.extend(esquerda[i:])
    resultado.extend(direita[j:])
    return resultado


def multiplicar_matrizes(a, b):
    """Multiplica duas matrizes quadradas."""
    n = len(a)
    resultado = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            for k in range(n):
                resultado[i][j] += a[i][k] * b[k][j]

    return resultado


# ========================
# FUNÇÕES DE VALIDAÇÃO
# ========================

def ler_lista():
    """
    Lê uma lista de números digitada pelo usuário.
    Exemplo: 1 2 3 4
    """
    while True:
        entrada = input("Digite números separados por espaço: ")

        try:
            lista = [int(x) for x in entrada.split()]
            return lista
        except ValueError:
            print("❌ Entrada inválida! Digite apenas números.")


def ler_tamanho_matriz():
    """Valida o tamanho da matriz."""
    while True:
        try:
            n = int(input("Digite o tamanho da matriz (n x n): "))
            if n > 0:
                return n
            print(" O tamanho deve ser maior que 0.")
        except ValueError:
            print(" Digite um número inteiro válido.")


def ler_matriz(n, nome="A"):
    """Lê uma matriz n x n."""
    print(f"\nDigite os valores da matriz {nome}:")

    matriz = []
    for i in range(n):
        while True:
            linha = input(f"Linha {i + 1}: ").split()

            if len(linha) != n:
                print(f"❌ Digite exatamente {n} valores.")
                continue

            try:
                linha = [int(x) for x in linha]
                matriz.append(linha)
                break
            except ValueError:
                print(" Apenas números são permitidos.")

    return matriz


# ========================
# MENU INTERATIVO
# ========================

def menu():
    """Exibe o menu e executa as opções."""
    while True:
        print("\n=== MENU ===")
        print("1 - Merge Sort")
        print("2 - Multiplicação de Matrizes")
        print("3 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            lista = ler_lista()
            resultado = merge_sort(lista)

            print("Lista ordenada:", resultado)

        elif opcao == "2":
            n = ler_tamanho_matriz()

            matriz_a = ler_matriz(n, "A")
            matriz_b = ler_matriz(n, "B")

            resultado = multiplicar_matrizes(matriz_a, matriz_b)

            print("\nResultado:")
            for linha in resultado:
                print(linha)

        elif opcao == "3":
            print("Saindo do programa...")
            break

        else:
            print(" Opção inválida! Escolha 1, 2 ou 3.")


# ========================
# EXECUÇÃO
# ========================

if __name__ == "__main__":
    menu()