import pandas as pd
import numpy as np

exam_data  = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
    'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
    'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
    'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}

def prob1():
    ds = pd.Series([2, 4, 6, 8, 10])
    print(ds)
    print(type(ds))
    conv = ds.tolist()
    print(conv)
    print(type(conv))

def prob2():
    ds1 = pd.Series([2, 4, 6, 8, 10])
    ds2 = pd.Series([1, 3, 5, 7, 10])
    print("Soma:")
    print(ds1 + ds2)
    print("Subtração:")
    print(ds1 - ds2)
    print("Maior que:")
    print(ds1 > ds2)

def prob3():
    df = pd.DataFrame(exam_data)
    print('Data Frame')
    print(df)
    print('Media Score:')
    print(df['score'].mean())
    print('Media Tentativas:')
    print(df['attempts'].mean())
    print('Tentaram mais de 1 vez:')
    print(df[(df['attempts'] > 1) & (df['qualify'] == 'no')])

def prob4_5():
    df = pd.DataFrame(exam_data)
    value = {"name" : "Suresh", "score": 15.5, "attempts": 1, "qualify": "yes"}
    df2 = df.append(value, ignore_index=True)
    print(df2)
    df2.to_csv('newData.csv', index=False)

def prob6():
    df = pd.read_csv('final.csv')
    ratio = []
    for index, row in df.iterrows():
        rt = row['score']/row['attempts']
        ratio.append(rt)
    df['ratio'] = ratio

    maximo = df["ratio"].max()
    minimo = df["ratio"].min()
    print("Maior ratio:")
    print(df[df["ratio"] == maximo])
    print("Menor ratio:")
    print(df[df["ratio"] == minimo])

    df = df.sort_values(by=['ratio'], ascending=[False])

    df.to_csv('final_update.csv',index=False)

if __name__ == '__main__':
    prob1()
    prob2()
    prob3()
    prob4_5()
    prob6()