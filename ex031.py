if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45
print('e o preco da sua passagem e de R${:.2f}'.format(preco))
