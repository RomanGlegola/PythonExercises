import random

sciezka = "cechy_glowne.txt"


def losowa_2k10():
    return random.randrange(19 + 1)


def losowa_k10():
    return random.randrange(10)


slownik_cech_glownych = {"Walka wręcz: ": losowa_2k10(), "Umiejętności Strzeleckie: ": losowa_2k10(),
                         "Krzepa: ": losowa_2k10(), "Odporność: ": losowa_2k10(), "Zręczność: ": losowa_2k10(),
                         "Siła woli: ": losowa_2k10(), "Inteligencja: ": losowa_2k10(), "Ogłada: ": losowa_2k10()}

slownik_cech_drugorzednych = {"Atak: ": 1, "Żywotność: ": losowa_k10()}

with open(sciezka, 'w+') as plik:
    #for cecha in slownik_cech_glownych:
    plik.writelines(f"{slownik_cech_glownych} {losowa_2k10()} \n")

    plik.writelines(f"{slownik_cech_drugorzednych} {losowa_k10()} \n")

    print(plik.read)

with open(sciezka, 'r') as plik:
    print((plik.read()))
