import random

sciezka = "Warhammer/cechy_glowne.txt"


def losowa_2k10():
    return random.randrange(18)+2


def losowa_k10():
    return random.randrange(9)+1

def cechy_glowne():

    slownik_cech_glownych = {"Walka wręcz: ": 0, "Umiejętności Strzeleckie: ": 0,
                             "Krzepa: ": 0, "Odporność: ": 0, "Zręczność: ": 0,
                             "Siła woli: ": 0, "Inteligencja: ": 0, "Ogłada: ": 0}
    for item in slownik_cech_glownych:
        slownik_cech_glownych[item] = losowa_2k10()
    return slownik_cech_glownych


def cechy_drugorzedne():

    slownik_cech_drugorzednych = {"Atak: ": 0, "Żywotność: ": 0,
                                  "Siła: ": 0, "Wytrzymałość: ": 0, "Szybkość: ": 0,
                                  "Magia: ": 0, "Punkty Obłędu: ": 0, "Punkty Przeznaczenia: ": 0}
    for item in slownik_cech_drugorzednych:
        slownik_cech_drugorzednych[item] = losowa_2k10()
    return slownik_cech_drugorzednych

def zapisanie_do_pliku():
    with open(sciezka, 'w+') as plik:
        for item, value in cechy_glowne().items():
            plik.writelines(f"{item} {value} \n")
        plik.writelines(30*"=" + "\n")
        for item, value in cechy_drugorzedne().items():
            plik.writelines(f"{item} {value} \n")

        print(plik.read)


def otwieranie_pliku():
    with open(sciezka, 'r') as plik:
        print((plik.read()))

zapisanie_do_pliku()