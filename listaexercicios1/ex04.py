valorc = float(input("Qual o valor da casa a ser comprada? "))
sal = float(input("Qual o valor do seu salário? "))
anos = float(input("Qual a quantidade de anos a pagar? "))

mes = anos * 12
prest = valorc/mes
psal = sal * 0.3

if prest > psal:
  print("Seu empréstimo foi negado.")
else:
  print("Seu empréstimo foi aprovado.")
  
