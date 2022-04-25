from poke_info import data_base
from poke_special import span_special
from traduccion import genera_span

tipo_lista = data_base["types"]

tipos = []
for item in tipo_lista:
    tipos.append(item["type"]["name"])

span_tipo = genera_span(tipos)

span_tipo = span_tipo + span_special
