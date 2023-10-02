"""Desenvolva um programa que receba o nome de um ciclista, a distância que ele percorreu em Km e o tempo que ele gastou nesse percurso, em horas.  
O programa deverá calcular a velocidade média do ciclista e, exibi-la na tela duas vezes, uma em Km/h e a outra em m/s. 
Dividimos por 3,6 quando queremos converter Km/h para m/s."""

nome_ciclista = input('Digite o nome do ciclista: ')
distancia = float(input('Digite a distância percorrida pelo ciclista: '))
tempo = float(input('Digite o tempo gasto pelo ciclista: '))

velocidade_media = distancia / tempo

print(f'A velocidade média do ciclista {nome_ciclista} é {velocidade_media:.2f}Km/h e {velocidade_media / 3.6:.2f}m/s')
