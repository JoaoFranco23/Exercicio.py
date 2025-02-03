#Importando uma base para definição de dados em pandas
import pandas as pd
import numpy as np

#Lista para Armazenar os dados
Informação = []

#Variavel Definindo as Colunas do DataFrame
Dados = ["Nome", "Idade", "Cidade", "Estado", "Curso"]
Cidade_Estado = pd.DataFrame({
    "Adamantina": "SP", "Lucélia": "SP", "Osvaldo Cruz": "SP", "Ribeirão Preto": "SP",
    "Marília": "SP", "São Paulo": "SP", "Campinas": "SP", "Taguatinga": "DF",
    "Plano Piloto": "DF", "Ceilândia": "DF", "Ajuricaba": "RS", "Água Santa": "RS",
    "Aceguá": "RS"
})

Nome = input("Informe o Seu Nome: ")
Idade = type("Idade: ")
#Cidade = input("Informe Sua Cidade: ")
#Estado = input("IInforme o Estado ")
Curso = input("Digite o curso que está realizando ")

#Dados = f"Seu Nome é {Nome}, Sua Idade é {Idade}, Mora na Cidade de {Cidade} Pertencendo ao Estado de {Estado} e Realizo o Curso de {Curso}"
#print(Dados)

def cadastro(Nome, Idade, Cidade, Estado, Curso):
    while True:
        Cidade = input("Informe Sua Cidade: ")
        Estado = input("IInforme o Estado ") 
        
    #Filtrando os Dados de Cidade e Estado que representa
    cadastro = Cidade_Estado[Cidade_Estado["Cidade" in "Estado"] == "SP", "DF", "RS"]
