def contar_vogaris(frase):
    format=frase.upper()
    palavra=list(format)
    contador=0
    for i in range(len(palavra)):
        if palavra[i] in 'AEIOU':
            contador+=1
    if contador ==0:
        return "Não há vogais na frase"
    else:        
        return contador

P=input("Digite uma frase: ")
print("A frase contém",contar_vogaris(P),"Vogais")
    

       