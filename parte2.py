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


# Slicing
# st = "Hello, World!"
# print(type(st))
# print(st[0])
# print(st[-1])
# print(st[:3])
# print(st[-4:-2])
# print(st[::2])

# print(len(st))
# print(st.find("World!"))
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


# linux_distros = ['Debian', 'Ubuntu', 'Fedora', 'CentOS', 'OpenSUSE',
#                     'Arch', 'Gentoo']
# for distro in linux_distros:
#     print(distro.upper())
# else:
#     print("Toda a lista foi percorrida")

# number_sets = [[2, 4, 6], [3, 6, 9], [4, 8, 12]]
# square_sets = []
# for number_set in number_sets:
#     square_sets.append([])
#     for number in number_set:
#         print("Numero original %d, numero ao quadrado %d."
#                  % (number, number ** 2))
#         square_sets[number_sets.index(number_set)].append(number ** 2)
# print(number_sets)
# print(square_sets)




# for distro in linux_distros:
#     if distro == "Ubuntu":
#         print("Distro valida")
#         break
# else:
#     print("Toda a lista foi percorrida. Nao eh uma distro valida")


# linux_distros = ['Debian', 'Ubuntu', 'Fedora', 'CentOS', 'OpenSUSE',
#                     'Arch', 'Gentoo']
# for distro in linux_distros:
#     if distro == "Ubuntu":
#         continue
#     print(distro)
# else:
#     print("Toda a lista foi percorrida.")

######################################################
# # Tuplas
######################################################
# tp = ('Bacon', 7, True, 11, 'Your mother was a hamster!')
# print(type(tp))
# print(tp[1])
# print(tp[-1])
# print(len(tp))


######################################################
# Dicionarios
######################################################
# distro_install_command = {'Debian': 'apt-get',
#                         'Ubuntu': 'apt-get',
#                         'Fedora': 'dnf',
#                         'CentOS': 'yum',
#                         'OpenSUSE': 'zypper',
#                         'Arch': 'pacman',
#                         'Gentoo': 'emerge'
# }
# print(distro_install_command['Gentoo'])
# distro_install_command[3] = "Carro"
# distro_install_command["NovoDic"] = {"Um":"valor",
#                                     "pode":"ser",
#                                     "outro":"dicionario"
#                                     }
# print(distro_install_command)
# print(distro_install_command["NovoDic"]["pode"])
# del distro_install_command[3]
# print(distro_install_command)

# distro_install_list = distro_install_command.items()
# print(distro_install_list)
# for distro, command in distro_install_command.items():
#     print("%s usa o comando %s." % (distro, command))

# distro_names = distro_install_command.keys()
# print(distro_names)
# for distro in distro_names:
#     print(distro)

# distro_commands = distro_install_command.values()
# print(distro_commands)
# for command in distro_commands:
#     print(command)

# print("Baseado na sua distro, voce deve usar %(Ubuntu)s, %(Fedora)s,\
#     %(CentOS)s, %(OpenSUSE)s, %(Arch)s ou %(Gentoo)s" % distro_install_command)

######################################################
# Funcoes
######################################################
# def minha_soma(a, b):
#     return a+b

def calculadora(a, b):
    return a+b,a-b

def parametro_nomeado(a = "Paulo"):
    print(a)

def altera_valores(minhaString, minhaLista):
    minhaString = "Nova String"
    print(minhaString)
    minhaLista.append("Novo valor")
    print(minhaLista)

if __name__ == '__main__':
#    print(minha_soma(1,2))
#    print(calculadora(1,2))
#    parametro_nomeado()
#    parametro_nomeado("Serra")

#    s = "String"
#    lst = ["Valor", "Valor"]
#    altera_valores(s, lst)
#    print("Depois da funcao")
#    print(s)
#    print(lst)
# else:
#     print("Estou sendo importado")