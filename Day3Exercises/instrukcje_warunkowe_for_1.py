# repeatHowManyTimes = int(input("Please tell me how many times to repeat..."))

for index in range(repeatHowManyTimes):
    print("Hello, it's me")

# 0 przypisz do zmiennej o odpowiedniej nazwie nazwy miesiaca (January, February) - mozna uzyc skrotow Jan, Feb itd...
# wypisz nazwy miesiaca funkcja print(), nazwy miesiaca musza byc oddzielone enterem (znak specjalny \n)
miesiace = ["January", "Febuary", "March", "April", "May", "June", "July", "August", "September",
            "October", "November", "December"]
for miesiac in miesiace:
    print(str(miesiac))

# # 1 wypisz co druga literę z napisu - uzyj petli for:
text = "Python is a fantastic snake"
jak_dużo_znakow = len(text)

for co_druga_litera in range(0, jak_dużo_znakow, 2):
    print(text[co_druga_litera], end="")

# 1.1 skrot - przeczytaj https://docs.python.org/release/2.3.5/whatsnew/section-slices.html i wypisz co druga litere, tym razem w krotszy sposob
# 1.2 wypisz teraz co trzecią literę :wink:
text = "Python is a fantastic snake"
print(text[::3])

# 2 wyszukaj w dokumentacji jak rozbić powyższy tekst na listę słów a nastepnie wydrukuj ta liste (for slowo in lista)
# # you need to use method on text to seperate words
text = "Python is a fantastic snake"
word_list = text.split()

for word in word_list:
    print(str(word))
# you need to print here

# 3 zmien program z punktu drugiego tak, aby uzytkownik sam wpisal jakis tekst, ktory program mu rozbije na liste slow
gadane = input()
word_list = gadane.split()

for gadane in word_list:
    print(str(gadane))
