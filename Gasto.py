 #Syntaxy responsavel por inserir os dados nas variaveis 
Nome = input("Digite o Seu Nome: ")
Pagamento = float(input("Informe Quanto Você Ganha: "))
Gasto = int(input("Informe Quanto Voce Gastou: "))
sobrou = type("res")

#Variaveis respossaveis por 
soma = "Pagamento", "Guardou"
subtração = "Pagamento", "Gasto"

res = Pagamento - Gasto

print(f"Olá {Nome}" + f"Do seu pagamento R${res}")

Guardar = input("{Nome} Você Gostaria de Investir ?")

#Definido um questionamento Sim ou Não
def Qustionamento(pergunta):
    resposta = input(f"Você Deseja Investir o Seu Dinheiro {pergunta} (Sim/Não)") 
    if resposta in ["Sim", "S"]:
        return "Sim"
    elif resposta in ["Não", "N"]:
        return "Não"
    else:
        return "Por Favor Digite 'Sim' ou 'Não'."
    
    pergunta = "Você Deseja Investir o Seu Dinheiro ?"
    print(f"Questionamento {pergunta}")
    
    
