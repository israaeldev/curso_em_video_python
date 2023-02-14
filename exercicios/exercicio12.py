import math
angulo =float(input('digite o angulo desejado:'))
se = math.sin(math.radians(angulo))
print('o angulo de {} tem o SENO de {:.2f}'.format(angulo, se))
co = math.cos(math.radians(angulo))
print('o angulo de {} tem o COSSENO de {:.2f}'.format(angulo, co))
ta = math.tan(math.radians(angulo))
print('o angulo de {} tem a TANGENTE de {:.2f}'.format(angulo, ta))

from math import sin, cos, tan, radians
angulo =float(input('digite o angulo desejado:'))
se = sin(radians(angulo))
print('o angulo de {} tem o SENO de {:.2f}'.format(angulo, se))
co = cos(radians(angulo))
print('o angulo de {} tem o COSSENO de {:.2f}'.format(angulo, co))
ta = tan(radians(angulo))
print('o angulo de {} tem a TANGENTE de {:.2f}'.format(angulo, ta))

