preco = float(input('Qual e o preco do produto? R$'))
novo = preco - (preco * 5/ 100)
print('O preco do produto que custava R${:.2f}, na promocao esta custando R${:.2f}.' .format(preco, novo))
