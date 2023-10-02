"""Desenvolva um programa que receba as notas de 5 alunos e, na sequência calcule e informe a média;
Além disso, mostre na tela as notas que são superiores à média da turma.

Digite a nota do aluno 1: 7
Digite a nota do aluno 2: 8
Digite a nota do aluno 3: 4
Digite a nota do aluno 4: 3
Digite a nota do aluno 5: 9.5
A média da turma é: 10.0
A nota 7.0 é superior à média da turma.
A nota 8.0 é superior à média da turma.
A nota 9.5 é superior à média da turma."""

notas = []

for i in range(5):
    notas.append(float(input(f'Digite a nota: ')))

media = sum(notas)/5
print(f'A média da turma é: {media:.2f}')

for nota in notas:
    if nota > media:
        print(f'A nota {nota} foi superior à média!')