'''
Ejercicios de Condicionales

Ejercicio 1
Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es
mayor de edad o no.
'''
from difflib import Match


print("--- Ejercicio 1 ---")
edad = int(input("Cual es tu edad? "))
if edad < 18:
  print("Eres menor de edad")
else: print("Eres mayor de edad")
'''
Ejercicio 2
Escribir un programa que almacene la cadena de caracteres contraseña en una
variable, pregunte al usuario por la contraseña e imprima por pantalla si la contraseña
introducida por el usuario coincide con la guardada en la variable sin tener en cuenta
mayúsculas y minúsculas.
'''
print("--- Ejercicio 2 ---")
password = "contraseña"
pass_ingresada= input("Ingrese su contraseña: ")
if password.upper() == pass_ingresada.upper():
  print("Contraseña correcta")
else: print("Contraseña incorrecta")

'''
Ejercicio 3
Escribir un programa que pida al usuario dos números y muestre por pantalla su
división. Si el divisor es cero el programa debe mostrar un error.
'''
print("--- Ejercicio 3 ---")

n1 = int(input("Ingrese un numero: "))
n2 = int(input("Ingrese un numero para dividir el primero: "))
if n2 == 0:
  print("No se puede dividir por cero")
else: print(f'El resultado de la divicion de {n1} y {n2} es {n1/n2}')

'''
Ejercicio 4
Escribir un programa que pida al usuario un número entero y muestre por pantalla si
es par o impar.
'''
print("--- Ejercicio 4 ---")
numero = int(input("Ingrese un numero entero: "))
if numero%2 == 0:
  print(f"El numero {numero} es par")
else: 
  print(f"El numero {numero} es impar")

'''
Ejercicio 5
Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos
ingresos iguales o superiores a 1000 € mensuales. Escribir un programa que pregunte
al usuario su edad y sus ingresos mensuales y muestre por pantalla si el usuario tiene
que tributar o no.
'''
print("--- Ejercicio 5 ---")
ingresos = int(input("Cual es su ingreso mensual? "))
edad = int(input("Cual es su edad? "))
if edad >= 16 and ingresos >= 1000: print("Usted debe tributar")
else: print("Usted no tributa")

'''
Ejercicio 6
Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el
nombre. El grupo A esta formado por las mujeres con un nombre anterior a la M y los
hombres con un nombre posterior a la N y el grupo B por el resto. Escribir un programa
que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo que le
corresponde.
'''
print("--- Ejercicio 6 ---")
nombre = input("Cual es tu nombre? ")
sexo = input("Cual es tu sexo? (H/M) ").upper()
if nombre[0] < "M" and sexo == "M":
  print("Grupo A")
elif nombre[0] < "N" and sexo == "H":
  print("Grupo A")
else: print("Grupo B")

'''
Ejercicio 7
Los tramos impositivos para la declaración de la renta en un determinado país son los
siguientes:
Renta Tipo impositivo
Menos de 10000€ 5%
Entre 10000€ y 20000€ 15%
Entre 20000€ y 35000€ 20%
Entre 35000€ y 60000€ 30%
Más de 60000€ 45%
Escribir un programa que pregunte al usuario su renta anual y muestre por pantalla el
tipo impositivo que le corresponde.
'''
print("--- Ejercicio 7 ---")
renta_anual = int(input("Ingrese su renta anual: "))
match renta_anual:
  case n if n < 10000:
    print("Debe pagar el 5%")
  case n if n < 20000 and n >= 10000:
    print("Debe pagar el 15%")
  case n if n < 35000 and n >= 20000:
    print("Debe pagar el 20%")
  case n if n < 60000 and n >= 35000:
    print("Debe pagar el 30%")
  case n if n > 60000:
    print("Debe pagar el 45%")
  
'''
Ejercicio 8
En una determinada empresa, sus empleados son evaluados al final de cada año. Los
puntos que pueden obtener en la evaluación comienzan en 0.0 y pueden ir
aumentando, traduciéndose en mejores beneficios. Los puntos que pueden conseguir
los empleados pueden ser 0.0, 0.4, 0.6 o más, pero no valores intermedios entre las
cifras mencionadas. A continuación se muestra una tabla con los niveles
correspondientes a cada puntuación. La cantidad de dinero conseguida en cada nivel
es de 2.400€ multiplicada por la puntuación del nivel.
Nivel Puntuación
Inaceptable 0.0
Aceptable 0.4
Meritorio 0.6 o más
Escribir un programa que lea la puntuación del usuario e indique su nivel de
rendimiento, así como la cantidad de dinero que recibirá el usuario.
'''
print("--- Ejercicio 8 ---")
puntuacion_usuario = round(float(input("Introduzca la puntuacion del usuario: ")),1)
print(puntuacion_usuario)

match puntuacion_usuario:
  case n if ((n*100)%2) != 0.0:
    print("La puntuacion es erronea")
  case n if n == 0.0:
    print("Es inaceptable, no cobra un plus")
  case n if n == 0.4:
    print(f"Es aceptable, cobra {2400*n}")
  case n if n >= 0.6:
    print(f"Es meritorio, cobra {2400*n}")

'''
Ejercicio 9
Escribir un programa para una empresa que tiene salas de juegos para todas las
edades y quiere calcular de forma automática el precio que debe cobrar a sus clientes
por entrar. El programa debe preguntar al usuario la edad del cliente y mostrar el
precio de la entrada. Si el cliente es menor de 4 años puede entrar gratis, si tiene entre
4 y 18 años debe pagar 5€ y si es mayor de 18 años, 10€
'''
print("--- Ejercicio 9 ---")
edad = int(input("Cual es su edad? "))
if edad <= 4:
  print("No debe abonar nada. Entra gratis.")
elif edad > 4 and edad < 18:
  print("El precio de la entrada es 5€.")
elif edad > 18:
  print("El precio de la entrada es 10€.")

'''
Ejercicio 10
La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. Los
ingredientes para cada tipo de pizza aparecen a continuación.
 Ingredientes vegetarianos: Pimiento y tofu.
 Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.
Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en
función de su respuesta le muestre un menú con los ingredientes disponibles para que
elija. Solo se puede eligir un ingrediente además de la mozzarella y el tomate que
están en todas la pizzas. Al final se debe mostrar por pantalla si la pizza elegida es
vegetariana o no y todos los ingredientes que lleva.
'''
print("--- Ejercicio 10 ---")

tipo_pizza = input("Que tipo de pizza quiere? Ingrese A o B\nA- Vegetariana\nB- No vegetariana\n  ")
ingredientes = ""
if tipo_pizza == "A":
  ingredientes = input("Que ingredientes quiere agregar? Ingrese A o B\nA- Pimiento\nB- Tofu\n  ")
  if ingredientes == "A": ingredientes = "Pimiento"
  else: ingredientes == "Tofu"
else: 
  ingredientes = input("Que ingredientes quiere agregar? Ingrese A, B o C\nA- Peperoni\nB- Jamon\nC- Salmon\n  ")
  if ingredientes == "A": ingredientes = "Peperoni"
  elif ingredientes == "B": ingredientes = "Jamon"
  else: ingredientes = "Salmon"
print(f"Usted eligio una pizza {tipo_pizza} con los siguientes ingredientes: mozzarella, tomate y {ingredientes}")
