import math
import sys as system

# zad 1

i1 = int(10)
i2 = int(1.2)
print(i1, i2)

f1 = float(21.37)
f2 = float(10)
print(f1, f2)

s1 = 'sznurek'
s2 = 'XD'
print(s1, s2)

x = 2 + 2j
y = 33 + 3j
z = 35 + 5j
print(f"{x} + {y} = {z}")

# zad 2
a = 0
print(a)
a += 2
print(a)
a -= 4
print(a)
a *= 4
print(a)
a /= 3.33
print(a)
a **= 2
print(a)
a %= 5
print(a)

# zad 3
# a)
print((math.e ** 10))
# b)
print(math.log(5 + (math.sin(8)) ** 2) ** 1.6)
# c)
for n in range(3, 55):
    print(n)
# d)
for n in range(4, 80):
    print(n)

# zad 4
imie = 'KACPER'
naziwsko = 'RUZCZYNSKI'

print(imie.capitalize() + ' ' + naziwsko.capitalize())

# zad 5
txt = "Na Na Na (Na Na Na Na Na Na Na Na Na Na Na Na Na) - My Chemical Romance"
cnt = txt.count("na")
print(cnt)

# zad 6
txt2 = "Związek Socjalistycznych Republik Radzieckich"
print(txt2[0] + txt2[8] + txt2[25] + txt2[34])

# zad 7
tx2 = txt2.split()
print(tx2)

# zad 9
string8 = 'str'
float8 = float(3.14)
hex8 = hex(64)
print(string8)
print(float(float8))
print(hex8)

# Zadanie 9
lista = ['darts', 'snooker', 'szachy', 'poker']
lista.reverse()
lista.append('nożna')
lista.append('ręczna')
print(lista)

# Zadanie 10
slownik = {'wyd.': 'wydanie', 't.': 'tom', 'nr': 'numer',
           'red.': 'redakcja', 'wydawn.': 'wydawnictwo', 'tłum.': 'tłumaczenie', }
print(slownik.keys())
print(slownik.values())


# czesc 2


# zad 1
a = input("Wpisz cokolwiek: ")
cnt = a.count("a")
print(f"Wpisałeś litere 'a' {cnt} razy")

# zad 2
system.stdout.write("Wpisz pierwszą liczbę całkowitą: ")
b = system.stdin.readline()
system.stdout.write("Wpisz drugą liczbę całkowitą: ")
c = system.stdin.readline()
system.stdout.write("Wpisz trzecią liczbę całkowitą: ")
d = system.stdin.readline()
e = int(b) ** int(c) + int(d)
print("Wynik: " + str(e))

# zad 3
f = input("Wpisz liczbę całkowitą f: ")
g = input("Wpisz drugą liczbę całkowitą g: ")
h = input("Wpisz trzecią liczbę całkowitą h: ")
f = int(f)
g = int(g)
h = int(h)
if (f > g) & (f > h):
    print("Liczba f jest największa")
elif (g > f) & (g > h):
    print("Liczba g jest największa")
else:
    print("Liczba h jest największa")

# zad 4
lista =[float(2.2), int(3.3), int(4), int(5)]
for i in range(len(lista)):
    lista[i] = lista[i] ** 2
    print(lista[i])

# zad 5
lista2 = []
x = 0

while x < 10:
    k = input("Podaj liczbę: ")
    if int(k) % 2 == 0:
        lista2.append(k)
    x += 1

print("Liczby parzyste:")
print(lista2)
