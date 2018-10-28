from faker import Factory

fake = Factory.create('pl_PL')
a = "dadad"
pesel = open("pesel.txt", "r")
peseltable = pesel.readlines()
for i in range(1000):
    print("insert into KLIENCI values (" + "\'" + peseltable[i].strip() + "\'" + ")")