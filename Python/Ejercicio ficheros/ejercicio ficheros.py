'''
Ejercicio 6

Escribir un programa para gestionar un listín telefónico con los nombres y los teléfonos de los clientes
de una empresa. El programa incorporar funciones crear el fichero con el listín si no existe, para
consultar el teléfono de un cliente, añadir el teléfono de un nuevo cliente y eliminar el teléfono de un
cliente. El listín debe estar guardado en el fichero de texto listin.txt donde el nombre del cliente y su
teléfono deben aparecer separados por comas y cada cliente en una línea distinta.
'''
import os

#Variables
opcion = 0

#diccionario
listin = {}

#fichero
def fichero():
  if os.path.isfile("listin.txt"):
    txt = open("listin.txt", "r")
    lista = txt.readlines()
    for linea in lista:
      elemento = linea.split(",")
      nombre = elemento[0]
      telefono = elemento[1]
      telefono = telefono.split("\n")
      telefono = telefono[0]
      listin[nombre.capitalize()]=telefono
    txt.close()

  else: 
    txt = open("listin.txt", "w")   

#lista
global listin_dic

listin_dic = listin.items()

#funciones
def menu():
  print("- M E N U -")
  print("[1] - Ver agenda")
  print("[2] - Buscar contacto")
  print("[3] - Agregar contacto")
  print("[4] - Borrar contacto")
  print("[5] - Salir\n")

  opcion = input("Elija una opcion: ")
  validar_opcion(opcion)


def validar_opcion(opcion):
  if opcion == "1":
    agenda()
  elif opcion == "2":
    buscar()
  elif opcion == "3":
    crear()
  elif opcion == "4":
    borrar()
  elif opcion == "5":
    txt = open("listin.txt", "w")   
    for nombre, telefono in listin_dic:
      txt.write(f"{nombre},{telefono}\n")
    txt.close()
    print("\nAdios!")
    exit()
  else: 
    print("\nOpcion incorrecta, intente nuevamente\n")
    menu()

def agenda():
  print("\n")
  for nombre, telefono in listin_dic:
    print(f"{nombre} : {telefono}")
  print("\n")
  
def buscar():
  busqueda = input("\nEscriba el nombre a buscar: ").capitalize()
  if busqueda in listin:
    print(f"\n{busqueda} : {listin[busqueda]}\n")
  else: 
    print("\nNo se encuentra el contacto\n")
    op=input("Quieres buscar nuevamente?\n[1] - Si\n[2] - No\n")
    if op == "1": buscar()
    
def crear():
  contacto = input("\nEscriba el nombre del contacto: ").capitalize()
  if contacto in listin:
    print("Se encontro el siguiente contacto con ese nombre\n")
    print(f"{contacto} : {listin[contacto]}\n")
    op=input(f"Esta seguro que quieres sobrescribir el contacto?\n[1] - Si\n[2] - No\n")
    if op == "1": 
      print(f"Nombre del contacto: {contacto}")
      telefono = input("Escriba el numero de telefono: ")
      listin[contacto]=telefono
      print(f"\nSe agrego el contacto '{contacto}' en la agenda.\n")
    else: crear()
  else: 
    telefono = input("Escriba el numero de telefono: ")
    listin[contacto]=telefono
    print(f"\nSe agrego el contacto '{contacto}' en la agenda.\n")

def borrar():
  busqueda = input("\nEscriba el nombre a buscar: ").capitalize()
  if busqueda in listin:
    op=input(f"\nEsta seguro que desea borrar el siguiente contacto?\n\n{busqueda} : {listin[busqueda]}\n\n[1] - Si\n[2] - No\n")
    if op == "1":
      del listin[busqueda]    
      print(f"\nEl contacto '{busqueda}' se borro correctamente.\n")
    else: 
      op=input("Quieres buscar nuevamente?\n[1] - Si\n[2] - No\n")
      if op == "1": borrar()
  else: 
    print("\nNo se encuentra el contacto\n")
    op=input("Quieres buscar nuevamente?\n[1] - Si\n[2] - No\n")
    if op == "1": borrar()


#programa
print(" - - - A G E N D A - - - ")
fichero()
while True:
  menu()
