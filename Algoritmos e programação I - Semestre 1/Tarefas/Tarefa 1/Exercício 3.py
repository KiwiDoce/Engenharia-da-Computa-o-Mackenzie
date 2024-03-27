# Exercício 3: Elabore um programa que calcule e apresente a menor quantidade de notas necessárias para utilizar o pagamento de uma compra sem utilizar if e else.

valor = int(input("Insira o valor do produto em reais:"))
print("Notas de 100:",int(valor/100))

valor = valor%100
print("Notas de 50:",int(valor/50))

valor = valor%50
print("Notas de 20:",int(valor/20))

valor = valor%20
print("Notas de 10:",int(valor/10))

valor = valor%10
print("Notas de 5:",int(valor/5))

valor = valor%5
print("Notas de 2:",int(valor/2))

valor = valor%2
print("Notas de 1:",int(valor/1))

