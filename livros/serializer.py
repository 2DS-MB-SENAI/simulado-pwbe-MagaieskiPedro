from .models import Usuario,Livros
from rest_framework import serializers

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        exclude = ('password')
class LivrosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Livros
        fields = "__all__"
