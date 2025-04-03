from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class livros(models.Model):
    titulo = models.CharField(max_length=50)
    autor = models.CharField(max_length=50)
    paginas = models.IntegerField()
class Usuario(AbstractUser):
    telefone = models.CharField(max_length=15,blank=True, null=True)