"""Faça uma função que calcule a média de um aluno (duas notas) de acordo com o critério definido neste curso.
Além, disso, faça uma segunda função que informe o status do aluno de acordo com a tabela a seguir:

Nota acima de 6.0: Aprovado
Nota entre 4.0 e 6.0: Verificaçao Suplementar
Nota abaixo de 4.0: Reprovado

Utilizar duas funções"""

def media(nota1, nota2):
    return (nota1 + nota2) / 2

def status(media):
    if media > 6:
        print ('Aprovado!!')
    elif media >= 4 and media <= 6 :
        print ('Verificação Suplementar!!')
    else:
        print ('Reprovado!!')
        
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

resultado = media(nota1, nota2)
status(resultado)
