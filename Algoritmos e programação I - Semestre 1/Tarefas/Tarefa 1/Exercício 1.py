# Exercício 1: Elaborar um programa para calcular e exibir distância entre 2 pontos.

import math
x1 = 1
y1 = 1
x2 = 5
y2 = 4

xd = (x2 - x1)**2
yd = (y2 - y1)**2

d = math.sqrt(xd + yd)
print(d)