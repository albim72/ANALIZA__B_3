print("kolekcje języka Python")
print("1 - lista(list)\n2 - krotka(tuple)\n3 - zbiór(set)\n4 - słownik(dict)")

print("LISTA - kolekcja mutowalna")
miasta = ["Kraków","Lublin","Opole","Gdańsk"]
print(miasta)
print(type(miasta))

print("KROTKA - kolekcja niemutowalna")
liczby = (45,25,7,3,8,25,853,78,7)
print(liczby)
print(type(liczby))

print("zbiór - kolekcja mutowalna, unikatowa, nieuporządkowna")
drzewa = {"dąb","sosna","jesion","buk","sosna","olcha"}
print(drzewa)
print(type(drzewa))

print("słownik - kolekcja mutowalna, uporządkowana, częściowo unikatowa (klucze)")
osoba = {
    "id":53454,
    "imię":"Janek",
    "nazwisko":"Kot",
    "rok urodzenia":1981,
    "miasto":"Toruń",
    "miejsce urodzenia":"Toruń"
}
