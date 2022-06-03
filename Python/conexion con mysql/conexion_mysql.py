'''
Insertar datos en MySQL desde
Python 3
Antes de continuar cabe mencionar que los ejemplos aquí son 100 %
seguros. Es decir, nuestras consultas prevendrán las inyecciones
SQL.
Para insertar una película hacemos esto:
'''
import pymysql
try:
  conexion = pymysql.connect(host='localhost',
                            user='root',
                            password='admin',
                            db='peliculas')
  try:
    with conexion.cursor() as cursor:
      consulta = "INSERT INTO peliculas(titulo, anio) VALUES (%s, %s);"
      #Podemos llamar muchas veces a .execute con datos distintos
      cursor.execute(consulta, ("Volver al futuro 1", 1985))
      cursor.execute(consulta, ("Ready Player One", 2018))
      cursor.execute(consulta, ("It", 2017))
      cursor.execute(consulta, ("Pulp Fiction", 1994))
      conexion.commit()
  finally:
    conexion.close()
except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
  print("Ocurrió un error al conectar: ", e)

'''
Como vemos, necesitamos tener la conexión. Y luego usamos un
cursor para ejecutar nuestra consulta sobre la misma.
Es importante notar que usamos %s en lugar del valor real, y luego
ponemos los verdaderos datos en la llamada a .execute del cursor.
Esto es para que sea una consulta segura y las variables sean
escapadas en caso de que un usuario malicioso quisiera aprovechar
esa vulnerabilidad.

Más abajo hacemos un commit. Esto es para guardar los cambios
que hicimos a la base de datos, si no llamamos a este método
ninguno de nuestros cambios se reflejará.
Todo eso lo encerramos en un bloque try/finally (aparte del que
pertenece a la conexión) y siempre cerramos la conexión. Así, si hay
un problema con la inserción, la conexión no quedará abierta.
'''
