def create_insert_file():
    id = open("id.txt", "r")
    miasto  = open("miasto.txt", "r")
    ulica = open("ulica.txt", "r")
    nr_bloku = open("nr_bloku.txt", "r")
    id_table = id.readlines()
    miastotable = miasto.readlines()
    ulica_table = ulica.readlines()
    nr_bloku = nr_bloku.readlines()
    adres = open("adresy.sql", "w")

    for i in range(2500):
        adres.write("insert into ADRESY values (" + "\'" + id_table[i].strip() + "\'" + ", "
                     + "\'" + miastotable[i].strip() + "\'" + ", "
                     + "\'" + ulica_table[i].strip() + "\'" + ", "
                     + "\'" + nr_bloku[i].strip() + "\'"
                     + ");\n")


create_insert_file()