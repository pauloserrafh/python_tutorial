# # While
# i = 0
# while i < 5:
#     print(i)
#     i += 1
# else:
#     print("i na saida %d" % i)

# # For
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


# # break
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

# continue
linux_distros = ['Debian', 'Ubuntu', 'Fedora', 'CentOS', 'OpenSUSE',
                    'Arch', 'Gentoo']
for distro in linux_distros:
    if distro == "Ubuntu":
        continue
    print(distro)
else:
    print("Toda a lista foi percorrida.")

i = 0
while i < 10 :
    i += 1
    if i == 5:
        continue
    print(i)
    # i += 1


# pass
i = 0
while i < 10:
    if (i >= 0 and i <= 3):
        print(i)
    elif (i >= 5 and i <= 6):
        print(2*i)
    else:
        # Aqui vai ser chamada uma funcao qualquer que ainda não foi implementada
        pass
    i += 1

