# set
# Create a set
num_set = set([0, 1, 2, 3, 4, 5])
for n in num_set:
    print(n)

# Cria frozenset
# x = frozenset([1, 2, 3, 4, 5])
# y = frozenset([3, 4, 5, 6, 7])
#use isdisjoint(). Return True if the set has no elements in common with other.
# print(x.isdisjoint(y))
#use difference(). Return a new set with elements in the set that are not in the others.
# print(x.difference(y))
#new set with elements from both x and y
# print(x | y)


# # map
# people = ['Dr. Christopher Brooks', 'Dr. Kevyn Collins-Thompson',
#             'Dr. VG Vinod Vydiswaran', 'Dr. Daniel Romero']

# def split_title_and_name(person):
#     p = person.split(" ")
#     return p[0] + " " + p[2]

# list(map(split_title_and_name, people))


# # lambda
# people = ['Dr. Christopher Brooks', 'Dr. Kevyn Collins-Thompson', 'Dr. VG Vinod Vydiswaran', 'Dr. Daniel Romero']

# def split_title_and_name(person):
#     return person.split()[0] + ' ' + person.split()[-1]

# #option 1
# for person in people:
#     my_func = lambda person:person.split()[0] + ' ' + person.split()[-1]
#     print(split_title_and_name(person) == (my_func(person)))

# # for person in people:
# #     print(split_title_and_name(person) == (lambda x: x.split()[0] + ' ' + x.split()[-1])(person))


# #option 2
# list(map(split_title_and_name, people)) == list(map(lambda person : person.split()[0] + ' ' + person.split()[-1], people))


# comprehension
# lista = []
# for n in range(0,1000):
#     if n % 2 == 0:
#         lista.append(n)
# print(lista)

# lista2 = [n for n in range(0,1000) if n % 2 == 0]
# print(lista2)

# print(lista2 == lista)


# def times_tables():
#     lst = []
#     for i in range(10):
#         for j in range (10):
#             lst.append(i*j)
#     return lst

# times_tables() == [(i*j) for i in range(10) for j in range(10)]

# t = [(i*j) for i in range(10) for j in range(10)]
