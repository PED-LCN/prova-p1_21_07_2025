valor_produto = float(input('digite o valor do produto que você deseja comprar '))
valor_pago = float(input('digite o valor que você usará para pagar '))

if valor_produto - valor_pago == 0:
    print('o valor pago é exatamente igual ao valor do produto, não há troco ')
elif valor_produto - valor_pago < 0:
    print(f'o troco vale {valor_pago - valor_produto:.2f}')
else:
    print(f'valor insuficiente para pagar o produto')
    