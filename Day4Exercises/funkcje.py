# x=int(input("podaj x: "))
# y=int(input("podaj y: "))
#
# def dodaj(x, y):
#     suma = x + y
#     return suma
#
# print(dodaj(x,y))
# print()
#
# 2. Napisz funkcję, powtarzającą słowo x razy (2 parametry - slowo oraz ile razy powtorzyc)
# (bedzie potrzebna petla for in oraz klasa range)
# #for loop to repeat(print) n times
# word = str(input("Jakie słowo powtórzyć: "))
# times_to_repeat = int(input("Ile razy mam powtórzyć: "))
# def repeat_n_times(word, times_to_repeat):
#     for i in range(times_to_repeat):
#         print(word)
#
# repeat_n_times(f"{word}", times_to_repeat)
# print()
# 3. Napisz funkcje, ktora rozbije zdanie na slowa i kazde z nich wypisze w nowej linii (bedzie potrzebna petla for in)
def split_sentence_to_words(sentence):
    return str(sentence).split(" ")
def split_sentence_to_words(sentence):
    words = str
print(split_sentence_to_words("Python Day Four"))