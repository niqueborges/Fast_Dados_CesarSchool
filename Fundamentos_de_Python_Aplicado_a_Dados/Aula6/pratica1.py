"""Calculadora"""

def soma (n1, n2):
    return n1 + n2      
def subtracao (n1, n2):
    return n1 - n2
def multiplicacao (n1, n2):
    return n1 * n2
def divisao (n1, n2):
    if n1 >= n2:
        return n1 / n2 
    else:
        return n2 / n1

# Programa Principal

resposta = input('Deseja realizar uma operação? [S/N] ').upper()
while resposta == 'S':
    num1 = int(input('Digite o primeiro número: '))
    num2 = int(input('Digite o segundo número: '))
    operacao = input('[S]Soma, [B]Subtração, [M]Multiplicação e  [D]Divisão : ').upper()
    
    if operacao =='S':
        print(soma(num1, num2))
    elif operacao =='B':
        print(subtracao(num1, num2))
    elif operacao =='M':
        print(multiplicacao(num1, num2))
    elif operacao =='D':
        print(divisao(num1, num2))
    else:
        print('Operação inválida!')
        
    resposta = input('Deseja realizar uma nova operação? [S/N] ').upper()

    
    