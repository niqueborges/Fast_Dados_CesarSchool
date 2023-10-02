"""Numa promoção exclusiva para o Dia da Mulher, uma loja quer dar descontos para todos, mas especialmente para as mulheres. 
Faça um programa que leia nome, sexo (F ou M) e o valor das compras do cliente e calcule o desconto. Sabendo que:
● Se for mulher, ganha 13% de desconto
● Senão, ganha 5% de desconto
Duas ações possíveis:
1. Aplicar 13% de desconto;
2. Aplicar 5% de desconto."""

nome = input('Digite o nome do cliente: ')
sexo = input('Digite o sexo do cliente (F ou M): ')
valor_compras = float(input('Digite o valor das compras: '))

if sexo == 'F':
    desconto = valor_compras * 0.13
else:
    desconto = valor_compras * 0.05
    
valor_final = valor_compras - desconto

print('cliente: ', nome)
print('valor das compras: R$ ', valor_compras)
print('desconto: R$ ', desconto)
print('valor final: R$ ', valor_final)


