from rest_framework import serializers

from .models import Livros,Usuario

class LivrosSerializer(serializers.ModelSerializer):
    class meta:
        model = Livros
        fields = "__all__"
class UsuarioSerializer(serializers.ModelSerializer):
    class meta:
        model = Usuario
        exclude = ("password")