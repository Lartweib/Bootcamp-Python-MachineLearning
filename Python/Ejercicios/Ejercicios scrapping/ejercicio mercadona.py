'''
Ejercicio

Escriba un programa en Python que permita sacar un listado de supermercados Mercadona
dada una geolocalización (lat,lon) como dato de entrada.
Pasos a seguir:

1. Utilizar el siguiente f-string para obtener la url de acceso: f https://info.mercadona.
es/es/supermercados?coord={lat}%2C{lon}
2. Aceptar las cookies al acceder al sitio web.
3. Hacer scroll hasta el final de la página para hacer visible el botón «Ver todos». Se
recomienda usar javascript para ello.
4. Localizar el botón «Ver todos» y hacer clic para mostrar todos los establecimientos
(de la geolocalización). Se recomienda una espera explícita con acceso por «xpath».
5. Recorrer los elementos desplegados li y mostrar el contenido textual de los elementos
h3 que hay en su interior.

Como detalle final, y una vez que compruebe que el programa funciona correctamente,
aproveche para inicializar el «driver» ocultando la ventana del navegador.

Puede probar su programa con la localización de Las Palmas de Gran Canaria (28.1035677,
-15.5319742).
'''
