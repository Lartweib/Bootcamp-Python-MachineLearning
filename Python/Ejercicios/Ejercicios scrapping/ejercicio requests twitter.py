'''
Utilizando el paquete requests, haga una petición GET a https://twitter.com y obtenga los
siguientes campos:
• Código de estado.
• Valor de la cookie guest_id
• Valor de la cabecera content-encoding
'''
import requests

response = requests.get('https://twitter.com')

codigo_de_estado = response.status_code
valor_cookie_guest_id = response.cookies.get('guest_id') 
valor_cabecera_content_encoding = response.headers.get('content-encoding')

print(f'{codigo_de_estado}, {valor_cookie_guest_id}, {valor_cabecera_content_encoding}')
