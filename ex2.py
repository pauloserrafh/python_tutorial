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

def segundo_maior2(numeros):
    if(len(numeros) < 2):
        return -1
    numeros.sort(reverse=True)
    return(numeros[1])

def find_key(dic):
    chaves = dic.keys()
    for chave in chaves:
        if chave == "teste":
            print("O valor da chave teste é %(teste)s" %dic)
            break
    else:
        print("Chave não encontrada")


def is_palindrome(x):
    # Inverte string usando slicing
    rev = x[::-1]
    if x != rev:
        return False
    return True

def concat_ends(st):
    if len(st) < 2:
        return ""
    return st[0:2] + st[-2:]

def print_tupla(tp):
    return (tp[2],tp[-5])

def lista_vazia(lista):
    if not lista:
        print("Lista vazia")
    else:
        print("Lista contem ao menos um elemento")

def lista2string(lista):
    return "".join(lista)

if __name__ == '__main__':
    # print(is_palindrome("arara"))
    # print(concat_ends("asdzxc"))
    # print(print_tupla((1,2,3,4,5,6)))
    # lista_vazia([])
    # print(lista2string(['p','y','t','h','o','n']))
    # print(segundo_maior([4, 6, 5, 1, 9]))
    # print(segundo_maior2([4, 6, 5, 1, 9]))
    # d = {'Debian': 'apt-get',
    #     'Ubuntu': 'apt-get',
    #     'Fedora': 'dnf',
    #     'CentOS': 'yum',
    #     'OpenSUSE': 'zypper',
    #     'Arch': 'pacman',
    #     'Gentoo': 'emerge',
    #     'teste': 'encontrado'
    # }
    # find_key(d)
