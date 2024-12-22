import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'd4aefdab47ebba2e0cf7b6672454d20d'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}
body_create = {
    "name": "Мульти",
    "photo_id": -1
}

body_name = {
    "pokemon_id": "166535",
    "name": "Боби",
    "photo_id": 2
}

body_pokeball = {
    "pokemon_id": "166535"
}

'''response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.text)'''

'''message = response_create.json()['message']
print(message)'''

'''response_name = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_name)
print(response_name.text)'''

response_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_pokeball)
print(response_pokeball.text)