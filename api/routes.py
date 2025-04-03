from django.urls import path
from . import views
urlpatterns = [
    path('auth/registro/',view=views.registrar, name="registro"),
    path('auth/login/',view=views.login, name="login"),
    path('api/livros/',view=views.listar_livros_endpoint, name="listar_livros"),
]