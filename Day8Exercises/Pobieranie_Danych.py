import requests
import csv
import folium


def pobierz_dane():
    data_url = 'https://raw.githubusercontent.com/infoshareacademy/isa-python12/master/Day8/exercises/airports.csv?token=AGMZVYOFLTW6SJTOMBVPTRS5HCKJ2'
    airports_data = requests.get(data_url) # pobieramy dane z repozytorium
    csv_data = airports_data.text
    csv_filename = 'airports.csv'
    with open(csv_filename, 'w') as csv_file:
        csv_file.write(csv_data)


pobierz_dane()

map = folium.Map()


def ikona():
    global icon
    icon = folium.Icon(  # zmieniamy ikonę wskaźnika
        icon='plane',  # nazwa ikony z https://fontawesome.com/
        prefix='fa',  # prefiks z dokumentacji do strony https://fontawesome.com/
        color='green'  # kolor ikony
    )
    return icon



with open('airports.csv', 'r') as csv_file:
    data = csv.reader(csv_file) # przypisujemy zmienną i wpisujemy w nią plik csv
    for airport in data:
        znacznik = folium.Marker(#ustawiamy znacznik na mapie
            location=[airport[5], airport[6]], #wskazuje lokalizację znacznika
            popup=airport[1], #dodaje opis na znaczniku
            icon=ikona()
        )
        map.add_child(znacznik) #dodaje znaczniki do mapy


map.save("mapa.html")