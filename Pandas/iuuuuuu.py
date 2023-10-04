import pandas as pd

estados = [['Amazonas', 'AM', '3,9 milhões', 'Manaus'],
           ['Minas Gerais', 'MG', '2.3 milhões', 'Governador Valadares'],
           ['Ceará', 'CE', '9,2 milhões', 'Fortaleza'],
           ['Maranhão', 'MA', '7,1 milhões', 'São Luís'],
           ['Paraíba', 'PB', '4,1 milhões', 'João Pessoa']]

df = pd.DataFrame(estados,columns=['Estado', 'Sigla', 'População', 'Cidade', 'Capital'])

idh = [0.956, 0.645, 0.641, 0.569, 0.651]
df['IDH'] = idh
print(df)