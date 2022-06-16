#----------
# CLASES
#----------

# Crear una clase
class StarWarsDroid: 
    pass

# Crear objetos o instancias de la clase
c3po = StarWarsDroid() 
r2d2 = StarWarsDroid() 
bb8 = StarWarsDroid()

print(type(c3po)) #el tipo que devuelve el objeto creado : __main__.StarWarsDroid

# Creamos un objeto nuevo
blue_droid = StarWarsDroid() 
golden_droid = StarWarsDroid() 

#----------
# CLASES.ATRIBUTOS
#----------

# Le añadimos atributos a los objetos ya creados
golden_droid.name = 'C-3PO' 
blue_droid.name = 'R2-D2'
blue_droid.height = 1.09
blue_droid.num_feet = 3
blue_droid.partner_droid = golden_droid # otro droide como atributo

# Accedemos a los atributos
print(golden_droid.name)
print(blue_droid.num_feet)

# Definimos un droide "socio"
print(blue_droid.partner_droid.name) #accedemos al nombre del droide socio

print(blue_droid.partner_droid.num_feet) # aún sin definir el atributo da error

blue_droid.partner_droid.num_feet = 2 # definimos el atributo


#----------
# CLASES.METODOS
#----------

# Creamos la clase
class Droid: 
    # Creacion de los metodos, se definen igual que las funciones pero se agrega
    # el primer parametro "self" que hace referencia a la instancia actual del obj
    def switch_on(self):
        print("Hi! I m a droid. Can I help you?")

    def switch_off(self):
        print("Bye! I m going to sleep")

k2so = Droid()
k2so.switch_on() # Hi! I m a droid. Can I help you?
k2so.switch_off() # Bye! I m going to sleep


#----------
# CLASES.METODOS.CONSTRUCTOR
#----------

# Creamos la clase
class Droid:
    # Creamos el constructor con el metodo especial "__init__"
    def __init__(self, name):
        self.name = name

# Creación del objeto (y llamada implícita al constructor)
droid = Droid('BB-8')
print(droid.name) # 'BB-8'


#----------
# CLASES.ATRIBUTOS.ACCESO DIRECTO
#----------

# En el siguiente ejemplo vemos que, aunque el atributo name se ha creado en el constructor
# de la clase, también podemos modificarlo desde «fuera» con un acceso directo
class Droid:
    def __init__(self, name):
        self.name = name

droid = Droid('C-3PO')
print(droid.name) # 'C-3PO'
droid.name = 'waka-waka' # esto sería válido


#----------
# CLASES.ATRIBUTOS.PROPIEDADES
#----------

# Los atributos son publicos, se puede regular la privacidad de los atributos 
# con el uso de propiedades. La forma mas comun de aplicarlas son atraves de "decoradores"

# • @property para leer el valor de un atributo.
# • @name.setter para escribir el valor de un atributo.

class Droid:
    def __init__(self, name):
        self.hidden_name = name

    @property
    def name(self):
        print('Dentro del getter')
        return self.hidden_name
    
    @name.setter
    def name(self, name):
        print('Dentro del setter')
        self.hidden_name = name

droid = Droid('N1-G3L')
print(droid.name) # Dentro del getter # 'N1-G3L'
droid.name = 'Nigel' # Dentro del setter 
print(droid.name) # Dentro del getter # 'Nigel'

# En cualquier caso, seguimos pudiendo acceder directamente a .hidden_name

print(droid.hidden_name) # 'Nigel'


#----------
# CLASES.ATRIBUTOS.PROPIEDADES.VALORES CALCULADOS
#----------

# Una propiedad también se puede usar para devolver un valor calculado (o computado).

class AstromechDroid:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    @property
    def periscope_height(self):
        return 0.3 * self.height

droid = AstromechDroid('R2-D2', 1.05)
print(droid.periscope_height) # podemos acceder como atributo # 0.315
droid.periscope_height = 10 # no podemos modificarlo:
'''
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
AttributeError: can t set attribute
'''


#----------
# CLASES.ATRIBUTOS.PROPIEDADES.OCULTANDO ATRIBUTOS
#----------

# Python tiene una convención sobre aquellos atributos que queremos hacer «privados» (u ocultos):
# comenzar el nombre con doble subguión __

class Droid:
    def __init__(self, name):
        self.__name = name

droid = Droid('BC-44')
print(droid.__name) # efectivamente no aparece como atributo
'''
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
AttributeError: Droid object has no attribute __name
'''

# Lo que realmente ocurre tras el telón se conoce como «name mangling» y consiste en
# modificar el nombre del atributo incorporado la clase como un prefijo. Sabiendo esto podemos
# acceder al valor del atributo supuestamente privado

print(droid._Droid__name) # 'BC-44'


#----------
# CLASES.ATRIBUTOS.PROPIEDADES.ATRIBUTOS DE CLASE
#----------

#Podemos asignar atributos a las clases y serán heredados por todos los objetos 
# instanciados de esa clase.
# A modo de ejemplo, en un principio, todos los droides están diseñados para que obedezcan
# a su dueño. Esto lo conseguiremos a nivel de clase, salvo que ese comportamiento se
# sobreescriba:

class Droid:
    obeys_owner = True # obedece a su dueño

good_droid = Droid()
print(good_droid.obeys_owner) # True

t1000 = Droid()
t1000.obeys_owner = False # T-1000 (Terminator)
print(t1000.obeys_owner) # False
print(Droid.obeys_owner) # el cambio no afecta a nivel de clase # True


#----------
# CLASES.METODOS.DE INSTANCIA
#----------

# Un método de instancia es un método que modifica el comportamiento del objeto al que
# hace referencia. Recibe self como primer parámetro, el cual se convierte en el propio objeto
# sobre el que estamos trabajando. Python envía este argumento de forma transparente

class Droid:
    def __init__(self, name): # método de instancia -> constructor
        self.name = name
        self.covered_distance = 0

    def move_up(self, steps): # método de instancia
        self.covered_distance += steps
        print(f'Moving {steps} steps')

droid = Droid('C1-10P')
print(droid.move_up(10)) # Moving 10 steps


#----------
# CLASES.METODOS.DE CLASE
#----------

# Un método de clase es un método que modifica el comportamiento de la clase a la
# que hace referencia. Recibe cls como primer parámetro, el cual se convierte en la propia
# clase sobre la que estamos trabajando. Python envía este argumento de forma transparente.
# La identificación de estos métodos se completa aplicando el decorador @classmethod a la
# función.
# Veamos un ejemplo en el que implementaremos un método de clase que lleva la cuenta de
# los droides que hemos creado:

class Droid:
    count = 0

    def __init__(self):
        Droid.count += 1

    @classmethod
    def total_droids(cls):
        print(f'{cls.count} droids built so far!')

droid1 = Droid()
droid2 = Droid()
droid3 = Droid()
Droid.total_droids() # 3 droids built so far!


#----------
# CLASES.METODOS.ESTATICOS
#----------

# Un método estático es un método que no modifica el comportamiento del objeto ni de la
# clase. No recibe ningún parámetro especial. La identificación de estos métodos se completa
# aplicando el decorador @staticmethod a la función.
# Veamos un ejemplo en el que creamos un método estático para devolver las categorías de
# droides que existen en StarWars:

class Droid:
    def __init__(self):
        pass

    @staticmethod
    def get_droids_categories():
        return ['Messeger','Astromech','Power','Protocol']

print(Droid.get_droids_categories()) # ['Messeger','Astromech','Power','Protocol']


#----------
# CLASES.METODOS.MAGICOS
#----------


# Los métodos mágicos empiezan y terminan por doble subguión __ (es por ello que también
# se les conoce como «dunder-methods»). Uno de los «dunder-methods» más famosos es el
# constructor de una clase: __init__().

# Importante: Digamos que los métodos mágicos se «disparan» de manera transparente
# cuando utilizamos ciertas estructuras y expresiones del lenguaje.

# Para el caso de los operadores, existe un método mágico asociado (que podemos personalizar).
# Por ejemplo la comparación de dos objetos se realiza con el método __eq__():

# Extrapolando esta idea a nuestro universo StarWars, podríamos establecer que dos droides
# son iguales si su nombre es igual, independientemente de que tengan distintos números de
# serie:


class Droid:
    def __init__(self, name, serial_number):
        self.serial_number = serial_number
        self.name = name

    def __eq__(self, droid):
        return self.name == droid.name

droid1 = Droid('C-3PO', 43974973242)
droid2 = Droid('C-3PO', 85094905984)
droid1 == droid2 # llamada implícita a __eq__ # True
droid1.__eq__(droid2) # True


# Veamos un ejemplo en el que «sumamos» dos droides. Esto se podría ver como una fusión.
# Supongamos que la suma de dos droides implica: 
# a) que el nombre del droide resultante es la concatenación de los nombres de los droides
# b) que la energía del droide resultante es la suma de la energía de los droides:

class Droid:
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def __add__(self, droid):
        new_name = self.name + '-' + droid.name
        new_power = self.power + droid.power
        return Droid(new_name, new_power) # Hay que devolver un objeto de tipo Droid

droid1 = Droid('C3PO', 45)
droid2 = Droid('R2D2', 91)
droid3 = droid1 + droid2
print(f'Fusion droid:\n{droid3.name} with power {droid3.power}')
# Fusion droid:
# C3PO-R2D2 with power 136


# Uno de los métodos mágicos más utilizados es __str__ que permite establecer la forma en
# la que un objeto es representado como cadena de texto:


class Droid:
    def __init__(self, name, serial_number):
        self.serial_number = serial_number
        self.name = name
    def __str__(self):
        return f'Droid "{self.name}" serial-no {self.serial_number}'

droid = Droid('K-2SO', 8403898409432)
print(droid) # llamada a droid.__str__() # Droid "K-2SO" serial-no 8403898409432
str(droid) # Droid "K-2SO" serial-no 8403898409432
f'Droid -> {droid}' # 'Droid -> Droid "K-2SO" serial-no 8403898409432'


# Otros operadores magicos disponibles: 

# De comparacion: 
# __eq__ (==)
# __ne__ (!=)
# __lt__ (<)
# __gt__ (>)
# __le__ (<=)
# __ge__ (>=)

# De matematicas: 
# __add__ (+)
# __sub__ (-)
# __mul__ (*)
# __floordiv__ (//)
# __truediv__ (/)
# __mod__ (%)
# __pow__ (**)


#----------
# CLASES.METODOS.MAGICOS.GESTORES DE CONTEXTO
#----------

# Se trata de un bloque de código en Python que engloba una serie
# de acciones a la entrada y a la salida del mismo.

# Hay dos métodos que son utilizados para implementar los gestores de contexto:
# __enter__() Acciones que se llevan a cabo al entrar al contexto.
# __exit__() Acciones que se llevan a cabo al salir del contexto.

# Veamos un ejemplo en el que implementamos un gestor de contexto que mide tiempos de
# ejecución:


from time import time

class Timer():
    def __enter__(self):
        self.start = time()
    
    def __exit__(self, exc_type, exc_value, exc_traceback):
        # Omit exception handling
        self.end = time()
        exec_time = self.end - self.start
        print(f'Execution time (seconds): {exec_time:.5f}')
with Timer():
    for _ in range(1_000_000):
        x = 2 ** 20
# Execution time (seconds): 0.05283
with Timer():
    x = 0
    for _ in range(1_000_000):
        x += 2 ** 20
# Execution time (seconds): 0.08749


#----------
# CLASES.HERENCIA
#----------

# La herencia consiste en crear una nueva clase partiendo de una clase existente, pero
# que añade o modifica ciertos aspectos. Se considera una buena práctica tanto para reutilizar
# código como para realizar generalizaciones.

# Nota: Cuando se utiliza herencia, la clase derivada, de forma automática, puede usar todo
# el código de la clase base sin necesidad de copiar nada explícitamente.


#----------
# CLASES.HERENCIA.DESDE UNA CLASE BASE
#----------

# Para que una clase «herede» de otra, basta con indicar la clase base entre paréntesis en la
# definición de la clase derivada.

# Sigamos con el ejemplo. Una de las grandes categorías de droides en StarWars es la de droides
# de protocolo. Vamos a crear una herencia sobre esta idea:

class Droid:
    # Clase Base
    pass

class ProtocolDroid(Droid):
    # Sub Clase 
    pass

issubclass(ProtocolDroid, Droid) # comprobación de herencia # True

r2d2 = Droid()
c3po = ProtocolDroid()

# Vamos a añadir un par de métodos a la clase base, y analizar su comportamiento:

class Droid:
    def switch_on(self):
        print("Hi! I m a droid. Can I help you?")

    def switch_off(self):
        print("Bye! I m going to sleep")

class ProtocolDroid(Droid):
    pass

r2d2 = Droid()
c3po = ProtocolDroid()
r2d2.switch_on() # Hi! I m a droid. Can I help you?
c3po.switch_on() # método heredado de Droid # Hi! I m a droid. Can I help you?
r2d2.switch_off() # Bye! I m going to sleep


#----------
# CLASES.HERENCIA.SOBREESCRIBIR UN METODO
#----------

# Como hemos visto, una clase derivada hereda todo lo que tiene su clase base. Pero en muchas
# ocasiones nos interesa modificar el comportamiento de esta herencia.

# En el ejemplo vamos a modificar el comportamiento del método switch_on() para la clase
# derivada:

class Droid:
    def switch_on(self):
        print("Hi! I m a droid. Can I help you?")

    def switch_off(self):
        print("Bye! I m going to sleep")

class ProtocolDroid(Droid):
    def switch_on(self):
        print("Hi! I m a PROTOCOL droid. Can I help you?")

r2d2 = Droid()
c3po = ProtocolDroid()
r2d2.switch_on() # Hi! I m a droid. Can I help you?
c3po.switch_on() # método heredado pero sobreescrito # Hi! I m a PROTOCOL droid. Can I help you?


#----------
# CLASES.HERENCIA.AÑADIR UN METODO
#----------

# La clase derivada también puede añadir métodos que no estaban presentes en su clase base.

# En el siguiente ejemplo vamos a añadir un método translate() que permita a los droides
# de protocolo traducir cualquier mensaje:


class Droid:
    def switch_on(self):
        print("Hi! I m a droid. Can I help you?")

    def switch_off(self):
        print("Bye! I m going to sleep")

class ProtocolDroid(Droid):
    def switch_on(self):
        print("Hi! I m a PROTOCOL droid. Can I help you?")

    def translate(self, msg, from_language):
        # Translate from language to Human understanding
        print(f'{msg} means "ZASCA" in {from_language}')

r2d2 = Droid()
c3po = ProtocolDroid()

c3po.translate('kiitos','Huttese') # idioma de Watoo # kiitos means "ZASCA" in Huttese
r2d2.translate('kiitos','Huttese') # droide genérico no puede traducir
# Traceback (most recent call last):
# File "<stdin>", line 1, in <module>
# AttributeError: Droid object has no attribute translate


#----------
# CLASES.HERENCIA.ACCEDIENDO A LA CLASE BASE
#----------

# Puede darse la situación en la que tengamos que acceder desde la clase derivada a métodos
# o atributos de la clase base. Python ofrece super() como mecanismo para ello.

# Veamos un ejemplo más elaborado con nuestros droides:

class Droid:
    def __init__(self, name):
        self.name = name

class ProtocolDroid(Droid):
    def __init__(self, name, languages):
        super().__init__(name) # llamada al constructor de la clase base
        self.languages = languages

droid = ProtocolDroid('C-3PO', ['Ewokese','Huttese','Jawaese'])
droid.name # fijado en el constructor de la clase base # C-3PO
droid.languages # fijado en el constructor de la clase derivada #['Ewokese','Huttese','Jawaese']


#----------
# CLASES.HERENCIA MULTIPLE
#----------

