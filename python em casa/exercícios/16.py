'''import math
num = float(input('digite um valor: '))
print('o valor digitado foi {} e sua porção inteira é {}'.format(num, math.trunc(num)))'''

'ou'

from math import trunc
num = float(input('digite um valor: '))
print('o valor digitado foi {} e sua porção inteira é {}'.format(num, trunc(num)))

