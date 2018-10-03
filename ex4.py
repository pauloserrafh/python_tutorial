import datetime as dt
import time

def prob1():
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

def prob2():
    monday1 = 0
    months = range(1,13)
    for year in range(2015, 2017):
        for month in months:
            if dt.datetime(year, month, 1).weekday() == 0:
                monday1 += 1
    print(monday1)

def prob3(entrada, saida):
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

if __name__ == '__main__':
    prob1()
    prob2()
    prob3('inverte.txt','invertido.txt')
