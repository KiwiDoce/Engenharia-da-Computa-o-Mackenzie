# Exercício 4: Construa uma estrutura condicional para verificar se n está no intervalo: 1 ≤ n ≤ 100.

n = float(input("Insira um número aqui: "))
if (1 <= n <= 100):
  print("O número", n,"está entre 1 e 100")
else:
  print("O número", n,"não está entre 1 e 100")