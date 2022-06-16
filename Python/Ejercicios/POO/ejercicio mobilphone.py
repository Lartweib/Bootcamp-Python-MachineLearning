'''
Ejercicio

Escriba una clase MobilePhone que represente un teléfono móvil.

Atributos:
• manufacturer (cadena de texto)
• screen_size (flotante)
• num_cores (entero)
• apps (lista de cadenas de texto)
• status (0: apagado, 1: encendido)

Métodos:
• __init__(self, manufacturer, screen_size, num_cores)
• power_on(self)
• power_off(self)
• install_app(self, app)
• uninstall_app(self, app)

Crear al menos una instancia (móvil) a partir de la clase creada y «jugar» con los métodos,
visualizando cómo cambian sus atributos.
¿Serías capaz de extender el método install_app() para instalar varias aplicaciones a la
vez?
'''

class MobilePhone:
    def __init__(self, manufacturer, screen_size, num_cores):
        self.manufacturer = manufacturer
        self.screen_size = float(screen_size)
        self.num_cores = int(num_cores)
        self.status = 0
        self.app = ['telefono','agenda','navegador']


    def power_on(self):
        self.status = 1
        print("El movil esta encendido.")

    def power_off(self):
        self.status = 0
        print("El movil esta apagado.")

    def install_app(self, *args):
        if self.status == 0:
            print("El movil no esta encendido.")
        else:
            for app in args:
                if app in self.app:
                    print(f"La aplicacion '{app}' ya se encuentra instalada.")
                else:
                    self.app.append(app)
                    print(f"La aplicacion '{app}' se instalo con exito.")
            print(f"Esta es la lista de aplicaciones instaladas actualmente:\n {self.app}")

    def uninstall_app(self, *args):
        if self.status == 0:
            print("El movil no esta encendido.")
        else:
            for app in args:
                if app in self.app:
                    self.app.remove(app)
                    print(f"La aplicacion '{app}' se desinstalo con exito.")
                else: 
                    print(f"ERROR: La aplicacion '{app}' no esta instalada.")
            print(f"Esta es la lista de aplicaciones tras la desinstalacion:\n {self.app}")
            

note20 = MobilePhone("samsung", 6.5, 8)

print(note20.manufacturer,note20.screen_size,note20.num_cores,note20.status,note20.app)

note20.power_on()

note20.power_off()

note20.install_app("whatsapp")

note20.uninstall_app("whatsapp")

note20.power_on()

note20.install_app("whatsapp")

note20.uninstall_app("pokemon")

note20.uninstall_app("whatsapp")

print(note20.app)

note20.install_app("whatsapp","instagram","facebook","snapchat")

note20.uninstall_app("pokemon","wasap", "instagram")
