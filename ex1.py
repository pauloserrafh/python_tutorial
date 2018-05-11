def div9():
    for x in range(30):
        if not x % 9:
            continue
        print(x)

def desenha():
    n=5;
    for i in range(n):
        for j in range(i):
            print ('* ', end="")
        print('')

    for i in range(n,0,-1):
        for j in range(i):
            print('* ', end="")
        print('')

def div7mul5():
    for x in range(1500, 2701):
        if (x%7==0) and (x%5==0):
            print(x)

def loop():
    while(True):
        print("Hello, World!")
        for i in range(1000000):
            pass

if __name__ == '__main__':
    div9()
    desenha()
    div7mul5()
    loop()
