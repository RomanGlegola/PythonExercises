zadanie = "\n\n\tZadanie z pracy domowej no."

print(zadanie + "4")
# 4. zapoznaj sie z metoda input() w Python - wyszukaj w dokumentacji i sprawdz dzialanie.
# Funkcja print zachec uzytkownika, aby podal liczbe, nastepnie wypisz kwadrat oraz szescian tej liczby.
# Postaraj sie o odpowiedni wyglad odpowiedzi, opisujacy uzyskane wyniki, np.
#                                   Szescian liczby x wynosi x^3, natomiast kwadrat x^2

x = input("wpisz cyfrę: ")
print(x + " jest wpisaną zmienną ")
print(type(x))

x = int(x)

y = int(x)**3
print(int(y))

z = int(x)**2
print(int(z))
