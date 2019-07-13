# stworz slownik - baze danych filmow, gdzie kluczem jest rok, natomiast wartoscia nazwa filmu z podanego roku

# spróbuj zamiast jednego filmu, przechowywac liste filmow z danego roku

# po stworzeniu listy filmów w np. roku 2000 i 2009, wypisz ładnie ;) na konsoli rok, a następnie filmy w danym roku
# uzyj np wciecia, aby pokazac przynaleznosc danych filmow do roku

# dictionaries plus lists
# napisz program odczytujacy plik - policz ilosc wystepujacych poszczegolnych slow
# Wskazowki:
# default dict values
# from collections import defaultdict
# set(
# list_dictionary = defaultdict(list)

# wypisz 10 najczęsciej i 10 najrzadziej wystepujacych slow

movie_db ={}


movie_db[2000] = ["animatrix", "transformers", "kolejny film 1"]
movie_db[2009] = ["transformers", "love story", "toy story", "king lion story"]


for key, value in movie_db.items():
    print(key)
    x=0
    for movie in value:
        movie = movie_db[key]
        print(f"")
        x+=1
    # print(f"W roku {key} wydano film(y): {value}")

movie_db[2000].append("Matrix")
#print(movie_db[2000])

