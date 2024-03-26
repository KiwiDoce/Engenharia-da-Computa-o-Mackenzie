# Exercício 2: Programa para informar o 1-tipo de carne; 2- quantidade de carne; 3- preço total; 4- tipo de pagamento; 5- valor do desconto; 6- valor a pagar.

valid = 0
TC = input("Informe o tipo de carne que gostaria:")
QK = float(input("Informe a quantidade de carne, em quilos, que deseja:"))
FormPag = input("Possui o cartão Real?:")

if (TC == "Patinho"):
  if(QK <= 5):
    valor = 4.9*QK
    if(FormPag == "não"):
      valorP = valor
      valid = 1
    elif (FormPag == "sim"):
      valorP = valor*0.95
      valid = 1
  elif (QK > 5):
    valor = 5.8*QK
    if(FormPag == "não"):
      valorP = valor
      valid = 1
    elif (FormPag == "sim"):
      valorP = valor*0.95
      valid = 1
elif (TC == "Contra filé"):
  if(QK <= 5):
    valor = 5.9*QK
    if(FormPag == "não"):
      valorP = valor
      valid = 1
    elif (FormPag == "sim"):
      valorP = valor*0.95
      valid = 1
  elif (QK > 5):
    valor = 6.8*QK
    if(FormPag == "não"):
      valorP = valor
      valid = 1
    elif (FormPag == "sim"):
      valorP = valor*0.95
      valid = 1
elif (TC == "Filé Mignon"):
  if(QK <= 5):
    valor = 6.9*QK
    if(FormPag == "não"):
      valorP = valor
      valid = 1
    elif (FormPag == "sim"):
      valorP = valor*0.95
      valid = 1
  elif (QK > 5):
    valor = 7.8*QK
    if(FormPag == "não"):
      valorP = valor
      valid = 1
    elif (FormPag == "sim"):
      valorP = valor*0.95
      valid = 1

if (valid == 1):
  valorD = valor - valorP

  print("O tipo de carne escolhida foi:", TC)
  print("A quantidade de carne em quilos escolhida foi:", QK)
  print("O preço total é:", valor)
  print("Você possui cartão real:", FormPag)
  print("A quantidade de desconto recebida foi:", valorD)
  print("O valor real a ser pago será:", valorP)
else: 
  print("erro!")