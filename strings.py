# Strings
print("Hello," + " " + "World!")

# print("Numero" + 2) # ERRO
print("Numero" + str(2))


st = "World!"
valor = 2
print("Hello, " + st)
print("Hello, %s %d" % (st, valor))


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

# # Listas
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

# # Tuplas
# tp = ('Bacon', 7, True, 11, 'Your mother was a hamster!')
# print(type(tp))
# print(tp[1])
# print(tp[-1])
# print(len(tp))


# Dicionarios
distro_install_command = {'Debian': 'apt-get',
                        'Ubuntu': 'apt-get',
                        'Fedora': 'dnf',
                        'CentOS': 'yum',
                        'OpenSUSE': 'zypper',
                        'Arch': 'pacman',
                        'Gentoo': 'emerge'
}
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

# # Condicionais
# nome1 = "Ai"
# nome2 = "Ui"

# if nome1[0] == nome2[0]:
#     print("Primeira letra igual")
# elif nome1[1] == nome2[1]:
#     print("Pelo menos a segunda letra é igual")
# else:
#     print("Tudo diferente")
