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

def detalhes_receita(request, id_receita):
    receita = Receita.objects.get(id = id_receita)
    context = {'receita': receita}

    return render(request, 'detalhes_receita.html', context)

def mostrar_categoria(request, id_categoria):
    categoria_encontratada = Categoria.objects.get(id = id_categoria)
    receitas = Receita.objects.filter(categoria = categoria_encontratada)
    context = {'categoria': categoria_encontratada,
               'receitas': receitas}

    return render(request, 'mostrar_categoria.html', context)