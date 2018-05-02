######################################################
# pandas
######################################################
import pandas as pd
import numpy as np

# s = pd.Series(np.random.randn(5), index=['a', 'b', 'c', 'd', 'e'])
# print(s)

# Series a partir de um dicionario
# d = {'a' : 0., 'b' : 1., 'c' : 2.}

# sd = pd.Series(d)
# print(sd)

# sd_index = pd.Series(d, index=['b', 'c', 'd', 'a'])
# print(sd_index)

# Acesso a valores da serie atraves do indice
# print(sd['a'])

# Operacoes com series
# print(sd)
# print(sd+sd)

# print(sd[1:])
# print(sd[:-1])
# print(sd[1:]+sd[:-1])


# d = {'one' : pd.Series([1., 2., 3.], index=['a', 'b', 'c']),
#     'two' : pd.Series([1., 2., 3., 4.], index=['a', 'b', 'c', 'd'])}

# df = pd.DataFrame(d)
# print(df)

# print(df.index)
# print(df.columns)
# print(df['one']['a'])

# DataFrame a partir de uma lista de dicionários
# data2 = [{'a': 1, 'b': 2}, {'a': 5, 'b': 10, 'c': 20}]

# Sem nomear indice explicitamente
# pd.DataFrame(data2)

# Nomeando indices explicitamente
# print(pd.DataFrame(data2, index=['first', 'second']))

# Restringindo colunas
# print(pd.DataFrame(data2, columns=['a', 'b']))

# Usando funcoes nativas e comparacoes
exam_data  = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
        'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
        'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

df = pd.DataFrame(exam_data , index=labels)
# print(df)
# print("\nMaior score no dataFrame:")
# max_score = df['score'].max()
# print(df[df['score'] == max_score])


# Leitura e escrita de CSV
# df.to_csv('exemplo.csv')
# df.to_csv('exemplo_noindex.csv', index=False)
# df.to_csv('exemplo_noheader.csv', header=False)

# df2 = pd.read_csv('exemplo.csv', index_col=0)
# print(df2)
# df2 = pd.read_csv('exemplo_noindex.csv')
# print(df2)
df2 = pd.read_csv('exemplo_noheader.csv', index_col=0, header=None)
print(df2)