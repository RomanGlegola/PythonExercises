# old_number = 4
# new_number = old_number
# old_number = 6
#
# print(old_number)
# print(new_number)
# print()
# #old_number i new_number jako typy proste odnoszą się do innego miejsca w pamięci.
#
# old_list = [1,2,3]
# new_list = old_list
# old_list[0] = 4
#
# print(old_list)
# print(new_list)
# print()
# #old_list i new_list jako typy złożone odnoszą się do takiego samego miejsca w pamięci.
#
# stara_lista = [1,2,3,4,5]
# nowa_lista = stara_lista.copy()
# nowa_lista = list(stara_lista)
# nowa_lista = stara_lista[:]
#
# print(stara_lista)
# print(nowa_lista)
# print()
# #stara_lista jest kopiowana do nowa_lista do nowego miejsca w pamięci.
#
# stary_string = "Mama"
# nowy_string = stary_string
# nowy_string = "nana"
#
# print(stary_string)
# print(nowy_string)
# print()
# #stary_string i nowy_string jako typy proste odnoszą się do innego miejsca w pamięci.
#
# stara_nowa_lista = list(range(0, 10))
# nowa_nowa_lista = []
# #1 rozwiązanie
# for n in stara_nowa_lista:
#     nowa_nowa_lista.append(n**2)
# print(stara_nowa_lista)
# print(nowa_nowa_lista)
# print()
#
# #2 rozwiązanie
# list_of_squares_2 = list(stara_nowa_lista[:])
# for index, number in enumerate(stara_nowa_lista):
#     list_of_squares_2[index] = number ** 2
# print(list(stara_nowa_lista))
# print(list_of_squares_2)
#
# #3 rozwiązanie
# last_list_of_squares = [x**2 for x in stara_nowa_lista]
# words = ["iTs", "mE", "PytHOn"]
# new_words = [word.upper() for word in words]
# print(new_words)
# print(last_list_of_squares)
# #podnosimy wartości stara_nowa_lista do potęgi 2 i wypisujemy wartości do nowa_nowa_lista.
#
# stara_nowsza_lista = [10, 10, 10, 10, 10, 10, 10, 10]
# nowa_nowsza_lista = [20, 20, 20, 20, 20, 20, 20, 20]
# z_sumowana_lista = []
# for n1 in range(0, len(stara_nowsza_lista)):
#     z_sumowana_lista.append(stara_nowsza_lista[n1] + nowa_nowsza_lista[n1])
# print(stara_nowsza_lista)
# print(nowa_nowsza_lista)
# print(z_sumowana_lista)
# print()
# #sumujemy stara_nowsza_lista i nowa_nowsza_lista do z_sumowana_lista.
#
# stara_jeszczenowsza_lista = [10, 10, 10, 10, 10, 10, 10, 10]
# nowa_jeszczenowsza_lista = [20, 20, 20, 20, 20, 20, 20, 20]
# dodawanie_lista = []
# wymienianie_przecinek_lista = []
# dodawanie_i_przecinek_lista = []
# dodawanie2_lista = []
# for ela, elb in zip(stara_jeszczenowsza_lista, nowa_jeszczenowsza_lista):
#     #print(f"{ela}, {elb}")
#     dodawanie_lista.append(ela + elb) #jedno elementowe
#     dodawanie2_lista.append([ela + elb]) #jedno elementowe z dodatkowym zagnieżdżeniem
#     wymienianie_przecinek_lista.append([ela, elb]) #dwu elementowe
#     dodawanie_i_przecinek_lista.append([[ela + elb], ela, elb]) #trzyelementowe
# print(dodawanie_lista)
# print(dodawanie2_lista)
# print(wymienianie_przecinek_lista)
# print(dodawanie_i_przecinek_lista)
# print()
# # listy i ich łączenie, sumowanie.

#
print(True and True) #true
print(True and False) #false
print(1==1 and 2==1) #false
print("test"=="test") #true
print(1==1 or 2!=1) #true
print(True and 1==1) #true
print(False and 0!=0) #false
print(True or 1==1) #true
print("Test" != "Testing") #false!
print("test" == 1) #false
print(not (True and False)) #true
print(not(1==1 and 0!=1)) #false
print(not(1!=10 or 3==4)) #false
print(not(10==1 or 1000 == 1000)) #false
print(not(1!=10 or 3==4)) #false
print(not("testing" == "testing" and "Zed" == "Cool Guy"))
print(1==1 and (not("testing" == 1 or 1==0)))

