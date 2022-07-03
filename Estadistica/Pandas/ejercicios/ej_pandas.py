
'''
Ejercicio 1

Escribir un programa que pregunte al usuario por las ventas de un rango de años y muestre por
pantalla una serie con los datos de las ventas indexada por los años, antes y después de aplicarles un
descuento del 10%.
'''
from tokenize import String
import pandas as pd

def info_ventas(anio1,anio2):
    ventas = {}
    if anio1 > anio2:
        diferencia = (anio1 - anio2) + 1
        anio_menor = anio2
    else:
        diferencia = (anio2 - anio1)+1
        anio_menor = anio1
    for x in range(diferencia):
        anio = int(anio_menor)+x
        venta = int(input(f"Ingrese las ventas del {anio}:"))
        ventas[anio] = venta
    return ventas

serie = pd.Series(info_ventas(2010,2020))
df = pd.DataFrame(serie, columns=['Ventas'])
#df = df.reset_index()
df.columns = ['Ventas']
df['-10%'] = df['Ventas'] * 0.9

print(df)


'''
Ejercicio 2

Escribir una función que reciba un diccionario con las notas de los alumno de un curso y devuelva
una serie con la nota mínima, la máxima, media y la desviación típica.
'''
import pandas as pd

diccionario = {'Jonathan':6,'Federico':8,'Jun':7,'Hector':3,'Bob':1,}

def serie(dic):
    notas = pd.Series(dic)
    serie_data = pd.Series([notas.max(),notas.min(),notas.mean(),notas.std()], index=['Maximo','Minimo','Media','Desviacion Estandar'])
    print(serie_data)

serie(diccionario)


'''
Ejercicio 3

Escribir una función que reciba un diccionario con las notas de los alumnos de un curso y devuelva
una serie con las notas de los alumnos aprobados ordenadas de mayor a menor.
'''
import pandas as pd

diccionario = {'Jonathan':6,'Federico':8,'Jun':7,'Hector':3,'Bob':1,}

def serie(dic):
    notas = pd.Series(dic)
    print(notas[notas>=5].sort_values(ascending=False))
    
serie(diccionario)

'''
Ejercicio 4

Escribir programa que genere y muestre por pantalla un DataFrame con los datos de la tabla
siguiente:

Mes Ventas Gastos
Enero 30500 22000
Febrero 35600 23400
Marzo 28300 18100
Abril 33900 20700
'''

import pandas as pd

dic= {'Mes':['Enero','Febrero','Marzo','Abril'],'Ventas': [30500,35600,28300,33900],'Gastos':[22000,23400,18100,20700]}

def dataFrame(diccionario):
    df = pd.DataFrame(diccionario)
    return df

df= dataFrame(dic)

print(df)

'''
Ejercicio 5

Escribir una función que reciba un DataFrame con el formato del ejercicio anterior, una lista de
meses, y devuelva el balance (ventas - gastos) total en los meses indicados.
'''

def balance(df,meses:list):
    df['Balance'] = df['Ventas'] - df['Gastos']
    df_filtrado = df[df.Mes.isin(meses)]
    return df_filtrado

meses=['Febrero','Marzo']
df = balance(dataFrame(dic),meses)

print(df)

'''
Ejercicio 6

El fichero cotizacion.csv contiene las cotizaciones de las empresas del IBEX35 con las
siguientes columnas: nombre (nombre de la empresa), Final (precio de la acción al cierre de
bolsa), Máximo (precio máximo de la acción durante la jornada), Mínimo (precio mínimo de la
acción durante la jornada), volumen (Volumen al cierre de bolsa), Efectivo (capitalización al
cierre en miles de euros). Construir una función que construya un DataFrame a partir del un fichero
con el formato anterior y devuelva otro DataFrame con el mínimo, el máximo y la media de dada
columna.
'''
import pandas as pd

def dfAnalisis(ruta:str):
    df = pd.read_csv(ruta, sep=';', decimal=',', thousands='.',header=0)
    #return pd.DataFrame([df.min(), df.max(), df.mean()], index=['Mínimo', 'Máximo', 'Media'])
    df_desc = df.describe()
    return df_desc.iloc[[3,7,1]]

ruta = "D:/Federico/Proyectos GIT/Proyectos/Bootcamp-Python-MachineLearning/Estadistica/Pandas/ejercicios/cotizacion.csv"

df = dfAnalisis(ruta)

print(df)

'''
Ejercicio 7

El fichero titanic.csv contiene información sobre los pasajeros del Titanic. Escribir un programa con
los siguientes requisitos:

    1. Generar un DataFrame con los datos del fichero. 
    2. Mostrar por pantalla las dimensiones del DataFrame, el número de datos que contiene, los 
    nombres de sus columnas y filas, los tipos de datos de las columnas, las 10 primeras filas y 
    las 10 últimas filas 
    3. Mostrar por pantalla los datos del pasajero con identificador 148. 
    4. Mostrar por pantalla las filas pares del DataFrame. 
    5. Mostrar por pantalla los nombres de las personas que iban en primera clase ordenadas 
    alfabéticamente. 
    6. Mostrar por pantalla el porcentaje de personas que sobrevivieron y murieron. 
    7. Mostrar por pantalla el porcentaje de personas que sobrevivieron en cada clase. 
    8. Eliminar del DataFrame los pasajeros con edad desconocida. 
    9. Mostrar por pantalla la edad media de las mujeres que viajaban en cada clase. 
    10.Añadir una nueva columna booleana para ver si el pasajero era menor de edad o no. 
    11.Mostrar por pantalla el porcentaje de menores y mayores de edad que sobrevivieron en cada 
    clase. 
'''

import pandas as pd

# Parte 1
df = pd.read_csv("Estadistica\Pandas\ejercicios/titanic.csv", sep=',')
print(df)

# Parte 2
print('Dimensiones:', df.shape)
print('Número de elemntos:', df.size)
print('Nombres de columnas:', df.columns)
print('Nombres de filas:', df.index)
print('Tipos de datos:\n', df.dtypes)
print('Primeras 10 filas:\n', df.head(10))
print('Últimas 10 filas:\n', df.tail(10))

# Parte 3
print(df.loc[148])

# Parte 4
print(df.iloc[range(0,df.shape[0],2)])
s
# Parte 5
print(df[df["Pclass"]==1]['Name'].sort_values())

# Parte 6
print(df['Survived'].value_counts(normalize=True) * 100)
#.value_counts devuelve recuentos unicos, al estar normalizado los cuenta y divide por la cantidad
