dias = float(input('Quantos dias o carro foi alugado?'))
km = float(input('Quantos km rodados?'))
pago = (dias * 60) + (km * 0.15)
print('O valor a pagar e de R${:.2f}'.format(pago))
