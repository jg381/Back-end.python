from django.shortcuts import render #Ja vem por padrão


#Chamar arquivos HTML (Template)
def home(request):


    titulo = "Nossos melhores clientes "

    nosso_cliente = {
        'nome': "João Gabriel",
        'idade':17,
        'nascimento': "20/01/2009"
    }

    nomes_clientes = ["Maria", "Joao", "Mateus", "Ana", "Marcos"]

    carros = [
        {'marca': "Chevrolet", 'modelo':'Onix LT', 'ano': '2020'},
        {'marca': "Fiat", 'modelo':'Uno', 'ano': '2010'},
        {'marca': "VW", 'modelo':'Gol', 'ano': '2022'},
    ]

    return render(request, "clientes/home.html", {'msg':titulo, 'lista_clientes':nosso_cliente, 'dados':nomes_clientes, 'meus_carros':carros})

def formulario(request):
    return render(request, "clientes/formulario.html" )