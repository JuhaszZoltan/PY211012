print('az a szöveg, amit kiír a terminálra')

szoveges_valtozo = 'szöveges változó'
egesz_valtozo = 100
lebegopontos_valtozo = 3.14
logika_valtozo = True # vagy False

# operátorok szövegen:

# összefűzés (konkatenáció)
valami = 'krumplis' + 'zsák'
# op: 'krumpliszsák'

# iteratív összefűzés/konkatenáció (CSAK Python)
valami = 'krumpli ' * 3
# op: 'krumpli krumpli krumpli '

# operátorok számokon:
valami = 10 +  3
valami = 10 *  3
valami = 10 -  3
valami = 10 /  3  # op: 3.3333..  hagyományos osztás
valami = 10 // 3  # op: 3         egész osztás
valami = 10 %  3  # op: 1         maradékképzés
valami += 10      # a 'valami' n. változó értékét megnöveli 10el (increment)
valami -= 10      # -||- csökkenti 10el (decrement)
                    # működik a többivel is: *=, /=, 

# logikai  és (konjukció): akkor igaz, ha mindkettő igaz
valami = True and False 

# logika vagy (diszjunkció): akkor igaz, ha valamelyik igaz
valami = True or  False 

# nem egyenlő, kizáró vagy (antivalencia) : akkor igaz, ha nem egyforma
valami = True !=  False 

# egyenló (ekvivalencia): akkor igaz, ha egyforma
valami = True ==  False

# tagadás (negáció), egy operandusú: az ellenkezője lesz
valami = not True


# összehasonlító (compare) operátorok:
# >; <; <=; >= (és NEM =>!!!)

# programozási vezérlők:
feltetel = True

# elágazások

# egyágú:
if feltetel:
    print('ez csak akkor fut le, ha a feltétel igaz')

# kétágú:
if feltetel:
    print('ez akkor fut le, ha a feltétel igaz')
else:
    print('ez akkor fut le, ha a feltétel hamis')

feltetel_1 = False 
feltetel_2 = False
feltetel_3 = False

# N-ágú:
if feltetel_1:
    print('1. ág')
else:
    if feltetel_2:
        print('2. ág')
    else:
        if feltetel_3:
            print('3. ág')
    # .....
        else:
            print('4. ág')

# ha, az 'else' ágat azonnal 'if' követi, akkor összevonható...
if feltetel_1:
    print('1. ág')
elif feltetel_2:
    print('2. ág')
elif feltetel_3:
    print('3. ág')
# .....
else:
    print('4. ág')
#... és így "szebb" (de amúgy ugyan azt csinálja)

# mgj: ha a blokk egyetlen szekvenciából áll, akkon
#      nem szükséges sortörést + indentációt tenni:
if   feltetel_1: print('1. ág')
elif feltetel_2: print('2. ág')
elif feltetel_3: print('3. ág')
# .....
else:            print('4. ág')
# és így "még szebb"

# ciklusok:

import random
# tesztelő:
while(feltetel):
    print('ez a sor addig ismétlődik, amíg a feltétel igaz')
    # ez a sor csak azért van itt, 
    # hogy ne hagyjuk a példát "végtelen" cikliusban:
    if random.randrange(10) == 0: feltetel = False

# számláló (bejáró):
adatszerkezet = range(10)
for x in adatszerkezet:
    print('minden iterációban az "X"')
    print('az adatszerkezet sornkövetkező elemének')
    print('értékét fogja felvenni')

# alapból nem tud "mindent" a nyelv
# vannak bizonyos ún. lib-ek,
# amik beemelését külön jeleznünk kell, pl:

import math    # matekkal kapcsolatos dolgok
import random  # random számok előáűllításával kapcsolatos dolgok
import time    # valós idővel kapcsolatos függvények
import os      # operációs rendszerrel kapcsolatos utasítások

# math:
# hatványozás
alap = 10
kitevo = 3
eredmeny = math.pow(alap, kitevo)
# négyzetgyök
eredmeny = math.sqrt(16)
# PI értéke:
pi_erteke = math.pi

# random:
a = 10
b = 30
# egész szám, zárt-ZÁRT intervallumból [10;30]:
veletlen = random.randint(a, b)
# egész szám zárt-NYÍLT intervallumból [10;30):
veletlen = random.randrange(a, b)
# lebegőpontos szám 0 és 1 között:
veletlen = random.random()

# -----
# várjon s másodpercig, mielőtt folytatódna a program:
s = 3
time.sleep(s)

# terminál törlése:
os.system('cls') # vagy linux-on os.system('clear')

# egyéb dolgok:

# [10; 20)on belülö egész számok listáját adja vissza:
lista = range(10, 20)
# [0, 10)on belüli egész számok listája:
lista = range(10)
# [0, 10)on belül az egész számok listája 2esével:
lista = range(0, 10, 2)

# formázott kiírás:
valtozo = "cica"
print(f'{valtozo} ', end=' ')
# - f betű a string előtt
# - {}-ek közt tudok változóra hivatkozni 
# - ebben az esetben a változó értéke jelenik majd meg a kiírásba
# - + paraméter: end=' ': a kiírás végén a "sortörést" (\n) szóközre cseréli
#   (tehát a köv. print még ugyan abban a sorban lesz kiírva)

# változó BEOLVASÁSA terminálról:
valtozo = input()
# lehet benne szöveg, amit kiír az input előtt:
valtozo = input('a változó értéke: ')
# a Python ún. "ducktype" nyelv, tehát ha SZÁMOT szeretnék beolvasni
# akkor át kell alakítanom az inputot:
egesz_szam = int(input('egész szám: '))
lebegopontos_szam = float(input('lebegőpontos szám: '))
# mgj: CSAK a magyarban van tizedes VESSZŐ (3,14),
# szóval itt mindenhol tizedes"pontot" kell használnunk a gyakorlatban (3.14)