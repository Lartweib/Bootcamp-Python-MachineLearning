'''
Ejercicios de Listas y Tuplas

Ejercicio 1
Escribir un programa que almacene las asignaturas de un
curso (por ejemplo Matemáticas, Física, Química, Historia y
Lengua) en una lista y la muestre por pantalla.
'''
print("--- Ejercicio 1 ---")

asignaturas = ["Matematicas","Fisica","Quimica", "Historia", "Lengua"]

print(asignaturas)

'''
Ejercicio 2
Escribir un programa que almacene las asignaturas de un
curso (por ejemplo Matemáticas, Física, Química, Historia y
Lengua) en una lista y la muestre por pantalla el mensaje Yo
estudio <asignatura>, donde <asignatura> es cada una de
las asignaturas de la lista.
'''
print("--- Ejercicio 2 ---")

asignaturas = ["Matematicas","Fisica","Quimica", "Historia", "Lengua"]

for i in range(len(asignaturas)):
    if i == 0:
        print("Yo estudio ", end="")
    elif i == len(asignaturas)-1: 
        print(f"y {asignaturas[i]}.") 
    elif i == len(asignaturas)-2: 
        print(f"{asignaturas[i]} ", end="")
    else: 
        print(f"{asignaturas[i]}, ", end="")

'''
Ejercicio 3
Escribir un programa que almacene las asignaturas de un
curso (por ejemplo Matemáticas, Física, Química, Historia y
Lengua) en una lista, pregunte al usuario la nota que ha
sacado en cada asignatura, y después las muestre por pantalla
con el mensaje En <asignatura> has sacado <nota> donde
<asignatura> es cada una des las asignaturas de la lista y
<nota> cada una de las correspondientes notas introducidas
por el usuario.
'''
print("--- Ejercicio 3 ---")

asignaturas = ["Matematicas","Fisica","Quimica", "Historia", "Lengua"]
notas = []

for i in asignaturas:
    notas.append(int(input(f"Que nota se saco en la asignatura {i}")))

for i in range(len(asignaturas)):
    print(f"En {asignaturas[i]} has sacado {notas[i]}")

'''
Ejercicio 4
Escribir un programa que pregunte al usuario los números
ganadores de la lotería primitiva, los almacene en una lista y
los muestre por pantalla ordenados de menor a mayor.
'''
print("--- Ejercicio 4 ---")
num_lot = []
i=1
while i <= 8:
    num = input(f"Ingrese el numero que salio en la loteria en la posicion {i}")
    if not num.isnumeric():
        print("Debe ingresar un numero")
        continue
    num = int(num)
    if num > 49 or num < 0 :
        print("El numero debe estar entre 00 y 49")
    else: 
        num_lot.append(num)
        i +=1
print(sorted(num_lot)) 

'''
Ejercicio 5
Escribir un programa que almacene en una lista los números
del 1 al 10 y los muestre por pantalla en orden inverso
separados por comas.
'''
print("--- Ejercicio 5 ---")
nums = list(range(1,11))
x = 1
for i in (list(reversed(nums))):
    if x == len(nums):
        print(i, end=". ")
    else:
        print(i, end=", ")
    x += 1    

'''
Ejercicio 6
Escribir un programa que almacene las asignaturas de un
curso (por ejemplo Matemáticas, Física, Química, Historia y
Lengua) en una lista, pregunte al usuario la nota que ha
sacado en cada asignatura y elimine de la lista las asignaturas
aprobadas. Al final el programa debe mostrar por pantalla las
asignaturas que el usuario tiene que repetir.
'''
print("--- Ejercicio 6 ---")

asignaturas = ["Matematicas","Fisica","Quimica", "Historia", "Lengua"]
asignaturas_aprobadas = []
notas = []

for i in asignaturas:
    nota = int(input(f"Que nota se saco en la asignatura {i}"))
    if nota < 5:
        notas.append(nota)
        asignaturas_aprobadas.append(i)

for i in range(len(asignaturas_aprobadas)):
    print(f"En {asignaturas_aprobadas[i]} has sacado {notas[i]}")

'''
Ejercicio 7
Escribir un programa que almacene el abecedario en una lista,
elimine de la lista las letras que ocupen posiciones múltiplos de
3, y muestre por pantalla la lista resultante.
'''
print("--- Ejercicio 7 ---")


'''
Ejercicio 8
Escribir un programa que pida al usuario una palabra y
muestre por pantalla si es un palíndromo.
'''

word = input("Introduce una palabra: ")
reversed_word = word
word = list(word)
reversed_word = list(reversed_word)
reversed_word.reverse()
if word == reversed_word:
    print("Es un palíndromo")
else:
    print("No es un palíndromo")

'''
Ejercicio 9
Escribir un programa que pida al usuario una palabra y
muestre por pantalla el número de veces que contiene cada
vocal.
'''

word = input("Introduce una palabra: ")
vocals = ['a', 'e', 'i', 'o', 'u']
for vocal in vocals:
    times = 0
    for letter in word:
        if letter == vocal:
            times += 1
    print("La vocal " + vocal + " aparece " + str(times) + " veces"
)

'''
Ejercicio 10
Escribir un programa que almacene en una lista los
siguientes precios, 50, 75, 46, 22, 80, 65, 8, y muestre por
pantalla el menor y el mayor de los precios.
'''

prices = [50, 75, 46, 22, 80, 65, 8]
min = max = prices[0]
for price in prices:
    if price < min:
        min = price
    elif price > max:
        max = price
print("El mínimo es " + str(min))
print("El máximo es " + str(max))

'''
Ejercicio 11
Escribir un programa que almacene los vectores (1,2,3) y (-
1,0,2) en dos listas y muestre por pantalla su producto
escalar.
'''

a = (1, 2, 3)
b = (-1, 0, 2)
product = 0
for i in range(len(a)):
    product += a[i]*b[i]
print("El producto de los vectores" + str(a) + " y " + str(b) + " es " + str(product))

'''
Ejercicio 12
Escribir un programa que almacene las
en una lista y muestre por pantalla su producto.
Nota: Para representar matrices mediante listas usar listas
anidadas, representando cada vector fila en una lista.
'''

a = ((1, 2, 3),(4, 5, 6))
b = ((-1, 0),(0, 1),(1,1))
result = [[0,0],[0,0]]
for i in range(len(a)):
    for j in range(len(b[0])):
        for k in range(len(b)):
            result[i][j] += a[i][k] * b[k][j]
for i in range(len(result)):
    result[i] = tuple(result[i])
result = tuple(result)
for i in range(len(result)):
    print(result[i])

'''
Ejercicio 13
Escribir un programa que pregunte por una muestra de
números, separados por comas, los guarde en una lista y
muestre por pantalla su media y desviación típica.
'''

sample = input("Introduce una muestra de números separados por comas: ")
sample = sample.split(',')
n = len(sample)
for i in range(n):
    sample[i] = int(sample[i])
sample = tuple(sample)
sum = 0
sumsq = 0
for i in sample:
    sum += i
    sumsq += i**2
mean = sum/n
stdev = (sumsq/n-mean**2)**(1/2)
print('La media es', mean, ', y la desviación típica es', stdev)

