# -*- coding: utf-8 -*-
"""
Created on Sun Jan 12 23:12:07 2025

@author: JOAOVITOR
"""

#Sistema de Sac
#Apresentação
print("Como podemos Ajudar?: ")
#Nome do usuario, será utilizado uma variavel para inserir o nome 
Nome = input("Digite o Seu Nome: ") 
print(f"Olá {Nome}, Seja Bem Vindo!: ")  

#Variavel, Conta Bancaria
Agencia = float(input("Insira o Numero da Agencia: "))
print(f"Informe o numero da agencia {Agencia}: ")
Conta = float(input("Insira o Numenro da Conta"))
print(f"Informe o número da conta {Conta}: ")

#Ticket de Atendimento 
def Questao1(Nome, Saldo):
    opçao = input(f"Você Deseja Verificar o Saldo da Conta {Saldo} (1 = Sim / 0 = Não): ").strip()
    if opçao in ["1", "Sim"]:
        print(f"{Nome}, Seu Saldo é R$ {Saldo}: ")
        return "Consulta Realizada Com Sucesso.: "
    elif opçao in ["0", "Não"]:
        return "Saindo..., Obrigado!"
        print(f"Digite, '1' ou '0'.")
        
def Questao2(Saldo, Depositar):
    opcao2 = input("Você Deseja Depositar o Seu Dinheiro R${Depositar}  (1 = Sim / 0 = Não): ")
    if opcao2 in ["1", "Sim"]:
        for Depositar in ["1", "Sim"]:
            Depositar = float(input("Quanto Você Deseja Depositar R${Depositar}?: "))
            Depositar += Saldo
            print(f"O Saldo R${Saldo} Total, Após o Deposito R${Depositar} é: ")
            return Depositar
        if opcao2 == "0":
            print("Deseja Depositar?")
        elif opcao2 in ["0", "Não"]:
            return "Saindo..., Obrigado!" 
        

#Variavel, Responsavel pelo Sac ou deposito do Dinheiro
Saldo = 1816.00 
#print(f"Olá, {Nome}! Seu Saldo Atual é R${Saldo:.2f}: ")
#Depositar = float(input("Informe a Quantidade que deseja Depositar R$: "))
#print(f"Informe a Quantia R${Depositar} Que deseja Depositar?: ")  
#Sac = float(input("Quanto Você Deseja retirar R${Saldo}: "))
