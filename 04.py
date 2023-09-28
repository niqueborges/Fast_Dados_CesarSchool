# Média 1 - Leia 2 valores reais A e B, que correspondem a 2 notas de um estudante. 
# A seguir, calcule a média do estudante, sabendo que a nota A tem peso 3.5 e a nota B tem peso 7.5 (A soma dos pesos, portanto, é 11). 
# Assuma que cada nota pode ir de 0 até 10.0.

a = float(input('Digite a primeira nota: '))
b = float(input('Digite a segunda nota: '))

media = (a * 3.5 + b * 7.5) / 11

print(f'A media de {a} e {b} é {media:.2f}')