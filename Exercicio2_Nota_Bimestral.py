#Faça um Programa que peça as 4 notas bimestrais e mostre a média.
#Foi utilizado uma variavel nome para ser inserido
Nome = input("Informe o seu Nome: ")
#Variavel das notas bimestrais 
Nota1 = float(input("Informe a Nota do Primeiro Bimestre: "))
Nota2 = float(input("Informe a Nota do Segundo Bimestre: "))
Nota3 = float(input("Informe a Nota do Terceiro Bimestre: "))
Nota4 = float(input("Informe a Nota do Quarto Bimestre: "))

Media = (Nota1 + Nota2 + Nota3 + Nota4) / 4
Resultado = f"A Média da Nota Bimestral é: {Media}"
print(Resultado)
Aluno = f"Olá Aluno {Nome}, A média da Sua Nota é {Resultado}"
print(Aluno)

#Na função, é declarado se a media for maior que 6, significa que passou, senão reprovado
if Media > 6:
    print(f"A Média do Aluno {Media} foi {Resultado}. Está Aprovado".format(Nome, Media))
elif Media < 6:
    print(f"A Média do Aluno {Media} foi {Resultado}. Ele Foi Reprovado".format(Nome.title(), Media)) #Dentro dessa tag, possui uma variavel que transforma a string em title
