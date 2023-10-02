"""Um número é considerado triangular se ele é produto de três números naturais consecutivos. 
Por exemplo: 120 é triangular, pois 4*5*6 = 120. 
O número 2730 é triangular, pois 13*14*15 = 2730. Após o usuário digitar um número natural (inteiro não-negativo), 
verifique se ele é triangular ou não."""

print('Determina se um numero n eh triangular\n')

n = int(input('Digite o valor de n: '))

i = 1
while i * (i+1) * (i+2) < n:
    i = i + 1

if i * (i+1) * (i+2) == n:
    print('%d eh o produto %d*%d*%d' %(n,i,i+1,i+2))
else:
    print('%d nao eh triangular' %(n))
