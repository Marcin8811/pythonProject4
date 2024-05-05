def dodaj(a,b):
    return a + b

def odejmi(a,b):
    return a - b

def pomnoz(a,b):
    return a * b

def podziel(a,b):
    if b != 0:
        return a / b
    else:
        return " Nie dzieli się przez zero!"

    #c = a + b
    #return c

#wynik = dodaj(10, 20)
#print(wynik)

print(dodaj(10, 20))
print(odejmi(20, 30))
print(pomnoz(11, 12))
print(podziel(10, 3))
print(podziel(10, 0))