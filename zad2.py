import math
from random import randint
import arythmethic
import geometry

# zad 1
x = [1 - x for x in range(1, 11)]
print(x)
y = [4 ** i for i in range(8)]
print(y)
z = [x for x in y if x % 2 == 0]
print(z)

# zad 2
lista1 = []
for i in range(10):
    lista1 = randint(0, 50)
lista2 = [i for i in lista1 if i % 2 == 0]
print(lista2)

# zad 3
prod = {"buraki": "kg", "chleb":  "szt", "woda": "litry", "mąka": "kg"}
sear = [key for key, value in prod.items() if value.count("szt")]
print(sear)

# zad 5


def p_trapez(a=3.0, b=2.0, h=2.5):
    surface = 0.5 * (a + b) * h
    return surface


print(p_trapez())

# zad 6


def ciag(g=1, h=4, ile=10):
    k = []
    if ile <= 0:
        print("err")
        return 0
    elif ile == 1:
        return g*h
    else:
        for x in range(ile):
            l = l * (g + h * x)
            k.append(l)
        return k


print(ciag())

# zad 7


def fun(* arg):
    if len(arg) == 0:
        return 0
    wynik = arg[0]
    for i in arg:
        wynik *= i
    return wynik


print(fun(1, 2, 3, 4, 5))

# zad 8


def produkty(**items):
    ile_produktow = len(items.keys())
    wartosc = sum(items.values())
    return ile_produktow, wartosc


x = produkty(papier=3.5, cukier=10, czekolada=5, baton=2, chleb=3.5)
print(x)

# zad 9
print(arythmethic.nx(1, 3, 1))
print((arythmethic.suma_n(9, 8, 7)))
print(geometry.nx(7, 14, 7))
print((geometry.suma_n(2, 7, 3)))

# zad 11
plik = open("przedział.py", "r+")
wiersze = plik.readlines()
print(wiersze)