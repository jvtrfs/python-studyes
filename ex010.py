real=float(input('Quanto dinheiro voce tem na carteira? R$ '))
dolar = real/5.55
euro = real/5.60
print('Com R${:.2f} voce pode comprar U${:.2f} e ${:.2f}'.format (real, dolar, euro))
