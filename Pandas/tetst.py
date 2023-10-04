import pandas as pd

dados = {
    "Nome": ["Jé", "Maria", "João"],
    "Cidade": ["Recife", "Porto Alegre", "Aracajú"],
    "Idade": [32, 30, 49],
    "Telefone": ["(81) 98374-2812", "(51) 98472-3920", "(01) 95748-3921"]
}
#Criar dataframe
df = pd.DataFrame(dados)
print(df)