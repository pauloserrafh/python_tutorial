def prob1(x):
    # Inverte string usando slicing
    rev = x[::-1]
    if x != rev:
        return False
    return True

def prob2(st):
    if len(st) < 2:
        return ""
    return st[0:2] + st[-2:]

def prob3(tp):
    return (tp[2],tp[-5])

def prob4(lista):
    if not lista:
        print("Lista vazia")
    else:
        print("Lista contem ao menos um elemento")

def prob5(lista):
    return "".join(lista)

def prob6_1(numeros):
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

def prob6_2(numeros):
    if(len(numeros) < 2):
        return -1
    numeros.sort(reverse=True)
    return(numeros[1])

def prob7_1(dic):
    for chave in dic.keys():
        if chave == "teste":
            print("O valor da chave teste é %(teste)s" %dic)
            break
    else:
        print("Chave não encontrada")

def prob7_2(dic):
    if "teste" in dic.keys():
        print("O valor da chave teste é %(teste)s" %dic)
    else:
        print("Chave não encontrada")

def prob7_3(dic):
    if "teste" in dic:
        print("O valor da chave teste é %(teste)s" %dic)
    else:
         print("Chave não encontrada")

if __name__ == '__main__':
    # print(prob1("arara"))
    # print(prob2("asdzxc"))
    # print(prob3((1,2,3,4,5,6)))
    # prob4([])
    # print(prob5(['p','y','t','h','o','n']))
    # print(prob6_1([4, 6, 5, 1, 9]))
    # print(prob6_2([4, 6, 5, 1, 9]))
    d = {'Debian': 'apt-get',
        'Ubuntu': 'apt-get',
        'Fedora': 'dnf',
        'CentOS': 'yum',
        'OpenSUSE': 'zypper',
        'Arch': 'pacman',
        'Gentoo': 'emerge',
        'teste': 'encontrado'
    }
    # prob7_1(d)
    prob7_2(d)
    prob7_3(d)
