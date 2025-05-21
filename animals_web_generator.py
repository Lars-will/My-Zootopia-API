import json
import requests

STR_API_KEY = "3gu5g01FCS8+wfLWZCnvWw==qfY8O3OHyyn8Vi4T"
STR_API_URL = "https://api.api-ninjas.com/v1/animals"


def write_html_file(str_file_name, str_data):
    """Function to write new html file."""
    with open(str_file_name, "w") as fileobj:
        fileobj.write(str_data)


def read_html_file(str_file_name):
    """Function to read html file"""
    with open(str_file_name, "r") as fileobj:
        return  fileobj.read()


def fetch_animals(str_search):
    """gets the animal data from the API and returns as list"""
    dict_params = {'name': str_search}
    dict_headers = {'X-Api-Key': STR_API_KEY}
    response = requests.get(STR_API_URL, params=dict_params, headers=dict_headers)
    return response.json()


def print_animals(animals_data):
    """Extracts certain fields from the animals_data list and prints them in the console"""
    for animal in animals_data:
        dict_taxonomy = animal['taxonomy']
        list_locations = animal['locations']
        dict_characteristics = animal['characteristics']
        print("--------------")

        if 'name' in animal.keys():
            print(animal['name'])
        if 'diet' in dict_characteristics.keys():
            print(dict_characteristics['diet'])

        print(list_locations[0])

        if 'type' in dict_characteristics.keys():
            print(dict_characteristics['type'])


def generate_animals_string(animals_data):
    """Function to generate the animals html string"""
    str_animals = ""
    for animal in animals_data:
        dict_taxonomy = animal['taxonomy']
        list_locations = animal['locations']
        dict_characteristics = animal['characteristics']
        str_animals += "<li class= 'cards__item'>"

        if 'name' in animal.keys():
            str_animals += f"<div class ='card__title'> {animal['name']} </div>\n"

        str_animals += "<p class ='card__text'>"

        if 'diet' in dict_characteristics.keys():
            str_animals += f"<strong>Diet:</strong> {dict_characteristics['diet']}<br>\n"

        str_animals += f"<strong>Location:</strong> {list_locations[0]}<br>\n"

        if 'type' in dict_characteristics.keys():
            str_animals += f"<strong>Type:</strong> {dict_characteristics['type']}<br>\n"

        str_animals += "</p>"
        str_animals += "</li>"

    return str_animals


def main():
    str_search = input("Hello. What type of animal are you looking for? ")
    animals_data = fetch_animals(str_search)
    str_html_file = read_html_file("animals_template.html")
    str_animals = generate_animals_string(animals_data)
    str_new_html_file = str_html_file.replace("__REPLACE_ANIMALS_INFO__", str_animals)
    write_html_file("animals.html", str_new_html_file)


if __name__ == "__main__":
    main()
