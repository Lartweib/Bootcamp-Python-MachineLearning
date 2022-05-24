'''
Ejercicio 1
Escribir un programa que muestre por pantalla la cadena ¡Hola Mundo!.
'''
print("--- Ejercicio 1 ---")
print("Hola mundo!")

'''
Ejercicio 2 Escribir un programa que almacene la cadena ¡Hola Mundo!
en una variable y luego muestre por pantalla el contenido de la
variable.
'''
print("--- Ejercicio 2 ---")
a = "Hola mundo!"
print(a)

'''
Ejercicio 3
Escribir un programa que pregunte el nombre del usuario en la
consola y después de que el usuario lo introduzca muestre por
pantalla la cadena ¡Hola <nombre>!, donde <nombre> es el
nombre que el usuario haya introducido.
'''
print("--- Ejercicio 3 ---")
nombre = input("Cual es tu nombre?")
print("Hola",nombre,"!")

'''
Ejercicio 4
Escribir un programa que muestre por pantalla el resultado de
la siguiente operación aritmética
'''
print("--- Ejercicio 4 ---")
a = 5+5
print("5 + 5 =",a)

'''
Ejercicio 5
Escribir un programa que pregunte al usuario por el número de
horas trabajadas y el coste por hora. Después debe mostrar
por pantalla la paga que le corresponde.
'''
print("--- Ejercicio 5 ---")
horas = int(input("Cuantas horas trabajaste?"))
costo = int(input("Cuanto vale la hora?"))
paga = horas * costo

print(f"La paga total correspondiente a {horas} horas con un valor de {costo} de costo por hora equivale a una paga de {paga} euros")

'''
Ejercicio 6
Escribir un programa que lea un entero positivo, n,
introducido por el usuario y después muestre en pantalla
la suma de todos los enteros desde 1 hasta , n.
La suma de los , n, primeros enteros positivos puede ser calculada de la siguiente
forma:
suma=n(n+1)2
'''
print("--- Ejercicio 6 ---")
n = int(input("Introduce un numero: "))
suma = n *(n+1) / 2
print(int(suma))

'''
Ejercicio 7
Escribir un programa que pida al usuario su peso (en kg) y
estatura (en metros), calcule el índice de masa corporal y lo
almacene en una variable, y muestre por pantalla la frase Tu
índice de masa corporal es <imc> donde <imc> es el
índice de masa corporal calculado redondeado con dos
decimales.
'''
print("--- Ejercicio 7 ---")
peso = int(input("Introduce tu peso en kg: "))
altura = float(input("Introduce tu altura en metros: "))
imc = peso * altura
print(f"Tu imc es {imc}")

'''
Ejercicio 8
Escribir un programa que pida al usuario dos números enteros
y muestre por pantalla la <n> entre <m> da un cociente
<c> y un resto <r> donde <n> y <m> son los números
introducidos por el usuario, y <c> y <r> son el cociente y el
resto de la división entera respectivamente.
'''
print("--- Ejercicio 8 ---")
 
n = int(input("Ingrese un numero entero: "))
m = int(input("Ingrese otro numero entero: "))
cociente = n / m 
resto = n % m
print(f"La divicion de {n} entre {m} da un cociente {cociente} y un resto {resto}")

'''
Ejercicio 9
Escribir un programa que pregunte al usuario una cantidad a
invertir, el interés anual y el número de años, y muestre por
pantalla el capital obtenido en la inversión.
'''
print("--- Ejercicio 9 ---")
inv = int(input("Ingrese una cantidad a invertir: "))
interes = int(input("Ingrese el interes anual: "))
anio = int(input("Ingrese la cantidad de años: "))
resultado = (inv * ((interes / 100)+1))*anio
print(f"Obtuviste el siguiente capital por tu invercion: {resultado}")

'''
Ejercicio 10
Una juguetería tiene mucho éxito en dos de sus productos:
payasos y muñecas. Suele hacer venta por correo y la
empresa de logística les cobra por peso de cada paquete así
que deben calcular el peso de los payasos y muñecas que
saldrán en cada paquete a demanda. Cada payaso pesa 112 g
y cada muñeca 75 g. Escribir un programa que lea el número
de payasos y muñecas vendidos en el último pedido y calcule
el peso total del paquete que será enviado.
'''
print("--- Ejercicio 10 ---")
payasos = 112
muñecas = 75
ventas_payasos = int(input("Cuantas ventas se realizaron de payasos? "))
ventas_muñecas = int(input("Cuantas ventas se realizaron de muñecas? "))
peso_total = (payasos * ventas_payasos) + (muñecas * ventas_muñecas)
print(f"El peso total del paquete que sera enviado es de {peso_total} gramos.")

'''
Ejercicio 11
Imagina que acabas de abrir una nueva cuenta de ahorros que
te ofrece el 4% de interés al año. Estos ahorros debido a
intereses, que no se cobran hasta finales de año, se te añaden
al balance final de tu cuenta de ahorros. Escribir un programa
que comience leyendo la cantidad de dinero depositada en la
cuenta de ahorros, introducida por el usuario. Después el
programa debe calcular y mostrar por pantalla la cantidad de
ahorros tras el primer, segundo y tercer años. Redondear cada
cantidad a dos decimales.
'''
print("--- Ejercicio 11 ---")
ahorros = int(input("Cuanto dinero tiene ahorrado en su cuenta? "))
interes = 1.04
balance_final = ahorros * interes
print(f"Al final del primer año tendria {round(balance_final,2)} euros")
balance_final *= interes
print(f"Al finalizar el segundo año tendria {round(balance_final,2)} euros")
balance_final *= interes
print(f"Al finalizar el tercer año tendria {round(balance_final,2)} euros")

'''
Ejercicio 12
Una panadería vende barras de pan a 3.49€ cada una. El pan
que no es el día tiene un descuento del 60%. Escribir un
programa que comience leyendo el número de barras vendidas
que no son del día. Después el programa debe mostrar el
precio habitual de una barra de pan, el descuento que se le
hace por no ser fresca y el coste final total.
'''
print("--- Ejercicio 12 ---")
precio_pan= 3.49
descuento_pv = 0.60
cant_pan_vend = int(input("Cuantas barras de pan viejo se vendieron? "))
print(f"El precio de la barra de pan habitual es {precio_pan}")
print(f"El precio de la barra de pan vieja es {precio_pan*descuento_pv}")
print(f"El descuento que se aplico por ser de ayer es: {descuento_pv*100}")
print(f"Se facturo por el total de panes viejos vendidos: {(precio_pan*descuento_pv)*cant_pan_vend}")

