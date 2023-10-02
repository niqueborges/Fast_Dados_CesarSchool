"""Peça ao usuario que informe um número, logo após, calcula e exibe o fatorial do número digitado. 
O fatorial de um número é calculado multiplicando todos os valores inteiros entre o próprio número e 1.
Exemplo: 5! = 5 x 4 x 3 x 2 x 1 = 120"""

n= int(input('Digite um número: '))
c=n
f=1
while c !=1:
    f=f*c
    c-=1
    print ('{} x {} = {}'.format(n,c,f))
print ('O valor fatorial de {} é igual a {}!'.format(n,f))


