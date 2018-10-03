import datetime as dt
import time
# import numpy as np

def converte():
    date_obj = dt.datetime.strptime('2016/05/12', '%Y/%m/%d')
    print(date_obj)

    now = dt.datetime.now()
    # Make a note of the date and time in a string
    # Date and time in string : 2016-11-05 11:24:24 PM

    # errado = "String " + str(now)
    # print(errado)

    # datestr = "String " + now.strftime("%Y-%m-%d %H:%M:%S %p")
    datestr = "String " + now.strftime("%Y-%m-%d")
    print(datestr)

def segundas():
    monday1 = 0
    months = range(1,13)
    for year in range(2015, 2017):
        for month in months:
            if dt.datetime(year, month, 1).weekday() == 0:
                monday1 += 1
    print(monday1)

def inverte(entrada, saida):
    with open(entrada) as f:
        array = []
        valor = int(f.readline())
        while (valor != '\n' and valor != ''):
            array.append(int(valor))
            valor = f.readline()
    inv = array[::-1]
    with open(saida,'w') as out:
        out.write(str(array)+'\n')
        out.write(str(inv)+'\n')

def to_array():
    my_list = [1, 2, 3, 4, 5, 6, 7, 8]
    print("List to array: ")
    print(np.asarray(my_list))
    my_tuple = ([8, 4, 6], [1, 2, 3])
    print("Tuple to array: ")
    print(np.asarray(my_tuple))

def soma():
    x = np.zeros((5,5))
    x += np.arange(5)
    print(x)

def multiplos():
    x = np.arange(1, 100)
    # find  multiple of 3 or 5
    n= x[(x % 3 == 0) | (x % 5 == 0)]
    print(n)
    # print sum the numbers
    print(n.sum())
    total = 0
    for valor in n:
        total += valor
    print(total)

def uniqueElements():
    x = np.array([10, 10, 20, 20, 30, 30])
    print("Original array:")
    print(x)
    print("Unique elements of the above array:")
    print(np.unique(x))
    x = np.array([[1, 1], [2, 3]])
    print("Original array:")
    print(x)
    print("Unique elements of the above array:")
    print(np.unique(x))

def repetidos():
    array1 = np.array([0, 10, 20, 40, 60])
    print("Array1: ",array1)
    array2 = [10, 30, 40]
    print("Array2: ",array2)
    print("Common values between two arrays:")
    print(np.intersect1d(array1, array2))


if __name__ == '__main__':
    # array = np.arange(10)**3
    converte()
    # segundas()
    # print(array)
    # inverte('inverte.txt','invertido.txt')
    # to_array()
    # soma()
    # multiplos()
