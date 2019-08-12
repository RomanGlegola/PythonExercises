import requests

# import json

response = requests.get('http://www.recipepuppy.com/api/', params = {'i': 'onions,garlic', 'q': 'omelet', 'p': '2'})
print(response.status_code)
recipes = response.json()['results']

for recipe in recipes:
    print("\n")
    print(recipe["title"])
    print(30*"~")
    print(recipe["ingredients"])


