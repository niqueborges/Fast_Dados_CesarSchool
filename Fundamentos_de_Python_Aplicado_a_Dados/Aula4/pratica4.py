"""Faça um programa que pergunte para um gerente de uma lanchonete se ele deseja remover, 
adicionar ou modificar o valor de um produto do cardápio,
apenas encerrando o algoritmo quando o usuário decidir.
No final, mostre o cardápio com as modificações. Segue o cardápio original (já cria o dicionário com esses valores):

# Item: coxinha, pastel, suco, bolo (R$ 5.00, R$ 4.00, R$ 3.50, R$ 4.50)"""

cardapio = {'coxinha': 5.00, 'pastel': 4.00, 'suco': 3.50, 'bolo': 4.50}
print(cardapio)

decisao = input('Você deseja modificar o cardápio? [S] ou [N] ').upper()


while decisao == 'S':
    pergunta = input('Você deseja [A]dicionar, [R]emover ou [M]odificar um item? ').upper()
    
    if pergunta == 'A':
        nome = input('Digite o nome do produto que deseja adicionar? ').capitalize()
        preco = float(input(f'Digite o preço do produto {nome}: '))
        cardapio[nome] = preco
        
    elif pergunta == 'R':
        nome = input('Digite o nome do produto que deseja remover? ').capitalize()
        if cardapio.get(nome):
            cardapio.pop(nome)
        else:
            print('Produto não encontrado!')
    elif pergunta == 'M':
        nome = input('Digite o nome do produto que deseja modificar? ').capitalize()
        if cardapio.get(nome):
            cardapio[nome] = preco
        else:
            print('Produto não encontrado!')
    else:
        print('Opção inválida!')
        
    decisao = input('\nVocê deseja continuar? [S] ou [N] ').upper()
    
print()
print(cardapio)