def create_insert_file():
    id_marki = open("id.txt", "r")
    nazwa = open("marki.txt", "r")
    id_marki_table = id_marki.readlines()
    nazwa_table = nazwa.readlines()
    marki = open("marki.sql", "w")

    for i in range(100):
        marki.write("insert into MARKI values (" + "\'" + id_marki_table[i].strip() + "\'" + ", "
                     + "\'" + nazwa_table[i].strip() + "\'"
                     + ");\n")


create_insert_file()