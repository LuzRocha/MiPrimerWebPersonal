from django.shortcuts import render, HttpResponse

html_base = """
<h1>Mi web personal</h1>
<ul>
  <li><a href="/">Portada</a></li>
  <li><a href="/about-me/">Acerca de</a></li>
  <li><a href="/portfolio/">portafolio</a></li>
  <li><a href="/contact/">Contacto</a></li>
</ul>  
"""

# Create your views here.
def home(request):
    return HttpResponse(html_base + """
    <h2>Portada</h2>
    <p>Esto es la portada</p)
    """)

def about(request):
    return HttpResponse(html_base + """
       <h2>Acerca de </h2>
    <P>Me llamo luz y soy programadora</p>
    """)

def portfolio(request):
    return HttpResponse(html_base + """
       <h2>portafolio</h2>
    <p>algunos de mis trabajos</p)
    """)

def contact(request):
    return HttpResponse(html_base + """
       <h2>Contacto</h2>
    <P>Aqui les dejo mi e-mail para preguntarme dudas: <a href="malto:hola@luz.net">hola@luz.net</p>
    """)