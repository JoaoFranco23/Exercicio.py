#Faça um Programa que peça as 4 notas bimestrais e mostre a média.

Nota1 = float(input("Informe a Nota do Primeiro Bimestre: "))
Nota2 = float(input("Informe a Nota do Segundo Bimestre: "))
Nota3 = float(input("Informe a Nota do Terceiro Bimestre: "))
Nota4 = float(input("Informe a Nota do Quarto Bimestre: "))

Media = (Nota1 + Nota2 + Nota3 + Nota4) / 4
Resultado = f"A Média da Nota Bimestral é: {Media}"
print(Resultado)
