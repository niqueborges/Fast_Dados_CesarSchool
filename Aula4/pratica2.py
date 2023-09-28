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

perguntas = []

perguntas.append(input("Conhece a vítima do furto? "))
perguntas.append(input("Esteve no local do furto? "))
perguntas.append(input("Mora perto da vítima? "))
perguntas.append(input("A vítima lhe devia? "))
perguntas.append(input("Já trabalhou com a vítima: "))
soma=0
for p in perguntas:
    if p=="SIM":
        soma+=1
if soma==2:
    print("Suspeita")
elif soma==3 or soma==4:
    print("Cúmplice")
elif soma==5:
    print("Ladrão")
else:
    print("Inocente")