# -*- coding: utf-8 -*-
"""
Created on Sun Dec 15 01:29:13 2024

@author: JOAOVITOR
"""
# Variaveis para inserir os dados 
Nome = input("Digite o Seu Nome:")
Pagamento = float(input("Informe Quanto Você Ganha"))
Guardou = float(input("Informe Quanto Você Guardou"))
Gasto = int(input("Informe Quanto Voce Gastou:")) 

#Segunda tag, foi definido caracteres matemáticos, 
def soma(Guardou, Gasto):
    return(Guardou + Gasto)
def divisão(Guardou, Gasto):
    return(Guardou / Gasto)
def multiplicação(Guardou, Gasto):
    return(Guardou * Gasto * 100)
def gasto(Guardou, Gasto):
    if Gasto != 0:
        div_result = Guardou / Gasto
        mult_result = Guardou * Gasto
        return div_result, mult_result
    else:
        return "Divisão por zero não permitida", None
    
    def operação(op, Guardou, Gasto):
        match op:
            case "soma":
                return som(Guardou, Gasto)
            case "divisão":
                return div(Guardou, Gasto)
            case "multiplicação":
                return mult(Guardou, Gasto)
            case "gasto":
                return gasto(Guardou, Gasto)
            case _:
                return "Operação Inválida"
           
            op = input("Escolha uma operação (soma, divisão, multiplicação, gasto): ").lower()
            resultado = operacao(op, Guardou, Gasto)
            print(f"Resultado da operação '{op}': {resultado}")
            

Dia = [5, 10, 20]
Mes = range(12) 

match (Dia):
    case 1:
        print("Segunda-Feira")
    case 2:
        print("Terça-Feira")
    case 3:
        print("Quarta-Feira")
    case 4:
        print("Quinta-Feira")
    case 5:
        print("Sexta-Feira")
    case 6:
        print("Sabado")
    case 7:
        print("Domingo")

match (Mes):
    case 1:
        print("Janeiro")
    case 2:
        print("Fevereiro")
    case 3:
        print("Março")
    case 4:
        print("Abril")
    case 5:
        print("Maio")
    case 6:
        print("Junho")
    case 7:
        print("Julho")
    case 8:
        print("Agosto")
    case 9:
        print("Setembro")
    case 10:
        print("Outubro")
    case 11:
        print("Novembro")
    case 12:
        print("Dezembro")
        
if Dia in Mes:
    if Dia in Pagamento:
        print(f"O pagamento foi realizado no dia {Dia}.")
    else:
        print(f"O dia {Dia} não é um dia de pagamento.")
