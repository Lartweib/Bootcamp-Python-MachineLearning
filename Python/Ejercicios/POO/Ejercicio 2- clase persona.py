'''
Ejercicio 2
Realizar un programa que tenga una clase Persona con las siguientes características. La
clase tendrá como atributos el nombre y la edad de una persona. Implementar los
métodos necesarios para inicializar los atributos, mostrar los datos e indicar si la
persona es mayor de edad o no.
'''

print("---- Ejercicio 2 ----")
class Persona:
    def __init__(self, nombre: str, edad: int):
        self.nombre = nombre
        self.edad = edad
        self.mayor = 'mayor de edad' if self.edad >=18 else 'menor de edad'

    def __str__ (self):
        return f'La persona llamada {self.nombre} tiene {self.edad} años y es {self.mayor}.'

    def mayorDeEdad(self):
        return print(f'{self.nombre} es {self.mayor}.')

persona1 = Persona('Federico', 8)
persona2 = Persona('Juan', 25)
persona3 = Persona('Jorge', 63)

print(persona1)
persona1.mayorDeEdad()
print(persona2)
persona2.mayorDeEdad()
print(persona3)
persona3.mayorDeEdad()
