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

def max_dois(x, y):
    if x > y:
        return x
    return y

def max_tres(x, y, z):
    return max_dois(x, max_dois(y, z))

def lista2string(lista):
    return "".join(lista)

if __name__ == '__main__':
    print(is_palindrome("arara"))
    print(concat_ends("asdzxc"))
    print(print_tupla((1,2,3,4,5,6)))
    lista_vazia([])
    print(max_tres(3, 6, -5))
    print(lista2string(['p','y','t','h','o','n']))
