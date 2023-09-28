#Incompleto (caiu a internet)
# Faça um programa que pergunte para um gerente de uma lanchonete se ele deseja remover, adicionar ou modificar o valor de um produto do cardápio,
# apenas encerrando o algoritmo quando o usuário decidir.
# No final, mostre o cardápio com as modificações. Segue o cardápio original (já cria o dicionário com esses valores):

# Item: coxinha, pastel, suco, bolo (R$ 5.00, R$ 4.00, R$ 3.50, R$ 4.50)

cardapio = {"coxinha": 5.00, "pastel": 4.00, "suco": 3.50, "bolo": 4.50}

while True:
    print("1 - Adicionar item")
    print("2 - Remover item")
    print("3 - Modificar valor de item")
    print("4 - Sair")
    opcao = int(input("Digite a opção desejada: "))
    if opcao == 1:
        item = input("Digite o nome do item: ")
        preco = float(input("Digite o preço do item: "))
        cardapio[item] = preco
    elif opcao == 2:
        item = input("Digite o nome do item: ")
        del cardapio[item]
    elif opcao == 3:
        item = input("Digite o nome do item: ")
        preco = float(input("Digite o preço do item: "))
        cardapio[item] = preco
    elif opcao == 4:
        break
    else:
        print("Opção inválida!")