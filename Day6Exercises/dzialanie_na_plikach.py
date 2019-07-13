sciezka = "tekst_dzialanie_na_plikach_filmy.txt"

spis_filmow = {}
spis_filmow[2000] = ["Animatrix", "Transformers 1"]
spis_filmow[2009] = ["Transformers 3"]
spis_filmow[2000].append("Matrix")

print(spis_filmow)

with open(sciezka, 'w+') as plik:
    for key, value in spis_filmow.items():
        plik.write("\n" + str(key) + "\n")
        for film in value:
            plik.write("\t" + str(film))
    spis_filmow = plik.read()
