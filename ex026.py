frase = str(input('digite seu nome completo: ')).upper().strip()
print('a letra A aparece {} vezes na frase'.format(frase.count('A')))
print('a primeira letra A aparece na posicao {} da frase'.format(frase.find('A')+1))
print('a ultima letra A aparece na posicao {} da frase'.format(frase.rfind('A')+1))

