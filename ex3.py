def prob1():
    lowercase = 'abcdefghijklmnopqrstuvwxyz'
    digits = '0123456789'
    lista = [a+b+c+d for a in lowercase for b in lowercase for c in digits
            for d in digits]
    print(lista[:50])

def prob2():
    array = [[['*' for col in range(6)] for col in range(4)]
            for row in range(3)]
    print(array)

def grt(entrada):
    if entrada[0] > 4:
        print ("%d tem valor %s" %(entrada[0], entrada[1]))

def prob4(d):
    list(map(grt,d.items()))

def prob5():
    x = {'key1': 1, 'key2': 1, 'key3': 2}
    y = {'key1': 1, 'key2': 2}
    for (key, value) in set(x.items()) & set(y.items()):
        print('%s: %s Está presente em ambos os dicionários' % (key, value))

if __name__ == '__main__':
    d = {8: 'apt-get',
    7: 'apt-get',
    6: 'dnf',
    5: 'yum',
    4: 'zypper',
    3: 'pacman',
    2: 'emerge',
    1: 'encontrado'
    }
    prob1()
    prob2()
    prob3 = lambda tp : (tp[2],tp[-5])
    print(prob3((1,2,3,4,5,6)))
    prob4(d)
    prob5()
