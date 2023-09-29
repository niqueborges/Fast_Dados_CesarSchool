# Faça um algoritmo que leia a primeira letra do estado civil de uma pessoa e mostre uma mensagem com a sua descrição (Solteiro, Casado, Viúvo, Divorciado). 
# Mostre uma mensagem de erro, caso a opção seja inválida.

estado_civil = input('Digite o estado civil: ')

if estado_civil == 'S':
  print('Pessoa solteira')
elif estado_civil == 'C':
  print('Pessoa casada')
elif estado_civil == 'V':
  print('Pessoa viúva')
elif estado_civil == 'D':
  print('Pessoa divorciada')
else:
  print('Error')
