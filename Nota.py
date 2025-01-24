#Variavel Nome 
Nome = input("Informe o seu Nome: ") 
print(f"Olá {Nome}, Seja Bem Vindo!: ")

notas = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10] #Lista de Números Contidos 
emissao = False

nota = float(input("Informe uma nota entre 0 a 10: ")) #A variavel pede que o usuario insira numeros entre 0 a 10

for nota in notas: #loop
    if 0 <= nota <= 10: #Se a nota for menor que 0 ou 10
        print("{Nome} Sua nota é: {nota}")
        emissao = True
        break
    if emissao:
        print("Está Na Lista")
    
