from faker import Factory
import random
fake = Factory.create('pl_PL')

indeksy = []
tupla = ()
lista = list(tupla)
lista2 = []
for i in range(2500):
    indeksy.append(str(i))
for x in indeksy:
    lista.append(x)

tupla = tuple(lista)
for i in range(100):
    lista2.append(fake.random_elements(elements=tupla, length=2, unique=True))
    print(lista2[i])
    print(lista2[i][0])