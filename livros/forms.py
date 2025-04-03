from django import forms
from .models import Livros

class LivroForm(forms.ModelForm):
    class Meta:
        model = Livros
        fields =  "__all__"