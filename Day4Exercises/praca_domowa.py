def wypisywanie_liczb(ilosc, co):
    """
    4. Napisz funkcję, która przyjmuje dowolną ilość parametrów - zaloz ze beda podawane liczbowe,
    funkcja ma wypisywac te parametry, uzywajac petli for in
    """
    x = 0
    for x in range(ilosc):
        print(f"{co}")
    x + 1

# wypisywanie_liczb(7, "nana")

def sumowanie_liczb(ilosc, co):
    """
   5. Zmodyfikuj funkcje z zadania wyzej tak, aby na koncu wypisala sume liczb podanych do funkcji
   """
    suma = 0
    x = 0

    for x in range(ilosc):
        suma += co
        x += 1
    print(f"{suma}")

# sumowanie_liczb(7, 1)

def add(first_number, second_number):
    """
    6. Inside - out - napisz dwie funckje - dodawanie (np o nazwie add)
    oraz mnozenie dwoch liczb (np o nazwie multiply), nastapnie wywolaj operację
    multiply(add(2, 6), 2)def add(first_number, second_number):
    This is how we document our code
    :param first_number:
    :param second_number:
    :return: sum of the params
    """
    print(first_number + second_number)

# add(2, 2)

def multiply(first_number, second_number):
    """
    6. Inside - out - napisz dwie funckje - dodawanie (np o nazwie add)
    oraz mnozenie dwoch liczb (np o nazwie multiply), nastapnie wywolaj operację
    multiply(add(2, 6), 2)def add(first_number, second_number):
    This is how we document our code
    :param first_number:
    :param second_number:
    :return: sum of the params
    """
    print(first_number * second_number)

# multiply(2, 2)

def podziel_i_sortuj(zdanie):
    """
    7. Napisz funkcję rozbijajaca zdanie na slowa (ma zwracac liste ze slowami)
    oraz funkcje sortujaca liste slow, nastepnie wywolaj sortowanie na slowach
    podanego przez uzytkownika zdania
    """
    podzielone_zdanie = zdanie.split()
    podzielone_zdanie.sort()
    print(podzielone_zdanie)

# podziel_i_sortuj("ja lubie pracki, ty lubisz placki, wszyscy lubimy placki")

def uzyj_funkcji_modulu(nazwa_pliku):
    """8 Zaimportuj modul (plik) i uzyj funkcji z tego modulu
    help(nazwa_pliku) - zadokumentuj troche kodu!
    """
    help(nazwa_pliku)

# uzyj_funkcji_modulu(podziel_i_sortuj)
