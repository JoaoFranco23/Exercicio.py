Nome = input("Digite o Seu Nome:")
Pagamento = float(input("Informe Quanto Você Ganha"))
Gasto = int(input("Informe Quanto Voce Gastou:")) 
Guardou = float(input("Informe Quanto Você Guardou"))


def subtracao(Gasto, Guardou):
    return(Gasto - Guardou)
def soma(Gasto, Guardou):
    return(Gasto + Guardou)
def divisão(Guardou, Gasto):
    if Gasto != 0:
        return Guardou / Gasto
    else:
        return "Divisão por zero não permitida"
    def multiplicação(Guardou, Gasto):
        return(Guardou * Gasto * 30) 
    def Gasto(Guardou, Gasto):
        if Gasto != 0:
            divisão = Guardou / Gasto
            multiplicação = Guardou * Gasto
            return divisão, multiplicação
        else:
            return "Divisão por zero não permitida", None 
        resultado = Gasto(100, 50)
        print(f"Resultados: Divisão = {resultado[0]}, Multiplicação = {resultado[1]}")
