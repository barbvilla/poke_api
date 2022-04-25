from poke_info import data_base

stats = data_base["stats"]

indicadores = []
for item in stats:
    indicadores.append(item["base_stat"])

poke_hp, poke_ataque, poke_defensa, poke_ataque_especial, poke_defensa_eespecial,poke_velocidad = indicadores

#print(indicadores)