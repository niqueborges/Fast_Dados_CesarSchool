"""Desenvolva um programa que leia dois números e efetue a adição. 
Caso o resultado seja maior que 10, este deverá ser apresentado somando-se a ele mais 5; caso o resultado seja menor ou igual a 10, 
este deverá ser apresentado subtraindo-se 5.""" 

num_A = int(input('Digite o primeiro número: '))
num_B = int(input('Digite o segundo número: '))

soma = num_A + num_B

if soma > 10:
    print(f'O resultado da soma é {soma + 5}')
else:
    print(f'O resultado da soma é {soma - 5}')
