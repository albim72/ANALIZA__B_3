def czytaj_liste(lista):
    for i,j in enumerate(lista): # i - indeks położzenia elementu w liście, j - wartość elementu
        print(f'Element listy numer: {i+1} -> wartość: {j}')


def czytaj_slownik(slownik):
    for x,y in slownik.items():
        print(f"klucz -> {x}, wartość -> {y}")
