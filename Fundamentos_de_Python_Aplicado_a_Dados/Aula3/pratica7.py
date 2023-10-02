"""Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax² + bx + c. 
O programa deverá perguntar ao usuário de quantas equações ele deseja calcular as raízes, e na sequência solicitar os valores de a, b e c.
Considere as seguintes situações:
1. Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve pedir os demais valores (b e c) ao usuário;
2. Se o delta calculado for negativo, a equação não possui raízes reais. Informe ao usuário;
Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax² + bx + c. 
O programa deverá perguntar ao usuário de quantas equações ele deseja calcular as raízes, e na sequência solicitar os valores de a, b e c.
Considere as seguintes situações:
1. Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve pedir os demais valores (b e c) ao usuário;
2. Se o delta calculado for negativo, a equação não possui raízes reais. Informe ao usuário;

PS: digite 'import math' no início do seu código. Para achar a raiz quadrada da variável x, faça: math.sqrt(x)."""

import math

print('Calculando as raízaes da equação do 2º grau: ax² + bx + c')

quant = int(input('De quantas equações você gostaria de calcular as raízes: '))

for i in range(quant):
    a = int(input('\nCoeficiente de a: '))
    
    if a == 0:
        print('Se a = 0 a equação não é do 2º grau!')
    else:
        b = int(input('Coeficiente de b: '))
        c = int(input('Coeficiente de c: '))
        delta = b**2 - 4*a*c
        
        if delta < 0:
            print('Delta menor que zero, a equação não possui raízes reais!')
        else:
            raiz1 = (-b + math.sqrt(delta)) / (2*a)
            raiz2 = (-b - math.sqrt(delta)) / (2*a)
            print(f'As raízes da equação são: {xraiz1} e {raiz2}')



