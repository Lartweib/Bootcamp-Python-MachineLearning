

'''
Ejercicio 4
Realizar un programa en el cual se declaren dos valores enteros por teclado utilizando
el método __init__. Calcular después la suma, resta, multiplicación y división. Utilizar
un método para cada una e imprimir los resultados obtenidos. Llamar a la clase
Calculadora.
'''

def ValidadorDeInput():
    while True:
        valor = input('Ingrese un numero: ')
        try:
            valor = float(valor)
            return valor
        except:
            print('Ingrese un numero entero o un numero decimal utilizando el punto como separador')
    
class Calculadora:
    def __init__(self):
        self.valorA = ValidadorDeInput()
        self.valorB = ValidadorDeInput()
        
    def sumar(self):
        self.suma = self.valorA + self.valorB
        return print(f'{self.valorA} + {self.valorB} = {self.suma}')        
        
    def restar(self):
        self.resta = self.valorA - self.valorB
        return print(f'{self.valorA} - {self.valorB} = {self.resta}')       

    def multiplicar(self):    
        self.multiplicacion = self.valorA * self.valorB
        return print(f'{self.valorA} x {self.valorB} = {self.multiplicacion}') 
        
    def dividir(self):
        self.division = None
        if self.valorB == 0:
            self.division = 'No se puede dividir entre cero.'
        else: 
            self.division = self.valorA / self.valorB
        return print(f'{self.valorA} / {self.valorB} = {self.division}')  

print('calculo 1')
calculo1 = Calculadora()
calculo1.sumar()
calculo1.restar()
calculo1.multiplicar()
calculo1.dividir()

print('calculo 2')
calculo2 = Calculadora()
calculo2.sumar()
calculo2.restar()
calculo2.multiplicar()
calculo2.dividir()

print('calculo 3')
calculo3 = Calculadora()
calculo3.sumar()
calculo3.restar()
calculo3.multiplicar()
calculo3.dividir()

print('calculo 4')
calculo4 = Calculadora()
calculo4.sumar()
calculo4.restar()
calculo4.multiplicar()
calculo4.dividir()
