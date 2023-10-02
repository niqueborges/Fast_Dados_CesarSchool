"""Desenvolva um programa para calcular a redução do tempo de vida de um fumante. 
Pergunte a quantidade média de cigarros fumados por dia e por quantos anos ele já fumou. 
Considere que um fumante perde 10 min de vida a cada cigarro.  
Calcule e exiba quantos dias de vida o fumante perdeu até o momento."""

cigarros_por_dia = int(input('Digite a quantidade de cigarros fumados por dia: '))
anos_fumando = int(input('Digite a quantidade de anos fumando: '))
minutos_perdidos = cigarros_por_dia * 10 * 365 * anos_fumando
dias_perdidos = minutos_perdidos / 1440

print(f'O fumante perdeu {dias_perdidos:.2f} dias de vida até o momento.')
