simple_dict = {1: "jeden", 2: "dwa"}

for key, value in simple_dict.items():
    print(f"pod kluczem {key} jest wartość {value}")

    simple_dict[1] = "trzy"

for key, value in simple_dict.items():
    print(f"pod kluczem {key} jest wartość {value}")

    simple_dict[1] = "Matrix"
    simple_dict[2] = "Johny Mnemonic"

for key, value in simple_dict.items():
    print(f"Keanu grał w filmie {key} ale rolą, która go do tego filmu zaprowadziła był film {value}")