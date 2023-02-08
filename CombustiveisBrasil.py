#Primeiro de manipulacao de dados usando python pandas
#autor: Rafael Almeida da Silva

from IPython.display import display 
import pandas as pd

combustiveis_df = pd.read_excel("ca202102_20230207120945.xlsx") #Coloca a bd em uma vareavel


display(combustiveis_df.head(15)) # serve para mostrar o n de linhas
display(combustiveis_df.shape) # serve para mostar o numero de colnas e linhas
display(combustiveis_df.info) #Quais sao as colunas e os tipos de dados que tem
display(combustiveis_df.describe()) # mostra as estatisticas basicas
display(combustiveis_df['Revenda'].head(11)) #Filtrar por uma coluna

#craicao de um novo df com as tres colnas especificadas
ca_df= combustiveis_df[['Revenda', 'Municipio', 'Produto','Valor de Venda']]
display(ca_df.head(10))

# Exibe a linha expecificada 
display(ca_df.loc[3])
display(ca_df.loc[9:19])# Filtragem por intervalo 


GASOLINA_df= ca_df.loc[ca_df['Produto'] == 'GASOLINA']
display(GASOLINA_df[['Revenda', 'Municipio','Valor de Venda']].max())