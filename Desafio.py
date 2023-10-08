"""Desenvolva um programa em Python que apure o resultado de uma votação para determinar o personagem favorito do desenho “The Simpsons”. Suponha que existam 2 candidatos cujos códigos são:

1 - Bart
2 - Homer
 
Considere que existe uma função que recebe e escreve em um arquivo .txt ou em uma lista/vetor os votos de 5 pessoas. Um voto é representado pelo código de identificação do candidato.

Na sequência, uma função para leitura deverá ser implementada, a qual deverá apresentar, como resultado:

o nome e a quantidade de votos do candidato mais votado
o nome e a quantidade de votos do menos votado
quantidade de votos nulos (um voto nulo é um voto cujo código de identificação é um valor diferente de 1 e 2)."""


# Função para receber e escrever os votos em um arquivo .txt
def receber_votos():
  # Abrir o arquivo em modo de escrita
  arquivo = open("votos.txt", "w")
  # Pedir os votos de 5 pessoas
  for i in range(5):
    print(f"Digite o código do seu personagem favorito do desenho 'The Simpsons':")
    print("1 - Bart")
    print("2 - Homer")
    # Receber o voto e validar se é um número inteiro
    try:
      voto = int(input("Voto: "))
    except ValueError:
      print("Valor inválido. Digite um número inteiro.")
      continue
    # Escrever o voto no arquivo com uma quebra de linha
    arquivo.write(str(voto) + "\n")
  # Fechar o arquivo
  arquivo.close()

# Função para ler e apurar os votos do arquivo .txt
def apurar_votos():
  # Abrir o arquivo em modo de leitura
  arquivo = open("votos.txt", "r")
  # Criar um dicionário para armazenar os votos de cada candidato
  votos = {1: 0, 2: 0}
  # Criar uma variável para contar os votos nulos
  nulos = 0
  # Ler cada linha do arquivo e incrementar os contadores de votos
  for linha in arquivo:
    # Converter a linha em um número inteiro
    voto = int(linha)
    # Verificar se o voto é válido (1 ou 2)
    if voto in votos:
      # Incrementar o voto do candidato correspondente
      votos[voto] += 1
    else:
      # Incrementar o voto nulo
      nulos += 1
  # Fechar o arquivo
  arquivo.close()
  # Criar uma lista para armazenar os nomes dos candidatos
  nomes = {1: "Bart", 2: "Homer"}
  # Criar uma variável para armazenar o código do candidato mais votado
  mais_votado = None
  # Criar uma variável para armazenar o código do candidato menos votado
  menos_votado = None
  # Criar uma variável para armazenar a maior quantidade de votos
  maior_qtd = None
  # Criar uma variável para armazenar a menor quantidade de votos
  menor_qtd = None
  # Percorrer o dicionário de votos e comparar as quantidades
  for codigo, qtd in votos.items():
    # Se a variável mais_votado for None ou a quantidade for maior que a maior_qtd
    if mais_votado == None or qtd > maior_qtd:
      # Atualizar as variáveis mais_votado e maior_qtd
      mais_votado = codigo
      maior_qtd = qtd
    # Se a variável menos_votado for None ou a quantidade for menor que a menor_qtd
    if menos_votado == None or qtd < menor_qtd:
      # Atualizar as variáveis menos_votado e menor_qtd
      menos_votado = codigo
      menor_qtd = qtd
  
  # Apresentar os resultados da apuração na tela
  print(f"O candidato mais votado foi {nomes[mais_votado]}, com {maior_qtd} votos.")
  print(f"O candidato menos votado foi {nomes[menos_votado]}, com {menor_qtd} votos.")
  print(f"A quantidade de votos nulos foi {nulos}.")