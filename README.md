# remove_ruido_gps
Remover registros com ruído de uma leitura de gps.

Seleciona dados de uma tabela .csv

Seleciona dados da coluna Latitude e Longitude (colunas 5 e 6)

Aplica o k-means com dois centroides, um centroide terá
os dados ruidosos em sua volta, e o outro com os dados 
sem ruido, rotulando na variavel labels

label 0 --> dados sem ruído
label 1 --> dados com ruído

Essencialmente, podería ter sido feito apenas um condicional retirando os valores zerados
de Latitude e Longitude (colunas 5 e 6) nos dados originais, todavia, outros dados ruidosos 
de algum outro GPS podem não ter necessariamente valores zerados, logo, uma técnica de classificação
pode vir a ser útil para separar estes dados.

Salva apenas os registros sem ruídos em um arquivo csv.

Para executar, em um terminal do linux, digite:

>> python remove_ruido_GPS.py 

Programa executado na versão 2.7.12 do Python, com os pacotes:

Pandas
Numpy
CSV
sklearn
