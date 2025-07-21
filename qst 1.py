valores = [True, False, True, False, True]
contador_verdadeiro = 0
contador_falso = 0
for i in valores:
    if i == True:
      contador_verdadeiro+=1
else:
       contador_falso +=1
print(f'o número de verdadeiros na lista valores vale {contador_verdadeiro}'
      f' e o número de falsos na lista de valores vale {contador_falso}')