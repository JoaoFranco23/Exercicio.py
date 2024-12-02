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
    while Continuar:
        Continuar = int(input("Digite 1 para continuar (0 = Sair)")) 
        if Continuar == 1:
            Nome = (input("Informe o Seu Nome"))
            Gasto1 = float(input("Informe Quanto gastou neste dia"))
            Gasto2 = float(input("Informe Quanto gastou no segundo dia")) 
            
            if Gasto1 > Gasto2:
                print("Você gastou mais no primeiro dia.") 
            elif Gasto2 < Gasto1:
                print("Voce gastou menos que o primeiro dia.")
            else:
                print("Voce  Gasotu o mesmo em ambos os dias.")
                return("Gasto1, Gasto2")
                """
                for opções in menu:
                    opções = "Saindo do Programa..."
                elif Continuar == 0:
                    print(opções) 
                else:
                    print()
              """
