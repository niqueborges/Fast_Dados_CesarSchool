"""Desenvolva uma função que permita receber uma variável inteira X inúmeras vezes 
(deve parar quando o valor digitado for igual a zero). 
Como retorno da função, para cada valor lido deverá ser imprimido a sequência de 1 até X (o número digitado), 
com um espaço entre cada número e seu sucessor. """

def imprimir_sequencia():
    while True:
        x = int(input('Informe número inteiro (0 para sair): '))
        
        if x == 0:
            break
        
        for i in range(1, x+1):
            print(i, end='')
        
        print()