from random import randint
from time import sleep
computador = randint(0, 5)  # faz o computador pensar
print('-=-' * 25)
print('vou pensar em um numero entre 0 e 5. tente adivinhar...')
print('-=-' * 25)
jogador = int(input('em qual numero eu pensei? ')) # jogador tenta adivinhar    
print('aguarde um momento...')
sleep(2)
if jogador == computador:
    print('Parabens, voce me venceu! :)')
else:
    print('GANHEI DE VOCE! O numero que eu pensei foi {} e nao {}'.format(computador, jogador))
