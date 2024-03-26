# Exercício 1: Calcular os descontos de um posto de gasolina.
comb = input("Insira A caso deseje Álcool ou G caso deseje gasolina:")
litros = float(input("Insira, em litros, a quantidade de comsbustível que gostaria colocar:"))

if (comb == "A"):
  if(litros <= 20):
    valor = (3*litros)*0.97
    print("A quantidade a ser paga será de:", valor)
  else:
    valor = (3*litros)*0.95
    print(valor)
elif (comb == "G"):
  if(litros < 20):
    valor = (5*litros)*0.96
    print(valor)
  else:
    valor = (5*litros)*0.94
    print(valor)