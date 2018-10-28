def create_insert_file():
    nr_karty = open("nr_karty.txt", "r")
    data  = open("data_wygasniecia.txt", "r")
    CVV = open("CVV.txt", "r")
    FK_klient = open("pesel.txt", "r")
    karta_table = nr_karty.readlines()
    date_table = data.readlines()
    cvv_table = CVV.readlines()
    FK_klient_table = FK_klient.readlines()
    karta = open("karty.sql", "w")

    for i in range(2500):
        karta.write("insert into KARTY values (" + "\'" + karta_table[i].strip() + "\'" + ", "
                     + "\'" + date_table[i].strip() + "\'" + ", "
                     + "\'" + cvv_table[i].strip() + "\'" + ", "
                     + "\'" + FK_klient_table[i].strip() + "\'"
                     + ");\n")


create_insert_file()