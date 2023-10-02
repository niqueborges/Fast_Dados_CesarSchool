"""Um petshop atende 5 cachorros por tarde. Faça um programa que solicite ao usuário o código do serviço efetuado: 
(1 - banho; 2 - tosa; 3 - banho e tosa; 4- outros). 
Por fim, exiba a quantidade de solicitações para cada um deles."""

serv1 = 0
serv2 = 0
serv3 = 0
serv4 = 0

for i in range(5):
    servico = int(input('Selecione o código do serviço:\n(1) banho\n(2) tosa\n(3) banho e tosa\n(4) outros\n'))

    if servico == 1:
        serv1 += 1
    elif servico == 2:
        serv2 += 1
    elif servico == 3:
        serv3 += 16
    elif servico == 4:
        serv4 += 1
    else:
        print('Código inválido!')
        servico = int(input('Selecione o código do serviço:\n(1) banho\n(2) tosa\n(3) banho e tosa\n(4) outros\n'))

print(f'Relatório diário de serviços:\n(1) banho: {serv1}\n(2) tosa: {serv2}\n(3) banho e tosa: {serv3}\n(4) outros: {serv4}')
