import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/brunamulinari/BasicPythonProjects/main/Base_ficticia/baseficticia.csv', sep = ',')

print(df.head())

type(df) 
pd.core.frame.DataFrame

df.head(n=6)