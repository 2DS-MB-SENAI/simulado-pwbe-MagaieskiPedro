from django.urls import path
from . import views
urlpatterns = [
    path('auth/registro/',view=views.registrar, name="registro"),
    path('auth/login/',view=views.login, name="login"),
    path('/livros/',view=views.listar_livros, name="listar_livros"),
]