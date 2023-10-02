"""Após o usuário digitar um número inteiro, informe se ele é um número perfeito.
Um número é perfeito se a soma dos seus divisores (exceto ele) for igual ao próprio número. Ex: : 6 é perfeito, pois 1+2+3 = 6."""

n = int(input('Digite um número: '))

soma = 0

# i reprsenta divisores

for i in range(1, n):
    if n % i == 0:
        soma = soma + i
        
if n == soma:
    print(f'O número {n} é perfeito')
else:
    print(f'O número {n} não é perfeito')