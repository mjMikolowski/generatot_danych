import random
def create_insert_file():
    id_samochodu = open("id.txt", "r")
    model = open("model.txt", "r")
    nr_rejes = open("nr_rejestracyjny.txt", "r")
    liczba_miejsc = open("liczba_miejsc.txt", "r")
    klasa = open("klasa.txt", "r")

    id_table = id_samochodu.readlines()
    model_table = model.readlines()
    nr_table = nr_rejes.readlines()
    liczba_miejsc_table = liczba_miejsc.readlines()
    klasa_table = klasa.readlines()

    samochody = open("samochody.sql", "w")

    for i in range(2500):
        FK_marka = random.randint(0, 100)
        samochody.write("insert into SAMOCHODY values (" + "\'" + id_table[i].strip() + "\'" + ", "
                     + "\'" + model_table[i].strip() + "\'" + ", "
                     + "\'" + nr_table[i].strip() + "\'" + ", "
                     + "\'" + str(FK_marka) + "\'" + ", "
                     + "\'" + liczba_miejsc_table[i].strip() + "\'" + ", "
                     + "\'" + klasa_table[i].strip() + "\'"
                     + ");\n")


create_insert_file()