def imc(alt,pes):
    calc = pes/(alt**2)
    if calc < 18.5:
        return "ABAIXO DO PESO"
    elif calc >= 18.5 and calc <= 24.9:
        return "PESO NORMAL"
    elif calc >= 25 and calc <= 29.9:
        return "SOBREPESO"
    elif calc >= 30 and calc <= 34.9:
        return "OBESIDADE GRAU 1 "
    else:
        return "OBESIDADE GRAU 2 "
    
altura = float(input("Informe sua altura[M]: "))
peso = float(input("Informe seu peso[Kg]: "))

print("Com base no seu IMC Vôce está com ",imc(altura,peso))

