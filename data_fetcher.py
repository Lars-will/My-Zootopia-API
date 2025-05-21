import requests
import os
from dotenv import load_dotenv

load_dotenv()

STR_API_URL = "https://api.api-ninjas.com/v1/animals"
STR_API_KEY = os.getenv('API_KEY')

def fetch_animals(str_search):

    """
      Fetches the animals data for the animal 'animal_name'.
      Returns: a list of animals, each animal is a dictionary:
      {
        'name': ...,
        'taxonomy': {
          ...
        },
        'locations': [
          ...
        ],
        'characteristics': {
          ...
        }
    },
    """

    dict_params = {'name': str_search}
    dict_headers = {'X-Api-Key': STR_API_KEY}
    response = requests.get(STR_API_URL, params=dict_params, headers=dict_headers)
    return response.json()