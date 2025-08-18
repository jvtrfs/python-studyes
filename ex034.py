salario = float(input('qual o salario do funcionario? '))
if salario <= 1250:
    novo = salario + (salario * 15 / 100)
else:
    novo = salario + (salario * 10 / 100)
print('quem ganhava RS{:.2f}, passa a ganhar R${:.2f}'.format(salario, novo))
