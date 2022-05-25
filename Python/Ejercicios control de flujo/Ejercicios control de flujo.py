'''
Ejercicios de Bucles

Ejercicio 1
Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10
veces.
'''
print("--- Ejercicio 1 ---")
palabra = input("Ingrese una palabra: ")
i = 0
while i < 10:
  print(palabra)
  i += 1

'''
Ejercicio 2
Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los
años que ha cumplido (desde 1 hasta su edad).
'''
print("--- Ejercicio 2 ---")
edad = int(input("Cual es tu edad? "))
i = 1
while i <= edad:
  print(i)
  i += 1

'''
Ejercicio 3
Escribir un programa que pida al usuario un número entero positivo y muestre por
pantalla todos los números impares desde 1 hasta ese número separados por comas.
'''
print("--- Ejercicio 3 ---")

numero = int(input("Ingrese un numero entero: "))
i = 1
while numero < 0:
  print("El numero debe ser positivo")
  numero = int(input("Ingrese un numero entero: "))
  
while i <= numero:
  if i%2 != 0:
    print(i)
  i += 1

'''
Ejercicio 4
Escribir un programa que pida al usuario un número entero positivo y muestre por
pantalla la cuenta atrás desde ese número hasta cero separados por comas.
'''
print("--- Ejercicio 4 ---")
numero = int(input("Ingrese un numero entero: "))

while numero < 0:
  print("El numero debe ser positivo")
  numero = int(input("Ingrese un numero entero: "))

i = numero

while i >= 0:
  if i != 0: print(i, end=",")
  else: print(i, end=".")
  i -= 1

'''
Ejercicio 5
Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y
el número de años, y muestre por pantalla el capital obtenido en la inversión cada año
que dura la inversión.
'''
print("--- Ejercicio 5 ---")
inversion = int(input("Cantidad a invertir? "))
interes_anual = int(input("Interes anual? "))
cantidad_anios = int(input("Cantidad de años? "))
i = 1
capital = inversion
while i <= cantidad_anios:
  capital_obtenido = capital * (interes_anual/100+1)
  print(f"Año {i}: Capital invertido: {capital}\nCapital obtenido: {capital_obtenido}")
  capital = capital_obtenido
  i+=1

'''
Ejercicio 6
Escribir un programa que pida al usuario un número entero y muestre por pantalla un
triángulo rectángulo como el de más abajo, de altura el número introducido.
*
**
***
****
*****
'''
print("--- Ejercicio 6 ---")
numero = int(input("Ingrese un numero? "))
i = 1
while i <= numero:
  print("*"*i) 
  i+=1

'''
Ejercicio 7
Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10.
'''
print("--- Ejercicio 7 ---")

i = 0
while i <= 10:
  print(f"{i} x 10 = {i*10}") 
  i+=1

'''
Ejercicio 8
Escribir un programa que pida al usuario un número entero y muestre por pantalla un
triángulo rectángulo como el de más abajo.
1
3 1
5 3 1
7 5 3 1
9 7 5 3 1
'''
print("--- Ejercicio 8 ---")
numero = int(input("Ingrese un numero? "))
string = "1"
for i in range(1,numero,2):
  if i == 1:
    print(string)
  else: 
    string += " "
    string += str(i)
    print(string[::-1])

'''
Ejercicio 9
Escribir un programa que almacene la cadena de caracteres contraseña en una
variable, pregunte al usuario por la contraseña hasta que introduzca la contraseña
correcta.
'''
print("--- Ejercicio 9 ---")
password = "contraseña"
pass_user = input("Introducir la contraseña: ")
intentos = 1
while (password).upper() != (pass_user).upper():
  print("La contraseña es incorrecta.")
  pass_user = input("Introducir la contraseña: ")
  intentos += 1
print("Contraseña correcta.")
print(f"Ingreso aceptado luego de {intentos} intentos")

'''
Ejercicio 10
Escribir un programa que pida al usuario un número entero y muestre por pantalla si
es un número primo o no.
'''
print("--- Ejercicio 10 ---")
num = int(input("Ingrese un numero: "))
primo = False
if num < 1:
  primo = False
  
elif num == 2:
  primo = True
else:
  for i in range(2, num):
    if num % i == 0:
      primo = False
      break
if primo is True:
  print(f"El numero {num} es primo.")
else: print(f"El numero {num} no es primo")

'''
Ejercicio 11
Escribir un programa que pida al usuario una palabra y luego muestre por pantalla una
a una las letras de la palabra introducida empezando por la última.
'''
print("--- Ejercicio 11 ---")

word = input("Introduce una palabra: ")
for i in range(len(word)-1, -1, -1):
    print(word[i])

'''
Ejercicio 12
Escribir un programa en el que se pregunte al usuario por una frase y una letra, y
muestre por pantalla el número de veces que aparece la letra en la frase.
'''
print("--- Ejercicio 12 ---")

frase = input("Introduce una frase: ")
letra = input("Introduce una letra")
contador = 0
for i in frase:
    if i == letra:
        contador += 1
print("La letra '%s' aparece %2i veces en la frase '%s'." % (letra, contador, frase))

'''
Ejercicio 13
Escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta
que el usuario escriba “salir” que terminará.
'''
print("--- Ejercicio 13 ---")

while True:
    frase = input("Introduce algo: ")
    if frase == "salir":
        break
    print(frase)

