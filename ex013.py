salario = float(input('Qual o salario do funcionario? R$'))
novo = salario + (salario * 15 / 100)
print('Um funcionario que ganhava {:.2f}, com um aumento de 15% em seu salario ganhara R${:.2f}'.format(salario, novo))
