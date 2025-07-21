N = int(input("Informe um número: "))
lista_soma =[]
for i in range(1,N+1):
    if i % 2 == 0:
        lista_soma.append(i)
print("Soma dos números pares", sum(lista_soma))