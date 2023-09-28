# A conta de energia elétrica de consumidores residenciais de uma cidade é calculada do seguinte modo:
# • se o consumo é de até 500 kw, a tarifa é de R$ 0,02 por unidade de kw;
# • se o consumo é maior que 500 kw, mas não excede 1000 kw, a tarifa é de R$10,00 por unidade de kw;
# • se o consumo é maior que 1000kw, a tarifa é de R$35,00 por unidade de kw;
# • em toda conta, é cobrada uma taxa básica de serviço de R$5,00, independentemente da quantidade de energia consumida.
# Escreva um programa que leia o consumo de energia de uma residência e imprima o valor da sua conta de energia.

kw = int(input('Digite a quantidade de kw consumida: '))

if kw <= 500:
    print('Valor da conta: R$ ', (kw*0.02) + 5.00)
elif kw > 500 and kw <= 1000:
    print('Valor da conta: R$ ', (kw*10.00) + 5.00)
else:
    print('Valor da conta: R$ ', (kw*35.00) + 5.00)