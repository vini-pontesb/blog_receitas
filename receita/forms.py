from django import forms
from .models import Receita, Categoria

class ReceitaForm(forms.ModelForm):
    class Meta:
        model = Receita
        fields = ['titulo', 'ingraditens', 'modo_preparo', 'categoria']