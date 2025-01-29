Num1 = float(input("Insira um Numero: "))
Num2 = float(input("Insira o Segundo Numero: "))

soma = Num1 + Num2
Subtração = Num1 - Num2
multiplicação = Num1 * Num2
Divisao = Num1 / Num2

def operaçao():
    if soma == "+":
        return Num1 + Num2
    elif Subtração == "-":
        return Num1 - Num2
    elif multiplicação == "*":
        return Num1 * Num2
    elif Divisao == "/":
        if Num2 != 0:
            return Num1 / Num2
        else:
            pass

resultado = f"A Soma do {Num1} e {Num2} é {Num1 + Num2} , A Subtração de {Num1 - Num2} é, A multiplicação de {Num1 * Num2} é" 
print(resultado)
