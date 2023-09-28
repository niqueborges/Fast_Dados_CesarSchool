# Escreva um programa que leia três valores com ponto flutuante: A, B e C. Em seguida, calcule e mostre:
# a área do triângulo retângulo que tem o valor de A como base e o valor de C como altura.
# a área do círculo que tem como raio o valor de C.
# a área do trapézio que tem A e B por bases e C por altura.
# a área do quadrado que tem como lado o valor de B.
# a área do retângulo que tem lados A e B.

A = float(input('Digite o valor de A: '))
B = float(input('Digite o valor de B: '))
C = float(input('Digite o valor de C: '))

area_triangulo = (A * C) / 2
area_circulo = 3.14159 * (C ** 2)
area_trapezio = ((A + B) * C) / 2
area_quadrado = B ** 2
area_retangulo = A * B

print(f'A área do triângulo retângulo é {area_triangulo:.2f}')
print(f'A área do círculo é {area_circulo:.2f}')
print(f'A área do trapézio é {area_trapezio:.2f}')
print(f'A área do quadrado é {area_quadrado:.2f}')
