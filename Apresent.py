#Tags para inserir os dados nas variaveis
Nome = input("Informe o Seu Nome");
Idade = int(input("Informe a Sua Idade"));
Email = input("Informe o Seu Email");
Cidade = input("Informe Sua Cidade"); 
Estado = input("Digite o estado")  

#condicional, a tag representa se o usuario é de maior ou nmenor de idade
if Idade >= 18:
    print("Parabens, Siga para proximas instruções")
else:
    Idade <= 18
    print("Infelizmente não podemos cadastrar, idade menor que 18 anos")
    
Apresentar = "Olá!" + "Seja Bem Vindo." + "Meu Nome é {Nome}. Eu Tenho {Idade} anos, Meu contato é {Email}, Moro em {cidade} no estado de {Estado}"

print(Apresentar + "Seja Bem Vindo")
