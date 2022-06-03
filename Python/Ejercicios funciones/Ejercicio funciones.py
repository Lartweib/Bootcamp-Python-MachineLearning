'''
Ejercicios de Funciones
Ejercicio 1
Escribir una función que muestre por pantalla el
saludo ¡Hola amiga! cada vez que se la invoque.
'''
print("--- Ejercicio 1 ---")
def saludo():
  print("¡Hola amiga!")

saludo()
'''
Ejercicio 2
Escribir una función a la que se le pase una
cadena <nombre> y muestre por pantalla el saludo ¡hola
<nombre>!.
'''
print("--- Ejercicio 2 ---")
def saludo(nombre):
  print(f"¡Hola {nombre}!")

saludo("Federico")

'''
Ejercicio 3
Escribir una función que reciba un número entero positivo y
devuelva su factorial.
'''
print("--- Ejercicio 3 ---")
def factorial(num):
  factorial = 1
  for i in range(1,num):
    factorial *= i+1
  return factorial

print(factorial(4))
print(factorial(5))


'''
Ejercicio 4
Escribir una función que calcule el total de una factura tras
aplicarle el IVA. La función debe recibir la cantidad sin IVA
y el porcentaje de IVA a aplicar, y devolver el total de la
factura. Si se invoca la función sin pasarle el porcentaje de
IVA, deberá aplicar un 21%.
'''
print("--- Ejercicio 4 ---")
def factura_final(importe,iva=21):
  final = importe * (iva/100+1)
  return final

factura_final(1000)

'''
Ejercicio 5
Escribir una función que calcule el área de un círculo y otra
que calcule el volumen de un cilindro usando la primera
función.
'''
print("--- Ejercicio 5 ---")
import math

def area(radio):
  pi = math.pi 
  area = pi * radio ** 2
  return area

def volumen_cil(radio, altura):
  volumen = area(radio) * altura
  return volumen

print(area(2))
print(volumen_cil(2,3))

'''
Ejercicio 6
Escribir una función que reciba una muestra de números en
una lista y devuelva su media.
'''
print("--- Ejercicio 6 ---")

def media(*args):
  cant = len(args)
  suma= 0
  for i in args:
    suma += i
  media = suma / cant
  return media

print(media(1,1,1,1,1,1))
'''
Ejercicio 7

Escribir una función que reciba una muestra de números en
una lista y devuelva otra lista con sus cuadrados.
'''
print("--- Ejercicio 7 ---")
lista_num = list(range(10))
def cuadrados(lista):
  cuadrados_list = []
  for i in lista:
    cuadrados_list.append(i**2)
  return cuadrados_list 

print(cuadrados(lista_num))
'''
Ejercicio 8
Escribir una función que reciba una muestra de números en
una lista y devuelva un diccionario con su media, varianza y
desviación típica.
'''
print("--- Ejercicio 8 ---")
lista_num = list(range(10))

def diccionario(lista_num):
    dic_1 = {}
    suma_num = 0
    sum_cuadrados = 0
    varianza = 0
    for i in lista_num:
        suma_num += i
        sum_cuadrados += i**2
    media = suma_num/len(lista_num)
    desviacion = (sum_cuadrados/len(lista_num)-media*2)*(1/2)
    for i in lista_num:
        varianza += (i-media)*2
    varianza = varianza/len(lista_num)
    dic_1["Media"]= media
    dic_1["Varianza"]= varianza
    dic_1["Desviacion"]=desviacion
    return dic_1
print(lista_num)
print(diccionario(lista_num))

dic = {"lista_num":diccionario(lista_num)}
print(dic)

'''
Ejercicio 9
Escribir una función que calcule el máximo común divisor
de dos números y otra que calcule el mínimo común
múltiplo.
'''
print("--- Ejercicio 9 ---")



'''
Ejercicio 10
Escribir una función que convierta un número decimal en
binario y otra que convierta un número binario en decimal.
'''
print("--- Ejercicio 10 ---")

'''
Ejercicio 11
Escribir un programa que reciba una cadena de caracteres
y devuelva un diccionario con cada palabra que contiene y
su frecuencia. Escribir otra función que reciba el diccionario
generado con la función anterior y devuelva una tupla con
la palabra más repetida y su frecuencia.
'''
print("--- Ejercicio 11 ---")
