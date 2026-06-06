from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Task
from .serializers import TaskSerializer


class TaskListCreate(generics.ListCreateAPIView):
    """
    GET  /tasks/v3/ → Lista as tarefas do usuario logado
    POST /tasks/v3/ → Cria uma tarefa vinculada ao usuario logado
    """

    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        Filtra as tarefas para retornar APENAS as do usuario logado.
        request.user contem o usuario autenticado pelo JWT.
        """
        return Task.objects.filter(responsible=self.request.user)

    def perform_create(self, serializer):
        """
        Ao criar uma tarefa, preenche automaticamente o campo 'responsible'
        com o usuario que esta fazendo a requisicao (request.user).
        """
        serializer.save(responsible=self.request.user)


# URL: path('v3/<int:pk>/', views.TaskDetail.as_view())

class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    GET    /tasks/v3/<pk>/ → Retorna uma tarefa do usuario
    PUT    /tasks/v3/<pk>/ → Atualiza uma tarefa do usuario
    PATCH  /tasks/v3/<pk>/ → Atualiza parcialmente
    DELETE /tasks/v3/<pk>/ → Exclui uma tarefa do usuario
    """

    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]
 
    def get_queryset(self):
        """
        Garante que o usuario so pode ver/editar/excluir SUAS tarefas.
        Se tentar acessar a tarefa de outro usuario, retorna 404.
        """
        return Task.objects.filter(responsible=self.request.user)
