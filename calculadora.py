from operadores import soma, sub, divi, mult

while True:
    opera = str(input("Digite um operador [+, -, *, / ou ! para fechar o programa]: ")).upper()
    if opera == "+":
        soma()
    elif opera == "-":
        sub()
    elif opera == "*":
        mult()
    elif opera == "/":
        divi()
    elif opera == "!":
        print("Obrigado!")
        break