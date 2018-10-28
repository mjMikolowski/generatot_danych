CREATE TABLE KLIENCI(
pesel bigint NOT NULL,
imie varchar(200),
nazwisko varchar(200),
nr_telefonu bigint,
email varchar(200),
NIP bigint,
PRIMARY KEY (pesel)
);

CREATE TABLE KARTY(
nr_karty bigint NOT NULL,
data_wygasniecia date,
cvv varchar,
FK_klient bigint REFERENCES KLIENCI(pesel),
PRIMARY KEY (nr_karty)
);

CREATE TABLE ADRESY(
ID_adres bigint,
PRIMARY KEY (ID_adres),
miasto varchar,
ulica varchar,
nr_bloku bigint
);

CREATE TABLE TRASY(
ID_trasa bigint,
PRIMARY KEY (ID_trasa),
FK_adres_start bigint REFERENCES ADRESY(ID_adres),
FK_adres_koniec bigint REFERENCES ADRESY(ID_adres)
);

CREATE TABLE MARKI(
ID_marka bigint,
PRIMARY KEY (ID_marka),
nazwa varchar
);

CREATE TABLE SAMOCHODY(
ID_samochod bigint,
PRIMARY KEY (ID_samochod),
model varchar,
nr_rejestracyjny varchar,
FK_marka bigint REFERENCES MARKI(ID_marka),
liczba_miejsc bigint,
klasa varchar
);

CREATE TABLE KIEROWCY(
pesel bigint,
PRIMARY KEY (pesel),
imie varchar,
nazwisko varchar,
nr_telefonu bigint,
nr_prawa_jazdy varchar,
zdjecie_link varchar,
FK_samochod bigint REFERENCES SAMOCHODY(ID_samochod)
);

CREATE TABLE FAKTURY(
nr_faktury varchar,
PRIMARY KEY (nr_faktury),
FK_klient bigint REFERENCES KLIENCI(pesel),
FK_kierowca bigint REFERENCES KIEROWCY(pesel),
FK_trasa bigint REFERENCES TRASY(ID_trasa),
oplata float,
kilometry float,
data_start date,
data_koniec date,
status_platnosci bit
);
