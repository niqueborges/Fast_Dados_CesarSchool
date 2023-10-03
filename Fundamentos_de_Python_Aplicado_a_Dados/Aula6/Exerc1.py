"""Faça um programa que receba um valor em horas e dê duas opções ao usuário, converter em minutos ou em segundos. 
A partir da escolha do usuário, o programa deverá chamar a função específica de conversão. 
A função para converter horas em minutos deverá receber como parâmetro a hora e retornar o valor em minutos. 
A função para converter horas em segundos deverá receber como parâmetro a hora e retornar o valor em segundos. 
Por fim, o programa principal imprime o valor retornado pela função. """

def converter_para_minutos(horas):
    min = horas * 60
    return min

def converter_para_segundos(horas):
    segundos = horas * 3600
    return segundos

horas = int(input('Informe o valor em horas: '))
escolha = input('Digite [M] para converter em minutos ou [S] para converter em segundos: ').upper()

if escolha.upper() == 'M':
    converter_para_minutos(horas)
    print(f'{horas} horas equivalem a {min} minutos.')
elif escolha.upper() == 'S':
    converter_para_segundos(horas)
    print(f'{horas} horas equivalem a {segundos} segundos.')
else:
    print('Entrada inválida.')