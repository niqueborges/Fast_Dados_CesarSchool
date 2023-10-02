"""Desenvolva um programa que permite ao usuário inserir os valores dos produtos comprados por um cliente. 
O programa deve terminar quando o usuário inserir o valor zero.
Se o usuário digitar um valor negativo, não deve ser processado e um novo valor deve ser solicitado como entrada.
Ao final informe o valor total a pagar.
Lembrando que, caso as vendas ultrapassem ao total de R$ 1.000,00 deverá ser aplicado um desconto de 10%."""

total = 0

while True:
    valor = float(input('Digite o valor do produto (ou 0 para encerrar): '))

    if valor == 0:
        break
    elif valor<0:
      print ('Valor inválido')

    total += valor

    if total > 1000:
        total = total * 0.9

print(f'O valor da compra com desconto é de {total}')