def eh_palindromo(lista):
    """
    Verifica recursivamente se uma lista é um palíndromo.

    Args:
        lista (list): Lista de caracteres.

    Returns:
        bool: True se for palíndromo, False caso contrário.
    """
    if len(lista) <= 1:
        return True

    if lista[0] != lista[-1]:
        return False

    return eh_palindromo(lista[1:-1])


def normalizar_texto(texto):
    """
    Remove espaços, converte para minúsculas e
    mantém apenas letras e números.

    Args:
        texto (str): Texto digitado pelo usuário.

    Returns:
        list: Lista de caracteres tratados.
    """
    texto = texto.lower()

    lista_filtrada = []
    for caractere in texto:
        if caractere.isalnum():  # mantém letras e números
            lista_filtrada.append(caractere)

    return lista_filtrada


def menu():
    """
    Menu interativo para verificar palíndromos.
    """
    while True:
        entrada = input("\nDigite uma frase (ou 'sair' para encerrar): ")

        if entrada.lower() == "sair":
            print("Encerrando programa...")
            break

        lista = normalizar_texto(entrada)

        if eh_palindromo(lista):
            print("✅ É palíndromo!")
        else:
            print("❌ Não é palíndromo.")


if __name__ == "__main__":
    menu()
