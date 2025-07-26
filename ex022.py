nome = str(input('Digite seu nome completo: ')).strip() #o strip elimina os espacos antes e depois
print('analisando seu nome...')
print('seu nome em mauisculas e: {} '.format(nome.upper()))
print('seu nome em minusculas e: {}'.format(nome.lower()))
# print('seu nome ao todoo tem: {} letras'.format(len(nome))) # conta como 10 letras por causa do espaco
print('seu nome ao todoo tem: {} letras'.format(len(nome) - nome.count(' '))) # a funcao nome.count elimina os espacos do meio do nome, assim fica basicamente (nome com espacos) MENOS (nome sem espacos)
# print('seu primeiro nome tem {} letras'.format(nome.find(' '))) #formula para achar o primeiro espaco, assim dando a nos o primeiro nome
