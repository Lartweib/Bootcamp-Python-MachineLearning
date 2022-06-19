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

import os
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

options=Options()
options.add_argument("--kiosk")
options.headless = True

driver = webdriver.Firefox(options=options, service_log_path=os.devnull)

lat = 28.1035677
lon = -15.5319742

driver.get(f'https://info.mercadona.es/es/supermercados?coord={lat}%2C{lon}')

accept_cookies = driver.find_element_by_id('third-btn')  
accept_cookies.click()

body = driver.find_element_by_tag_name('body')
driver.execute_script('arguments[0].scrollIntoView(false)', body)

vermas_xpath = '/html/body/div[1]/div[3]/div/div/div[2]/div[1]/ul/div/button'
vertodos = WebDriverWait(driver, 5 ).until(EC.presence_of_element_located((By.XPATH,vermas_xpath)))
vertodos.click()

li_supermercados = driver.find_elements_by_class_name('panelLateralResultadosElemento')

count = 1
for supermercado in li_supermercados:
    print(f'{count} - ',supermercado.find_element_by_tag_name('h3').text)
    count += 1


driver.quit()
