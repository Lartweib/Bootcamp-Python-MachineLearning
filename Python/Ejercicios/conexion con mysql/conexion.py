'''
Primera conexión
Antes de hacer el CRUD vamos a ver si nos podemos conectar a la
base de datos. Para ello ponemos este fragmento de código en
un try/except:
'''


import pymysql
try:
  conexion = pymysql.connect(host='localhost',
                            user='root',
                            password='admin',
                            db='peliculas')
  print("Conexión correcta")
except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
  print("Ocurrió un error al conectar: ", e)

'''
Aquí hay unos parámetros que debemos tener en cuenta.
- host: el host en donde nuestro servidor MySQL escucha.
Normalmente es localhost o 127.0.0.1 pero igualmente podría
ser otro, basta con poner la ip
- user: el usuario que puede administrar la base de datos
- password: la contraseña del usuario. Si está vacía dejamos las
comillas vacías
- db: el nombre de la base de datos a la que intentamos
conectarnos
Si todo va bien, al ejecutar el script debe mostrar el mensaje:
Conexión correcta
En caso de que no, se mostrarán errores. 
'''
