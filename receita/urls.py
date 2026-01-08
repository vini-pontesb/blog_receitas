from django.urls import path
from . import views

urlpatterns = [
    path('receitas/', views.receitas, name="receitas"),
    path('categorias/', views.categorias, name="categorias"),
    path('detalhes_receita/<int:id_receita>/', views.detalhes_receita, name="detalhes_receita"),
    path('mostrar_categoria/<int:id_categoria>/', views.mostrar_categoria, name="mostrar_categoria")
]
