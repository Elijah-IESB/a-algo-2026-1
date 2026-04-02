def f_recursiva(n: int) -> int:
    """
    Calcula F(n) de forma recursiva.
    """
    if n == 1:
        return 2
    return 2 * f_recursiva(n - 1) + n ** 2


def f_iterativa(n: int) -> int:
    """
    Calcula F(n) de forma iterativa.
    """
    resultado = 2
    for i in range(2, n + 1):
        resultado = 2 * resultado + i ** 2
    return resultado


def ler_inteiro_positivo(mensagem: str) -> int:
    """
    Valida entrada garantindo um inteiro positivo.
    """
    while True:
        try:
            valor = int(input(mensagem))
            if valor < 1:
                print("❌ Digite um número maior ou igual a 1.")
                continue
            return valor
        except ValueError:
            print("❌ Entrada inválida. Digite um número inteiro.")


def menu():
    """
    Menu interativo do programa.
    """
    while True:
        print("\n===== MENU =====")
        print("1 - Calcular F(n) recursivo")
        print("2 - Calcular F(n) iterativo")
        print("3 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            n = ler_inteiro_positivo("Digite n: ")
            print(f"F({n}) (recursivo) = {f_recursiva(n)}")

        elif opcao == "2":
            n = ler_inteiro_positivo("Digite n: ")
            print(f"F({n}) (iterativo) = {f_iterativa(n)}")

        elif opcao == "3":
            print("Saindo...")
            break

        else:
            print("❌ Opção inválida.")


# Recursivo chama a função dentro dela mesma.
# Iterativo usa repetição com laço (for/while).

def main():
    menu()


if __name__ == "__main__":
    main()