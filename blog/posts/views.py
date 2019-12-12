from django.shortcuts import render

# Create your views here.

def home(request):
    nome = 'Felipe'
    lista =['RG', ' Genero', 'cor', 'Trabalha']
    contexto = {
        'nome' : nome,
        'lista' : lista
    }
    return render(request, 'home.html', contexto)