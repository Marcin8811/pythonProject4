#Utwórz klasę TodoList, która pozwoli na zarządzanie listą do wykonania. Napisz testy jednostkowe.
#       indexy        0    1     2      3
przykladowa_lista = [12, 'abc', 3.14, True]

print(przykladowa_lista) # drukujemy całą liste
print(przykladowa_lista[2]) # drukujemy index 2

przykladowa_lista.append('kolejny element')
print(przykladowa_lista)

przykladowa_lista.append(['inna', 'lista', 4, False])
print(przykladowa_lista)

print(przykladowa_lista[5])
print(przykladowa_lista[5][1])

przykladowa_lista.append('coś jeszcze')
print(przykladowa_lista)
przykladowa_lista[5].append(['kolejna lista', 3423432, 23432, 3465436])
print(przykladowa_lista)
print(przykladowa_lista[5][4])
print(przykladowa_lista[5][4][1])