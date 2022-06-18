"""
Ejercicio 5
Realizar una clase que administre una agenda. Se debe almacenar para cada contacto
el nombre, el teléfono y el email. Además deberá mostrar un menú con las siguientes
opciones: 
-Añadir contacto
-Lista de contactos
-Buscar contacto
-Editar contacto
-Cerrar agenda
"""

# clases
class Agenda:
    def __init__(self):
        self.contactos = {
            'Federico':{'Numero':665455565,'Mail':'fede@gmail.com'},
            'Juan':{'Numero':654789988,'Mail':'juan@gmail.com'},
            'Lucas':{'Numero':665123456,'Mail':'lucas@gmail.com'}
            }

    def listar(self):
        for contacto in self.contactos:
            print(f'''
Nombre: {contacto} 
Numero: {self.contactos[contacto]['Numero']}
Mail: {self.contactos[contacto]['Mail']}''')
        input("\nPresione enter para volver al menu.")

    def buscar(self):
        busqueda = input("\nEscriba el nombre a buscar: ").capitalize()
        if busqueda in self.contactos:
            print(f'''
Nombre: {busqueda} 
Numero: {self.contactos[busqueda]['Numero']}
Mail: {self.contactos[busqueda]['Mail']}
            ''')
            input("\nPresione enter para volver al menu.")
        else:
            print("\nNo se encuentra el contacto\n")
            op = input("Quieres buscar nuevamente?\n[1] - Si\n[2] - No\n")
            if op == "1":
                self.buscar()

    
    def crear(self):
        nombre = input("\nEscriba el nombre del contacto: ").capitalize()
        if nombre in self.contactos:
            print("Se encontro el siguiente contacto con ese nombre\n")
            print(f'''
Nombre: {nombre} 
Numero: {self.contactos[nombre]['Numero']}
Mail: {self.contactos[nombre]['Mail']}
            ''')
            op = input(
                f"Esta seguro que quieres sobrescribir el contacto?\n[1] - Si\n[2] - No\n"
            )
            if op == "1":
                while True:
                    print(f"Nombre del contacto: {nombre}")
                    telefono = input("Escriba el numero de telefono: ")
                    try:
                        telefono = int(telefono)
                        break
                    except:
                        print('\nDebes ingresar solo numeros\n')
                mail = input("Escriba el mail: ")
                self.contactos[nombre] = {'Numero':telefono,'Mail':mail}
                print(f"\nSe agrego el contacto '{nombre}' en la agenda.\n")
            else:
                self.crear()
        else:
            while True:
                telefono = input("Escriba el numero de telefono: ")
                try:
                    telefono = int(telefono)
                    break
                except:
                    print('\nDebes ingresar solo numeros\n')
            mail = input("Escriba el mail: ")
            self.contactos[nombre] = {'Numero':telefono,'Mail':mail}
            print(f"\nSe agrego el contacto '{nombre}' en la agenda.\n")

    def editar(self):
        nombre = input("\nEscriba el nombre del contacto a editar: ").capitalize()
        if nombre in self.contactos:
            print("Se encontro el siguiente contacto con ese nombre\n")
            print(f'''
Nombre: {nombre}
Numero: {self.contactos[nombre]['Numero']}
Mail: {self.contactos[nombre]['Mail']}
            ''')
            op = input(
                f"Esta seguro que quieres editar el contacto?\n[1] - Si\n[2] - No\n"
            )
            if op == "1":
                while True:
                    print(f"Nombre del contacto: {nombre}")
                    telefono = input("Escriba el numero de telefono: ")
                    try:
                        telefono = int(telefono)
                        break
                    except:
                        print(f'Debes ingresar solo numeros')
                mail = input("Escriba el mail: ")
                print(f"\nNombre del contacto: {nombre}")
                print(f"Telefono del contacto: {telefono}")
                print(f"Mail del contacto: {mail}\n")
                self.contactos[nombre] = {'Numero':telefono,'Mail':mail}
                print(f"\nSe modifico el contacto '{nombre}' en la agenda.\n")
            else:
                self.editar()
        else:
            print("\nNo se encuentra el contacto\n")
            op = input("Quieres buscar nuevamente?\n[1] - Si\n[2] - No\n")
            if op == "1":
                self.editar()

    def borrar(self):
        busqueda = input("\nEscriba el nombre a buscar: ").capitalize()
        if busqueda in self.contactos:
            op = input(f'''
Esta seguro que desea borrar el siguiente contacto?

Nombre: {busqueda} 
Numero: {self.contactos[busqueda]['Numero']}
Mail: {self.contactos[busqueda]['Mail']}

[1] - Si
[2] - No

'''         )
            if op == "1":
                del self.contactos[busqueda]
                print(f"\nEl contacto '{busqueda}' se borro correctamente.\n")
            else:
                op = input("Quieres buscar nuevamente?\n[1] - Si\n[2] - No\n")
                if op == "1":
                    self.borrar()
        else:
            print("\nNo se encuentra el contacto\n")
            op = input("Quieres buscar nuevamente?\n[1] - Si\n[2] - No\n")
            if op == "1":
                self.borrar()
    

# funciones
def menu():
    print("\n- M E N U -")
    print("[1] - Ver agenda")
    print("[2] - Buscar contacto")
    print("[3] - Agregar contacto")
    print("[4] - Editar contacto")
    print("[5] - Borrar contacto")
    print("[6] - Salir\n")

    opcion = input("Elija una opcion: ")
    validar_opcion(opcion)


def validar_opcion(opcion):
    if opcion == "1":
        agenda.listar()
    elif opcion == "2":
        agenda.buscar()
    elif opcion == "3":
        agenda.crear()
    elif opcion == "4":
        agenda.editar()
    elif opcion == "5":
        agenda.borrar()
    elif opcion == "6":
        print("\nAdios!")
        exit()
    else:
        print("\nOpcion incorrecta, intente nuevamente\n")
        menu()



# programa
print(" - - - A G E N D A - - - ")
agenda = Agenda()
while True:
    menu()

