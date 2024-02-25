#1-Exercício: programar em Python para calcular o IMC de uma pessoa
Nome = input("Seu nome:")
Peso = int(input('Seu peso: '))
Altura = float(input('Sua altura:'))
quadrado_altura = Altura**2
imc = Peso/quadrado_altura
print ("Olá",Nome,"seu IMC é",imc)