# aula sobre o uso de bibliotecas que nao encontramos como padrao no python, ex: math

#ex de importacao: from math import sqrt

# usar as bibliotecas no comeco dos programas para utilizar as variaveis delas

#ex de programa abaixo utiliazndo a biblioteca math, podemos utilizar ctrl+espaco para vermos as opcoes
import math
num = int(input('digite a raiz quadrada:'))
raiz = math.sqrt(num)
print('a raiz quadrada de {} e igual a {:.2f}'.format(num, raiz))


# podemos fazer diretamente, importando somente a variavel que queremos, ex abaixo
from math import sqrt
num = int(input('digite a raiz quadrada:'))
raiz = sqrt(num)
print('a raiz quadrada de {} e igual a {:.2f}'.format(num, raiz))

#Dica: Tem ainda como vc escolher como vc quer chamar os metodos! por exemplo:
#utilizando "as" vc pode dar apelido a alguma função da biblioteca. Vejamos com o sqrt:

from math import sqrt as raizquadrada

#agora ao inves de usar sqrt(4), eu uso raizquadrada(4)

#obviamente, no exemplo ficou foi mais extenso o apelido, mas é so pra demonstrar, vc poderia chamar ele de "r" no caso e vai funcionar igualmente.

#from math import sqrt as r

#r(4)

#pronto! isso retorna = 2, pois a raiz quadrada de 4 é 2.
