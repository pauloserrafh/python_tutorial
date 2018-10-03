# print("Hello, World!")

# print(2 and 4)
# print(2 & 4)
# print(not 2)
# print(~2)
# print("Hello" not in "Hello, World")


######################################################
# Condicionais
######################################################
# hello = "Hello"
# world = "World"
# numero1 = 1
# numero2 = 1

# if hello == world:
#     print("Palavras Iguais")
# elif numero1 == numero2:
#     print("Numeros Iguais")
# else:
#     print("Tudo diferente")

# if __name__ == '__main__':
#     print("Hello, World!")
# print("Teste")
# print(__name__)


######################################################
# While
######################################################
# i = 0
# while i < 5:
#     print(i)
#     i += 1
#     if(i==3):
#         print("Break")
#         break
# else:
#     print("i na saida %d" % i)


######################################################
# For
######################################################
# for i in range(1,10):
#     print(i)
# else:
#     print("i na saida %d" % i)


######################################################
# break
######################################################
# i = 0
# while True:
#     if i > 10:
#         break
#     print(i)
#     i += 1

######################################################
# continue
######################################################
# i = 0
# while i < 10 :
#     i += 1
#     if i == 5:
#         continue
#     print(i)
    # i += 1 #Inserindo o contador aqui, causamos um loop infinito

######################################################
# pass
######################################################
i = 0
while i < 10:
    if (i >= 0 and i <= 3):
        print(i)
    elif (i >= 5 and i <= 6):
        print(2*i)
    else:
        # Aqui vai ser chamada uma funcao qualquer que ainda nao foi implementada
        pass
    i += 1
