import numpy as np

def prob1():
    my_list = [1, 2, 3, 4, 5, 6, 7, 8]
    print("List to array: ")
    print(np.asarray(my_list))
    my_tuple = ([8, 4, 6], [1, 2, 3])
    print("Tuple to array: ")
    print(np.asarray(my_tuple))

def prob2():
    x = np.zeros((5,5))
    x += np.arange(5)
    print(x)
    with open("ex5prob2.txt", mode = 'w', encoding = 'utf-8') as f:
        f.write(str(x))

def prob3():
    x = np.arange(1, 100)
    # find  multiple of 3 or 5
    n= x[(x % 3 == 0) | (x % 5 == 0)]
    print(n)
    # print sum the numbers
    print(n.sum())
    total = 0
    for valor in n:
        total += valor
    print(total)

def prob4():
    x = np.array([10, 10, 20, 20, 30, 30])
    print("Original array:")
    print(x)
    print("Unique elements of the above array:")
    print(np.unique(x))
    x = np.array([[1, 1], [2, 3]])
    print("Original array:")
    print(x)
    print("Unique elements of the above array:")
    print(np.unique(x))

def prob5():
    array1 = np.array([0, 10, 20, 40, 60])
    print("Array1: ",array1)
    array2 = [10, 30, 40]
    print("Array2: ",array2)
    print("Common values between two arrays:")
    print(np.intersect1d(array1, array2))

if __name__ == '__main__':
    prob1()
    prob2()
    prob3()
    prob4()
    prob5()
