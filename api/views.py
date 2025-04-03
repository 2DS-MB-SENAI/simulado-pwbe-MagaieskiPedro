from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated

from .models import Livros,Usuario
from .serializer import LivrosSerializer
# AUTH:
@api_view(['POST'])
def registrar(request):
    nome = request.data.get("nome")
    senha = request.data.get("senha")
    telefone = telefone.data.get("telefone")

    if not nome or not senha:
        return Response({"error":"Nome e senha são obrigatorios"},status=status.HTTP_400_BAD_REQUEST)
    if Usuario.objects.filter(username=nome).exists():
        return Response({"error":"O usuario já existe"},status=status.HTTP_400_BAD_REQUEST)
    usuario = Usuario.objects.create_user(
        username = nome,
        password = senha,
        telefone = telefone
    )
    return Response({"mensagem":"Usuario criado com sucesso"},status=status.HTTP_201_CREATED)
@api_view(['POST'])
def login(request):
    nome = request.data.get("nome")
    senha = request.data.get("senha")
    usuario = authenticate(username=nome, password=senha)
    
    if usuario:
        refresh = RefreshToken.for_user(usuario)
        return Response({
            "Acesso":str(refresh.access_token),
            "Refresh":str(refresh)
            },status=status.HTTP_200_OK)
    else:
        return Response({"Erro":"usuario ou senha não encontrados"},status=status.HTTP_400_BAD_REQUEST)

# api view :
@api_view(['GET','POST'])
def listar_livros_endpoint(request):
    if request.method == 'POST':
        serializer = LivrosSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
            livro = Livros.objects.all()
            serializer = LivrosSerializer(livro, many=True)
            return Response(serializer.data)
# forms :
def listar_livros(request):
    livros = Livros.objects.all()
    return render(request, 'livros.html', {'livros':livros})