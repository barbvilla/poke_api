from get_module import get_info
from poke_info import poke_numero
import random

url_previa = f"https://pokeapi.co/api/v2/pokemon-species/{poke_numero}"

data_etapa_previa = get_info(url_previa)

poke_etapa_previa = data_etapa_previa['evolves_from_species']
if poke_etapa_previa is not None:
    poke_etapa_previa = (poke_etapa_previa['name']).capitalize()
else:
    poke_etapa_previa = 'No tiene'
    
    #print (poke_etapa_previa)

comentarios = data_etapa_previa["flavor_text_entries"]

filtro = [item["flavor_text"].replace("\n"," ") for item in comentarios if item["language"]["name"] == 'es']

poke_comentario = random.choice(filtro)
#print(pok_comentario)