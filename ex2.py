def sublista(l, s):
    sub_set = False
    if s == []:
        sub_set = True
    elif s == l:
        sub_set = True
    elif len(s) > len(l):
        sub_set = False
    else:
        for i in range(len(l)):
            if l[i] == s[0]:
                n = 1
                while (n < len(s)) and (l[i+n] == s[n]):
                    n += 1
                if n == len(s):
                    sub_set = True
    return sub_set

def segundo_maior(numeros):
    if len(numeros) < 2:
        return -1
    fst = -1
    scd = -1
    for n in numeros:
        if n > fst:
            scd = fst
            fst = n
        elif n > scd:
            scd = n
    return scd

def lista2dic(lista):
    tmp = {}
    dic = tmp
    for nome in lista:
        tmp[nome] = {}
        tmp = tmp[nome]
    return dic


if __name__ == '__main__':
    a = [2,4,3,5,7]
    b = [4,3]
    c = [3,7]
    print(sublista(a, b))
    print(sublista(a, c))
    print(segundo_maior([4, 6, 5, 1, 9]))
    print(lista2dic([4, 6, 5, 1, 9]))
