'''
Ejercicio 1
Realizar un programa que conste de una clase llamada Alumno que tenga como
atributos el nombre y la nota del alumno. Definir los métodos para inicializar sus
atributos, imprimirlos y mostrar un mensaje con el resultado de la nota y si ha
aprobado o no.
'''
print("---- Ejercicio 1 ----")
class Alumno:
    def __init__(self, nombre: str, nota: float):
        self.nombre = nombre
        self.nota = nota
        self.aprobado = 'aprobado' if self.nota >=5 else 'desaprobado'

    def __str__ (self):
        return f'El alumno {self.nombre} con nota {self.nota} se encuentra {self.aprobado}.'

alumno1 = Alumno('Federico', 8)
alumno2 = Alumno('Juan', 5)
alumno3 = Alumno('Jorge', 3)

print(alumno1)
print(alumno2)
print(alumno3)
