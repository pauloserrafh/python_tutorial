print("Hello, World!")

######################################################
# Funções
######################################################
# def minha_soma(a, b):
#     return a+b

# def calculadora(a, b):
#     return a+b,a-b

# def parametro_nomeado(a = "Paulo"):
#     print(a)

# if __name__ == '__main__':
#     print("Hello, World!")
#     print(minha_soma(1,2))
#     print(calculadora(1,2))
#     parametro_nomeado()
#     parametro_nomeado("Serra")
# else:
#     print("Estou sendo importado")

######################################################
# Strings
######################################################
# print("Hello," + " " + "World!")

# print("Numero" + 2) # ERRO
# print("Numero" + str(2))


# st = "World!"
# valor = 2
# print("Hello, " + st)
# print("Hello, %s %d" % (st, valor))


# # Slicing
# st = "Hello, World!"
# print(type(st))
# # print(st[0])
# # print(st[-1])
# # print(st[:3])
# # print(st[-4:-2])
# print(st[::2])

# # print(len(st))
# # print(st.find("World!"))
# print(st.replace("World", "Everybody"))

######################################################
# # Listas
######################################################
# linux_distros = ['Debian', 'Ubuntu', 'Fedora', 'CentOS', 'OpenSUSE',
#                     'Arch', 'Gentoo']
# print(type(linux_distros))
# debian_distros = linux_distros[:2]
# linux_distros.append("Mint")
# print(linux_distros)
# print(linux_distros.pop())
# linux_distros.insert(2, "Mint")
# print(linux_distros)
# linux_distros.remove("Arch")
# print(linux_distros)

######################################################
# # Tuplas
######################################################
# tp = ('Bacon', 7, True, 11, 'Your mother was a hamster!')
# print(type(tp))
# print(tp[1])
# print(tp[-1])
# print(len(tp))

######################################################
# # Condicionais
######################################################
# nome1 = "Ai"
# nome2 = "Ui"

# if nome1[0] == nome2[0]:
#     print("Primeira letra igual")
# elif nome1[1] == nome2[1]:
#     print("Pelo menos a segunda letra é igual")
# else:
#     print("Tudo diferente")
