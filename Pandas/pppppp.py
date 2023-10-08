import pandas as pd

lista = [['Maria', '8.5'],
         ['João', '7.8'],
         ['Luis', '9.2'],
         ['Vivian', '6.5'],
         ['Nana', '8.9']]

# CRIAR DATASET

dataLista = pd.DataFrame(lista, columns=['Nome', 'Media'])

# ADICIONANDO COLUNA

status = ['Aprovado', 'Aprovado', 'Aprovado', 'Reprovado', 'Aprovado']
dataLista['Status'] = status

busca = ['Aprovado']
dataLista[dataLista['Status'].isin(busca)]