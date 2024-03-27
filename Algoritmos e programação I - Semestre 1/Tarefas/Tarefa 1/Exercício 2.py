# Exercício 2: Elaborar um programa para calcular e exibir o perímetro e a áera de um triângulo.

import math
a = 3
b = 4
c = 5
perimetro = a + b + c
sp = (perimetro)/2

area = math.sqrt(sp*(sp-a)*(sp-b)*(sp-c))
print("O perímetro do seu triângulo é", perimetro, "e a área é", area)