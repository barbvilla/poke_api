from get_module import get_info
from poke_tipo import tipo_lista
from traduccion import genera_span


type_url = []
for item in tipo_lista:
    type_url.append(item["type"]["url"])

#print(type_url)

damage_relations = {}
for n in range(len(type_url)):
    data_damage = get_info(type_url[n])
    damage_relations.update(data_damage['damage_relations'])

#print (damage_relations)

for k in damage_relations:
    type_name = []
    for n in range(len(damage_relations[k])):
        type_name.append(damage_relations[k][n]['name'])
    damage_relations[k] = type_name

#print(damage_relations)

double_damage_from = []
for item in damage_relations['double_damage_from']:
     double_damage_from.append(item)

span_ddf = genera_span(double_damage_from)

""" print (span_ddf)
print(double_damage_from) """

double_damage_to = []
for item in damage_relations['double_damage_to']:
     double_damage_to.append(item)

span_ddt = genera_span(double_damage_to)

""" print (span_ddt)
print(double_damage_to) """

half_damage_from = []
for item in damage_relations['half_damage_from']:
     half_damage_from.append(item)

span_hdf = genera_span(half_damage_from)

""" print (span_hdf)
print(half_damage_from) """

half_damage_to = []
for item in damage_relations['half_damage_to']:
     half_damage_to.append(item)

span_hdt = genera_span(half_damage_to)

""" print (span_hdt)
print(half_damage_to) """

no_damage_from = []
for item in damage_relations['no_damage_from']:
     no_damage_from.append(item)

span_ndf = genera_span(no_damage_from)

""" print (span_ndf)
print (no_damage_from) """

no_damage_to = []
for item in damage_relations['no_damage_to']:
     no_damage_from.append(item)

span_ndt = genera_span(no_damage_to)

""" print (span_ndt)
print (no_damage_to) """
