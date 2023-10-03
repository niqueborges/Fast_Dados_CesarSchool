"""Faça uma função:
armazenaridades, onde vários nomes e idades são armazenados em duas listas. Apenas “Maria” não pode ser adicionada. 
O programa deve finalizar quando -1 for digitado.
Utilize break e continue.
A função deve retornar as listas de nomes e idades.
No programa principal, imprima o retorno da função."""

def armazenar_idades():
    nomes = []
    idades = []
    
    while True:
        nome = input('Digite o nome: ')
        idade = int(input(f'Digite a idade de {nome}: '))
        
        if nome == 'Maria':
            print('Maria não pode ser adicionada')
            continue
        if idade == -1:
            break
        
        nomes.append(nome)
        idades.append(idade)
    return nomes, idades

print(armazenar_idades())
        