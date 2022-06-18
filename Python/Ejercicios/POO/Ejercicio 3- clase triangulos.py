'''
Ejercicio 3
Desarrollar un programa que cargue los datos de un triángulo. Implementar una clase
con los métodos para inicializar los atributos, imprimir el valor del lado con un tamaño
mayor y el tipo de triángulo que es (equilátero, isósceles o escaleno).
'''
print("---- Ejercicio 3 ----")

class Triangulo:

    def __init__(self, ladoa: float, ladob: float, ladoc: float):
        self.ladoa = ladoa
        self.ladob = ladob
        self.ladoc = ladoc
        self.tipo = None
        if self.ladoa == self.ladob and self.ladob == self.ladoc:
            self.tipo = 'equilatero'
        elif self.ladoa == self.ladob or self.ladoa == self.ladoc or self.ladob == self.ladoc:
            self.tipo = 'isósceles'
        else: 
            self.tipo =  'escaleno'    

    def __str__(self):
        return f'Es un triangulo {self.tipo} y las medidas de sus lados son: {self.ladoa},{self.ladob},{self.ladoc}.'

    def ladoMayor(self):
        mayor = None
        if self.ladoa >= self.ladob:
            if self.ladoa >= self.ladoc:
                mayor = self.ladoa
            else:
                mayor =self.ladoc
        else:
            if self.ladob >= self.ladoc:
                mayor = self.ladob
            else:
                mayor = self.ladoc    
        return print(f'El lado mayor mide {mayor}')    
            
trianguloa = Triangulo(30,30,30)
triangulob = Triangulo(30,40,30)
trianguloc = Triangulo(30,20,10)

print(f'Triangulo A: {trianguloa}')
trianguloa.ladoMayor()
print(f'Triangulo B: {triangulob}')
triangulob.ladoMayor()
print(f'Triangulo C: {trianguloc}')
trianguloc.ladoMayor()
