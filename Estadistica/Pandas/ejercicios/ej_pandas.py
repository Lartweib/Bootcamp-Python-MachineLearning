
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

ruta = "Estadistica\Pandas\ejercicios/archivos\cotizacion.csv"

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
df = pd.read_csv("Estadistica\Pandas\ejercicios/archivos/titanic.csv", sep=',')
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

# Parte 5
print(df[df["Pclass"]==1]['Name'].sort_values())

# Parte 6
print(df['Survived'].value_counts(normalize=True) * 100)
#.value_counts devuelve recuentos unicos, al estar normalizado los cuenta y divide por la cantidad total

# Parte 7
print(df.groupby('Pclass')['Survived'].value_counts(normalize=True) *100)

# Parte 8
df.dropna(subset=['Age'])

# Parte 9
print(df.groupby(['Pclass','Sex'])['Age'].mean().unstack()['female'])
# con groupby agrupamos por sexo y clase, luego sacamos la media de edad por los grupos, con unstack
# pivotamos el nivel de las etiquetas sexo para que aparezcan como columnas y por ultimo solo mostramos las mujeres

# Parte 10
df['Young'] = df['Age'] < 18
print(df)

# Parte 11
print(df.groupby(['Pclass', 'Young'])['Survived'].value_counts(normalize = True) * 100)


'''
Ejercicio 8

Los ficheros emisiones-2016.csv, emisiones-2017.csv, emisiones-2018.csv y emisiones-2019.csv, 
contienen datos sobre las emisiones contaminates en la ciudad de Madrid en los años 2016, 2017, 
2018 y 2019 respectivamente. Escribir un programa con los siguientes requisitos:

    1. Generar un DataFrame con los datos de los cuatro ficheros. 
    2. Filtrar las columnas del DataFrame para quedarse con las columnas ESTACION, 
    MAGNITUD, AÑO, MES y las correspondientes a los días D01, D02, etc. 
    3. Reestructurar el DataFrame para que los valores de los contaminantes de las columnas de los
    días aparezcan en una única columna. 
    4. Añadir una columna con la fecha a partir de la concatenación del año, el mes y el día (usar el
    módulo datetime). 
    5. Eliminar las filas con fechas no válidas (utilizar la función isnat del módulo numpy) y 
    ordenar el DataFrame por estaciones contaminantes y fecha. 
    6. Mostrar por pantalla las estaciones y los contaminantes disponibles en el DataFrame. 
    7. Crear una función que reciba una estación, un contaminante y un rango de fechas y devuelva
    una serie con las emisiones del contaminante dado en la estación y rango de fechas dado. 
    8. Mostrar un resumen descriptivo (mínimo, máximo, media, etc.) para cada contaminante. 
    9. Mostrar un resumen descriptivo para cada contaminante por distritos. 
    10.Crear una función que reciba una estación y un contaminante y devuelva un resumen 
    descriptivo de las emisiones del contaminante indicado en la estación indicada. 
    11.Crear una función que devuelva las emisiones medias mensuales de un contaminante y un 
    año dados para todos las estaciones. 
    12.Crear un función que reciba una estación de medición y devuelva un DataFrame con las 
    medias mensuales de los distintos tipos de contaminantes.
'''

import pandas as pd
import numpy as np
import datetime as dt


# Parte 1
e_2016 = pd.read_csv('Estadistica/Pandas/ejercicios/archivos/emisiones-2016.csv', sep = ';')
e_2017 = pd.read_csv('Estadistica/Pandas/ejercicios/archivos/emisiones-2017.csv', sep = ';')
e_2018 = pd.read_csv('Estadistica/Pandas/ejercicios/archivos/emisiones-2018.csv', sep = ';')
e_2019 = pd.read_csv('Estadistica/Pandas/ejercicios/archivos/emisiones-2019.csv', sep = ';')

emisiones = pd.concat([e_2016, e_2017, e_2018, e_2019])

emisiones


# Parte 2
columnas = ['ESTACION', 'MAGNITUD', 'ANO', 'MES']

columnas.extend([col for col in emisiones if col.startswith('D')])

emisiones = emisiones[columnas]

emisiones


# Parte 3
emisiones = emisiones.melt(id_vars=['ESTACION', 'MAGNITUD', 'ANO', 'MES'], var_name='DIA', value_name='VALOR')
# con melt podemos cambiar la orientacion de las columnas
# el parametro id_vars sirve para identificar las columnas que van a ser identificadoras
# los parametros var_name y value_name se utilizan para darle nombre a las columnas creadas

emisiones


# Parte 4

emisiones['DIA'] = emisiones.DIA.str.strip('D')
# Primero eliminamos el caracter D del comienzo de la columna de los días

emisiones['FECHA'] = emisiones.ANO.apply(str) + '/' + emisiones.MES.apply(str) + '/' + emisiones.DIA.apply(str)
# Concatenamos las columnas del año, mes y día

emisiones['FECHA'] = pd.to_datetime(emisiones.FECHA, format='%Y/%m/%d', infer_datetime_format=True, errors='coerce')
# Convertimos la nueva columna al tipo fecha

emisiones


# Parte 5

emisiones = emisiones.drop(emisiones[np.isnat(emisiones.FECHA)].index)

emisiones.sort_values(['ESTACION', 'MAGNITUD', 'FECHA'])


# Parte 6

print('Estaciones:', emisiones.ESTACION.unique())
print('Contaminantes:', emisiones.MAGNITUD.unique())
# se utiliza cuando tratamos con una sola columna de un DataFrame y devuelve todos los elementos únicos de una columna

# Parte 7

def evolucion(estacion, contaminante, desde, hasta):
    return emisiones[(emisiones.ESTACION == estacion) & (emisiones.MAGNITUD == contaminante) & (emisiones.FECHA >= desde) & (emisiones.FECHA <= hasta)].sort_values('FECHA').VALOR

evolucion(4, 1, '2017/08/15','2018/04/10')

# Parte 8

emisiones.groupby('MAGNITUD').VALOR.describe()

# Parte 9

emisiones.groupby(['ESTACION', 'MAGNITUD']).VALOR.describe()

# Parte 10

def resumen(estacion, contaminante):
    return emisiones[(emisiones.ESTACION == estacion) & (emisiones.MAGNITUD == contaminante)].VALOR.describe()

print(f'Resumen de estacion 35 contaminante 8:\n {resumen(35, 8)}')

print(f'Resumen de estacion 56 contaminante 8:\n {resumen(56, 8)}\n')


# Parte 11

def emisiones_medias_mensuales(contaminante, año):
    return emisiones[(emisiones.MAGNITUD == contaminante) & (emisiones.ANO == año)].groupby(['ESTACION', 'MES']).VALOR.mean().unstack('MES')
    # agrupa por estacion y mes, se le indica que saque la media de la columna VALOR, y luego que pivotee la columna mes para mostrarla horizontalmente

emisiones_medias_mensuales(6, 2016)


# Parte 12
'''
    12.Crear un función que reciba una estación de medición y devuelva un DataFrame con las 
    medias mensuales de los distintos tipos de contaminantes.
'''

def medias_mensuales(estacion):
    return emisiones[(emisiones.ESTACION == estacion)].groupby(['MAGNITUD', 'MES']).VALOR.mean().unstack('MAGNITUD')

medias_mensuales(8)
