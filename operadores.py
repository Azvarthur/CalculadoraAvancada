def soma():
    n1 = None
    n2 = None
    while n1 is None:
        try:
            n1 = int(input("Digite o 1º número: "))
        except ValueError:
            print("Digite apenas números!")
    while n2 is None:
        try:
            n2 = int(input("Digite o 1º número: "))
        except ValueError:
            print("Digite apenas números!")

    return print(f"{n1} + {n2} = {n1+n2}")


def sub():
    n1 = None
    n2 = None
    while n1 is None:
        try:
            n1 = int(input("Digite o 1º número: "))
        except ValueError:
            print("Digite apenas números!")
    while n2 is None:
        try:
            n2 = int(input("Digite o 1º número: "))
        except ValueError:
            print("Digite apenas números!")

    return print(f"{n1} - {n2} = {n1 - n2}")


def mult():
    n1 = None
    n2 = None
    while n1 is None:
        try:
            n1 = int(input("Digite o 1º número: "))
        except ValueError:
            print("Digite apenas números!")
    while n2 is None:
        try:
            n2 = int(input("Digite o 1º número: "))
        except ValueError:
            print("Digite apenas números!")

    return print(f"{n1} x {n2} = {n1 * n2}")


def divi():
    n1 = None
    n2 = None
    while n1 is None:
        try:
            n1 = int(input("Digite o 1º número: "))
        except ValueError:
            print("Digite apenas números!")
    while n2 is None:
        try:
            n2 = int(input("Digite o 1º número: "))
        except ValueError:
            print("Digite apenas números!")

    return print(f"{n1} / {n2} = {n1 / n2}")
