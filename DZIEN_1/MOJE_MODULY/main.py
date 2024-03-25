# import dane
# import dane as dn
from dane import nb as filia
from dane import book as bk
from funkcje.bfunkcje import czytaj_liste,czytaj_slownik
from klasy.cklasa import CDane

#CTRL +D - powielenie linii/bloku tekstu
#CTRL + / - komentowanie/odkomentowanie zaznaczonych linii kodu

print("_______ czytanie ze źródeł danych - bezpośrednie ___________")
print(filia)
print(bk)

print("_______ czytanie pomocą funkcji ___________")
czytaj_liste(filia)
czytaj_slownik(bk)

print("_______ czytanie pomocą obiektu ___________")
cd = CDane(filia,bk)
cd.czytajl()
cd.czytajs()
