 #Syntaxy responsavel por inserir os dados nas variaveis 
Nome = input("Digite o Seu Nome: ")
Pagamento = float(input("Informe Quanto Você Ganha: "))
Gasto = int(input("Informe Quanto Voce Gastou: "))
sobrou = type("res")
#Criar uma variavel, sobre investimento 
#invest = float(int("Quanto Você Deseja Investir?: "))
investimento = type("invest")
juros = type("juros") 
mes = int(input("Quantos meses você deseja investir?: "))

#Variaveis respossaveis por 
soma = "Pagamento", "Guardou", "Investimento"
subtração = "Pagamento", "Gasto" 


res = Pagamento - Gasto
investimento = investimento + Pagamento
juros = investimento * (1 + juros / 100) ** mes 
lucro = investimento - juros

print(f"Olá {Nome}" + f"Do seu pagamento R${res}")


Guardar = input("{Nome} Você Gostaria de Investir ?")

#Definindo um questionamento Sim ou Não
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
    
    def Questionamento(pergunta):
        if resposta in ["Sim", "S"]:
            try:
                instimento = float(input("Quanto voce Deseja Investir: R$?"))
                
                print(f"O investimento de R$ {investimento:.2f}" + f"Durante ao Mes {mes}" + f"Durante a taxa de Juros {juros}% ao mês")
                print(f"Você terá o Lucro de: R${lucro:.2f}")
                print(f"O total é: R${jurs:.2f}")
            except ValueError:
                print("Invalido, insira um valor R$(>= 10)")
