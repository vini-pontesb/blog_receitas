from django.shortcuts import render
from .models import Receita, Categoria

def receitas(request):
    receitas = Receita.objects.all()
    context = {'receitas': receitas}

    return render(request, 'minhas_receitas.html', context)

def categorias(request):
    categorias = Categoria.objects.all()
    context = {'categorias': categorias}

    return render(request, 'categorias_receitas.html', context)
