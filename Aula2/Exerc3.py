"""A fabricação dos presentes para o Natal é um processo muito complicado. 
Diversas vezes os duendes ficam até tarde trabalhando para que tudo possa ser terminado a tempo e com perfeição. 
Para melhor gerenciar seus cronogramas, os duendes estipularam quantos minutos são necessários para fabricar cada presente.
Já está quase no final do expediente, e um dos duendes pediu sua ajuda. 
Faltam N minutos para a hora de ir embora, e restam dois presentes para o duende Ed fabricar. 
Solicite quantos minutos faltam, e quanto tempo é necessário para fabricar cada um dos presentes. 
Ajude-o a descobrir se conseguirá fabricar os dois ainda hoje, ou se deve deixar para amanhã."""

minutos = int(input('Quantos minutos faltam para a hora de ir embora? '))
tempo1 = int(input('Quanto tempo você precisa para fabricar o primeiro presente? '))
tempo2 = int(input('Quanto tempo você precisa para fabricar o segundo presente?'))

if minutos >= (tempo1) + (tempo2):
  print('Você conseguirá fabricar os presentes')
else:
  print('Que pena, Ed! Você terá que terminar amanhã')