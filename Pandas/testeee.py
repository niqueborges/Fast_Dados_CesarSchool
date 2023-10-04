import pandas as pd

estados=[['Alagoas', 'AL', '3,4 milhões', 'Maceió'],
         ['Bahia', 'BA', '15,4 milhões', 'Salvador'],
         ['Ceará', 'CE', '9,2 milhões', 'Fortaleza'],
         ['Maranhão', 'MA', '7,1 milhões', 'São luiz'],
         ['Paraiba', 'PB', '4.0 milhões', 'João Pessoa'],
         ['Pernambuco', 'PE', '3,4 milhões', 'Recife'],
         ['Piauí', 'PI', '3,3 milhões', 'Teresina'],
         ['Rio Grande do Norte', 'RN', '3,5 milhões', 'Natal'],
         ['Sergipe', 'SE', '2,4 milhões', 'Aracaju']]
df = pd.DataFrame(estados,columns=['Estado', 'Sigla', 'População', 'Capital'])
print(df)