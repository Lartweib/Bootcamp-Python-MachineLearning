#--------------------------
# BEAUTIFULSOUP
#--------------------------

'''
El paquete Beautiful Soup es ampliamente utilizado en técnicas de «scraping» permitiendo
«parsear» principalmente código HTML

$ pip install beautifulsoup4
'''


#--------------------------
# BEAUTIFULSOUP.HACIENDO LA SOPA
#--------------------------

'''
Para empezar a trabajar con Beautiful Soup es necesario construir un objeto de tipo
BeautifulSoup que reciba el contenido a «parsear»:
'''
from bs4 import BeautifulSoup

contents ='''
<html lang="en">
<head>
    <title>Just testing</title>
</head>
<body>
    <h1>Just testing</h1>
    <div class="block">
        <h2>Some links</h2>
        <p>Hi there!</p>
        <ul id="data">
            <li class="blue"><a href="https://example1.com">Example 1</a></li>
            <li class="red"><a href="https://example2.com">Example 2</a></li>
            <li class="gold"><a href="https://example3.com">Example 3</a></li>
        </ul>
    </div>
    <div class="block">
        <h2>Formulario</h2>
        <form action="" method="post">
            <label for="POST-name">Nombre:</label>
            <input id="POST-name" type="text" name="name">
            <input type="submit" value="Save">
        </form>
    </div>
    <div class="footer">
        This is the footer
        <span class="inline"><p>This is span 1</p></span>
        <span class="inline"><p>This is span 2</p></span>
        <span class="inline"><p>This is span 2</p></span>
    </div>
</body>
</html>
'''

soup = BeautifulSoup(contents, features='html.parser')


#--------------------------
# BEAUTIFULSOUP.LOCALIZAR ELEMENTOS
#--------------------------

'''
Una de las tareas más habituales en técnicas de «scraping» y en «parsing» de contenido es
la localización de determinadas elementos de interés.
'''


#--------------------------
# BEAUTIFULSOUP.LOCALIZAR ELEMENTOS.FORMULAS DE LOCALIZACION
#--------------------------

'''
A continuación se muestran, mediante ejemplos, distintas fórmulas para localizar elementos
dentro del DOM:

• Localizar todos los enlaces:
'''

print(soup.find_all('a'))
# [<a href="https://example1.com">Example 1</a>,
# <a href="https://example2.com">Example 2</a>,
# <a href="https://example3.com">Example 3</a>]

'''
El primer argumento posicional de find_all() es el nombre del «tag» que queremos
localizar.

• Localizar todos los elementos con la clase inline:
'''

print(soup.find_all(class_='inline'))
# [<span class="inline"><p>This is span 1</p></span>,
# <span class="inline"><p>This is span 2</p></span>,
# <span class="inline"><p>This is span 2</p></span>]

'''
Los argumentos nominales de find_all() se utilizan para localizar elementos que
contengan el atributo referenciado.

Truco: Si el atributo a localizar tiene guiones medios (por ejemplo aria-label) no
podremos usarlo como nombre de argumento (error sintáctico). Pero sí podemos usar
un diccionario en su lugar:
'''

print(soup.find_all(attrs={'aria-label':'box'}))

'''
• Localizar todos los «divs» con la clase footer:
'''

print(soup.find_all('div', class_='footer')) # ≈ soup.find_all('div','footer')
# [<div class="footer">
# This is the footer
# <span class="inline"><p>This is span 1</p></span>
# <span class="inline"><p>This is span 2</p></span>
# <span class="inline"><p>This is span 2</p></span>
# </div>]

'''
• Localizar todos los elementos cuyo atributo type tenga el valor text:
'''

print(soup.find_all(type='text'))
# [<input id="POST-name" name="name" type="text"/>]

'''
• Localizar todos los los h2 que contengan el texto Formulario:
'''

print(soup.find_all('h2', string='Formulario'))
# [<h2>Formulario</h2>]

'''
• Localizar todos los elementos de título h1, h2, h3, .... Esto lo podemos atacar
usando expresiones regulares:
'''
import re

print(soup.find_all(re.compile(r'^h\d+.*')))
# [<h1>Just testing</h1>, <h2>Some links</h2>, <h2>Formulario</h2>]

'''
• Localizar todos los «input» y todos los «span»:
'''

print(soup.find_all(['input','span']))
# [<input id="POST-name" name="name" type="text"/>,
# <input type="submit" value="Save"/>,
# <span class="inline"><p>This is span 1</p></span>,
# <span class="inline"><p>This is span 2</p></span>,
# <span class="inline"><p>This is span 2</p></span>]

'''
• Localizar todos los párrafos que están dentro del pie de página (usando selectores
CSS):
'''

print(soup.select('.footer p'))
# [<p>This is span 1</p>, <p>This is span 2</p>, <p>This is span 2</p>]

'''
Nota: En este caso se usa el método select().
'''


#--------------------------
# BEAUTIFULSOUP.LOCALIZAR ELEMENTOS.LOCALIZAR UNICO ELEMENTO
#--------------------------

'''
Hasta ahora hemos visto las funciones find_all() y select() que localizan un conjunto de
elementos. Incluso en el caso de encontrar sólo un elemento, se devuelve una lista con ese
único elemento.

Beautiful Soup nos proporciona la función find() que trata de localizar un único
elemento. Hay que tener en cuenta dos circunstancias:

• En caso de que el elemento buscado no exista, se devuelve None.
• En caso de que existan múltiples elementos, se devuelve el primero.

Veamos algunos ejemplos de esto:
'''

print(soup.find('form'))
# <form action="" method="post">
# <label for="POST-name">Nombre:</label>
# <input id="POST-name" name="name" type="text"/>
# <input type="submit" value="Save"/>
# </form>

# Elemento que no existe
print(soup.find('strange-tag')) # (no devuelve nada)

# Múltiples "li". Sólo se devuelve el primero
print(soup.find('li'))
# <li class="blue"><a href="https://example1.com">Example 1</a></li>


#--------------------------
# BEAUTIFULSOUP.LOCALIZAR ELEMENTOS.LOCALIZAR DESDE ELEMENTO
#--------------------------

'''
Todas las búsquedas se pueden realizar desde cualquier elemento preexistente, no únicamente
desde la raíz del DOM.

Veamos un ejemplo de ello. Si tratamos de localizar todos los títulos «h2» vamos a
encontrar dos de ellos:
'''

print(soup.find_all('h2'))
# [<h2>Some links</h2>, <h2>Formulario</h2>]

'''
Pero si, previamente, nos ubicamos en el segundo bloque de contenido, sólo vamos a encontrar
uno de ellos:
'''

second_block = soup.find_all('div','block')[1]
print(second_block)
# <div class="block">
# <h2>Formulario</h2>
# <form action="" method="post">
# <label for="POST-name">Nombre:</label>
# <input id="POST-name" name="name" type="text"/>
# <input type="submit" value="Save"/>
# </form>
# </div>

print(second_block.find_all('h2'))
# [<h2>Formulario</h2>]


#--------------------------
# BEAUTIFULSOUP.LOCALIZAR ELEMENTOS.OTRAS FUNCIONES DE BUSQUEDA
#--------------------------


'''
Hay definidas una serie de funciones adicionales de búsqueda para cuestiones más
particulares:

• Localizar los «div» superiores a partir de un elemento concreto:
'''

gold = soup.find('li','gold')
print(gold.find_parents('div'))
# [<div class="block">
# <h2>Some links</h2>
# <p>Hi there!</p>
# <ul id="data">
# <li class="blue"><a href="https://example1.com">Example 1</a></li>
# <li class="red"><a href="https://example2.com">Example 2</a></li>
# <li class="gold"><a href="https://example3.com">Example 3</a></li>
# </ul>
# </div>]

'''
Se podría decir que la función find_all() busca en descendientes y que la función
find_parents() busca en ascendientes.

También existe la versión de esta función que devuelve un único elemento:
find_parent().

• Localizar los elementos hermanos siguientes a uno dado:
'''

blue_li = soup.find('li','blue')
print(blue_li.find_next_siblings())
# [<li class="red"><a href="https://example2.com">Example 2</a></li>,
# <li class="gold"><a href="https://example3.com">Example 3</a></li>]

'''
Al igual que en las anteriores, es posible aplicar un filtro al usar esta función.
También existe la versión de esta función que devuelve un único elemento:
find_next_sibling().

• Localizar los elementos hermanos anteriores a uno dado:
'''

gold_li = soup.find('li','gold')
print(gold_li.find_previous_siblings())
# [<li class="red"><a href="https://example2.com">Example 2</a></li>,
# <li class="blue"><a href="https://example1.com">Example 1</a></li>]

'''
Al igual que en las anteriores, es posible aplicar un filtro al usar esta función.
También existe la versión de esta función que devuelve un único elemento:
find_previous_sibling().

• Localizar todos los elementos a continuación de uno dado:
'''

submit = soup.find('input', type='submit')
print(submit.find_all_next())
# [<div class="footer">
# This is the footer
# <span class="inline"><p>This is span 1</p></span>
# <span class="inline"><p>This is span 2</p></span>
# <span class="inline"><p>This is span 2</p></span>
# </div>,
# <span class="inline"><p>This is span 1</p></span>,
# <p>This is span 1</p>,
# <span class="inline"><p>This is span 2</p></span>,
# <p>This is span 2</p>,
# <span class="inline"><p>This is span 2</p></span>,
# <p>This is span 2</p>]

'''
Al igual que en las anteriores, es posible aplicar un filtro al usar esta función.
También existe la versión de esta función que devuelve un único elemento: find_next().

• Localizar todos los elementos previos a uno dado:
'''

ul_data = soup.find('ul', id='data')

print(ul_data.find_all_previous(['h1','h2']))
# [<h2>Some links</h2>, <h1>Just testing</h1>]

'''
También existe la versión de esta función que devuelve un único elemento:
find_previous().

Si hubiéramos hecho esta búsqueda usando find_parents() no habríamos obtenido el
mismo resultado ya que los elementos de título no son elementos superiores de «ul»:
'''

print(ul_data.find_parents(['h1','h2'])) # []


#--------------------------
# BEAUTIFULSOUP.LOCALIZAR ELEMENTOS.ATAJOS PARA BUSQUEDAS
#--------------------------

'''
Dado que la función find_all() es la más utilizada en Beautiful Soup se ha implementado
un atajo para llamarla:
'''

print(soup.find_all('span'))
# [<span class="inline"><p>This is span 1</p></span>,
# <span class="inline"><p>This is span 2</p></span>,
# <span class="inline"><p>This is span 2</p></span>]

print(soup('span'))
# [<span class="inline"><p>This is span 1</p></span>,
# <span class="inline"><p>This is span 2</p></span>,
# <span class="inline"><p>This is span 2</p></span>]

'''
Aunque uno de los preceptos del Zen de Python es «Explicit is better than implicit», el uso
de estos atajos puede estar justificado en función de muchas circunstancias.
'''


#--------------------------
# BEAUTIFULSOUP.ACCEDER AL CONTENIDO
#--------------------------

'''
Simplificando, podríamos decir que cada elemento de la famosa «sopa» de Beautiful Soup
puede ser un bs4.element.Tag o un «string».

Para el caso de los «tags» existe la posibilidad de acceder a su contenido, al nombre del
elemento o a sus atributos.
'''


#--------------------------
# BEAUTIFULSOUP.ACCEDER AL CONTENIDO.NOMBRE DE ETIQUETA
#--------------------------

'''
Podemos conocer el nombre de la etiqueta de un elemento usando el atributo name:

Truco: Es posible modificar el nombre de una etiqueta con una simple asignación.
'''

print(soup.name) # [document]

elem = soup.find('ul', id='data')
print(elem.name) # ul

elem = soup.find('h1')
print(elem.name) # h1


#--------------------------
# BEAUTIFULSOUP.ACCEDER AL CONTENIDO.ACCESO A ATRIBUTOS
#--------------------------

'''
Los atributos de un elemento están disponibles como claves de un diccionario:

'''
elem = soup.find('input', id='POST-name')

print(elem)
# <input id="POST-name" name="name" type="text"/>

print(elem['id'])
# POST-name

print(elem['name'])
# name

print(elem['type'])
# text

'''
Exite una forma de acceder al diccionario completo de atributos:

Truco: Es posible modificar el valor de un atributo con una simple asignación.
'''

print(elem.attrs)
# { id : POST-name , type : text , name : name }


#--------------------------
# BEAUTIFULSOUP.ACCEDER AL CONTENIDO.CONTENIDO TEXTUAL
#--------------------------

'''
Es necesario aclarar las distintas opciones que proporciona Beautiful Soup para acceder al
contenido textual de los elementos del DOM.


Atributo            Devuelve
-------------------------------------------------------------------------------------------
text                Una cadena de texto con todos los contenidos textuales del elemento
                    incluyendo espacios y saltos de línea
-------------------------------------------------------------------------------------------
strings             Un generador de todos los contenidos textuales del elemento incluyendo
                    espacios y saltos de línea
-------------------------------------------------------------------------------------------
stripped_strings    Un generador de todos los contenidos textuales del elemento eliminando
                    espacios y saltos de línea
-------------------------------------------------------------------------------------------
string              Una cadena de texto con el contenido del elemento, siempre que contenga
                    un único elemento textual
-------------------------------------------------------------------------------------------

Ejemplos:
'''

footer = soup.find(class_='footer')

print(footer.text)
# '\n This is the footer\n This is span 1\nThis is span 2\nThis is span 2\n'

print(list(footer.strings))
# [ '\n This is the footer\n ',
# 'This is span 1 ',
# '\n ',
# 'This is span 2 ',
# '\n ',
# 'This is span 2 ',
# '\n ']

print(list(footer.stripped_strings))
# [ 'This is the footer' , 'This is span 1' , 'This is span 2' , 'This is span 2' ]

print(footer.string) # El "footer" contiene varios elementos

print(footer.span.string) # El "span" sólo contiene un elemento
# 'This is span 1'


#--------------------------
# BEAUTIFULSOUP.ACCEDER AL CONTENIDO.MOSTRANDO ELEMENTOS
#--------------------------

'''
Cualquier elemento del DOM que seleccionemos mediante este paquete se representa con el
código HTML que contiene. 

Por ejemplo:
'''

data = soup.find(id='data')

print(data)
# <ul id="data">
# <li class="blue"><a href="https://example1.com">Example 1</a></li>
# <li class="red"><a href="https://example2.com">Example 2</a></li>
# <li class="gold"><a href="https://example3.com">Example 3</a></li>
# </ul>

'''
Existe la posibilidad de mostrar el código HTML en formato «mejorado» a través de la
función prettify():
'''

pretty_data = data.prettify()

print(pretty_data)
# <ul id="data">
#   <li class="blue">
#       <a href="https://example1.com">
#           Example 1
#       </a>
#   </li>
#   <li class="red">
#       <a href="https://example2.com">
#           Example 2
#       </a>
#   </li>
#   <li class="gold">
#       <a href="https://example3.com">
#           Example 3
#       </a>
#   </li>
# </ul>


#--------------------------
# BEAUTIFULSOUP.NAVEGAR POR EL DOM.MOVERSE HACIA ABAJO
#--------------------------

'''
Además de localizar elementos, este paquete permite moverse por los elementos del DOM de
manera muy sencilla.

Para ir profundizando en el DOM podemos utilizar los nombres de los «tags» como
atributos del objeto, teniendo en cuenta que si existen múltiples elementos sólo se accederá
al primero de ellos:
'''

print(soup.div.p)
# <p>Hi there!</p>

print(soup.form.label)
# <label for="POST-name">Nombre:</label>

print(type(soup.span))
# bs4.element.Tag

'''
Existe la opción de obtener el contenido (como lista) de un determinado elemento:
'''

print(type(soup.form)) # todos los elementos del DOM son de este tipo
# bs4.element.Tag

print(soup.form.contents)
# [ \n ,
# <label for="POST-name">Nombre:</label>,
# \n ,
# <input id="POST-name" name="name" type="text"/>,
# \n ,
# <input type="submit" value="Save"/>,
# \n ]

print(type(soup.form.contents))
# list

'''
Advertencia: En la lista que devuelve contents hay mezcla de «strings» y objetos
bs4.element.Tag.

Si no se quiere explicitar el contenido de un elemento como lista, también es posible usar un
generador para acceder al mismo de forma secuencial:
'''

print(soup.form.children)
# <list_iterator at 0x106643100>

for elem in soup.form.children:
    print(repr(elem))

# '\n'
# <label for="POST-name">Nombre:</label>
# '\n'
# <input id="POST-name" name="name" type="text"/>
# '\n'
# <input type="submit" value="Save"/>
# '\n'

'''
El atributo contents sólo tiene en cuenta descendientes directos. Si queremos acceder
a cualquier elemento descendiente (de manera recursiva) tenemos que usar
descendants:

Importante: Tener en cuenta que descendants es un generador que devuelve un iterable.
'''

block = soup.find_all('div')[1]

print(block.contents)
# [ \n ,
# <h2>Formulario</h2>,
# \n ,
# <form action="" method="post">
# <label for="POST-name">Nombre:</label>
# <input id="POST-name" name="name" type="text"/>
# <input type="submit" value="Save"/>
# </form>,
# \n ]

print(block.descendants)
# <generator object Tag.descendants at 0x10675d200>

print(list(block.descendants))
# [ \n ,
# <h2>Formulario</h2>,
# Formulario ,
# \n ,
# <form action="" method="post">
# <label for="POST-name">Nombre:</label>
# <input id="POST-name" name="name" type="text"/>
# <input type="submit" value="Save"/>
# </form>,
# \n ,
# <label for="POST-name">Nombre:</label>,
# Nombre: ,
# \n ,
# <input id="POST-name" name="name" type="text"/>,
# \n ,
# <input type="submit" value="Save"/>,
# \n ,
# \n ]

#--------------------------
# BEAUTIFULSOUP.NAVEGAR POR EL DOM.MOVERSE HACIA ARRIBA
#--------------------------

'''
Para acceder al elemento superior de otro dado, podemos usar el atributo parent:
'''

li = soup.find('li','blue')
li.parent
# <ul id="data">
# <li class="blue"><a href="https://example1.com">Example 1</a></li>
# <li class="red"><a href="https://example2.com">Example 2</a></li>
# <li class="gold"><a href="https://example3.com">Example 3</a></li>
# </ul>

'''
También podemos acceder a todos los elementos superiores (ascendientes) usando el
generador parents:
'''

for elem in li.parents:
    print(elem.name)
# ul
# div
# body
# html
# [document]


#--------------------------
# BEAUTIFULSOUP.NAVEGAR POR EL DOM.OTROS MOVIMIENTOS
#--------------------------

'''
En la siguiente tabla se recogen el resto de atributos que nos permiten movernos a partir de
un elemento del DOM:


Atributo                Descripción
-------------------------------------------------------------------------------
next_sibling            Obtiene el siguiente elemento «hermano»
-------------------------------------------------------------------------------
previous_sibling        Obtiene el anterior elemento «hermano»
-------------------------------------------------------------------------------
next_siblings           Obtiene los siguientes elementos «hermanos» (iterador)
-------------------------------------------------------------------------------
previous_siblings       Obtiene los anteriores elementos «hermanos» (iterador)
-------------------------------------------------------------------------------
next_element            Obtiene el siguiente elemento
-------------------------------------------------------------------------------
previous_element        Obtiene el anterior elemento
-------------------------------------------------------------------------------


Advertencia: Con estos accesos también se devuelven los saltos de línea \n como
elementos válidos. Si se quieren evitar, es preferible usar las funciones definidas aquí .
'''
