def menu():
    print("Olá:")
    print("Seja Bem Vindo!")
    print('''
          Menu:
              [1] - Continuar
              [0] - Sair
          
    ''')
    str(input("Escolha uma opção: ")) #Foi definido uma string para chamar as opções do menu
    
    Continuar = "1"
    Sair = "0"
    
    menu = ["Continuar1", "Sair0"]
    try:
        menu = int(input("Escolha uma opção:"))
        if Continuar:
            print("Digite (1 = Continuar) Para continuar: ")
            for Continuar in menu:
                Nome = input("Digite o Seu Nome:")
                Mes1 = float(input("Informe Quanto Voce Guardou no Primeiro Dia: "))
                Mes2 = float(input("Informe Quanto Voce Guardou no Segundo Dia: "))
                Gasto = int(input("Informe Quanto Voce Gastou:"))
                def som(Mes1, Mes2):
                    return(Mes1 + Mes2)
                def div(Mes1, Mes2):
                    return(Mes1 / Mes2)
                def mult(Mes1, Mes2):
                    return(Mes1 * Mes2 * 100)
                def gasto(Mes1, Mes2):
                    div = Mes1 / Mes2
                    if Mes2 != 0:
                           mult = Mes1 * Mes2
                           return div, mult
                    else: 
                        return"Divisão por zero não permitido", None
                    soma = som(Mes1, Mes2)
                    div, mult = Gasto(Mes1, Mes2) 
                    
                    print(f"\nResultado {Nome}:") 
                    print(f"Soma Acumulado: {soma}" + f"Divisão: {div}" + f"Multiplicado: {mult}")
                    
                        try:
                            Sair = input("Para Sair Digite (1 = Sair)")
                            if Sair == 0:
                                
