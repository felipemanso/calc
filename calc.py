import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("Não é possível dividir por zero!")
    return x / y

def rule_of_three(a, b, c):
    return (a * c) / b

while True:
    clear_screen()
    print(" ____________________")
    print("|       CALCULADORA   |")
    print("|____________________|")
    print("|                    |")
    print("| 1. Somar           |")
    print("| 2. Subtrair        |")
    print("| 3. Multiplicar     |")
    print("| 4. Dividir         |")
    print("| 5. Regra de três   |")
    print("| 6. Sair            |")
    print("|____________________|")

    escolha = input("Digite sua escolha (1/2/3/4/5/6): ")

    if escolha == '6':
        break

    try:
        num1 = float(input("Digite o primeiro número: ").replace(',', '.'))
        num2 = float(input("Digite o segundo número: ").replace(',', '.'))
    except ValueError:
        print("Por favor, digite apenas números!")
        input("Pressione ENTER para continuar...")
        continue

    if escolha == '1':
        resultado = add(num1, num2)
        sinal = "+"
    elif escolha == '2':
        resultado = subtract(num1, num2)
        sinal = "-"
    elif escolha == '3':
        resultado = multiply(num1, num2)
        sinal = "*"
    elif escolha == '4':
        try:
            resultado = divide(num1, num2)
            sinal = "/"
        except ValueError as erro:
            print(erro)
            input("Pressione ENTER para continuar...")
            continue
    elif escolha == '5':
        try:
            num3 = float(input("Digite o terceiro número: ").replace(',', '.'))
            resultado = rule_of_three(num1, num2, num3)
            sinal = ""
        except ValueError as erro:
            print(erro)
            input("Pressione ENTER para continuar...")
            continue
    else:
        print("Opção inválida!")
        input("Pressione ENTER para continuar...")
        continue

    clear_screen()
    print(" ____________________")
    print("|       CALCULADORA   |")
    print("|____________________|")
    if sinal == "":
        print(f"| {num1:.2f} {sinal} {num2:.2f} {sinal} {num3:.2f} = {resultado:,.2f} |".replace('.', ','))
    else:
        print(f"| {num1:.2f} {sinal} {num2:.2f} = {resultado:,.2f} |".replace('.', ','))
    print("|____________________|")
    input("Pressione ENTER para continuar...")
