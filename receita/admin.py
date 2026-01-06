from django.contrib import admin
from .models import Categoria, Receita


class Receitas(admin.ModelAdmin):
    list_display = ['titulo', 'categoria']
    search_fields = ['titulo']
    list_filter = ['categoria']

class Categorias(admin.ModelAdmin):
    search_fields = ['nome']

admin.site.register(Categoria, Categorias)
admin.site.register(Receita, Receitas)
