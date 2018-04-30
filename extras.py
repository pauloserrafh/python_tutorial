import numpy as np

######################################################
# Questoes numpy
######################################################
def bordas():
    x = np.ones((3,3))
    print(x)
    x = np.pad(x, pad_width=1, mode='constant', constant_values=0)
    print(x)

def maior_que(val):
    x = np.array([[0, 10, 20], [20, 30, 40]])
    print(x)
    print("Valores maiores que 10 =", x[x>val])

def ordena():
    a = np.array([[4, 6],[2, 1]])
    print("Original array: ")
    print(a)
    print("Sort along the first axis: ")
    x = np.sort(a, axis=0)
    print(x)
    print("Sort along the last axis: ")
    y = np.sort(x, axis=1)
    print(y)

def divide():
    x = np.arange(1, 15)
    print("Original array:",x)
    print("After splitting:")
    print(np.split(x, [2, 6]))

def continuo():
    x = np.array([[10, 20, 30], [20, 40, 50]])
    print("Original array:")
    print(x)
    y = np.ravel(x)
    print("New flattened array:")
    print(y)

def maior_menor():
    x = np.array([1, 2, 3, 4, 5, 6])
    print("Original array: ",x)
    print("Maximum Values: ",x[np.argmax(x)])
    print("Minimum Values: ",x[np.argmin(x)])

def concatena():
    a = np.array([[0, 1, 3], [5, 7, 9]])
    b = np.array([[0, 2, 4], [6, 8, 10]])
    c = np.concatenate((a, b), 1)
    print(c)

######################################################
# questoes String
######################################################
def divide_delimitador():
    str1 = "w,3,r,e,s,o,u,r,c,e"
    print(str1.rsplit(',', 1))
    print(str1.rsplit(',', 2))
    print(str1.rsplit(',', 5))

def vowel(text):
    vowels = "aeiuoAEIOU"
    print(len([letter for letter in text if letter in vowels]))
    print([letter for letter in text if letter in vowels])

def strip_chars(str, chars):
    return "".join(c for c in str if c not in chars)

def reverse_string_words(text):
    for line in text.split('\n'):
        return(' '.join(line.split()[::-1]))

def conta_ocorrencias(str1, sub):
    print(str1.count(sub))

######################################################
# Questoes listas
######################################################
def last(n): return n[-1]

def sort_list_last(tuples):
  return sorted(tuples, key=last)

def long_words(n, str):
    word_len = []
    txt = str.split(" ")
    for x in txt:
        if len(x) > n:
            word_len.append(x)
    return word_len

def common_data(list1, list2):
     result = False
     for x in list1:
         for y in list2:
             if x == y:
                 result = True
                 break
     return result

def inteiro():
    L = [11, 33, 50]
    print("Original List: ",L)
    x = int("".join(map(str, L)))
    print("Single Integer: ",x)

if __name__ == '__main__':
    bordas()
    # maior_que(10)
    # ordena()
    # divide()
    # continuo()
    # maior_menor()
    # concatena()
    # vowel('Paulo');
    # print(strip_chars("The quick brown fox jumps over the lazy dog.", "aeiou"))
    # print(reverse_string_words("The quick brown fox jumps over the lazy dog."))
    # print(reverse_string_words("Python Exercises."))
    # conta_ocorrencias("The quick brown fox jumps over the lazy dog.","e")
    # print(sort_list_last([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]))
    # print(long_words(3, "The quick brown fox jumps over the lazy dog"))
    # print(common_data([1,2,3,4,5], [5,6,7,8,9]))
    # inteiro()
