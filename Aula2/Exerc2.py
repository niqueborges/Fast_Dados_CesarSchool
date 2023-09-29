# Desenvolva um programa que seja capaz de calcular a média ponderada de um aluno. 
# Inicialmente solicite o nome e as três notas do aluno, logo após, calcule e exiba na tela a média.  
# Na média ponderada considere os seguintes pesos nas notas: 2, 3 e 5. Essa é a fórmula para calcular a média.

# mediafinal = n1 * 2 + n2 * 3 + n3 * 5 / 10

# Logo após verifique e informe o status do aluno na disciplina baseando nas seguintes informações:

# Média até 4.9: reprovado
# Média entre 5.0 e 6.9: recuperação
# Média 7.0 ou superior: aprovado

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
n3 = float(input('Digite a terceira nota: '))

media_ponderada = ((n1 * 2) + (n2 * 3) + (n3 * 5)) / 10

if media_ponderada <= 4.9:
  print('Que pena! Você está reprovado.')
elif media_ponderada >= 5.0 and media_ponderada <= 6.9:
  print('Quase lá! Você está na recuperação.')
else:
  print('Arrasou! Você está aprovado!')


