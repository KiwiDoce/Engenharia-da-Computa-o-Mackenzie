#Exercicio 2: Calcular a média de 2 notas e arredondar para cima
import math
nota1 = float(input("Primeira nota: "))
nota2 = float(input("Segunda nota:"))
média = (nota1 + nota2)/2
print (math.ceil(média))
