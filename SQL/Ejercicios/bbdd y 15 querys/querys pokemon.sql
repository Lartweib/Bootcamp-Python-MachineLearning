# 01) lista de pokemon y su peso donde el peso este entre 6 y 10 kg ordenados por peso de forma descendente
# 02) ordena los primeros 76 nombres de los pokemon en orden descendente#03) ordena y lista los movimientos que tengan probabilidad de generar estados de forma ascendente #04) muestra la cantidad de tipos de pokemon que tienen id_tipo_ataque con valor 2 renombrando la columna como "cantidad  de tipos id ataque 2" 
# 03) ordena y lista los movimientos que tengan probabilidad de generar estados de forma ascendente 
# 04) muestra la cantidad de tipos de pokemon que tienen id_tipo_ataque con valor 2 renombrando la columna como "cantidad  de tipos id ataque 2" 
# 05) lista los nombres de los pokemon tipo agua y su numero de pokedex ordenandolos por su numero de forma descendente 
# 06)listar el nombre de los movimientos y cuantos pokemon pueden aprenderlos renombrando el ultimo campo como "cant. poke"
# 07)listar nombre y valor del ataque de pokemon con el "ataque" mas alto de sus estadisticas base 
# 08) lista de movimientos que tengan como efecto secundario "bajar defensa"

# 09) media de puntos de salud de los pokemon tipo bicho
# 10) listar los primeros 15 pokemon por nombre en orden descendente que pueden aprender el movimiento puño trueno
# 11) lista de pokemon que no puedan seguir evolucionando y/o que no tengan evolucion
# 12) listar los nombres de los pokemon y su evolucion proxima 
# 13) listar todas las mt que aprende el pokemon "kadabra"
# 14) cuantos nombres de pokemon empiezan con las primeras 2 letras del pokemon que aprende "Psiquico" en el nivel 66.
# 15) Listado de todos los nombres de tipo de pokemon con la media de daño de todos los pokemon de ese tipo.
	# Solo seleccionar los tipos los cuales la media de daño de sus pokemon este comprendida entre 65 y 95 
	# y solo en caso que existan entre 10 y 30 pokemon de ese tipo.





#SOLUCIONES
# 01) lista de pokemon y su peso donde el peso este entre 6 y 10 kg ordenados por peso de forma descendente
select nombre, peso from pokemon where peso between 6 and 10 order by peso desc;

# 02) ordena los primeros 76 nombres de los pokemon en orden descendente
select nombre from pokemon order by nombre desc limit 76; #De zubat a magnemite

# 03) ordena y lista los movimientos que tengan probabilidad de generar estados de forma ascendente 
select nombre from movimiento where descripcion like "%\%%" order by nombre; #absorber a ventisca

# 04) muestra la cantidad de tipos de pokemon que tienen id_tipo_ataque con valor 2 renombrando la columna como "cantidad  de tipos id ataque 2" 
select count(*) as "cantidad  de tipos id ataque 2" from tipo where id_tipo_ataque = 2; #7

# 05) lista los nombres de los pokemon tipo agua y su numero de pokedex ordenandolos por su numero de forma descendente 
select p.nombre, p.numero_pokedex from pokemon p
join pokemon_tipo pt
on p.numero_pokedex = pt.numero_pokedex
join tipo
on tipo.id_tipo = pt.id_tipo
where tipo.nombre = "agua"
order by p.numero_pokedex desc;  # 141 a 7

#06)listar el nombre de los movimientos y cuantos pokemon pueden aprenderlos renombrando el ultimo campo como "cant. poke"
select m.nombre, count(*) as "cant. poke"
from pokemon_movimiento_forma pkf
join movimiento m
on pkf.id_movimiento = m.id_movimiento
group by m.id_movimiento; # placaje 38 - puño mareo 1

#07)listar nombre y valor del ataque de pokemon con el "ataque" mas alto de sus estadisticas base 
select pokemon.nombre, eb.ataque from pokemon 
join estadisticas_base eb
on pokemon.numero_pokedex = eb.numero_pokedex 
where eb.ataque = (select max(estadisticas_base.ataque) from estadisticas_base); #Dragonite

#08) lista de movimientos que tengan como efecto secundario "bajar defensa"
select m.nombre, es.efecto_secundario from movimiento m
join movimiento_efecto_secundario mes
on mes.id_movimiento = m.id_movimiento
join efecto_secundario es
on es.id_efecto_secundario = mes.id_efecto_secundario
where es.efecto_secundario like 'Bajar defensa'; #Hueso palo

#09) media de puntos de salud de los pokemon tipo bicho
select avg(ps) from tipo t
join pokemon_tipo pt
on t.id_tipo = pt.id_tipo
join estadisticas_base eb
on eb.numero_pokedex = pt.numero_pokedex
where t.nombre = "Bicho";

#10) listar los primeros 15 pokemon por nombre en orden descendente que pueden aprender el movimiento puño trueno
select p.nombre  from pokemon p
join pokemon_movimiento_forma pmf
on p.numero_pokedex = pmf.numero_pokedex
join movimiento m
on pmf.id_movimiento = m.id_movimiento
where m.nombre = "puño trueno" 
order by p.nombre desc
limit 15;

#11) lista de pokemon que no puedan seguir evolucionando y/o que no tengan evolucion

#12) listar los nombres de los pokemon y su evolucion proxima 
select p.nombre, po.nombre  from pokemon p
join evoluciona_de ed
on p.numero_pokedex = ed.pokemon_origen
join pokemon po
on ed.pokemon_evolucionado = po.numero_pokedex;

#13) listar todas las mt que aprende el pokemon "kadabra"
select mt.MT from mt 
join forma_aprendizaje fa
on fa.id_forma_aprendizaje = mt.id_forma_aprendizaje
join pokemon_movimiento_forma pmf
on pmf.id_forma_aprendizaje = fa.id_forma_aprendizaje
join pokemon p
on p.numero_pokedex=pmf.numero_pokedex
where upper(p.nombre = "KADABRA");

#14) cuantos nombres de pokemon empiezan con las primeras 2 letras del pokemon que aprende "Psiquico" en el nivel 66.
select count(*) as "cantidad de pokemon" from pokemon where nombre like concat((select substring(p.nombre,1,2)
from pokemon p
join pokemon_movimiento_forma pmf
on p.numero_pokedex = pmf.numero_pokedex
join movimiento m
on m.id_movimiento = pmf.id_movimiento
join forma_aprendizaje fa
on fa.id_forma_aprendizaje = pmf.id_forma_aprendizaje
join nivel_aprendizaje na
on na.id_forma_aprendizaje = fa.id_forma_aprendizaje
where na.nivel = 66),"%");

#15)Listado de todos los nombres de tipo de pokemon con la media de daño de todos los pokemon de ese tipo.
	# Solo seleccionar los tipos los cuales la media de daño de sus pokemon este comprendida entre 65 y 95 
	# y solo en caso que existan entre 10 y 30 pokemon de ese tipo.
select t.nombre, avg(eb.ataque)
from estadisticas_base eb
join pokemon_tipo pt
on eb.numero_pokedex = pt.numero_pokedex
join tipo t
on t.id_tipo = pt.id_tipo
where pt.id_tipo IN
(select pt.id_tipo
from pokemon_tipo pt
join pokemon p on p.numero_pokedex = pt.numero_pokedex
group by pt.id_tipo
having count(*) between 10 and 30
order by pt.id_tipo)
group by nombre
having avg(eb.ataque) between 65 and 95
order by avg(eb.ataque);