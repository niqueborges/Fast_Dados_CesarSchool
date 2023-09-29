# Crie um programa que leia o ano de nascimento de cinco pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores de idade.

from datetime import date

ano_atual = date.today().year
maior_idade = 0
menor_idade = 0

for i in range(5):
  ano = int(input("Digite o seu ano de nascimento: "))

  if ano_atual-ano>=18:
    maior_idade+=1
  else:
    menor_idade+=1

print(f"{maior_idade} pessoas são maiores de idade e {menor_idade} são menores de idade: ")