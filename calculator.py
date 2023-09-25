def divisao(n1:float, n2: float) ->float:
    return n1 / n2






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
            pass



        case "-":
            pass



        case "*":
            pass



        case "/":
            n1 = float(input("Digite o dividendo: "))
            n2 = float(input("Digite o divisor: "))

            input(f"O resultado entre {n1} dividido por {n2} é igual a {divisao(n1, n2)}")


        case _:
            break