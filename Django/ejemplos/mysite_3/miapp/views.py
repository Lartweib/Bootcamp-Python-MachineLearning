from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
#MVC Modelo vista controlador --> acciones (métodos de una clase)
#MVT Modelo Template  Vista

#resquest es un parametro que me va ha permitir recibir peticiones que haga a esta url
#datos que le pase al enviar un formulario

layout = """
<h1>Web con Django</h1>
<hr/>
<ul>
    <li>
        <a href = "/inicio">Inicio</a>
    </li>
    <li>
        <a href = "/hola-mundo">Hola Mundo </a>
    </li>
    <li>
        <a href = "/pagina-pruebas">Página de pruebas</a>
    </li>
    <li>
        <a href = "/contacto">Contacto</a>
    </li>
</ul>
<hr/>
"""

def index(request):
    #primero importar (HttpResponse)
    # return HttpResponse("Hola Mundo !")
    html = """
        <h1>Inicio</h1>
        <p>Años hasta 2050</p>
        <ul>
    """
    year = 2021
    while year <= 2050:
        if year % 2 == 0:
            html += f"<li>{str(year)}</li>"
        year+=1

    html += "</ul>"
    return render(request,'index.html')
    #hay que cargar miapp en settings.py 



def hola_mundo(request):
    return render(request,'hola_mundo.html')
    # return HttpResponse('hola mundo')



def pagina(request, redirigir = 0):
    #primero importar (HttpResponse)
    # return HttpResponse("Hola Mundo !")

    if redirigir == 1:
        #import redirect
        return redirect("/inicio/")
    if redirigir == 2:
        #import redirect
        return redirect("/contacto/Oscar/Burgos/")
    if redirigir == 3:
        #import redirect
        return redirect("http://www.google.com")
    return render(request,'pagina.html')


def contacto(request, nombre="nombre", apellidos="apellidos"):
    #primero importar (HttpResponse)
    # return HttpResponse("Hola Mundo !")
    html = ""
    if nombre and apellidos:
        html += "<p>El nombre completo es: </p>"
        html += f"<h3>{nombre} {apellidos}</h3>"
    return HttpResponse(layout+f"<h2>Contacto:</h2>"+html) #http://127.0.0.1:8000/contacto/Hola
