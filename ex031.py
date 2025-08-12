distancia = float(input('qual a distancia da sua viagem? '))
print ('voce esta prestes a comecar uma viagem de {}Km'.format(distancia))
if distancia <= 200:
    preço = distancia * 0.50
else:
    preço = distancia * 0.45
print('e o preco da sua passagem e de R${:.2f}'.format(preço))
