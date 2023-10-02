"""Faça uma função que retorne o reverso de um número inteiro pelo usuário. Por exemplo: 127 -> 721"""

def reverso(num):
    return str(num)[::-1]

numero = int(input('Digite um número inteiro: '))
print(reverso(numero))