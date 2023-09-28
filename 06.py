# Salário - Escreva um programa que leia o número de um funcionário, seu número de horas trabalhadas, o valor que recebe por hora e calcule o salário desse funcionário. 
# A seguir, mostre o número e o salário do funcionário.

num_func = int(input('Digite o número do funcionário: '))
horas_trab = int(input('Digite as horas trabalhadas: '))
valor_hora = float(input('Digite valor por hora: '))

salario = horas_trab * valor_hora

print('número = ', num_func)
print('salário = R$ %0.2f'%salario)


