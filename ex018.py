from math import sin, cos, tan, radians
ang = float(input('digite o angulo que voce deseja: '))
seno = sin(radians(ang))
cosseno = cos(radians(ang))
tangente = tan(radians(ang))
print('o angulo de {} tem o SENO {:.2f}, o COSSENO de {:.2f}, e a TANGENTE de {:.2f}.'.format(ang, seno, cosseno, tangente))