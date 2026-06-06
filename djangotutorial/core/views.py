from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Profile
from .serializers import ProfileSerializer


def home(request):
    return render(request, 'portfolio/home.html')


class PerfilDetail(generics.RetrieveUpdateAPIView):
    """
    GET   /perfil/ → Retorna o perfil do usuario logado
    PUT   /perfil/ → Atualiza o perfil completo
    PATCH /perfil/ → Atualiza parcialmente
    """

    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        """
        Em vez de buscar pelo pk da URL, busca pelo usuario logado.
        Se o perfil nao existir, cria um vazio automaticamente.
        """
        perfil, created = Profile.objects.get_or_create(
            usuario=self.request.user,
            defaults={'name': self.request.user.username},
        )
        return perfil