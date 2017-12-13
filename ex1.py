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


if __name__ == '__main__':
    print(is_palindrome("arara"))
    print(concat_ends("asdzxc"))
