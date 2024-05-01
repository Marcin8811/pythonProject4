class Osoba:
     def __init__(self, xxx, yyy):
         self.imie = xxx
         self.wiek = yyy
     def przedstaw_sie(self):
        print(f"Nazywam sie {self.imie}!")

     def ile_masz_lat(self):
         print(f"Mam lat {self.wiek}.")

     def zmien_imie(self, zzz):
         self.imie = zzz

     def dodaj(self, a, b):
         print(f"Ja {self.imie} twierdzę, że: {a} + {b} = {a + b}")


class Test:

    def odejmij(selfself, c, d):
        return c - d

#Osoba().przedstaw_sie()

marcin = Osoba("Marcin", 35)
marcin.przedstaw_sie()
marcin.ile_masz_lat()

pawel = Osoba("Paweł", 45)
pawel.przedstaw_sie()
pawel.ile_masz_lat()

marcin.zmien_imie("Florian")
marcin.przedstaw_sie()
marcin.dodaj(10,20)
pawel.dodaj(10,20)

print(Test().odejmij(30, 20))

