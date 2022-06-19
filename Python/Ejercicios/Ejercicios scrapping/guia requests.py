#--------------------------
# SCRAPPING
#--------------------------

'''
Si bien existen multitud de datos estructurados en forma de ficheros, hay otros muchos que
están embebidos en páginas web y que están preparados para ser visualizados mediante un
navegador.

Sin embargo, las técnicas de «scraping» nos permiten extraer este tipo de información
web para convertirla en datos estructurados con los que poder trabajar de forma más
cómoda.
'''

#--------------------------
# REQUESTS
#--------------------------

'''
El paquete requests es uno de los paquetes más famosos del ecosistema Python. Como dice
su lema «HTTP for Humans» permite realizar peticiones HTTP de una forma muy sencilla
y realmente potente.1

$ pip install requests
'''

#--------------------------
# REQUESTS.REALIZAR UNA PETICION
#--------------------------

'''
Realizar una petición HTTP mediante requests es realmente sencillo:
'''

import requests

response = requests.get('https://pypi.org')

'''
Hemos ejecutado una solicitud GET al sitio web https://pypi.org. 

La respuesta se almacena en un objeto de tipo requests.models.Response muy rica en métodos y atributos
'''

print(type(response)) # requests.models.Response

'''
Quizás lo primero que nos interese sea ver el contenido de la respuesta. En este sentido
requests nos provee del atributo text que contendrá el contenido html del sitio web en
cuestión como cadena de texto:
'''

print(response.text) # imprime el html

'''
Algo que es realmente importante en una petición HTTP es comprobar el estado de la
misma. Por regla general, si todo ha ido bien, deberíamos obtener un código 200, pero
existen muchos otros códigos de estado de respuesta HTTP:

Truco: Para evitar la comparación directa con el literal 200, existe la variable requests.
codes.ok.
'''

print(response.status_code == 200) # True

print(response.status_code == requests.codes.ok) # True


#--------------------------
# REQUESTS.TIPOS DE PETICIONES
#--------------------------

'''
Con requests podemos realizar peticiones mediante cualquier método HTTP.
Para ello, simplemente usamos el método correspondiente del paquete:


Método HTTP Llamada
------------------------------
GET ------> requests.get()
POST -----> requests.post()
PUT ------> requests.put()
DELETE ---> requests.delete()
HEAD  ----> requests.head()
OPTIONS --> requests.options()

'''

#--------------------------
# REQUESTS.USANDO PARAMETROS
#--------------------------
'''
Cuando se realiza una petición HTTP es posible incluir parámetros. 
Veamos distintas opciones que nos ofrece requests para ello.
'''

#--------------------------
# REQUESTS.USANDO PARAMETROS.QUERY STRING
#--------------------------

'''
En una petición GET podemos incluir parámetros en el llamado «query string». Los
parámetros se definen mediante un diccionario con nombre y valor de parámetro.
Veamos un ejemplo sencillo. Supongamos que queremos buscar paquetes de Python que
contengan la palabra «astro»:

Truco: El atributo url nos devuelve la URL a la se ha accedido. Útil en el caso de paso de
parámetros.
'''

payload = {'q':'astro'}

response = requests.get('https://pypi.org', params=payload)

print(response.url) # https://pypi.org/?q=astro


#--------------------------
# REQUESTS.USANDO PARAMETROS.POST
#--------------------------

'''
Una petición POST, por lo general, siempre va acompañada de una serie de parámetros que
típicamente podemos encontrar en un formulario web. Es posible realizar estas peticiones en
requests adjuntando los parámetros que necesitemos en el mismo formato de diccionario que
hemos visto para «query string».

Supongamos un ejemplo en el que tratamos de logearnos en la página de GIPHY con
nombre de usuario y contraseña. Para ello, lo primero que debemos hacer es inspeccionar
los elementos del formulario e identificar los nombres («name») de los campos. En este caso
los campos son email y password:
'''
url = 'https://giphy.com/login'

payload = {'email':'sdelquin@gmail.com','password':'1234'}

response = requests.post(url, data=payload)

print(response.status_code) # 403

'''
Hemos obtenido un código de estado 403 indicando que el acceso está prohibido.
'''


#--------------------------
# REQUESTS.USANDO PARAMETROS.ENVIO DE CABECERAS
#--------------------------

'''
Hay veces que necesitamos modificar o añadir determinados campos en las cabeceras de la
petición. Su tratamiento también se realiza a base de diccionarios que son pasados al método
correspondiente.

Uno de los usos más típicos de las cabeceras es el «user agent» donde se especifica el tipo
de navegador que realiza la petición. Supongamos un ejemplo en el que queremos especificar
que el navegador corresponde con un Google Chrome corriendo sobre Windows 10:
'''

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'

headers = {'user-agent':user_agent}

response = requests.get('https://pypi.org', headers=headers)

print(response.status_code) # 200


#--------------------------
# REQUESTS.ANALIZANDO LA RESPUESTA.CONTENIDO JSON
#--------------------------

'''
El formato JSON es ampliamente utilizado para el intercambio de datos entre aplicaciones.
Hay ocasiones en las que la respuesta a una petición viene en dicho formato. Para facilitar
su tratamiento requests nos proporciona un método que convierte el contenido JSON a un
diccionario de Python.

Supongamos que queremos tener un pronóstico del tiempo en Santa Cruz de Tenerife.
Existen múltiples servicios online que ofrecen datos meteorológicos. En este caso vamos a
usar https://open-meteo.com/. La cuestión es que los datos que devuelve esta API son en
formato JSON. Así que aprovecharemos para convertirlos de forma apropiada:
'''

sc_tfe = (28.4578025, -16.3563748)
params = dict(latitude=sc_tfe[0], longitude=sc_tfe[1], hourly='temperature_2m')
url = 'https://api.open-meteo.com/v1/forecast'

response = requests.get(url, params=params)

print(response.url) # https://api.open-meteo.com/v1/forecast?latitude=28.4578025&longitude=-16.3563748&hourly=temperature_2m

data = response.json()
print(type(data)) # dict

print(data.keys()) # dict_keys([ utc_offset_seconds , elevation , latitude , hourly_units , longitude, generationtime_ms , hourly ])

'''
Ahora podríamos mostrar la predicción de temperatures de una manera algo más visual.
Según la documentación de la API sabemos que la respuesta contiene 168 medidas de
temperatura correspondientes a todas las horas durante 7 días. 

Supongamos que sólo queremos mostrar la predicción de temperaturas hora a hora para el día de mañana:
'''

temperatures = data['hourly']['temperature_2m']
# Las temperaturas también incluyen el día de hoy
for i, temp in enumerate(temperatures[24:48], start=1):
    print(f'{temp:4.1f}', end=' ')
    if i % 6 == 0:
        print()

# 12.0 11.9 11.9 11.8 11.8 11.7
# 11.7 11.7 11.6 12.0 12.8 13.6
# 13.9 14.0 14.1 13.9 13.7 13.3
# 12.8 12.2 11.8 11.7 11.6 11.5


#--------------------------
# REQUESTS.ANALIZANDO LA RESPUESTA.CABECERAS DE RESPUESTA
#--------------------------

'''
Tras una petición HTTP es posible recuperar las cabeceras que vienen en la respuesta a
través del atributo headers como un diccionario:
'''

response = requests.get('https://pypi.org')
print(response.status_code) # 200

print(response.headers.get('Content-Type')) # text/html; charset=UTF-8

print(response.headers.get('Server')) # 'nginx/1.13.9'

#--------------------------
# REQUESTS.ANALIZANDO LA RESPUESTA.COOKIES
#--------------------------

'''
Si una respuesta contiene «cookies» es posible acceder a ellas mediante el diccionario cookies:

Nota: Las cookies también se pueden enviar en la petición usando requests.get(url, cookies=cookies).
'''

response = requests.get('https://github.com')

print(response.cookies.keys()) # ['_octo','logged_in','_gh_sess']

print(response.cookies.get('logged_in')) # 'no'


#--------------------------
# REQUESTS.DESCARGAR UN FICHERO
#--------------------------

'''
Hay ocasiones en las que usamos requests para descargar un fichero, bien sea en texto plano
o binario. Veamos cómo proceder para cada tipo.
'''

#--------------------------
# REQUESTS.DESCARGAR UN FICHERO.EN TEXTO PLANO
#--------------------------

'''
El procedimiento que utilizamos es descargar el contenido desde la url y volcarlo a un fichero
de manera estándar:

Consejo: Usamos response.text para obtener el contenido ya que nos interesa en formato
«unicode».
'''

url = 'https://www.ine.es/jaxi/files/tpx/es/csv_bdsc/50155.csv'

response = requests.get(url)

print(response.status_code) # 200

with open('data.csv','w') as f:
    f.write(response.text)


#--------------------------
# REQUESTS.DESCARGAR UN FICHERO.BINARIOS
#--------------------------

'''
Para descargar ficheros binarios seguimos la misma estructura que para ficheros en texto
plano, pero indicando el tipo binario a la hora de escribir en disco:

Consejo: Usamos response.content para obtener el contenido ya que nos interesa en formato «bytes».
'''

url = 'https://www.ine.es/jaxi/files/tpx/es/xlsx/50155.xlsx'

response = requests.get(url)

print(response.status_code) # 200

with open('data.xlsx','wb') as f:
    f.write(response.content)


#--------------------------
# REQUESTS.DESCARGAR UN FICHERO.NOMBRE DE FICHERO
#--------------------------

'''
En los ejemplos anteriores hemos puesto el nombre de fichero «a mano». Pero podría
darse la situación de necesitar el nombre de fichero que descargamos. Para ello existen dos
aproximaciones en función de si aparece o no la clave «attachment» en las cabeceras de
respuesta.

Podemos escribir la siguiente función para ello:
'''
def get_filename(response):
    try:
        return response.headers['Content-Disposition'].split(';')[1].split('=')[1]
    except (KeyError, IndexError):
        return response.url.split('/')[-1]

'''
Caso para el que no disponemos de la cabecera adecuada:
'''

url = 'https://media.readthedocs.org/pdf/pytest/latest/pytest.pdf'
response = requests.get(url)

# 'attachment' in response.headers.get('Content-Disposition') # False

print(get_filename(response)) # pytest.pdf

'''
Caso para el que sí disponemos de la cabecera adecuada:
'''

url = 'https://www.ine.es/jaxi/files/tpx/es/csv_bdsc/45070.csv'
response = requests.get(url)

print('attachment' in response.headers.get('Content-Disposition')) # True

print(get_filename(response)) # 45070.csv

