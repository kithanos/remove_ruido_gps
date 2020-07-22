import pandas as pd
import numpy as np
import csv

#Leitura de dados do arquivo csv com pandas
dados = pd.read_csv('gps_dataset_15.csv')

#Seleciona dados apenas das colunas 5 e 6 (Latitude e Longitude)
X = dados.iloc[:, 5:7].values
print('\nDados de Latitude e Longitude\n')
print(X)

#Aplica K-means, para identificar dados com ruido
#Neste caso, os dados ruidos vieram com registros zerados.
from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters = 2, init = 'random')
kmeans.fit(X)

#Salva labels de classificao
labels = pd.DataFrame(data=kmeans.labels_,columns=["Y"])
print('\nClassificacao\n')
print (labels)

#Seleciona o rotulo das imagens (ID imagens)
Imagens = pd.DataFrame(dados.iloc[:, 2:3].values,columns=["Imagem_ID"])
print('\nRotulo Imagens\n')
print(Imagens)

#Junta os dados originais, com o resultado da classificao
#Seleciona apenas os dados classificados com sem ruido (Y=0)
dados_finais = pd.DataFrame.join(dados,labels,sort=False)
ruidos = dados_finais["Y"]==0

#Salva em um arquivo CSV
final = dados_finais[ruidos]
print(final)
final.to_csv("Resultado.csv")
