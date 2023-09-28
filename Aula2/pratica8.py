# Uma empresa deseja reavaliar os salários dos seus funcionários. Será reajustado o salário daqueles que estão há 2 anos ou mais sem receber aumento.
# O ajuste acontecerá da seguinte forma: 
# • Funcionário com mais de 10 anos de casa, 30%.
# • Funcionário que tem entre 5 a 10 anos de casa, 20%.
# • Funcionário com menos de 5 anos de casa, 10%.
# Aqueles que receberam aumento salarial há menos de 2 anos não estão aptos ao reajuste salarial coletivo. 
# Faça um programa que receba as seguintes informações sobre o funcionário:
# • Ano de admissão;
# • salário atual;
# • ano do último reajuste salarial.
# O programa deverá mostrar o novo salário do funcionário ou uma mensagem informando que ele não está apto ao reajuste salarial coletivo.

import os
os.system('cls')
from datetime import date

ano_atual = date.today().year
ano_admissao = int(input('Digite o ano de admissão: '))
salario_atual = float(input('Digite o salário atual: '))
ano_ultimo_reajuste = int(input('Digite o ano do último reajuste salarial: '))

tempo_aumento = ano_atual - ano_ultimo_reajuste
tempo_empresa = ano_atual - ano_admissao

if tempo_aumento >= 2:
    if tempo_empresa >= 10:
       novo_salario = salario_atual*1.3
    elif tempo_empresa >= 5 and tempo_empresa < 10:
        novo_salario = salario_atual*1.2
    else:
        novo_salario = salario_atual*1.1
        
    print('\nApto a receber reajuste salarial coletivo!')
    print('Novo salário: R$ ', novo_salario)
else:
    print('\nNão está apto a receber reajuste salarial coletivo!')


