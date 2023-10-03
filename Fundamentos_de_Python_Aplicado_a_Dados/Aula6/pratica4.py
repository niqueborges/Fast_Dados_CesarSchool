"""Faça um programa que tenha uma lista(vetor) chmamada números e duas funções chamadas sorteia() e somaPar().
A primeira função vai sortar 5 números (entre 0 e 99) e vai colocá-los dentros da lista.
A segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior."""

from random import randint

def sorteia():
    numeros = []
    for i in range(5):
        numeros.append(randint(0, 99))
    return numeros

def somaPar(numeros):
    soma = []
    for i in numeros:
        if i % 2 == 0:
            soma.append(i)
    print(f'Os números sorteados foram: {numeros}')
    print(f'A soma dos números pares é: {sum(soma)}')
    
somaPar(sorteia())




