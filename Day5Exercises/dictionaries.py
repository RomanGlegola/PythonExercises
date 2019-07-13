simple_dict = {1: "jeden", 2: "dwa"}

for key, value in simple_dict.items():
    print(f"pod kluczem {key} jest wartość {value}")

    simple_dict[1] = "trzy"

for key, value in simple_dict.items():
    print(f"pod kluczem {key} jest wartość {value}")

    simple_dict[1999] = "Matrix"
    simple_dict[2] = "Johny Mnemonic"

for key, value in simple_dict.items():
    print(f"w roku {key} w kinach pojawił się {value}")