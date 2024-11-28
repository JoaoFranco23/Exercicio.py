#Nesta primeira tag, foi utilizado variaveis para inserir dados, junto com a tag float responsavel para converter os valores e realizar operaçoes matemáticas.
num1 = float(input("Digite o Primeiro Numero"))
num2 = float(input("Digite o Segundo Numero")) 

#O segundo codigo, utilizei funções para definir os calculo
def soma(num1, num2):
    return(num1 + num2)
def subt(num1, num2):
    return(num1 - num2)
def mult(num1, num2):
    return(num1 * num2)
def divs(num1, num2): 
    if divs == 0: #Dentro da definição de função, foi utilizado a tag if para verificar se o divisor é zero 
        return("Erro: Divisão por zero ")
    return num1 / num2 

#A string é responsavel por mostrar o resultado único
Resultado = (
    f"Soma: {soma(num1, num2)}"
    f"subt: {subt(num1, num2)}"
    f"mult: {mult(num1, num2)}"
    f"divs: {divs(num1, num2)}"
    )
print(Resultado)
