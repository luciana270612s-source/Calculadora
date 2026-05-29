import os
import time


def calculadora(num1: float, num2: float, operador: str) -> float:
    """
    Primeira versão da calculadora.
    Usa if / elif para verificar o operador.
    """
    resultado = float("nan")

    if operador == "+":
        resultado = num1 + num2
    elif operador == "-":
        resultado = num1 - num2
    elif operador == "*":
        resultado = num1 * num2
    elif operador == "/":
        if num2 == 0:
            raise ZeroDivisionError
        resultado = num1 / num2
    elif operador == "**":
        resultado = num1 ** num2
    elif operador == "%":
        if num2 == 0:
            raise ZeroDivisionError
        resultado = num1 % num2

    return resultado


def calculadora_alternativa(num1: float, num2: float, operador: str) -> float:
    """
    Segunda versão da calculadora.
    Tem a mesma assinatura: recebe dois floats e uma string, e devolve float.
    Usa dicionário de operações.
    """
    if operador == "/" and num2 == 0:
        raise ZeroDivisionError

    if operador == "%" and num2 == 0:
        raise ZeroDivisionError

    operacoes = {
        "+": num1 + num2,
        "-": num1 - num2,
        "*": num1 * num2,
        "/": num1 / num2 if num2 != 0 else float("nan"),
        "**": num1 ** num2,
        "%": num1 % num2 if num2 != 0 else float("nan")
    }

    return operacoes.get(operador, float("nan"))


if __name__ == "__main__":
    continuar = "s"

    while continuar.lower() == "s":
        os.system("cls" if os.name == "nt" else "clear")

        try:
            print("Calculadora")
            print("----------------------------------")
            print("Escolha uma das operações disponíveis:")
            print("+  Soma")
            print("-  Subtração")
            print("*  Multiplicação")
            print("/  Divisão")
            print("** Exponenciação")
            print("%  Módulo")
            print("----------------------------------\n")

            numero1 = float(input("Introduza o primeiro número: "))
            numero2 = float(input("Introduza o segundo número: "))
            operador = input("Introduza a operação (+, -, *, /, **, %): ")

            resultado1 = calculadora(numero1, numero2, operador)
            resultado2 = calculadora_alternativa(numero1, numero2, operador)

            if resultado1 != resultado1:
                print("\nOperação inválida!")
            else:
                print(f"\nResultado usando calculadora(): {resultado1}")
                print(f"Resultado usando calculadora_alternativa(): {resultado2}")

            continuar = input("\nDeseja continuar? (s/n): ")

        except ValueError:
            print("\nDados inválidos! Tente novamente.")
            time.sleep(2)

        except ZeroDivisionError:
            print("\nImpossível dividir por zero! Tente novamente.")
            time.sleep(2)

    print("\nVolte sempre!\n")
