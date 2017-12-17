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

# print("Baseado na sua distro, você deve usar %(Ubuntu)s, %(Fedora)s,\
#     %(CentOS)s, %(OpenSUSE)s, %(Arch)s ou %(Gentoo)s" % distro_install_command)

######################################################
# # While
######################################################
# i = 0
# while i < 5:
#     print(i)
#     i += 1
# else:
#     print("i na saida %d" % i)

######################################################
# # For
######################################################
# for i in range(1,10):
#     print(i)
# else:
#     print("i na saida %d" % i)

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

######################################################
# # break
######################################################
# for distro in linux_distros:
#     if distro == "Ubuntu":
#         print("É uma distro válida")
#         break
# else:
#     print("Toda a lista foi percorrida. Não é uma distro válida")

# i = 0
# while True:
#     if i > 10:
#         break
#     print(i)
#     i += 1

######################################################
# continue
######################################################
# linux_distros = ['Debian', 'Ubuntu', 'Fedora', 'CentOS', 'OpenSUSE',
#                     'Arch', 'Gentoo']
# for distro in linux_distros:
#     if distro == "Ubuntu":
#         continue
#     print(distro)
# else:
#     print("Toda a lista foi percorrida.")

# i = 0
# while i < 10 :
#     i += 1
#     if i == 5:
#         continue
#     print(i)
#     # i += 1 #Inserindo o contador aqui, causamos um loop infinito

######################################################
# pass
######################################################
# i = 0
# while i < 10:
#     if (i >= 0 and i <= 3):
#         print(i)
#     elif (i >= 5 and i <= 6):
#         print(2*i)
#     else:
#         # Aqui vai ser chamada uma funcao qualquer que ainda não foi implementada
#         pass
#     i += 1

