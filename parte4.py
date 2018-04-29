######################################################
# classes
######################################################
# class MinhaClasse:
#     helloWorld = "Hello, World!"

#     def __init__(self, nome):
#         self.nome = nome

#     def hello(self):
#         print("Hello, %s" %self.nome)

#     def whoAmI(self):
#         return(self.nome)

#     def batizar(self, novoNome):
#         self.nome = novoNome

# if __name__ =='__main__':
#     obj = MinhaClasse("Paulo")

#     print(obj.helloWorld)

#     meuNome = obj.whoAmI()
#     print("Eu me chamo %s" %(meuNome))

#     obj.hello()

#     obj.batizar("Serra")
#     meuNome = obj.whoAmI()
#     print("Fui batizado como o novo nome: %s" %(meuNome))
#     obj.hello()


######################################################
# arquivos
######################################################
# Abre o arquivo apenas para leitura
# f = open('inverte.txt', 'r')
# print(f.readline())
# print(f.readline())
# print(f.readline())
# print(f.readline())
# print(f.readline())
# print(f.readline())
# f.close()

# Nao precisa fechar o arquivo explicitamente
# with open('inverte.txt') as f:
#     print(f.readlines())


######################################################
# datetime
######################################################
# import datetime

# print(datetime.datetime.now())
# print("Or like this: " ,datetime.datetime.now().strftime("%y-%m-%d-%H-%M"))
# print("Current year: ", datetime.date.today().strftime("%Y"))
# print("Month of year: ", datetime.date.today().strftime("%B"))
# print("Week number of the year: ", datetime.date.today().strftime("%W"))
# print("Weekday of the week: ", datetime.date.today().strftime("%w"))
# print("Day of year: ", datetime.date.today().strftime("%j"))
# print("Day of the month : ", datetime.date.today().strftime("%d"))
# print("Day of week: ", datetime.date.today().strftime("%A"))

# dt = datetime.datetime.now()
# print(dt.year)
# print(dt.microsecond)

# delta = datetime.timedelta(days = 100)
# hj = datetime.date.today()
# diff = hj - delta
# print(diff)


######################################################
# numpy
######################################################
# import numpy

# a = numpy.array([2,3,4])
# print(a)
# print(a.dtype)
# b = numpy.array([1.2, 3.5, 5.1])
# print(b)
# print(b.dtype)

# b = numpy.arange(12).reshape(4,3)
# print(b)

# c = numpy.arange(24).reshape(2,3,4)
# print(c)

# z = numpy.zeros((3,4))
# print(z)

# print(numpy.arange(10, 30, 5))

# print(numpy.linspace( 0, 2, 9 ))

# a = numpy.arange(10)**3
# print(a)
# print(a[2:5])
# a[:6:2] = -1000
# print(a)

# b = numpy.arange(12).reshape(4,3)
# for linha in b:
#     for coluna in linha:
#         print(coluna)

# for valor in b.flat:
#     print(valor)

# a = numpy.arange(10)**3
# b = numpy.arange(10)**2
# print(a)
# print(b)
# print(a+b)
