# Você deve fazer um programa que leia um valor qualquer e apresente uma mensagem dizendo em qual dos seguintes intervalos ([0,25], (25,50], (50,75], (75,100]) este valor se encontra. 
# Obviamente se o valor não estiver em nenhum destes intervalos, deverá ser impressa a mensagem “Fora de intervalo”.
# O símbolo ( representa "maior que". 
# Por exemplo: [0,25]  indica valores entre 0 e 25, inclusive eles.
# (25,50] indica valores maiores que 25 Ex: 25.1 até o valor 50

valor = float(input('Digite um valor: '))

if valor >= 0 and valor <= 25:
  print(f'O valor {valor} se encontra entre 0 e 25')
elif valor > 25 and valor <= 50:
  print(f'O valor {valor} se encontra entre 25 e 50')
elif valor > 50 and valor <= 75:
  print(f'O valor {valor} se encontra entre 50 e 75')
elif valor > 75 and valor <= 100:
  print(f'O valor {valor} se encontra entre 75 e 100')
else:
  print('Fora do intervalo')
