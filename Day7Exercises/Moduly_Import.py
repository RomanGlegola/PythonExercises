import os

# print(os.listdir())
# print(os.path.isdir())
# print(os.path.isfile())
#
# Wyswietl:
#
# Katalog: __pycache__
# Katalog: .idea
# Plik: test.py
# list = []

list = os.listdir()
# if not list:
#     print("Lista jest pusta 1")
# if len(list) == 0:
#     print("Lista jest pusta 2")

try:
    list[0]
    wynik = 10/0
except IndexError:
    print('error')
    exit()
except ZeroDivisionError:
    print('nieznany mi błąd')
else:
    for item in os.listdir():
        if os.path.isfile(item):
            print(f"Plik: {item}")
        elif os.path.isdir():
            print(f"Plik: {item}")
