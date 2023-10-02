"""Foi realizada uma pesquisa de algumas características físicas de 5 alunos de um curso, 
a qual coletou os seguintes dados referentes a cada pessoa para serem analisados:
sexo (masculino e feminino)
cor dos olhos (azuis, verdes ou castanhos)
cor dos cabelos ( louros, castanhos, pretos)
idade

Faça um algoritmo que determine e escreva:
a) a quantidade de pessoas do sexo feminino cuja idade está entre 18 e 35;
b) a quantidade de pessoas que têm olhos castanhos e cabelos pretos."""

rangeidade = 0
cabelocastanho = 0

for i in range(5):
    sexo = int(input('Digite seu gênero:\n(1) para feminino\n(2) para masculino\n'))
    olhos = int(input('Digite a cor dos seus olhos:\n(1) para azul\n(2) para verde\n(3) para castanho\n'))
    cabelo = int(input('Digite a cor do seu cabelo:\n(1) para loiro\n(2) para castanho\n(3) para preto\n'))
    idade = int(input('Digite a sua idade:\n'))

    if sexo == 1 and 18 <= idade <= 35:
        rangeidade += 1
    if olhos == 3 and cabelo == 3:
        cabelocastanho += 1

print(f'A quantidade de pessoas do sexo feminino cuja idade está entre 18 e 35 é {rangeidade}')
print(f'A quantidade de pessoas que têm olhos castanhos e cabelos pretos é {cabelocastanho}')