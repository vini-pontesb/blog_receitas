from django.urls import path
from . import views

urlpatterns = [
    path('receitas/', views.receitas, name="receitas"),
    path('categorias/', views.categorias, name="categorias"),
    path('detalhes_receita/<int:id_receita>/', views.detalhes_receita, name="detalhes_receita"),
    path('mostrar_categoria/<int:id_categoria>/', views.mostrar_categoria, name="mostrar_categoria"),
    path('nova_receita/', views.nova_receita, name="nova_receita"),
    path('nova_categoria/', views.nova_categoria, name="nova_categoria"),
    path('', views.home, name="home"),
    path('editar_receita/<int:id_receita>', views.editar_receita, name="editar_receita")
]
