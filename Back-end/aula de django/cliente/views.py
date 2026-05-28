from django.shortcuts import render

#importar classe (ferramenta) HttpResponse
from django.http import HttpResponse #Vai responder a solicitação do navegador


#Cria a função que responde a solicitação do navegador
def contato(request):
    return HttpResponse("<h1>Contato</h1>  <form>  <input type=text placeholder=email@email.com>  <input text=text placeholder=(21)99999-9999> <button>enviar</button> </form>")
 

#Chamr arquivo html (Template)

def home(request):
    return render (request, "clientes/home.html")

def formulario(request):
    return render (request, "clientes/formularios.html")