# exercicio de condicao simples
velocidade = float(input('qual a velocidade do carro? '))
if velocidade > 80:
    print('MULTADO! voce excedeu o limite da via que e de 80Km/h')
    multa = (velocidade - 80) * 7
