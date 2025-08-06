from random import randint
from time import sleep
computador = randint(0, 5)
print('-=-' * 25)
print('vou pensar em um numero entre 0 e 5. tente adivinhar...')
print('-=-' * 25)
jogador = int(input('em qual numero eu pensei? '))
print('aguarde um momento...')
sleep(2)
if jogador == computador:
    print('Parabens, voce me venceu! :)')
else:
