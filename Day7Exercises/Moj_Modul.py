import os

# Wyświetl:

# Katalog: __pycache__
# Katalog: .idea
# Plik: test.py

def wypisanie():
    x = {}
    list = os.listdir()
    if len(list) == 0:
        x[0] = "Katalog jest pusty"

    for item in list:
        if os.path.isfile(item):
            x[item] = f"Plik: {item}"
        elif os.path.isdir(item):
            x[item] = f"Katalog: {item}"
    return x

def printowanie_slownika():
    for item, value in wypisanie().items():
        print(f"{value}")
