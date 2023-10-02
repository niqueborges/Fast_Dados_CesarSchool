"""Crie um programa que leia vários números digitados pelo usuário e mostre no final o somatório entre eles. 
Obs: O programa será interrompido quando o número 1111 for digitado."""

soma = 0

while True:
    numero = int(input('Digite um número para ser somado ou Digite(1111) para encerrar o programa:\n'))

    if numero == 1111:
        break

    soma += numero

print(f'A soma é: {soma}')
