from cgitb import text
import pandas as pd
import plotly.express as px
import os

#Importar banco de dados
tabela = pd.read_csv('telecom_users.csv')
print(tabela)

#axis = 1 -> coluna | axis = 0 -> linha
tabela = tabela.drop(["Unnamed: 0", "IDCliente"], axis=1)
print(tabela)

#Tratar banco de dados
tabela['TotalGasto'] = pd.to_numeric(tabela['TotalGasto'], errors="coerce")
print(tabela.info())

#removendo colunas que estão inteiras vazias
tabela = tabela.dropna(how='all', axis=1)

#removendo linhas que tem alguma informação faltando (celulas em branco)
tabela = tabela.dropna(how='any', axis=0)

print(tabela.info())

#Analisar banco de dados
print(tabela['Churn'].value_counts()) #analisando coluna churn, contando informações contidas
print(tabela['Churn'].value_counts(normalize=True).map('{:.1%}'.format)) #coloca as informações em porcentagem
#map -> formatação da porcentagem com 1 casa decimal

#Descobrir motivos dos cancelamentos
for coluna in tabela.columns:   
        #criar grafito
        grafico = px.histogram(tabela, x=coluna, color='Churn', text_auto=True)
        grafico.show()
     
#conclusões
