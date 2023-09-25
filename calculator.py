def adicao(n1: float, n2: float) -> float:
    return n1 + 2


def subtracao(n1: float, n2: float) -> float:
    return n1 - n2


def multiplicacao(n1:float, n2: float) ->float:
    return n1 * n2


while True:
    operacao = input("""
Informe a a operação para efetuar o cálculo entre dois números:
(+) Adição
(-) Subtração
(*) Multiplicação
(/) Divisão
""")

    match operacao:
        case "+":
            n1 = float(input("Insira o primeiro número a ser somado: "))
            n2 = float(input("Insira o segundo número a ser somado: "))

            input(f"A soma entre {n1} e {n2} é igual a {adicao(n1, n2)}")

        case "-":
            n1 = float(input("Insira o primeiro número: "))
            n2 = float(input("Insira o segundo número: "))

            input(f"A soma entre {n1} e {n2} é igual a {subtracao(n1, n2)}")

        case "*":
            n1 = float(input("Informe o primeiro valor: "))
            n2 = float(input("Informe o segundo valor: "))

            input(f"a multiplicação entre {n1} e {n2} é igual a {multiplicacao(n1, n2)}")


        case "/":
            pass



        case _:
            break