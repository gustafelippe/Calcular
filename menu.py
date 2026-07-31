"""Menu de linha de comando da calculadora."""

from calculadora import dividir, multiplicar, somar, subtrair, potencia, raiz

OPERACOES = {
    "1": ("Soma", somar),
    "2": ("Subtração", subtrair),
    "3": ("Multiplicação", multiplicar),
    "4": ("Divisão", dividir),
    "5": ("Exponencial", potencia),
    "6": ("Radiciação", raiz)
}


def mostrar_menu():
    print("=== Calculadora Git ===")
    for codigo, (nome, _) in OPERACOES.items():
        print(f"{codigo} - {nome}")
    print("0 - Sair")


def executar():
    while True:
        mostrar_menu()
        escolha = input("Escolha uma operação: ").strip()
        if escolha == "0":
            print("Até a próxima!")
            break
        if escolha not in OPERACOES:
            print("Opção inválida. Tente novamente.")
            continue
        if  escolha == "1":
            nome, funcao = OPERACOES[escolha]
            a = int(input("Quantos numeros irá somar: "))
            try:
                resultado = funcao(a)
            except ValueError as erro:
                print(f"Erro: {erro}")
            else:
                print(f"{nome}: {resultado}")
        else:
            nome, funcao = OPERACOES[escolha]
            a = float(input("Primeiro número: "))
            b = float(input("Segundo número: "))
            try:
                resultado = funcao(a, b)
            except ValueError as erro:
                print(f"Erro: {erro}")
            else:
                print(f"{nome}: {resultado}")


if __name__ == "__main__":
    executar()