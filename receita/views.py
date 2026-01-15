from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Receita, Categoria
from .forms import ReceitaForm, CategoriaForm

def receitas(request):
    receitas = Receita.objects.all()
    context = {'receitas': receitas}

    return render(request, 'minhas_receitas.html', context)

def buscar_receita(request):
    titulo_buscado = request.GET.get('titulo')
    if titulo_buscado:
        receitas_encontradas = Receita.objects.filter(titulo__icontains=titulo_buscado)
    else:
        receitas_encontradas = None
    context = {'receitas_encontradas': receitas_encontradas, 'buscar': True}
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

def editar_receita (request, id_receita):
    receita = get_object_or_404(Receita, id = id_receita)
    if request.method == 'POST':
        form_receita = ReceitaForm(request.POST, instance=receita) 
        if form_receita.is_valid():
            form_receita.save()
            messages.success(request, "RECEITA EDITADA!")
            return redirect('receitas')
    else:
        form_receita = ReceitaForm(instance=receita)
    context = {'form_receita': form_receita, 'editar': True}
    return render(request, 'nova_receita.html', context)
