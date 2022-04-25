from poke_etapa_previa import data_etapa_previa

clase_tipo = ''
if data_etapa_previa['is_mythical']:
    clase_tipo = 'Místico'
elif data_etapa_previa['is_baby']:
    clase_tipo = 'Bebé'
elif data_etapa_previa['is_legendary']:
    clase_tipo = 'Legendario'
#print (clase_tipo)

span_special = ''
if clase_tipo:
    span_special += f'<span class="label other">{clase_tipo}</span>'
#print (span_special) 
