# -*- coding: utf-8 -*-
"""
Created on Sun Dec 15 01:29:13 2024

@author: JOAOVITOR
"""

Nome = input("Digite o Seu Nome:")
Pagamento = float(input("Informe Quanto Você Ganha"))
Guardou = float(input("Informe Quanto Você Guardou"))
Gasto = int(input("Informe Quanto Voce Gastou:")) 

Dia = input("Informe a Data do Pagamento {Dia}") 
Mes = 12 

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
                
if Dia in Pagamento:
    Pagamento = "Quanto Voce Recebeu {Pagamento}"
    for Dia in Mes:
        
