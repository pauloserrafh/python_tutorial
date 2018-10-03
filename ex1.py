def prob1():
    for x in range(30):
        if not x % 9:
            continue
        print(x)

def prob2():
    n=5
    for i in range(n):
        for j in range(i):
            print ('* ', end="")
        print('')

    for i in range(n,0,-1):
        for j in range(i):
            print('* ', end="")
        print('')

def prob3():
    for x in range(1500, 2701):
        if (x%7==0) and (x%5==0):
            print(x)

def prob4():
    while(True):
        print("Hello, World!")
        for i in range(1000000):
            pass

if __name__ == '__main__':
    prob1()
    prob2()
    prob3()
    prob4()
