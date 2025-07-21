def maior_numero(n1 ,n2 ,n3):
    if n1 > n2 and n1 >n3:
        return n1
    elif n2>n1 and n2>n3:
        return n2
    else:
        return n3
verificador_do_maior_numero = maior_numero( 8,5,6)
print(f' dos números digitados, o maior número vale {verificador_do_maior_numero}')