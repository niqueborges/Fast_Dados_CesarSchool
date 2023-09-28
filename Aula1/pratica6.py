# Peça ao usuário para inserir a temperatura em Fahrenheit. Na sequência, calcule e exiba na tela a temperatura em Celsius.

temperatura = float(input('Digite a temperatura em Fahrenheit: '))

celcius = (temperatura - 32) / 1.8

print(f'A temperatura em Celcius é de {celcius:.2f}')