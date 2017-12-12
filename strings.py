####Trabalhando com strings#########
print("Hello," + " " + "World!")

#ERRO
# print("Numero" + 2)
print("Numero" + str(2))


st = "World!"
valor = 2
print("Hello, " + st)
print("Hello, %s %d" %(st, valor))


######Slicing
st = "Hello, World!"
# print(st[0])
# print(st[-1])
# print(st[:3])
# print(st[-4:-2])
print(st[::2])

# print(len(st))
# print(st.find("World!"))
print(st.replace("World","Everybody"))

####Trabalhando com listas#########
linux_distros = ['Debian', 'Ubuntu', 'Fedora', 'CentOS', 'OpenSUSE', 'Arch', 'Gentoo']
debian_distros = linux_distros[:2]
linux_distros.append("Mint")
linux_distros.pop()
linux_distros.insert(2, "Mint")
linux_distros.remove("Arch")

