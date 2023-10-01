# Um furto de celular aconteceu na cidade do RJ e você foi contratado para desenvolver um programa que possa ajudar sua professora 
# a identificar uma das pessoas envolvidas.
# Desenvolva uma solução utilizando vetor que faça 5 perguntas para apenas uma pessoa, sendo elas:
# Conhece a vítima do furto?
# Esteve no local do furto?
# Mora perto da vítima?
# A vítima lhe devia?
# Já trabalhou com a vítima?

# Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita",
# Entre 3 e 4 como "Cúmplice" e 5 como "Ladrão".
# Caso contrário, ela será classificada como "Inocente".

resposta = []
cont = 0

print('Responda as perguntas com SIM ou NÃO')
resposta.append(input('Conhece a vítima do furto? '))
resposta.append(input('Esteve no local do furto? '))
resposta.append(input('Mora perto da vítima? '))
resposta.append(input('A vítima lhe devia? '))
resposta.append(input('Já trabalhou com a vítima? '))

for i in resposta:
    if i == "SIM":
        cont += 1
        
if cont == 2:
    print('Pessoa suspeita')
elif (cont == 3 ) or (cont == 4):
    print('Pessoa cúmplice')
elif cont == 5:
    print('Ladrão')
else:
    print('Pessoa inocente')