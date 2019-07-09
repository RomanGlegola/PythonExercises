#Challenging:

def temperatura():
    """
    5. Warunek if - przy pomocy metody input pobierz od uzytkownia wartosc temperatury.
    Ustaw 3 minimalne temperatury jako zmienne - zimna, ciepla, goraca (np. 10 stopni, 20 stopni, 30 stopni)
    i na podstawie temperatury podanej przez uzytkownika, wyswietl czy jest zimno, cieplo, czy goraco
    """
    x = int(input("Podaj temperaturę: "))

    if x >= 10 and x < 20:
        print(f"Temperatura {x} sprawia, że jest zimno.")
    elif x >= 20 and x < 30:
        print(f"Temperatura {x} sprawia, że jest ciepło.")
    elif x >= 30:
        print(f"Temperatura {x} sprawia, że jest gorąco.")
    else:
        print(f"Temperatura {x} jest niezdefiniowana.")

# temperatura()

def silnia():
    """
    6. Petla while - Oblicz silnie z podanej przez uzytkownika (metoda input) liczby -
    wyszukaj algorytm na silnie i napisz - przydadza sie zmienne, warunek if, operator *=
    """
    x = int(input("Podaj liczbę do obliczenia silni: "))

    silnia = x**x
    print(silnia)

# silnia()

def silnia_while():
    """
    6. Petla while - Oblicz silnie z podanej przez uzytkownika (metoda input) liczby -
    wyszukaj algorytm na silnie i napisz - przydadza sie zmienne, warunek if, operator *=
    """
    x = int(input("Podaj liczbę do obliczenia silni: "))
    i = 0
    silnia = 1
    while i < x:
        silnia *= x
        i += 1
    print(silnia)

# silnia_while()