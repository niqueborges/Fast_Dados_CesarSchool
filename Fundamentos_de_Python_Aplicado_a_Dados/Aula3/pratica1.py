"""Desenvolva um programa que some os números pares entre o intervalo de dois números. 
O número inicial e o final do intervalo são fornecidos pelo usuário. Caso esses valores sejam pares, eles também entram na contagem."""

import os

os.system('cls')

num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
soma = 0

while num1 <= num2:
    if num1 % 2 == 0:
        soma = soma + num1
    num1 += 1
print(f'A soma dos números pares é: {soma}')