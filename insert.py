def create_insert_file():
    pesel = open("pesel.txt", "r")
    imie  = open("imie.txt", "r")
    nazwisko = open("nazwisko.txt", "r")
    nr_telefonu = open("nr_telefonu.txt", "r")
    email = open("email.txt", "r")
    nip = open("nip.txt", "r")
    klient = open("klient.sql", "w")
    peseltable = pesel.readlines()
    imietable = imie.readlines()
    nazwiskotable = nazwisko.readlines()
    nr_telefonutable = nr_telefonu.readlines()
    emailtable = email.readlines()
    niptable = nip.readlines()

    for i in range(1000):
        klient.write("insert into KLIENCI values (" + "\'" + peseltable[i].strip() + "\'" + ", "
                     + "\'" + imietable[i].strip() + "\'" + ", "
                     + "\'" + nazwiskotable[i].strip() + "\'" + ", "
                     + "\'" + nr_telefonutable[i].strip() + "\'" + ", "
                     + "\'" + emailtable[i].strip() + "\'" + ", "
                     + "\'" + niptable[i].strip() + "\'"
                     + ");\n")


create_insert_file()
