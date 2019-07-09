zadanie = "\n\n\tZadanie z pracy domowej no."

print(zadanie + "1")
# 1. Przypisz do zmiennej o nazwie float_but_int wartosc dzielenia 50 / 2.
float_but_int = 50/2
print(float_but_int)

# Jakiego typu jest wynik (do sprawdzenia typu type(zmienna))?
print(type(float_but_int))

print(zadanie + "2")
# 2. (Kalkulator, albo Python) - liczba zapisana w systemie binarnym na 8 bitach - 11011010 to w systemie dziesietnym liczba:
print("218")

print(zadanie + "3")
#3. Przypisz do 3 zmiennych pojedyncze slowa "Sun", "is", "setting", polacz je w jeden ciag znaków, ale tak,
# aby kazde slowo bylo w nowej linii, kazda nowa linia ma miec jedno wiecej wciecie tabulatora, tak aby wygladalo to nastepujaco:
#Sun
#              is
#                             setting

zmienna_1 = "Sun"
zmienna_2 = "is"
zmienna_3 = "setting"

print(zmienna_1 + "\n\t" + zmienna_2 + "\n\t\t" + zmienna_3)