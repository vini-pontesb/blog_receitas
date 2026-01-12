from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Receita, Categoria
from .forms import ReceitaForm, CategoriaForm

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

def nova_receita(request):
    if request.method == 'POST':
        form_receita = ReceitaForm(request.POST)
        if form_receita.is_valid():
            form_receita.save()
            messages.success(request, "RECEITA SALVA !")
            return redirect('receitas')
    else:
        form_receita = ReceitaForm()
    context = {'form_receita': form_receita}
    return render(request, 'nova_receita.html', context)

def nova_categoria(request):
    if request.method == 'POST':
        form_categoria = CategoriaForm(request.POST)
        if form_categoria.is_valid():
            form_categoria.save()
            return redirect('categorias')
    else:
        form_categoria = CategoriaForm()
    context = {'form_categoria': form_categoria}
    return render(request, 'nova_categoria.html', context)

def home(request):
    home = 'home'
    context = {'home': home}
    return render(request, 'home.html', context)