# Uma revendedora de carros usados paga a seus vendedores um salário fixo por mês, mais uma comissão também fixa para cada carro vendido 
# e mais 5% do valor das vendas por ele efetuadas.
# Escreva um algoritmo que leia o número de carros vendidos por uma pessoa vendedora, o valor total de suas vendas, o salário fixo e a
# comissão que a pessoa receberá por carro vendido. Calcule e escreva o salário final. 

salario_fixo = float(input('Digite o salário fixo: '))
comissao = float(input('Digite a comissão por carro vendido: '))
carros_vendidos = int(input('Digite o número de carros vendidos: '))
valor_vendas = float(input('Digite o valor total das vendas: '))

salario_final = salario_fixo + (comissao * carros_vendidos) + (valor_vendas * 0.05)

print(f'O salário final do vendedor é de R$ {salario_final:.2f}')
