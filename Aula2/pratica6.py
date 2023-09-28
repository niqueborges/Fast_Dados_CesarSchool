# Desenvolva um programa de teatro, que após inserida a idade de uma pessoa, seja indicado o valor do ingresso segundo as regras:
# a) A entrada para qualquer pessoa com menos de 4 anos ou maior que 60 é gratuita.
# b) A entrada para qualquer pessoa com idade entre 4 e 18 custa 20 reais.
# c) A entrada para qualquer pessoa com 18 ou mais custa 30 reais.

idade = int(input('Digite a idade da pessoa: '))

if idade < 4 or idade > 60:
    print('Entrada gratuita!')
elif idade >= 4 and idade <= 18:
    print('Valor do ingresso: R$ 20.00')
else:
    print('Valor do ingresso: R$ 30.00')