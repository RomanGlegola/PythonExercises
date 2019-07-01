# Napisz program, który przyjmuje zdanie od użytkownika (input)
# jeżeli napis zaczyna się na literę 'a' powiedz użytkownikowi, że zaczyna się od pierwszej litery alfabetu
# jeśli na literę 'z' powiedz użytkownikowi, że zaczyna się od ostatniej litery alfabetu
# w przeciwnym razie powiedz, że zaczyna od innej litery niż 'a' lub 'z'

zdanie = input("Wpisz zdanie: ")

a = "a"
z = "z"
b = "A"
y = "Z"

if(zdanie[0] == a or zdanie[0] == b):
    print("Twoje zdanie zaczyna się na literę 'a'")
elif(zdanie[0] == z or zdanie[0] == y):
    print("Twoje zdanie zaczyna się na literę 'z'")
else:
    print("Twoje zdanie zaczyna się na literę inną niż 'a' lub 'z'")
