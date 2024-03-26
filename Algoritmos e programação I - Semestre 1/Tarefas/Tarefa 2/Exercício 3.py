# Exercício 3:Programa em pyton para informar se 3 valores podem formar um triângulo, indicando se é equilátero, isóceles ou escaleno.

a = float(input("Insira o primeiro lado do triângulo:"))
b = float(input("Insira o segundo lado do triângulo:"))
c = float(input("Insira o terceiro lado do triângulo:"))

if (a+b > c) and (b+c > a) and (a+c > b):
  resposta = ("É um triângulo")
  if (a == b) and (a == c):
    print(resposta, "equilátero")
  elif (a == b) or (a == c) or (b == c):
    print(resposta, "isóceles")
  else: 
    print(resposta, "escaleno")
else:
  print("Não é um triângulo")