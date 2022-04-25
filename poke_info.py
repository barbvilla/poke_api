from get_module import get_info
import poke_validation as pv

name = input("Introduzca el nombre del Pokémon a procesar: ")

name = pv.validate(name)

poke_name = name.capitalize()

url_base = f"https://pokeapi.co/api/v2/pokemon/{name}"

data_base = get_info(url_base)
#print(data_base)

poke_numero = data_base["id"]

poke_imagen = data_base['sprites']['other']['official-artwork']['front_default']

poke_peso = data_base["weight"]
poke_peso = poke_peso / 10

poke_altura = data_base["height"]
poke_altura = poke_altura / 10