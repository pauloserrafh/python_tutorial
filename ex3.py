def combinacoes():
    lowercase = 'abcdefghijklmnopqrstuvwxyz'
    digits = '0123456789'
    lista = [a+b+c+d for a in lowercase for b in lowercase for c in digits
            for d in digits]
    print(lista[:50])

def vetor():
    array = [[['*' for col in range(6)] for col in range(4)]
            for row in range(3)]
    print(array)

def grt(entrada):
    if entrada[0] > 4:
        print ("%d tem valor %s" %(entrada[0], entrada[1]))

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
    combinacoes()
    vetor()
    my_func = lambda tp : (tp[2],tp[-5])
    print(my_func((1,2,3,4,5,6)))
    list(map(grt,d.items()))
