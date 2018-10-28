from faker import Factory
fake = Factory.create('pl_PL')


def create_insert_file():
    id = open("id.txt", "r")
    adres_start_i_koniec = []
    id_table = id.readlines()
    marki = open("trasy.sql", "w")
    indeksy = []
    tupla = ()
    lista = list(tupla)
    for i in range(2500):
        indeksy.append(str(i))
    for x in indeksy:
        lista.append(x)

    tupla = tuple(lista)



    for i in range(10000):
        adres_start_i_koniec.append(fake.random_elements(elements=tupla, length=2, unique=True))
        marki.write("insert into TRASY values (" + "\'" + str(i) + "\'" + ", "
                     + "\'" + adres_start_i_koniec[i][0] + "\'" + ", "
                     + "\'" + adres_start_i_koniec[i][1] + "\'"
                     + ");\n")


create_insert_file()