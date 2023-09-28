# Par ou ímpar  - Faça um programa para saber se o número digitado é Par ou Ímpar.

num = int(input('Digite um número inteiro' ))

imparPar = num%2

print('')

if imparPar == 0:
    print(str(num))