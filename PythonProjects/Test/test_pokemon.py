import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'd4aefdab47ebba2e0cf7b6672454d20d'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}
TRAINER_ID = 12098

def test_status_code():
    response = requests.get(url = f'{URL}/trainers', params = {'trainer_id': TRAINER_ID})
    assert response.status_code == 200