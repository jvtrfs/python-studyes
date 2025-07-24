import random
n1 = str(input('digite o nome do primeriro aluno: '))
n2 = str(input('digite o nome do segundo aluno: '))
n3 = str(input('digite o nome do terceiro aluno: '))
n4 = str(input('digite o nome do quarto aluno: '))
lista = [n1, n2, n3, n4]
escolhido = random.choice(lista)
print('o aluno escolhido foi {}'.format(escolhido))

