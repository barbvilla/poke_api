from string import Template
import poke_info
from poke_etapa_previa import poke_etapa_previa, poke_comentario
import poke_stats
from poke_tipo import span_tipo
from show import show_pics
import poke_damage

with open('output.html','r',encoding='utf-8') as infile:
    entrada = infile.read()

document_template = Template(entrada)

document_template_nuevo = document_template.safe_substitute(
    pok_n = poke_info.poke_numero,
    pok_name = poke_info.poke_name,
    pok_img = poke_info.poke_imagen,
    pok_peso = poke_info.poke_peso,
    pok_altura = poke_info.poke_altura,
    pok_etapa_previa = poke_etapa_previa,
    pok_hp = poke_stats.poke_hp,
    pok_at = poke_stats.poke_ataque,
    pok_de = poke_stats.poke_defensa,
    pok_ate = poke_stats.poke_ataque_especial,
    pok_dee = poke_stats.poke_defensa_eespecial,
    pok_ve = poke_stats.poke_velocidad,
    span_tipo = span_tipo,
    pok_comentario = poke_comentario,
    span_sup_ef = poke_damage.span_ddt, 
    span_deb_co = poke_damage.span_ddf,
    span_res_co = poke_damage.span_hdf,
    span_poe_co = poke_damage.span_hdt,
    span_inm_co = poke_damage.span_ndf,
    span_ine_co = poke_damage.span_ndt)

show_pics(document_template_nuevo, 'pokedex')
