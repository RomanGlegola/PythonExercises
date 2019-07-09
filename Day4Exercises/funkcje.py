def dodaj():

    x = int(input("podaj x: "))
    y = int(input("podaj y: "))

    suma = x + y

    print(suma)
    print()

#dodaj()

def repeat_n_times():
    """
    2. Napisz funkcję, powtarzającą słowo x razy (2 parametry - slowo oraz ile razy powtorzyc)
    (bedzie potrzebna petla for in oraz klasa range)
    #for loop to repeat(print) n times
    """
    word = str(input("Jakie słowo powtórzyć: "))
    times_to_repeat = int(input("Ile razy mam powtórzyć: "))

    for i in range(times_to_repeat):
        print(word)

    repeat_n_times(f"{word}", times_to_repeat)
    print()

#repeat_n_times()

def split_sentence_to_words(sentence):

    """
    3. Napisz funkcje, ktora rozbije zdanie na slowa i kazde z nich wypisze w nowej linii (bedzie potrzebna petla for in)
    """
    words = sentence.split()
    for x in range(len(sentence.split())):
        print(str(words[x]))

split_sentence_to_words("python day four")