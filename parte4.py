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
