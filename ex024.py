cid = str(input('em que cidade voce mora? '))
# print(cid[:5] == 'Santo') o programa esta correto mas tem falhas porque segue fielmente a palavra, assim nao aceitando escritas de formas diferentes, ex: SaNto
print(cid[:5].upper() == 'SANTO')
