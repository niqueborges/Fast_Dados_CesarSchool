# O CESAR deseja enviar uma mensagem aos seus funcionários informando sobre um bônus especial.
# Escreva um programa que receba o valor do salário mensal do funcionário e sobre esse salário, calcule um bônus de 10%.
# Ao final, imprima na tela o salário inicial, o salário final e quanto de acréscimo o funcionário recebeu em reais.

# recebendo o valor do salário mensal do funcionário
salario_mensal = float(input('Digite o valor do salário mensal do funcionário: '))

# calculando o bônus de 10%
bonus = salario_mensal * 0.1

# calculando o salário final com o bônus
salario_final = salario_mensal + bonus

# Exibindo as informações na tela
print(f'O salário inicial é de R$ {salario_mensal:.2f} e o salário final é de R$ {salario_final:.2f}. O funcionário recebeu um acréscimo de R$ {bonus:.2f} em seu salário.')


