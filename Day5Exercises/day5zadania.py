def sumuj_liste1():
    """
    napisz funkcję sumujący wszystkie elementy w liscie
    """
    lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    return sum(lista)


# print(sumuj_liste1)

def sumuj_liste2():
    """
    napisz funkcję sumujący wszystkie elementy w liscie
    """
    axa = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    suma = 0
    for znacznik in axa:
        suma = suma + znacznik
    return suma


# print(sumuj_liste2)

def wypisz_min_i_max():
    """
    znajdz najwiekszy / najmniejszy element w liscie - napisz dwie funkcje
    2 sposoby - najpierw ręcznie, następnie sprytnie
    """
    axa = [5, 6, 7, 8, 9, 1, 2, 3, 4]
    sorted(axa)
    największa = 0
    for cyfra in axa:
        if największa < cyfra:
            największa = cyfra
    return największa
    najmniejsza = największa
    for cyfra in axa:
        if najmniejsza > cyfra:
            najmniejsza = cyfra
    return najmniejsza

# print(sumuj_wypisz_min_i_max)

def zrob_liste_wyrazow():
    """
    funkcja ktory zmieni zdanie w liste wyrazow
    zdanie = "Ala ma kota, kot ma Ale
    """
    zdanie = "Ala ma kota, kot ma Ale"
    slowa = zdanie.split()
    return slowa

# print(zrob_liste_wyrazow())

def wypisz_stringi_dluzsze_niz_dwa_palindrom():
    """
    napisz funkcję przyjmujaca liste stringow,
    a zwracakaca liczbe stringow dl. min. 2, ktore zaczynaja sie i koncza na te same znaki
    ['abc', 'xyz', 'aba', '1221'] - odp = 2
    """
    lista = ['abc', 'xyz', 'aba', '1221']
    znacznik = 0

    for slowo in lista:
        if (len(slowo) >= 2 and slowo[0] == slowo[-1]):
            znacznik += 1
    return znacznik

# print(wypisz_stringi_dluzsze_niz_dwa_palindrom())

def znajdz_wartosci_wystepujace_raz():
    """
    program znajdujacy wartosci, ktre wystepuja tylko raz
    lista_a = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]
    """
    lista_a = [40, 10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]
    lista_poprawnych_cyfr = []
    cyfra = 0
    for cyfra in lista_a:
        if lista_a.count(cyfra) == 1:
            lista_poprawnych_cyfr.append(cyfra)
    return cyfra

# print(znajdz_wartosci_wystepujace_raz())

def usun_zduplikowane_wartosci():
    """
    # program usuwajacy zduplikowane wartosci w liscie (w miejscu! - tzn bez drugiej listy)
    # podpowiedz - del lub pop()
    lista_b = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]
    """
    lista_b = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]
    return list(set(lista_b))

# print(usun_zduplikowane_wartosci())

def sprawdz_wspolny_element():
    """
    # program sprawdza czy dwie listy maja co najmniej jeden wspolny element,
    # jesli tak wypisuje True
    """
    lista_a = [1, 2]
    lista_b = [3, 4]
    for x in range(len(lista_a)):
        lista_a[x]
        for y in range(len(lista_b)):
            lista_b[y]
            if lista_a[x] == lista_b[y]:
                return True
                y+1
        x+1
    if lista_a[x] != lista_b[y]:
        return False

# print(sprawdz_wspolny_element())

def stworz_macierz():
    """
    # stworz macierz (4 x 5), ktorej wszystkie komorki wypelnione sa znakiem *
    """
    macierz = [4 * ["*"]] * 5
    macierz
    for x in range(len(macierz)):
        return str(macierz[x])

# print(stworz_macierz())

def losowy_element():
    """
    # wybierz losowo element z listy
    # wskazowka - import random
    """
    lista = [10, 10, 20, 10, 10, 20, 10, 20, 20, 20, 40, 50, 40, 10, 30, 50, 50, 30]

    import random
    x = random.randrange(len(lista))
    return (lista[x])

# print(losowy_element())


def czestotliwosc_elementow():
    """
    # oblicz częstość elementów w liście (ile razy)
    # jedna wersja zwykla pętle, ify itd
    # druga - moze jest jakis modul gotowy???
    lista = [10, 10, 20, 10, 10, 20, 10, 20, 20, 20, 40, 50, 40, 10, 30, 50, 50, 30]
    """
    lista = [10, 10, 20, 10, 10, 20, 10, 20, 20, 20, 40, 50, 40, 10, 30, 50, 50, 30]
    x = 0
    lista.sort()

    for x in lista:
        print(f"{x} element w liście ma {lista.count(x)}")
        x+1

# print(czestotliwosc_elementow())
